# -*- coding: utf-8 -*-
"""
测试黑色背景下的不同展台排版效果
"""
import os
import asyncio
from playwright.async_api import async_playwright
import catalog_data_v2

async def test_dark_stages():
    item = catalog_data_v2.ITEMS[0] # AERO-STREAM 7
    img_path = os.path.abspath(os.path.join("e:/brochure/飞机截图", item["image"])).replace("\\", "/")

    html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
@page {{ size: 297mm 210mm; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    background: #0a0a0c;
    color: #f5f5f7;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
}}
.page {{
    width: 297mm;
    height: 210mm;
    background: #0a0a0c;
    padding: 16mm 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
}}
.running-header {{
    display: flex;
    justify-content: space-between;
    border-bottom: 0.75px solid rgba(255, 255, 255, 0.2);
    padding-bottom: 4mm;
    font-size: 8pt;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #a1a1a6;
}}
.running-header strong {{ color: #f5f5f7; }}

/* 方案 A: 极简纯白工作室展台卡片 (Apple Pro Gallery Window) */
.stage-a {{
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 6mm 0;
}}
.window-a {{
    width: 100%;
    height: 140mm;
    background: #ffffff;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    position: relative;
}}
.window-a img {{
    max-width: 95%;
    max-height: 94%;
    object-fit: contain;
}}
.window-a-tag {{
    position: absolute;
    bottom: 8px;
    right: 14px;
    font-size: 8pt;
    font-family: "SF Mono", monospace;
    color: #888;
    letter-spacing: 1px;
}}

/* 方案 B: 柔和羽化消融在黑底中 (Radial Mask / Gradient Vignette) */
.stage-b {{
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 6mm 0;
}}
.window-b {{
    max-width: 100%;
    max-height: 140mm;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}}
.window-b img {{
    max-width: 95%;
    max-height: 135mm;
    object-fit: contain;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.15);
}}

/* 方案 C: 磨砂深灰底展台 (Dark Metallic Pedestal) */
.stage-c {{
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 6mm 0;
}}
.window-c {{
    width: 100%;
    height: 140mm;
    background: #141416;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}}
.window-c img {{
    max-width: 95%;
    max-height: 94%;
    object-fit: contain;
    border-radius: 6px;
}}

.footer {{
    border-top: 0.5px solid rgba(255, 255, 255, 0.15);
    padding-top: 4mm;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}}
.caption-title {{
    font-size: 11pt;
    font-weight: 700;
    color: #f5f5f7;
}}
.caption-sub {{
    font-size: 8pt;
    color: #a1a1a6;
    margin-top: 2px;
}}
.folio {{
    font-size: 10pt;
    font-weight: 700;
    color: #f5f5f7;
}}
</style>
</head>
<body>

<!-- Page 1: 方案 A (纯白工程展窗，极具现代画廊展签质感) -->
<div class="page">
    <div class="running-header">
        <div><strong>AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS</strong></div>
        <div>OPTION A : WHITE GALLERY WINDOW</div>
    </div>
    <div class="stage-a">
        <div class="window-a">
            <img src="file:///{img_path}" alt="">
            <div class="window-a-tag">CAD ISOMETRIC VIEW // {item["code"]}</div>
        </div>
    </div>
    <div class="footer">
        <div>
            <div class="caption-title">01 / {item["name_zh"].split("//")[0].strip()}</div>
            <div class="caption-sub">{item["tagline"]}</div>
        </div>
        <div class="folio">005</div>
    </div>
</div>

<!-- Page 2: 方案 B (带极细微光边框的悬浮图) -->
<div class="page">
    <div class="running-header">
        <div><strong>AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS</strong></div>
        <div>OPTION B : FLOATING FINE-BORDER PLAGUE</div>
    </div>
    <div class="stage-b">
        <div class="window-b">
            <img src="file:///{img_path}" alt="">
        </div>
    </div>
    <div class="footer">
        <div>
            <div class="caption-title">01 / {item["name_zh"].split("//")[0].strip()}</div>
            <div class="caption-sub">{item["tagline"]}</div>
        </div>
        <div class="folio">005</div>
    </div>
</div>

<!-- Page 3: 方案 C (深曜石灰背景舱) -->
<div class="page">
    <div class="running-header">
        <div><strong>AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS</strong></div>
        <div>OPTION C : DARK OBSIDIAN CHAMBER</div>
    </div>
    <div class="stage-c">
        <div class="window-c">
            <img src="file:///{img_path}" alt="">
        </div>
    </div>
    <div class="footer">
        <div>
            <div class="caption-title">01 / {item["name_zh"].split("//")[0].strip()}</div>
            <div class="caption-sub">{item["tagline"]}</div>
        </div>
        <div class="folio">005</div>
    </div>
</div>

</body>
</html>'''

    with open("e:/brochure/test_output/test_dark_stages.html", "w", encoding="utf-8") as f:
        f.write(html)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 990})
        await page.goto(f"file:///{os.path.abspath('e:/brochure/test_output/test_dark_stages.html').replace('\\', '/')}")
        pages = await page.query_selector_all(".page")
        await pages[0].screenshot(path="e:/brochure/test_output/dark_stage_a.png")
        await pages[1].screenshot(path="e:/brochure/test_output/dark_stage_b.png")
        await pages[2].screenshot(path="e:/brochure/test_output/dark_stage_c.png")
        await browser.close()
    print("Dark stages test completed!")

if __name__ == "__main__":
    asyncio.run(test_dark_stages())
