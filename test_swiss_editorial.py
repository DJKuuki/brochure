# -*- coding: utf-8 -*-
"""
测试瑞士网格与图书典藏版面设计 (Swiss Grid Book Editorial Layout)
对比之前 Web 仪表盘卡片风，全面转向真正的出版物/画册排版：
- 剔除 Web 圆角灰框、浮夸卡片阴影、胶囊按钮
- 采用瑞士网格、经典裁线 (Hairline Rules)、双栏报纸/期刊级版面排版
- 规范的图版编号 (FIG. 01.1)、公式编号 [Eq. 01.1]、图书级 Booktabs 数据矩阵
- 纯客户面向语言，彻底消除印刷制作/纸张对裱等幕后元信息
"""
import os
import asyncio
from playwright.async_api import async_playwright
import catalog_data_v2
import generate_svgs

async def test_editorial():
    item = catalog_data_v2.ITEMS[0] # AERO-STREAM 7
    img_path = os.path.abspath(os.path.join("e:/brochure/飞机截图", item["image"])).replace("\\", "/")
    svg_markup = generate_svgs.get_svg_diagram(item["svg_type"])

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<style>
@page {{
    size: 297mm 210mm;
    margin: 0;
}}
* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    background: #ffffff;
    color: #111111;
    -webkit-font-smoothing: antialiased;
}}
.page {{
    width: 297mm;
    height: 210mm;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    background: #ffffff;
}}

/* ========================================================= */
/* 奇数页：左页 · 纯粹展项画幅 (Verso / Pure Exhibition) */
/* ========================================================= */
.page-verso {{
    padding: 16mm 22mm 16mm 24mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}
/* 页面顶部眉线 (Running Header) */
.running-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 0.75px solid #111111;
    padding-bottom: 4.5mm;
}}
.rh-title {{
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #111111;
}}
.rh-section {{
    font-size: 7.5pt;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #666666;
}}

/* 中央主体展区：纯净留白，无虚饰边框 */
.verso-stage {{
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10mm 15mm;
}}
.verso-stage img {{
    max-width: 100%;
    max-height: 125mm;
    object-fit: contain;
}}

/* 底部图注与页码 */
.verso-footer {{
    border-top: 0.5px solid #d2d2d7;
    padding-top: 4.5mm;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}}
.caption-block {{
    display: flex;
    flex-direction: column;
    gap: 2px;
}}
.caption-title {{
    font-size: 11pt;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: #111111;
}}
.caption-sub {{
    font-size: 8pt;
    color: #555555;
    letter-spacing: 0.5px;
}}
.caption-meta {{
    font-size: 7.5pt;
    font-family: "SF Mono", Menlo, Consolas, monospace;
    color: #888888;
    margin-top: 1px;
}}
.page-folio {{
    font-size: 10pt;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
    color: #111111;
}}

/* ========================================================= */
/* 偶数页：右页 · 瑞士网格严谨学术讲解 (Recto / Editorial & Theory) */
/* ========================================================= */
.page-recto {{
    padding: 16mm 24mm 16mm 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}

/* 标题区：严谨书籍排版，无Web胶囊标签 */
.editorial-header {{
    margin-top: 4mm;
    margin-bottom: 5mm;
}}
.editorial-title-row {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}}
.editorial-main-title {{
    font-size: 20pt;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #111111;
    line-height: 1.15;
}}
.editorial-category-tag {{
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #0071e3;
}}
.editorial-subtitle {{
    font-size: 9.5pt;
    font-weight: 600;
    color: #333333;
    margin-top: 3px;
}}

/* 双栏正文叙述 (Two-column narrative block) */
.editorial-narrative-columns {{
    column-count: 2;
    column-gap: 8mm;
    text-align: justify;
    margin-bottom: 5mm;
}}
.editorial-narrative-columns p {{
    font-size: 8.5pt;
    line-height: 1.55;
    color: #333333;
    text-indent: 0;
}}

/* 中部：科学图版与控制方程 (Technical Theory Plate) */
.technical-plate {{
    border-top: 1px solid #111111;
    border-bottom: 0.75px solid #d2d2d7;
    padding: 4.5mm 0;
    margin-bottom: 5mm;
}}
.plate-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 3.5mm;
}}
.plate-num {{
    font-size: 8pt;
    font-weight: 800;
    letter-spacing: 1px;
    color: #111111;
    text-transform: uppercase;
}}
.plate-subject {{
    font-size: 8pt;
    font-weight: 700;
    color: #0071e3;
}}
.plate-layout {{
    display: grid;
    grid-template-columns: 1.15fr 1fr;
    gap: 8mm;
    align-items: center;
}}
.plate-text-col {{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}
.plate-desc {{
    font-size: 8.2pt;
    line-height: 1.55;
    color: #444444;
    text-align: justify;
}}
.plate-equation-box {{
    margin-top: 3.5mm;
    border-left: 2px solid #0071e3;
    padding: 2.5mm 3.5mm;
    background: #f8f9fa;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}
.eq-label {{
    font-size: 7.5pt;
    font-family: "SF Mono", Menlo, Consolas, monospace;
    font-weight: 700;
    color: #111111;
}}
.eq-tag {{
    font-size: 7.5pt;
    font-family: "SF Mono", Menlo, Consolas, monospace;
    color: #888888;
}}
.plate-figure-col {{
    height: 38mm;
    display: flex;
    align-items: center;
    justify-content: center;
}}

/* 底部：指标与技术规格矩阵 (Classic Booktabs Spec Matrix) */
.specs-and-metrics-block {{
    display: grid;
    grid-template-columns: 0.95fr 1.35fr;
    gap: 8mm;
    align-items: stretch;
}}
/* 左侧：4大核心遥测数据 */
.metrics-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4mm 6mm;
    align-content: center;
}}
.metric-cell {{
    border-bottom: 0.5px solid #e5e5ea;
    padding-bottom: 2mm;
}}
.metric-val {{
    font-size: 15pt;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #111111;
    line-height: 1.1;
}}
.metric-lbl {{
    font-size: 7pt;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: #666666;
    margin-top: 1.5mm;
}}

/* 右侧：经典书籍规格表 (LaTeX Booktabs Table Style) */
.booktabs-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7.8pt;
}}
.booktabs-table thead tr {{
    border-top: 1px solid #111111;
    border-bottom: 0.75px solid #111111;
}}
.booktabs-table th {{
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    padding: 1.5mm 0;
    color: #111111;
}}
.booktabs-table td {{
    padding: 1.6mm 0;
    border-bottom: 0.5px solid #f0f0f2;
    vertical-align: middle;
}}
.booktabs-table tbody tr:last-child td {{
    border-bottom: 1px solid #111111;
}}
.spec-key {{
    color: #555555;
    width: 25%;
}}
.spec-val {{
    color: #111111;
    font-weight: 600;
    width: 25%;
}}
</style>
</head>
<body>

<!-- 奇数页：左页 (Verso) · 纯粹模型展示 -->
<div class="page page-verso">
    <div class="running-header">
        <div class="rh-title">AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS</div>
        <div class="rh-section">SYSTEM MONOGRAPH // SECTION 01</div>
    </div>

    <div class="verso-stage">
        <img src="file:///{img_path}" alt="{item["name_zh"]}">
    </div>

    <div class="verso-footer">
        <div class="caption-block">
            <div class="caption-title">01 / {item["name_zh"].split("//")[0].strip()}</div>
            <div class="caption-sub">{item["tagline"]}</div>
            <div class="caption-meta">PLATFORM IDENTIFICATION : {item["code"]} // CATEGORY: {item["category_zh"]} ({item["category_en"]})</div>
        </div>
        <div class="page-folio">005</div>
    </div>
</div>

<!-- 偶数页：右页 (Recto) · 瑞士网格严谨学术讲解 -->
<div class="page page-recto">
    <div class="running-header">
        <div class="rh-title">SECTION 01: TACTICAL &amp; AUTONOMOUS MULTIROTOR PLATFORMS</div>
        <div class="rh-section">PLATE 01.1 // {item["code"]}</div>
    </div>

    <div class="editorial-header">
        <div class="editorial-title-row">
            <h1 class="editorial-main-title">{item["name_zh"].split("//")[0].strip()}</h1>
            <span class="editorial-category-tag">{item["category_zh"]}</span>
        </div>
        <div class="editorial-subtitle">{item["name_en"]} — {item["tagline"]}</div>
    </div>

    <!-- 双栏正文叙述 (图书排版核心) -->
    <div class="editorial-narrative-columns">
        <p>{item["desc"]}</p>
    </div>

    <!-- 科学图版与理论公式 -->
    <div class="technical-plate">
        <div class="plate-header">
            <span class="plate-num">FIG. 01.1 // {item["theory_title"]}</span>
            <span class="plate-subject">FLIGHT PHYSICS &amp; BOUNDARY LAYER DYNAMICS</span>
        </div>
        <div class="plate-layout">
            <div class="plate-text-col">
                <p class="plate-desc">{item["theory_desc"]}</p>
                <div class="plate-equation-box">
                    <span class="eq-label">{item["theory_formula"]}</span>
                    <span class="eq-tag">[Eq. 01.1]</span>
                </div>
            </div>
            <div class="plate-figure-col">
                {svg_markup}
            </div>
        </div>
    </div>

    <!-- 遥测数据与经典规格表 (Booktabs) -->
    <div class="specs-and-metrics-block">
        <div class="metrics-grid">
            <div class="metric-cell">
                <div class="metric-val">{item["hero_stats"][0]["val"]}</div>
                <div class="metric-lbl">{item["hero_stats"][0]["lbl"]}</div>
            </div>
            <div class="metric-cell">
                <div class="metric-val">{item["hero_stats"][1]["val"]}</div>
                <div class="metric-lbl">{item["hero_stats"][1]["lbl"]}</div>
            </div>
            <div class="metric-cell">
                <div class="metric-val">{item["hero_stats"][2]["val"]}</div>
                <div class="metric-lbl">{item["hero_stats"][2]["lbl"]}</div>
            </div>
            <div class="metric-cell">
                <div class="metric-val">{item["hero_stats"][3]["val"]}</div>
                <div class="metric-lbl">{item["hero_stats"][3]["lbl"]}</div>
            </div>
        </div>

        <table class="booktabs-table">
            <thead>
                <tr>
                    <th>技术参数指标</th>
                    <th>工程标定值</th>
                    <th>分系统配置</th>
                    <th>设计规范</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="spec-key">{item["specs"][0]["label"]}</td>
                    <td class="spec-val">{item["specs"][0]["value"]}</td>
                    <td class="spec-key">{item["specs"][4]["label"]}</td>
                    <td class="spec-val">{item["specs"][4]["value"]}</td>
                </tr>
                <tr>
                    <td class="spec-key">{item["specs"][1]["label"]}</td>
                    <td class="spec-val">{item["specs"][1]["value"]}</td>
                    <td class="spec-key">{item["specs"][5]["label"]}</td>
                    <td class="spec-val">{item["specs"][5]["value"]}</td>
                </tr>
                <tr>
                    <td class="spec-key">{item["specs"][2]["label"]}</td>
                    <td class="spec-val">{item["specs"][2]["value"]}</td>
                    <td class="spec-key">{item["specs"][6]["label"]}</td>
                    <td class="spec-val">{item["specs"][6]["value"]}</td>
                </tr>
                <tr>
                    <td class="spec-key">{item["specs"][3]["label"]}</td>
                    <td class="spec-val">{item["specs"][3]["value"]}</td>
                    <td class="spec-key">{item["specs"][7]["label"]}</td>
                    <td class="spec-val">{item["specs"][7]["value"]}</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="verso-footer" style="margin-top:3mm;">
        <div style="font-size:7.5pt; color:#888888; letter-spacing:0.5px;">AEROSPACE MONOGRAPH // TECHNICAL SPECIFICATION MATRIX</div>
        <div class="page-folio">006</div>
    </div>
</div>

</body>
</html>'''

    with open("e:/brochure/test_output/test_swiss.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 990})
        await page.goto(f"file:///{os.path.abspath('e:/brochure/test_output/test_swiss.html').replace('\\', '/')}")
        
        pages_els = await page.query_selector_all(".page")
        await pages_els[0].screenshot(path="e:/brochure/test_output/sample_swiss_verso.png")
        await pages_els[1].screenshot(path="e:/brochure/test_output/sample_swiss_recto.png")
        await browser.close()
    print("Swiss editorial test completed!")

if __name__ == "__main__":
    asyncio.run(test_editorial())
