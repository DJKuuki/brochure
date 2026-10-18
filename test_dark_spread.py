# -*- coding: utf-8 -*-
"""
测试黑色背景 (Dark Obsidian) 下的整套排版与封面 GREET AERO
"""
import os
import asyncio
from playwright.async_api import async_playwright
import catalog_data_v2
import generate_svgs

# 修改 SVG 颜色以完美适配黑底
def get_dark_svg(svg_markup):
    # 将浅色背景替换为深色高科技黑灰背景
    dark = svg_markup.replace('background:#fbfbfd', 'background:#141418')
    dark = dark.replace('border:1px solid #e5e5ea', 'border:1px solid rgba(255,255,255,0.12)')
    dark = dark.replace('#f0f0f2', 'rgba(255,255,255,0.04)')
    dark = dark.replace('#1d1d1f', '#f5f5f7')
    dark = dark.replace('#424245', '#d1d1d6')
    dark = dark.replace('#515154', '#a1a1a6')
    dark = dark.replace('#d2d2d7', '#333336')
    dark = dark.replace('#e5e5ea', '#2c2c2e')
    dark = dark.replace('rgba(0,113,227,0.06)', 'rgba(41,151,255,0.12)')
    dark = dark.replace('rgba(0,113,227,0.12)', 'rgba(41,151,255,0.2)')
    dark = dark.replace('rgba(0,113,227,0.15)', 'rgba(41,151,255,0.25)')
    dark = dark.replace('#0071e3', '#2997ff')
    return dark

async def test_dark_mode():
    item = catalog_data_v2.ITEMS[0] # AERO-STREAM 7
    img_path = os.path.abspath(os.path.join("e:/brochure/飞机截图", item["image"])).replace("\\", "/")
    svg_raw = generate_svgs.get_svg_diagram(item["svg_type"])
    svg_dark = get_dark_svg(svg_raw)

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
    background: #0a0a0c;
    color: #f5f5f7;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    -webkit-font-smoothing: antialiased;
}}
.page {{
    width: 297mm;
    height: 210mm;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    background: #0a0a0c;
}}

/* 顶部眉线 (Running Header) */
.running-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 0.75px solid rgba(255, 255, 255, 0.2);
    padding-bottom: 4mm;
}}
.rh-title {{
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #f5f5f7;
}}
.rh-section {{
    font-size: 7.5pt;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #a1a1a6;
}}

/* 底部眉线与页码 (Running Footer) */
.verso-footer {{
    border-top: 0.5px solid rgba(255, 255, 255, 0.15);
    padding-top: 4mm;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}}
.page-folio {{
    font-size: 10pt;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
    color: #f5f5f7;
}}

/* ========================================================= */
/* PAGE 01: COVER WITH "GREET AERO" SLOGAN */
/* ========================================================= */
.page-cover {{
    padding: 16mm 22mm 14mm 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: radial-gradient(circle at 50% 40%, #141418 0%, #0a0a0c 70%, #000000 100%);
}}
.cover-hero-center {{
    margin: auto 0;
    text-align: center;
}}
.cover-slogan {{
    display: inline-block;
    font-size: 15pt;
    font-weight: 900;
    letter-spacing: 7px;
    color: #2997ff;
    text-transform: uppercase;
    border: 1px solid rgba(41, 151, 255, 0.4);
    padding: 3px 18px 3px 22px;
    border-radius: 20px;
    background: rgba(41, 151, 255, 0.08);
    margin-bottom: 5mm;
}}
.cover-main-title {{
    font-size: 44pt;
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1.1;
    color: #ffffff;
}}
.cover-sub-title {{
    font-size: 22pt;
    font-weight: 600;
    letter-spacing: -0.01em;
    color: #e5e5ea;
    margin-top: 3mm;
}}
.cover-hairline {{
    width: 60px;
    height: 2px;
    background: #2997ff;
    margin: 5mm auto;
}}
.cover-scope-desc {{
    font-size: 10pt;
    line-height: 1.6;
    color: #a1a1a6;
    max-width: 620px;
    margin: 0 auto;
}}
.cover-four-disciplines {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8mm;
    margin-top: 10mm;
    text-align: left;
    border-top: 1px solid rgba(255, 255, 255, 0.2);
    padding-top: 6mm;
}}
.discipline-col {{
    display: flex;
    flex-direction: column;
}}
.disc-num {{
    font-size: 11pt;
    font-weight: 800;
    color: #2997ff;
    font-family: "SF Mono", Menlo, Consolas, monospace;
}}
.disc-title {{
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #f5f5f7;
    margin-top: 1mm;
}}
.disc-cn {{
    font-size: 8pt;
    font-weight: 600;
    color: #d1d1d6;
    margin-top: 0.5mm;
}}
.discipline-col p {{
    font-size: 7.5pt;
    line-height: 1.45;
    color: #8e8e93;
    margin-top: 1.5mm;
}}
.cover-footer-row {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid rgba(255, 255, 255, 0.2);
    padding-top: 4mm;
}}
.cover-footer-left .corp-brand {{
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #f5f5f7;
}}
.cover-footer-left .corp-sub {{
    font-size: 7.5pt;
    color: #8e8e93;
    margin-top: 1mm;
}}
.cover-barcode-group {{
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}}
.barcode-lines {{
    display: flex;
    height: 16px;
    gap: 1.8px;
    align-items: stretch;
}}
.barcode-lines span {{
    background: #f5f5f7;
    display: inline-block;
}}
.barcode-text {{
    font-size: 7pt;
    font-family: "SF Mono", Consolas, monospace;
    color: #8e8e93;
    margin-top: 1mm;
}}

/* ========================================================= */
/* EXHIBITION (VERSO / ODD PAGES) */
/* ========================================================= */
.page-verso {{
    padding: 16mm 22mm 16mm 24mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}
.verso-stage {{
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 6mm 10mm;
}}
.verso-stage img {{
    max-width: 95%;
    max-height: 130mm;
    object-fit: contain;
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 16px 45px rgba(0, 0, 0, 0.6);
}}
.caption-block {{
    display: flex;
    flex-direction: column;
    gap: 1.5px;
}}
.caption-title {{
    font-size: 11pt;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: #f5f5f7;
}}
.caption-sub {{
    font-size: 8pt;
    color: #a1a1a6;
    letter-spacing: 0.5px;
}}
.caption-meta {{
    font-size: 7.2pt;
    font-family: "SF Mono", Menlo, Consolas, monospace;
    color: #8e8e93;
    margin-top: 1px;
}}

/* ========================================================= */
/* EDITORIAL (RECTO / EVEN PAGES) */
/* ========================================================= */
.page-recto {{
    padding: 16mm 24mm 16mm 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}
.editorial-header {{
    margin-top: 3mm;
    margin-bottom: 4mm;
}}
.editorial-title-row {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}}
.editorial-main-title {{
    font-size: 19pt;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #ffffff;
    line-height: 1.15;
}}
.editorial-category-tag {{
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #2997ff;
}}
.editorial-subtitle {{
    font-size: 9pt;
    font-weight: 600;
    color: #a1a1a6;
    margin-top: 2px;
}}
.editorial-narrative-columns {{
    column-count: 2;
    column-gap: 8mm;
    text-align: justify;
    margin-bottom: 4mm;
}}
.editorial-narrative-columns p {{
    font-size: 8.2pt;
    line-height: 1.55;
    color: #d1d1d6;
}}
.technical-plate {{
    border-top: 1px solid rgba(255, 255, 255, 0.25);
    border-bottom: 0.75px solid rgba(255, 255, 255, 0.15);
    padding: 3.5mm 0;
    margin-bottom: 4mm;
}}
.plate-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 3mm;
}}
.plate-num {{
    font-size: 8pt;
    font-weight: 800;
    letter-spacing: 0.8px;
    color: #f5f5f7;
    text-transform: uppercase;
}}
.plate-subject {{
    font-size: 7.5pt;
    font-weight: 700;
    color: #2997ff;
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
    font-size: 8pt;
    line-height: 1.55;
    color: #b0b0b5;
    text-align: justify;
}}
.plate-equation-box {{
    margin-top: 3mm;
    border-left: 2px solid #2997ff;
    padding: 2mm 3mm;
    background: #141418;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}
.eq-label {{
    font-size: 7.2pt;
    font-family: "SF Mono", Menlo, Consolas, monospace;
    font-weight: 700;
    color: #f5f5f7;
}}
.eq-tag {{
    font-size: 7.2pt;
    font-family: "SF Mono", Menlo, Consolas, monospace;
    color: #8e8e93;
}}
.plate-figure-col {{
    height: 36mm;
    display: flex;
    align-items: center;
    justify-content: center;
}}
.specs-and-metrics-block {{
    display: grid;
    grid-template-columns: 0.95fr 1.35fr;
    gap: 8mm;
    align-items: stretch;
}}
.metrics-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3.5mm 6mm;
    align-content: center;
}}
.metric-cell {{
    border-bottom: 0.5px solid rgba(255, 255, 255, 0.12);
    padding-bottom: 1.5mm;
}}
.metric-val {{
    font-size: 14pt;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #ffffff;
    line-height: 1.1;
}}
.metric-lbl {{
    font-size: 6.8pt;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: #8e8e93;
    margin-top: 1.2mm;
}}
.booktabs-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7.5pt;
}}
.booktabs-table thead tr {{
    border-top: 1px solid rgba(255, 255, 255, 0.8);
    border-bottom: 0.75px solid rgba(255, 255, 255, 0.3);
}}
.booktabs-table th {{
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    padding: 1.2mm 0;
    color: #f5f5f7;
}}
.booktabs-table td {{
    padding: 1.4mm 0;
    border-bottom: 0.5px solid rgba(255, 255, 255, 0.08);
    vertical-align: middle;
}}
.booktabs-table tbody tr:last-child td {{
    border-bottom: 1px solid rgba(255, 255, 255, 0.8);
}}
.spec-key {{
    color: #a1a1a6;
    width: 25%;
}}
.spec-val {{
    color: #f5f5f7;
    font-weight: 600;
    width: 25%;
}}
</style>
</head>
<body>

<!-- Page 1: COVER WITH "GREET AERO" -->
<div class="page page-cover">
    <div class="running-header">
        <div class="rh-title">AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS</div>
        <div class="rh-section">ENGINEERING MONOGRAPH &amp; TECHNICAL COMPENDIUM</div>
    </div>
    
    <div class="cover-hero-center">
        <div class="cover-slogan">GREET AERO</div>
        <h1 class="cover-main-title">未来飞行</h1>
        <h2 class="cover-sub-title">航空航天飞行系统工程图鉴</h2>
        <div class="cover-hairline"></div>
        <p class="cover-scope-desc">
            工业级智能飞行平台 · 复合翼垂直起降系统 · 高效微型推进总成 · 先进航空复合材料<br>
            A Comprehensive Monograph on Applied Aerodynamics, Flight Dynamics and Structural Mechanics
        </p>

        <div class="cover-four-disciplines">
            <div class="discipline-col">
                <span class="disc-num">01</span>
                <span class="disc-title">AERODYNAMICS</span>
                <span class="disc-cn">流体力学与附面层控制</span>
                <p>普朗特附面层流动、超临界翼梢减阻与微后掠气动声学抑制</p>
            </div>
            <div class="discipline-col">
                <span class="disc-num">02</span>
                <span class="disc-title">FLIGHT DYNAMICS</span>
                <span class="disc-cn">飞行动力学与自适应解耦</span>
                <p>六自由度刚体动力学、倒V尾舵面交叉解耦与倾转推力矢量控制</p>
            </div>
            <div class="discipline-col">
                <span class="disc-num">03</span>
                <span class="disc-title">PROPULSION</span>
                <span class="disc-cn">高效动力总成与电磁优化</span>
                <p>高槽满率外转子无刷马达、动平衡G1.0与闭环LC电源滤波网络</p>
            </div>
            <div class="discipline-col">
                <span class="disc-num">04</span>
                <span class="disc-title">COMPOSITES</span>
                <span class="disc-cn">先进复材与结构力学</span>
                <p>日本东丽T700/T800热压罐共固化、闭口抗扭盒段与蔡-吴破坏校核</p>
            </div>
        </div>
    </div>

    <div class="cover-footer-row">
        <div class="cover-footer-left">
            <div class="corp-brand">AERO ADVANCED DYNAMICS &amp; AUTONOMOUS SYSTEMS LABORATORY</div>
            <div class="corp-sub">AEROSPACE MONOGRAPH CLASSIFICATION : TECH-SPEC-AERO // EDITION 2026-2027</div>
        </div>
        <div class="cover-footer-right">
            <div class="cover-barcode-group">
                <div class="barcode-lines">
                    <span style="width:2px;"></span><span style="width:1px;"></span><span style="width:3px;"></span>
                    <span style="width:1px;"></span><span style="width:2px;"></span><span style="width:4px;"></span>
                    <span style="width:1px;"></span><span style="width:2px;"></span><span style="width:1px;"></span>
                    <span style="width:3px;"></span><span style="width:2px;"></span><span style="width:1px;"></span>
                    <span style="width:4px;"></span><span style="width:2px;"></span><span style="width:1px;"></span>
                    <span style="width:3px;"></span><span style="width:1px;"></span><span style="width:2px;"></span>
                </div>
                <span class="barcode-text">ISBN 978-7-900826-46-0</span>
            </div>
            <div class="page-folio">001</div>
        </div>
    </div>
</div>

<!-- Page 2: VERSO PURE EXHIBIT -->
<div class="page page-verso">
    <div class="running-header">
        <div class="rh-title">AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS</div>
        <div class="rh-section">SYSTEM MONOGRAPH // SECTION 01</div>
    </div>

    <div class="verso-stage">
        <img src="file:///{img_path}" alt="">
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

<!-- Page 3: RECTO EDITORIAL & THEORY -->
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

    <div class="editorial-narrative-columns">
        <p>{item["desc"]}</p>
    </div>

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
                {svg_dark}
            </div>
        </div>
    </div>

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
        <div style="font-size:7.5pt; color:#666666; letter-spacing:0.5px;">AEROSPACE MONOGRAPH // TECHNICAL SPECIFICATION MATRIX</div>
        <div class="page-folio">006</div>
    </div>
</div>

</body>
</html>'''

    with open("e:/brochure/test_output/test_dark_spread.html", "w", encoding="utf-8") as f:
        f.write(html)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 990})
        await page.goto(f"file:///{os.path.abspath('e:/brochure/test_output/test_dark_spread.html').replace('\\', '/')}")
        pages = await page.query_selector_all(".page")
        await pages[0].screenshot(path="e:/brochure/test_output/dark_cover_greet_aero.png")
        await pages[1].screenshot(path="e:/brochure/test_output/dark_verso_sample.png")
        await pages[2].screenshot(path="e:/brochure/test_output/dark_recto_sample.png")
        await browser.close()
    print("Dark spread test completed!")

if __name__ == "__main__":
    asyncio.run(test_dark_mode())
