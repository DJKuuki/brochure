# -*- coding: utf-8 -*-
"""
测试圆角精装卡片式展示与微投影效果
"""
import os
import asyncio
from playwright.async_api import async_playwright
import catalog_data_v2

async def test_frame():
    item = catalog_data_v2.ITEMS[0]
    img_path = os.path.abspath(os.path.join("e:/brochure/飞机截图", item["image"])).replace("\\", "/")
    
    html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
@page {{ size: 297mm 210mm; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif;
    background: #fbfbfd;
    color: #1d1d1f;
}}
.page-exhibition {{
    width: 297mm;
    height: 210mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 14mm 20mm 12mm 20mm;
    background: #fbfbfd;
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
}}
.exhibit-cat-pill {{
    font-size: 10px;
    font-weight: 600;
    color: #0071e3;
    background: #ffffff;
    border: 1px solid #e5e5ea;
    padding: 4px 12px;
    border-radius: 12px;
}}
.exhibit-hero {{
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 10px 0;
}}
.hero-stage {{
    width: 100%;
    height: 142mm;
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
    position: relative;
    overflow: hidden;
}}
.hero-stage img {{
    max-width: 95%;
    max-height: 94%;
    object-fit: contain;
    border-radius: 8px;
}}
.stage-watermark {{
    position: absolute;
    bottom: 12px;
    right: 18px;
    font-size: 9.5px;
    font-family: "SF Mono", Consolas, monospace;
    font-weight: 600;
    color: #d2d2d7;
    letter-spacing: 1px;
}}
.exhibit-bottom {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid #e5e5ea;
    padding-top: 8px;
}}
.exhibit-name-block h2 {{
    font-size: 17px;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: #1d1d1f;
}}
.exhibit-name-block p {{
    font-size: 11px;
    color: #86868b;
    margin-top: 2px;
}}
.exhibit-folio {{
    font-size: 14px;
    font-weight: 600;
    color: #86868b;
    font-variant-numeric: tabular-nums;
}}
</style>
</head>
<body>
<div class="page-exhibition">
    <div class="exhibit-top">
        <div class="exhibit-series">EXHIBIT // 01 · AERO MASTER BLUEPRINT</div>
        <div class="exhibit-cat-pill">{item["category_zh"]} · {item["category_en"]}</div>
    </div>
    <div class="exhibit-hero">
        <div class="hero-stage">
            <img src="file:///{img_path}" alt="">
            <div class="stage-watermark">ENGINEERING CAD RENDERING // 3D MODEL ISOMETRIC</div>
        </div>
    </div>
    <div class="exhibit-bottom">
        <div class="exhibit-name-block">
            <h2>{item["name_zh"]}</h2>
            <p>{item["name_en"]} — {item["code"]}</p>
        </div>
        <div class="exhibit-folio">005</div>
    </div>
</div>
</body>
</html>'''

    with open("e:/brochure/test_output/test_frame.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 990})
        await page.goto(f"file:///{os.path.abspath('e:/brochure/test_output/test_frame.html').replace('\\', '/')}")
        await page.screenshot(path="e:/brochure/test_output/sample_frame.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_frame())
