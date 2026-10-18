# -*- coding: utf-8 -*-
"""
测试 Apple 风格单页排版与 Playwright 渲染效果
"""
import os
import asyncio
from playwright.async_api import async_playwright
import catalog_data_v2
import generate_svgs

async def test_render():
    item = catalog_data_v2.ITEMS[0] # AERO-STREAM 7
    svg_markup = generate_svgs.get_svg_diagram(item["svg_type"])
    
    img_path = os.path.abspath(os.path.join("e:/brochure/飞机截图", item["image"])).replace("\\", "/")
    
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
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "PingFang SC", "Segoe UI", "Microsoft YaHei", sans-serif;
    background: #fbfbfd;
    color: #1d1d1f;
    -webkit-font-smoothing: antialiased;
}}
.page {{
    width: 297mm;
    height: 210mm;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    background: #fbfbfd;
}}

/* 奇数页：纯大图展示页 */
.page-exhibition {{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 16mm 20mm 14mm 20mm;
    background: radial-gradient(circle at 50% 48%, #ffffff 0%, #fbfbfd 65%, #f5f5f7 100%);
}}
.exhibit-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
}}
.exhibit-series {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #86868b;
    text-transform: uppercase;
}}
.exhibit-cat-pill {{
    font-size: 10px;
    font-weight: 600;
    color: #0071e3;
    background: rgba(0, 113, 227, 0.08);
    padding: 4px 12px;
    border-radius: 12px;
    letter-spacing: 0.5px;
}}
.exhibit-hero {{
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
}}
.hero-img-box {{
    max-width: 90%;
    max-height: 80%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    z-index: 2;
}}
.hero-img-box img {{
    max-width: 100%;
    max-height: 125mm;
    object-fit: contain;
    filter: drop-shadow(0 20px 35px rgba(0, 0, 0, 0.08));
    transition: transform 0.3s;
}}
.hero-pedestal {{
    width: 65%;
    height: 20px;
    background: radial-gradient(ellipse at center, rgba(0, 0, 0, 0.07) 0%, rgba(0, 0, 0, 0) 70%);
    margin-top: -10px;
    z-index: 1;
}}
.exhibit-bottom {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid rgba(0, 0, 0, 0.05);
    padding-top: 10px;
}}
.exhibit-name-block h2 {{
    font-size: 18px;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: #1d1d1f;
}}
.exhibit-name-block p {{
    font-size: 11px;
    color: #86868b;
    margin-top: 3px;
    letter-spacing: 0.5px;
}}
.exhibit-folio {{
    font-size: 14px;
    font-weight: 600;
    color: #86868b;
    font-variant-numeric: tabular-nums;
}}

/* 偶数页：图文并茂专业理论讲解页 */
.page-editorial {{
    padding: 14mm 18mm 12mm 18mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #fbfbfd;
}}
.edit-header {{
    margin-bottom: 8px;
}}
.edit-badge-row {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 6px;
}}
.badge-cat {{
    font-size: 9.5px;
    font-weight: 600;
    color: #1d1d1f;
    background: #e5e5ea;
    padding: 3px 8px;
    border-radius: 6px;
}}
.badge-code {{
    font-size: 9.5px;
    font-weight: 700;
    color: #0071e3;
    font-family: "SF Mono", Menlo, Consolas, monospace;
    background: rgba(0, 113, 227, 0.08);
    padding: 3px 8px;
    border-radius: 6px;
}}
.edit-title {{
    font-size: 19px;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: #1d1d1f;
    line-height: 1.25;
}}
.edit-tagline {{
    font-size: 11.5px;
    font-weight: 600;
    color: #0071e3;
    margin-top: 3px;
}}
.edit-narrative {{
    font-size: 10.5px;
    line-height: 1.55;
    color: #424245;
    margin-top: 6px;
    text-align: justify;
}}

/* 理论深度卡片 */
.theory-card {{
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 12px;
    padding: 12px 14px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
    margin: 8px 0;
}}
.theory-card-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
    border-bottom: 1px solid #f0f0f2;
    padding-bottom: 6px;
}}
.theory-card-tag {{
    font-size: 9.5px;
    font-weight: 700;
    color: #0071e3;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}}
.theory-title {{
    font-size: 12px;
    font-weight: 700;
    color: #1d1d1f;
}}
.theory-body {{
    display: grid;
    grid-template-columns: 1.15fr 0.95fr;
    gap: 14px;
    align-items: center;
}}
.theory-desc {{
    font-size: 10px;
    line-height: 1.55;
    color: #515154;
    text-align: justify;
}}
.theory-formula-box {{
    margin-top: 8px;
    background: #f5f5f7;
    border-left: 3px solid #0071e3;
    padding: 6px 10px;
    border-radius: 0 6px 6px 0;
    font-family: "SF Mono", Consolas, monospace;
    font-size: 9.5px;
    color: #1d1d1f;
}}
.theory-diagram-box {{
    height: 135px;
    display: flex;
    align-items: center;
    justify-content: center;
}}

/* 底部指标与规格 */
.edit-bottom-grid {{
    display: grid;
    grid-template-columns: 1fr 1.25fr;
    gap: 14px;
    align-items: stretch;
}}
.stats-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
}}
.stat-card {{
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    padding: 8px 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}}
.stat-val {{
    font-size: 17px;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: #1d1d1f;
}}
.stat-lbl {{
    font-size: 9.5px;
    color: #86868b;
    margin-top: 2px;
}}
.specs-table {{
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    padding: 8px 12px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 14px;
    row-gap: 4px;
    align-content: center;
}}
.spec-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #f5f5f7;
    padding: 3px 0;
    font-size: 9.5px;
}}
.spec-lbl {{
    color: #86868b;
}}
.spec-val {{
    font-weight: 600;
    color: #1d1d1f;
}}

.edit-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(0, 0, 0, 0.05);
    padding-top: 8px;
    margin-top: 6px;
    font-size: 9.5px;
    color: #86868b;
}}
</style>
</head>
<body>

<!-- 纯大图展示页 (奇数页 P.005) -->
<div class="page page-exhibition">
    <div class="exhibit-top">
        <div class="exhibit-series">EXHIBIT // 01 · MASTER SERIES</div>
        <div class="exhibit-cat-pill">{item["category_zh"]} · {item["category_en"]}</div>
    </div>
    <div class="exhibit-hero">
        <div class="hero-img-box">
            <img src="file:///{img_path}" alt="{item["name_zh"]}">
        </div>
        <div class="hero-pedestal"></div>
    </div>
    <div class="exhibit-bottom">
        <div class="exhibit-name-block">
            <h2>{item["name_zh"]}</h2>
            <p>{item["name_en"]} — {item["code"]}</p>
        </div>
        <div class="exhibit-folio">005</div>
    </div>
</div>

<!-- 理论讲解页 (偶数页 P.006) -->
<div class="page page-editorial">
    <div class="edit-header">
        <div class="edit-badge-row">
            <span class="badge-cat">{item["category_zh"]}</span>
            <span class="badge-code">{item["code"]}</span>
        </div>
        <h1 class="edit-title">{item["name_zh"]}</h1>
        <div class="edit-tagline">{item["tagline"]}</div>
        <p class="edit-narrative">{item["desc"]}</p>
    </div>

    <!-- 理论卡片 -->
    <div class="theory-card">
        <div class="theory-card-header">
            <span class="theory-card-tag">◈ AERODYNAMICS & FLIGHT PHYSICS // 气动与飞行物理</span>
            <span class="theory-title">{item["theory_title"]}</span>
        </div>
        <div class="theory-body">
            <div>
                <p class="theory-desc">{item["theory_desc"]}</p>
                <div class="theory-formula-box">
                    <span style="color:#86868b; margin-right:4px;">GOVERNING EQ:</span>
                    <strong>{item["theory_formula"]}</strong>
                </div>
            </div>
            <div class="theory-diagram-box">
                {svg_markup}
            </div>
        </div>
    </div>

    <!-- 底部指标与规格 -->
    <div class="edit-bottom-grid">
        <div class="stats-grid">
            <div class="stat-card">
                <span class="stat-val">{item["hero_stats"][0]["val"]}</span>
                <span class="stat-lbl">{item["hero_stats"][0]["lbl"]}</span>
            </div>
            <div class="stat-card">
                <span class="stat-val">{item["hero_stats"][1]["val"]}</span>
                <span class="stat-lbl">{item["hero_stats"][1]["lbl"]}</span>
            </div>
            <div class="stat-card">
                <span class="stat-val">{item["hero_stats"][2]["val"]}</span>
                <span class="stat-lbl">{item["hero_stats"][2]["lbl"]}</span>
            </div>
            <div class="stat-card">
                <span class="stat-val">{item["hero_stats"][3]["val"]}</span>
                <span class="stat-lbl">{item["hero_stats"][3]["lbl"]}</span>
            </div>
        </div>

        <div class="specs-table">
            <div class="spec-row"><span class="spec-lbl">{item["specs"][0]["label"]}</span><span class="spec-val">{item["specs"][0]["value"]}</span></div>
            <div class="spec-row"><span class="spec-lbl">{item["specs"][1]["label"]}</span><span class="spec-val">{item["specs"][1]["value"]}</span></div>
            <div class="spec-row"><span class="spec-lbl">{item["specs"][2]["label"]}</span><span class="spec-val">{item["specs"][2]["value"]}</span></div>
            <div class="spec-row"><span class="spec-lbl">{item["specs"][3]["label"]}</span><span class="spec-val">{item["specs"][3]["value"]}</span></div>
            <div class="spec-row"><span class="spec-lbl">{item["specs"][4]["label"]}</span><span class="spec-val">{item["specs"][4]["value"]}</span></div>
            <div class="spec-row"><span class="spec-lbl">{item["specs"][5]["label"]}</span><span class="spec-val">{item["specs"][5]["value"]}</span></div>
            <div class="spec-row"><span class="spec-lbl">{item["specs"][6]["label"]}</span><span class="spec-val">{item["specs"][6]["value"]}</span></div>
            <div class="spec-row"><span class="spec-lbl">{item["specs"][7]["label"]}</span><span class="spec-val">{item["specs"][7]["value"]}</span></div>
        </div>
    </div>

    <div class="edit-footer">
        <span>AEROSPACE DYNAMICS & AUTONOMOUS FLIGHT SYSTEMS // MASTER BLUEPRINT</span>
        <span style="font-weight:600; font-variant-numeric:tabular-nums;">006</span>
    </div>
</div>

</body>
</html>'''

    with open("e:/brochure/test_spread.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    os.makedirs("e:/brochure/test_output", exist_ok=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 990})
        await page.goto(f"file:///{os.path.abspath('e:/brochure/test_spread.html').replace('\\', '/')}")
        await page.wait_for_timeout(1000)
        
        # 截图两个页面
        pages_elements = await page.query_selector_all(".page")
        for i, el in enumerate(pages_elements):
            await el.screenshot(path=f"e:/brochure/test_output/sample_page_{i+1}.png")
        
        # 导出 PDF
        await page.pdf(
            path="e:/brochure/test_output/sample_spread.pdf",
            print_background=True,
            prefer_css_page_size=True
        )
        await browser.close()
    
    print("Test render completed! Check e:/brochure/test_output/")

if __name__ == "__main__":
    asyncio.run(test_render())
