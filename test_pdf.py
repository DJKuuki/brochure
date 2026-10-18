import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        img_path = os.path.abspath(r'e:\brochure\飞机截图\7.jpg').replace('\\', '/')
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ background: #0b0f19; color: #fff; font-family: sans-serif; }}
                img {{ width: 400px; border-radius: 8px; }}
            </style>
        </head>
        <body>
            <h1>Aero Test</h1>
            <img src="file:///{img_path}" />
        </body>
        </html>
        """
        await page.set_content(html)
        pdf = await page.pdf(width='297mm', height='210mm', print_background=True)
        print(f"Generated test PDF, size: {len(pdf)} bytes")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
