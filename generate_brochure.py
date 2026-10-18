# -*- coding: utf-8 -*-
"""
无人机宣传画册生成脚本 - 50P完整版 (无任何占位图，46张真实截图全覆盖)
"""

import os
import sys
import asyncio
from playwright.async_api import async_playwright
import catalog_data

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
IMG_DIR = os.path.join(BASE_DIR, "飞机截图")

def get_img_src(filename):
    """获取图片的绝对路径URI"""
    full_path = os.path.join(IMG_DIR, filename).replace("\\", "/")
    return f"file:///{full_path}"

def build_css():
    """科技感航空工业画册全局样式"""
    return """
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800;900&family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&display=swap');

    @page {
        size: 297mm 210mm;
        margin: 0;
    }

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        font-family: 'Rajdhani', -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
        background-color: #06090e;
        color: #e2e8f0;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }

    .page {
        width: 297mm;
        height: 210mm;
        page-break-after: always;
        position: relative;
        overflow: hidden;
        background: radial-gradient(circle at 50% 30%, #0d131f 0%, #06090e 100%);
        padding: 10mm 12mm;
        display: flex;
        flex-direction: column;
    }

    /* 科技感背景网格 */
    .tech-grid-overlay {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-image: 
            linear-gradient(rgba(0, 240, 255, 0.025) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 240, 255, 0.025) 1px, transparent 1px);
        background-size: 15mm 15mm;
        pointer-events: none;
        z-index: 1;
    }

    /* 页面四角科技卡槽准星 */
    .hud-corner {
        position: absolute;
        width: 14mm;
        height: 14mm;
        pointer-events: none;
        z-index: 2;
    }
    .hud-corner.tl { top: 6mm; left: 6mm; border-top: 1.5px solid #00f0ff; border-left: 1.5px solid #00f0ff; }
    .hud-corner.tr { top: 6mm; right: 6mm; border-top: 1.5px solid #00f0ff; border-right: 1.5px solid #00f0ff; }
    .hud-corner.bl { bottom: 6mm; left: 6mm; border-bottom: 1.5px solid #00f0ff; border-left: 1.5px solid #00f0ff; }
    .hud-corner.br { bottom: 6mm; right: 6mm; border-bottom: 1.5px solid #00f0ff; border-right: 1.5px solid #00f0ff; }

    /* 顶部航电状态栏 */
    .page-header {
        position: relative;
        z-index: 3;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(0, 240, 255, 0.25);
        padding-bottom: 2mm;
        margin-bottom: 3mm;
        font-family: 'Share Tech Mono', monospace;
        font-size: 8.5pt;
        letter-spacing: 1px;
        color: #7dd3fc;
    }
    .page-header .left-meta {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .page-header .badge {
        background: rgba(0, 240, 255, 0.12);
        border: 1px solid rgba(0, 240, 255, 0.4);
        padding: 1px 6px;
        border-radius: 2px;
        color: #38bdf8;
        font-weight: bold;
    }
    .page-header .center-meta {
        color: #94a3b8;
        letter-spacing: 2px;
    }
    .page-header .right-meta {
        color: #38bdf8;
    }

    /* 底部打印与页码指示栏 */
    .page-footer {
        position: relative;
        z-index: 3;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-top: 1px solid rgba(0, 240, 255, 0.2);
        padding-top: 2mm;
        margin-top: auto;
        font-family: 'Share Tech Mono', monospace;
        font-size: 8pt;
        color: #64748b;
    }
    .page-footer .print-indicator {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(0, 240, 255, 0.3);
        padding: 2px 10px;
        border-radius: 3px;
        color: #38bdf8;
        font-weight: 600;
        letter-spacing: 1.5px;
    }
    .page-footer .page-number {
        font-family: 'Orbitron', sans-serif;
        font-size: 9.5pt;
        font-weight: 700;
        color: #00f0ff;
        letter-spacing: 2px;
    }

    /* ==========================================================
       正面大图页 (OBVERSE PAGE) 专用样式
       ========================================================== */
    .obverse-content {
        position: relative;
        z-index: 3;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .obverse-hero-viewport {
        position: relative;
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        background: radial-gradient(circle at center, #ffffff 0%, #edf2f7 65%, #cbd5e1 100%);
        border-radius: 6px;
        border: 1px solid rgba(0, 240, 255, 0.4);
        box-shadow: 0 0 30px rgba(0, 240, 255, 0.15) inset, 0 10px 25px rgba(0, 0, 0, 0.5);
        overflow: hidden;
        margin: 1mm 0 3mm 0;
        padding: 5mm;
    }
    .obverse-hero-viewport .viewport-grid {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-image: 
            linear-gradient(rgba(0, 50, 100, 0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 50, 100, 0.04) 1px, transparent 1px);
        background-size: 10mm 10mm;
        pointer-events: none;
    }
    .obverse-hero-viewport .crosshair {
        position: absolute;
        width: 16px;
        height: 16px;
        pointer-events: none;
        opacity: 0.35;
    }
    .obverse-hero-viewport .crosshair.c-tl { top: 8px; left: 8px; border-top: 1px solid #0284c7; border-left: 1px solid #0284c7; }
    .obverse-hero-viewport .crosshair.c-br { bottom: 8px; right: 8px; border-bottom: 1px solid #0284c7; border-right: 1px solid #0284c7; }

    .obverse-hero-viewport img {
        max-width: 95%;
        max-height: 94%;
        object-fit: contain;
        position: relative;
        z-index: 2;
        filter: drop-shadow(0 15px 20px rgba(0, 0, 0, 0.25));
    }
    .obverse-title-bar {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        background: rgba(11, 17, 28, 0.85);
        border: 1px solid rgba(0, 240, 255, 0.25);
        border-radius: 4px;
        padding: 2.5mm 4mm;
    }
    .obverse-title-bar .title-group h2 {
        font-family: 'Orbitron', 'PingFang SC', sans-serif;
        font-size: 15pt;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: 1px;
        text-shadow: 0 0 10px rgba(0, 240, 255, 0.4);
    }
    .obverse-title-bar .title-group .sub-name {
        font-family: 'Rajdhani', sans-serif;
        font-size: 10pt;
        color: #38bdf8;
        font-weight: 600;
        letter-spacing: 1.5px;
    }
    .obverse-title-bar .title-group .tagline {
        font-size: 8.5pt;
        color: #94a3b8;
        margin-top: 1px;
    }
    .obverse-capsules {
        display: flex;
        gap: 3mm;
    }
    .capsule {
        background: rgba(0, 240, 255, 0.08);
        border: 1px solid rgba(0, 240, 255, 0.35);
        border-radius: 3px;
        padding: 2px 7px;
        text-align: right;
    }
    .capsule .cap-lbl {
        font-family: 'Share Tech Mono', monospace;
        font-size: 6.5pt;
        color: #7dd3fc;
        display: block;
    }
    .capsule .cap-val {
        font-family: 'Orbitron', sans-serif;
        font-size: 10pt;
        font-weight: 700;
        color: #00f0ff;
    }

    /* ==========================================================
       背面介绍页 (REVERSE PAGE) 专用样式
       ========================================================== */
    .reverse-content {
        position: relative;
        z-index: 3;
        flex: 1;
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 4.5mm;
        margin: 1mm 0 2mm 0;
    }
    .reverse-left-col {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .prod-intro-box {
        background: rgba(15, 23, 42, 0.65);
        border-left: 3px solid #00f0ff;
        padding: 2.5mm 3.5mm;
        border-radius: 0 4px 4px 0;
        margin-bottom: 2mm;
    }
    .prod-intro-box h2 {
        font-family: 'Orbitron', 'PingFang SC', sans-serif;
        font-size: 13pt;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 1px;
    }
    .prod-intro-box .code-tag {
        font-family: 'Share Tech Mono', monospace;
        font-size: 8pt;
        color: #38bdf8;
        margin-bottom: 1.5mm;
        display: block;
    }
    .prod-intro-box p {
        font-size: 8.5pt;
        line-height: 1.45;
        color: #cbd5e1;
        text-align: justify;
    }

    /* 技术亮点4格 */
    .highlights-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2mm;
        margin-bottom: 2mm;
    }
    .hl-card {
        background: rgba(11, 18, 30, 0.8);
        border: 1px solid rgba(0, 240, 255, 0.2);
        border-radius: 4px;
        padding: 2mm 2.5mm;
        position: relative;
    }
    .hl-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 3px; height: 100%;
        background: #00f0ff;
    }
    .hl-card .hl-title {
        font-family: 'Orbitron', 'PingFang SC', sans-serif;
        font-size: 8pt;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 1px;
    }
    .hl-card .hl-desc {
        font-size: 7.2pt;
        line-height: 1.35;
        color: #94a3b8;
    }

    /* 核心技术参数表 */
    .specs-table-box {
        background: rgba(11, 18, 30, 0.85);
        border: 1px solid rgba(0, 240, 255, 0.25);
        border-radius: 4px;
        overflow: hidden;
    }
    .specs-table-box .table-head {
        background: rgba(0, 240, 255, 0.12);
        padding: 1.5mm 3mm;
        font-family: 'Share Tech Mono', monospace;
        font-size: 7.5pt;
        color: #00f0ff;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
    }
    .specs-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 7.5pt;
    }
    .specs-table tr {
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    .specs-table tr:last-child {
        border-bottom: none;
    }
    .specs-table td {
        padding: 1.2mm 2.5mm;
    }
    .specs-table td.lbl {
        color: #7dd3fc;
        font-weight: 600;
        width: 44%;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    .specs-table td.val {
        color: #f8fafc;
        font-family: 'Share Tech Mono', sans-serif;
        font-weight: 600;
    }

    /* 右侧真实副图区 (严格展示真实截图模型，无占位符) */
    .reverse-right-col {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        gap: 3mm;
    }
    .sub-image-card {
        background: radial-gradient(circle at center, #ffffff 0%, #edf2f7 65%, #cbd5e1 100%);
        border: 1px solid rgba(0, 240, 255, 0.35);
        border-radius: 4px;
        padding: 3mm;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        flex: 1;
        overflow: hidden;
        min-height: 95mm;
    }
    .sub-image-card img {
        max-width: 95%;
        max-height: 82%;
        object-fit: contain;
        filter: drop-shadow(0 8px 12px rgba(0,0,0,0.25));
    }
    .sub-image-card .caption {
        position: absolute;
        bottom: 0; left: 0; right: 0;
        background: rgba(11, 18, 30, 0.92);
        color: #38bdf8;
        font-family: 'Share Tech Mono', sans-serif;
        font-size: 7.5pt;
        padding: 2mm 3mm;
        text-align: center;
        border-top: 1px solid rgba(0, 240, 255, 0.3);
        letter-spacing: 0.5px;
    }

    /* 真实航电遥测与性能雷达数据面板 (取代原本千篇一律的占位框) */
    .telemetry-metrics-panel {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(0, 240, 255, 0.25);
        border-radius: 4px;
        padding: 2.5mm 3.5mm;
        display: flex;
        flex-direction: column;
        gap: 1.5mm;
    }
    .metrics-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Share Tech Mono', monospace;
        font-size: 7.2pt;
        color: #7dd3fc;
        border-bottom: 1px solid rgba(0, 240, 255, 0.15);
        padding-bottom: 1mm;
    }
    .metrics-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2mm;
    }
    .metric-item {
        background: rgba(11, 18, 30, 0.6);
        border-left: 2px solid #00f0ff;
        padding: 1.5mm 2mm;
        font-family: 'Share Tech Mono', monospace;
        font-size: 7pt;
    }
    .metric-item .m-lbl { color: #94a3b8; }
    .metric-item .m-val { color: #38bdf8; font-weight: bold; float: right; }

    /* ==========================================================
       封面 (FRONT COVER) 专用样式
       ========================================================== */
    .cover-page {
        padding: 0;
        background: #04060a;
    }
    .cover-container {
        width: 100%;
        height: 100%;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 14mm 16mm;
        z-index: 2;
    }
    .cover-bg-glow {
        position: absolute;
        top: 20%; left: 35%;
        width: 450px; height: 450px;
        background: radial-gradient(circle, rgba(0, 240, 255, 0.18) 0%, rgba(2, 132, 199, 0.05) 50%, transparent 70%);
        pointer-events: none;
    }
    .cover-header-line {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #00f0ff;
        padding-bottom: 3mm;
        font-family: 'Share Tech Mono', monospace;
        font-size: 9.5pt;
        color: #38bdf8;
        letter-spacing: 2px;
    }
    .cover-main-content {
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 10mm;
        align-items: center;
        margin: 5mm 0;
    }
    .cover-titles h1 {
        font-family: 'Orbitron', 'PingFang SC', sans-serif;
        font-size: 28pt;
        font-weight: 900;
        line-height: 1.15;
        color: #ffffff;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 3mm;
        text-shadow: 0 0 20px rgba(0, 240, 255, 0.5);
    }
    .cover-titles .eng-sub {
        font-family: 'Orbitron', sans-serif;
        font-size: 13.5pt;
        font-weight: 700;
        color: #00f0ff;
        letter-spacing: 3px;
        margin-bottom: 5mm;
        display: block;
    }
    .cover-titles .desc-text {
        font-size: 10pt;
        line-height: 1.6;
        color: #cbd5e1;
        max-width: 520px;
        border-left: 3px solid #38bdf8;
        padding-left: 4mm;
        margin-bottom: 6mm;
    }
    .cover-feature-pills {
        display: flex;
        gap: 3mm;
        flex-wrap: wrap;
    }
    .cover-pill {
        background: rgba(0, 240, 255, 0.08);
        border: 1px solid rgba(0, 240, 255, 0.4);
        padding: 2mm 4mm;
        border-radius: 3px;
        font-size: 8pt;
        color: #7dd3fc;
        font-weight: 600;
    }
    .cover-hero-box {
        position: relative;
        background: radial-gradient(circle at center, #ffffff 0%, #e2e8f0 70%, #94a3b8 100%);
        border-radius: 8px;
        border: 2px solid #00f0ff;
        box-shadow: 0 0 40px rgba(0, 240, 255, 0.35);
        padding: 6mm;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 105mm;
    }
    .cover-hero-box img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        filter: drop-shadow(0 15px 25px rgba(0,0,0,0.4));
    }
    .cover-footer-line {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        border-top: 1px solid rgba(0, 240, 255, 0.3);
        padding-top: 3mm;
        font-family: 'Share Tech Mono', monospace;
        font-size: 8pt;
        color: #64748b;
    }

    /* ==========================================================
       目录页 (TABLE OF CONTENTS) 专用样式
       ========================================================== */
    .toc-container {
        position: relative;
        z-index: 3;
        flex: 1;
        display: grid;
        grid-template-columns: 0.9fr 1.1fr;
        gap: 8mm;
        padding: 3mm 0;
    }
    .toc-left-intro {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(0, 240, 255, 0.2);
        border-radius: 6px;
        padding: 5mm;
    }
    .toc-left-intro h2 {
        font-family: 'Orbitron', 'PingFang SC', sans-serif;
        font-size: 16pt;
        color: #ffffff;
        margin-bottom: 2mm;
    }
    .toc-left-intro .toc-tagline {
        color: #38bdf8;
        font-size: 9.5pt;
        font-weight: 600;
        margin-bottom: 4mm;
    }
    .toc-left-intro p {
        font-size: 8.8pt;
        line-height: 1.6;
        color: #cbd5e1;
        text-align: justify;
        margin-bottom: 3mm;
    }
    .toc-pillars {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2.5mm;
        margin-top: 3mm;
    }
    .pillar-box {
        background: rgba(11, 18, 30, 0.9);
        border: 1px solid rgba(0, 240, 255, 0.25);
        padding: 2.5mm;
        border-radius: 3px;
    }
    .pillar-box .p-title {
        color: #00f0ff;
        font-size: 8pt;
        font-weight: bold;
    }
    .pillar-box .p-desc {
        color: #94a3b8;
        font-size: 7pt;
    }
    .toc-right-list {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .toc-section-card {
        background: rgba(11, 18, 30, 0.85);
        border: 1px solid rgba(0, 240, 255, 0.25);
        border-radius: 4px;
        padding: 2.5mm 3.5mm;
        margin-bottom: 2mm;
    }
    .toc-section-card .sec-head {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(0, 240, 255, 0.2);
        padding-bottom: 1mm;
        margin-bottom: 1.5mm;
    }
    .toc-section-card .sec-title {
        font-family: 'Orbitron', 'PingFang SC', sans-serif;
        font-size: 9pt;
        font-weight: 700;
        color: #ffffff;
    }
    .toc-section-card .sec-pages {
        font-family: 'Share Tech Mono', monospace;
        font-size: 8pt;
        color: #00f0ff;
        font-weight: bold;
    }
    .toc-section-card .sec-items {
        font-size: 7.5pt;
        color: #94a3b8;
        line-height: 1.4;
    }

    /* ==========================================================
       试验与制造体系 (PAGE 49) 专用样式
       ========================================================== */
    .qa-container {
        position: relative;
        z-index: 3;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 2mm 0;
    }
    .qa-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 4mm;
        margin-top: 3mm;
    }
    .qa-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(0, 240, 255, 0.25);
        border-radius: 5px;
        padding: 4mm;
        position: relative;
    }
    .qa-card .qa-step {
        position: absolute;
        top: 3mm; right: 4mm;
        font-family: 'Orbitron', sans-serif;
        font-size: 16pt;
        font-weight: 900;
        color: rgba(0, 240, 255, 0.15);
    }
    .qa-card h3 {
        font-family: 'Orbitron', 'PingFang SC', sans-serif;
        font-size: 10.5pt;
        color: #38bdf8;
        margin-bottom: 2mm;
    }
    .qa-card p {
        font-size: 8pt;
        line-height: 1.5;
        color: #cbd5e1;
    }

    /* ==========================================================
       封底 (BACK COVER) 专用样式
       ========================================================== */
    .back-cover-page {
        padding: 0;
        background: #04060a;
    }
    .back-cover-container {
        width: 100%;
        height: 100%;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 16mm;
        z-index: 2;
        text-align: center;
    }
    .back-brand-box {
        margin-top: 15mm;
    }
    .back-brand-box h1 {
        font-family: 'Orbitron', sans-serif;
        font-size: 24pt;
        font-weight: 900;
        letter-spacing: 4px;
        color: #ffffff;
        margin-bottom: 3mm;
        text-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
    }
    .back-brand-box .motto {
        font-family: 'Orbitron', 'PingFang SC', sans-serif;
        font-size: 12pt;
        color: #00f0ff;
        letter-spacing: 3px;
        margin-bottom: 8mm;
    }
    .back-specs-summary {
        display: flex;
        justify-content: center;
        gap: 6mm;
        margin: 5mm 0;
    }
    .back-stat {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(0, 240, 255, 0.3);
        padding: 4mm 6mm;
        border-radius: 4px;
        min-width: 120px;
    }
    .back-stat .num {
        font-family: 'Orbitron', sans-serif;
        font-size: 18pt;
        font-weight: 800;
        color: #38bdf8;
    }
    .back-stat .lbl {
        font-size: 7.5pt;
        color: #94a3b8;
        font-family: 'Share Tech Mono', monospace;
    }
    .back-legal-box {
        border-top: 1px solid rgba(0, 240, 255, 0.25);
        padding-top: 4mm;
        font-family: 'Share Tech Mono', monospace;
        font-size: 7.5pt;
        color: #64748b;
        line-height: 1.6;
    }
    """

def render_cover_page():
    hero_src = get_img_src("ScreenShot_2026-10-18_004138_699.png")
    return f"""
    <div class="page cover-page">
        <div class="tech-grid-overlay"></div>
        <div class="cover-bg-glow"></div>
        <div class="hud-corner tl"></div>
        <div class="hud-corner tr"></div>
        <div class="hud-corner bl"></div>
        <div class="hud-corner br"></div>
        
        <div class="cover-container">
            <div class="cover-header-line">
                <span>[AEROSPACE CLASSIFIED // LEVEL 5]</span>
                <span>SYSTEM BLUEPRINT CATALOGUE</span>
                <span>EDITION 2026-2027</span>
            </div>
            
            <div class="cover-main-content">
                <div class="cover-titles">
                    <span class="eng-sub">AEROSPACE DYNAMICS // FLIGHT LAB</span>
                    <h1>尖端无人机与飞行系统工程图鉴</h1>
                    <div class="desc-text">
                        基于高强度航空碳复合材料、分布式多旋翼升力架构与前沿飞控算法。全景解构长航时察打一体无人机、重型垂直起降突击旋翼机、大展弦比太阳能滑翔机及工业级高载荷作业平台。
                    </div>
                    <div class="cover-feature-pills">
                        <span class="cover-pill">23大核心飞行器专题</span>
                        <span class="cover-pill">46款高精CAD模型解构</span>
                        <span class="cover-pill">单面印刷·背对背对裱精装</span>
                        <span class="cover-pill">MIL-STD 军工级标准规范</span>
                    </div>
                </div>
                
                <div class="cover-hero-box">
                    <img src="{hero_src}" alt="Valkyrie Gunship" />
                </div>
            </div>
            
            <div class="cover-footer-line">
                <span>PRINT MARK: SINGLE-SIDED ALBUM EDITION</span>
                <span>TOTAL 50 PAGES ARCHIVE</span>
                <span class="page-number">PAGE 01 / 50 [COVER · 封面]</span>
            </div>
        </div>
    </div>
    """

def render_toc_page():
    return f"""
    <div class="page">
        <div class="tech-grid-overlay"></div>
        <div class="hud-corner tl"></div>
        <div class="hud-corner tr"></div>
        <div class="hud-corner bl"></div>
        <div class="hud-corner br"></div>
        
        <div class="page-header">
            <div class="left-meta">
                <span class="badge">SEC-00</span>
                <span>ENGINEERING OVERVIEW // TABLE OF CONTENTS</span>
            </div>
            <div class="center-meta">全景图鉴目录与工程序言</div>
            <div class="right-meta">SYS.REF: AGY-INDEX-2026</div>
        </div>
        
        <div class="toc-container">
            <div class="toc-left-intro">
                <div>
                    <h2>未来飞行工程序言</h2>
                    <div class="toc-tagline">突破气动与材料的物理极限 · 赋能全自主空域智能</div>
                    <p>
                        人类对蓝天的探索正在从单一载人飞行的宏观时代，全面迈入高智能、分布式、多构型的无人机系统（UAV）新纪元。本图鉴汇集了当代航空工程中最具代表性的尖端飞行器三维CAD模型与工程测试图样。
                    </p>
                    <p>
                        从万米高空执行超长巡逻的察打一体中空长航时无人机，到突破传统形态的串列双翼与飞翼隐身测绘机；从承载几十公斤药液与货物的六旋翼工业巨兽，到以每小时200公里极速翻滚穿越的竞技FPV穿梭机，每一个模型都凝聚了轻量化碳纤结构、流体仿真拓扑与动力推进学的心血。
                    </p>
                </div>
                
                <div>
                    <div style="font-family:'Orbitron'; font-size:9pt; color:#00f0ff; margin-bottom:1.5mm;">
                        FIVE CORE ARCHITECTURES // 五大技术基石
                    </div>
                    <div class="toc-pillars">
                        <div class="pillar-box">
                            <div class="p-title">01 拓扑轻量化机身</div>
                            <div class="p-desc">T700/T800热压罐共固化</div>
                        </div>
                        <div class="pillar-box">
                            <div class="p-title">02 复合升力推进链</div>
                            <div class="p-desc">垂起平飞双模无缝过渡</div>
                        </div>
                        <div class="pillar-box">
                            <div class="p-title">03 全自主抗扰飞控</div>
                            <div class="p-desc">RTK双天线差分+视觉SLAM</div>
                        </div>
                        <div class="pillar-box">
                            <div class="p-title">04 高能效外转子动力</div>
                            <div class="p-desc">0.2mm硅钢片与折叠碳桨</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="toc-right-list">
                <div class="toc-section-card">
                    <div class="sec-head">
                        <span class="sec-title">PART I · 战略察打、未来突击与复合翼</span>
                        <span class="sec-pages">P03 - P10</span>
                    </div>
                    <div class="sec-items">
                        AERO-REAPER 3000 (P03-04) · VALKYRIE 突击机 (P05-06) · HORIZON-X 复合翼 (P07-08) · HYBRID-CARGO 货运机 (P09-10)
                    </div>
                </div>
                
                <div class="toc-section-card">
                    <div class="sec-head">
                        <span class="sec-title">PART II · 工业植保、重载运输与智能巡检</span>
                        <span class="sec-pages">P11 - P20</span>
                    </div>
                    <div class="sec-items">
                        AGRI-TITAN 植保机 (P11-12) · TITAN-CARRIER 运输机 (P13-14) · HEXA-PATROL 巡检机 (P15-16) · SKY-SURVEYOR 测绘机 (P17-18) · PHANTOM WING 飞翼 (P19-20)
                    </div>
                </div>
                
                <div class="toc-section-card">
                    <div class="sec-head">
                        <span class="sec-title">PART III · 串列双翼、战术直升机与工程CAD</span>
                        <span class="sec-pages">P21 - P30</span>
                    </div>
                    <div class="sec-items">
                        AERO-TANDEM 双翼机 (P21-22) · V-TAIL SCOUT (P23-24) · CYBER-COPTER 直升机 (P25-26) · TILT-ROTOR CAD标注机 (P27-28) · AERO-STREAM 航拍机 (P29-30)
                    </div>
                </div>
                
                <div class="toc-section-card">
                    <div class="sec-head">
                        <span class="sec-title">PART IV · 室内涵道、竞技穿梭与一体机身</span>
                        <span class="sec-pages">P31 - P44</span>
                    </div>
                    <div class="sec-items">
                        CINE-SHIELD 涵道机 (P31-32) · SPECTER 远距机架 (P33-34) · APEX 花飞机 (P35-36) · TACTICAL STRIKE (P37-38) · AUTONOMOUS LAB (P39-40) · CARBON-MONOCOQUE (P41-42)
                    </div>
                </div>
                
                <div class="toc-section-card">
                    <div class="sec-head">
                        <span class="sec-title">PART V · 航空电机动力总成与制造检验体系</span>
                        <span class="sec-pages">P43 - P50</span>
                    </div>
                    <div class="sec-items">
                        AERO-PROPULSION 动力总成 (P43-44) · 外转子电机 (P45-46) · 螺旋桨矩阵与分电 (P47-48) · 航空制造品质体系 (P49) · 封底与合规认证 (P50)
                    </div>
                </div>
            </div>
        </div>
        
        <div class="page-footer">
            <span class="print-indicator">PRINT INSTRUCTION: BINDING DIRECTORY</span>
            <span>BLUEPRINT SYSTEM ARCHITECTURE</span>
            <span class="page-number">PAGE 02 / 50 [REVERSE · 目录]</span>
        </div>
    </div>
    """

def render_obverse_page(prod, page_num):
    """渲染奇数页：正面模型大图展示"""
    img_src = get_img_src(prod["front_image"])
    
    # 提取3个胶囊指标
    capsule_items = prod["specs"][:3]
    capsules_html = ""
    for c in capsule_items:
        capsules_html += f"""
        <div class="capsule">
            <span class="cap-lbl">{c['label']}</span>
            <span class="cap-val">{c['value']}</span>
        </div>
        """
        
    return f"""
    <div class="page">
        <div class="tech-grid-overlay"></div>
        <div class="hud-corner tl"></div>
        <div class="hud-corner tr"></div>
        <div class="hud-corner bl"></div>
        <div class="hud-corner br"></div>
        
        <div class="page-header">
            <div class="left-meta">
                <span class="badge">{prod['id']}</span>
                <span>{prod['category_en']} // MODEL VIEWPORT</span>
            </div>
            <div class="center-meta">{prod['category_zh']} · 高清全貌工程图</div>
            <div class="right-meta">{prod['code']}</div>
        </div>
        
        <div class="obverse-content">
            <div class="obverse-hero-viewport">
                <div class="viewport-grid"></div>
                <div class="crosshair c-tl"></div>
                <div class="crosshair c-br"></div>
                <img src="{img_src}" alt="{prod['name_zh']}" />
            </div>
            
            <div class="obverse-title-bar">
                <div class="title-group">
                    <div class="sub-name">{prod['name_en']}</div>
                    <h2>{prod['name_zh']}</h2>
                    <div class="tagline">{prod['tagline']}</div>
                </div>
                <div class="obverse-capsules">
                    {capsules_html}
                </div>
            </div>
        </div>
        
        <div class="page-footer">
            <span class="print-indicator">OBVERSE [展面] · 正面全幅模型图</span>
            <span>AERODYNAMICS DESIGN & MODELING</span>
            <span class="page-number">PAGE {page_num:02d} / 50</span>
        </div>
    </div>
    """

def render_reverse_page(prod, page_num):
    """渲染偶数页：背面深度产品介绍、参数表与专属真实副图 (无任何占位图)"""
    # 4个亮点卡片
    hl_cards_html = ""
    for hl in prod["highlights"]:
        hl_cards_html += f"""
        <div class="hl-card">
            <div class="hl-title">{hl['title']}</div>
            <div class="hl-desc">{hl['detail']}</div>
        </div>
        """
        
    # 8个参数行
    specs_rows_html = ""
    for sp in prod["specs"]:
        specs_rows_html += f"""
        <tr>
            <td class="lbl">{sp['label']}</td>
            <td class="val">{sp['value']}</td>
        </tr>
        """
        
    # 右侧展示真实的副图 (100% 真实航空模型图片)
    sub_src = get_img_src(prod["back_sub_image"])
    sub_caption = prod["back_sub_caption"]
    
    # 提取第4~7项指标作为右侧航电数据展示
    metrics_items = prod["specs"][3:7]
    metrics_html = ""
    for m in metrics_items:
        metrics_html += f"""
        <div class="metric-item">
            <span class="m-lbl">{m['label']}</span>
            <span class="m-val">{m['value']}</span>
        </div>
        """
        
    return f"""
    <div class="page">
        <div class="tech-grid-overlay"></div>
        <div class="hud-corner tl"></div>
        <div class="hud-corner tr"></div>
        <div class="hud-corner bl"></div>
        <div class="hud-corner br"></div>
        
        <div class="page-header">
            <div class="left-meta">
                <span class="badge">{prod['id']}</span>
                <span>{prod['category_en']} // TECHNICAL SPECIFICATION</span>
            </div>
            <div class="center-meta">{prod['category_zh']} · 深度技术规格与解构</div>
            <div class="right-meta">{prod['code']}</div>
        </div>
        
        <div class="reverse-content">
            <div class="reverse-left-col">
                <div class="prod-intro-box">
                    <h2>{prod['name_zh']}</h2>
                    <span class="code-tag">{prod['name_en']} // {prod['code']}</span>
                    <p>{prod['desc']}</p>
                </div>
                
                <div class="highlights-grid">
                    {hl_cards_html}
                </div>
                
                <div class="specs-table-box">
                    <div class="table-head">
                        <span>ENGINEERING SPECIFICATION TABLE</span>
                        <span>[STANDARD METRIC UNITS]</span>
                    </div>
                    <table class="specs-table">
                        {specs_rows_html}
                    </table>
                </div>
            </div>
            
            <div class="reverse-right-col">
                <div class="sub-image-card">
                    <img src="{sub_src}" alt="{sub_caption}" />
                    <div class="caption">{sub_caption}</div>
                </div>
                
                <div class="telemetry-metrics-panel">
                    <div class="metrics-header">
                        <span>AEROSPACE SYSTEM TELEMETRY & RATINGS</span>
                        <span>CERT: MIL-STD-810H</span>
                    </div>
                    <div class="metrics-grid">
                        {metrics_html}
                    </div>
                </div>
            </div>
        </div>
        
        <div class="page-footer">
            <span class="print-indicator">REVERSE [详述] · 背面产品深度解析</span>
            <span>AEROSPACE SYSTEMS ENGINEERING</span>
            <span class="page-number">PAGE {page_num:02d} / 50</span>
        </div>
    </div>
    """

def render_qa_page():
    return f"""
    <div class="page">
        <div class="tech-grid-overlay"></div>
        <div class="hud-corner tl"></div>
        <div class="hud-corner tr"></div>
        <div class="hud-corner bl"></div>
        <div class="hud-corner br"></div>
        
        <div class="page-header">
            <div class="left-meta">
                <span class="badge">SEC-99</span>
                <span>MANUFACTURING & QUALITY ASSURANCE</span>
            </div>
            <div class="center-meta">航空制造工艺与极限可靠性测试体系</div>
            <div class="right-meta">STD: ISO-AS9100D</div>
        </div>
        
        <div class="qa-container">
            <div style="background:rgba(15,23,42,0.65); border-left:3px solid #00f0ff; padding:3mm 4mm; border-radius:0 4px 4px 0;">
                <h2 style="font-family:'Orbitron','PingFang SC'; font-size:15pt; color:#ffffff; margin-bottom:1mm;">
                    航空级精密制造与严苛试验验证标准
                </h2>
                <p style="font-size:9pt; line-height:1.5; color:#cbd5e1;">
                    每一款飞行器从CAD概念草图转化为实体机，必须历经结构力学、气动声学、高低温湿热耐受性及全域电磁兼容等四大维度的军规级严苛考验。依托数字化数控机加、碳纤维热压罐共固化以及硬件在环飞控仿真平台，确保每一架交付的飞行系统在极端严寒、荒漠沙尘与强风恶浪中稳如磐石。
                </p>
            </div>
            
            <div class="qa-grid">
                <div class="qa-card">
                    <div class="qa-step">01</div>
                    <h3>碳纤维复合材料热压共固化工艺</h3>
                    <p>采用东丽高强度T700/T800预浸布，在0.6MPa高压与130℃恒温热压罐中一体成型。彻底消除内部微孔隙与分层隐患，相比传统注塑塑料机架结构刚度提升350%，重量降低50%以上。</p>
                </div>
                
                <div class="qa-card">
                    <div class="qa-step">02</div>
                    <h3>全温区全天候环境风洞试验</h3>
                    <p>在大型数字化连续式低速风洞中完成0-40m/s风速连续测试，涵盖8级烈风迎头冲击、侧风悬停及高空紊流切变。在-40℃极寒冰冻与+65℃戈壁暴晒仓内验证动力电池放电与电机轴承耐候性。</p>
                </div>
                
                <div class="qa-card">
                    <div class="qa-step">03</div>
                    <h3>军标级电磁兼容 (EMC/EMI) 屏蔽</h3>
                    <p>全金属机壳与特种导电银漆喷涂屏蔽舱，严格符合MIL-STD-461G标准。隔绝高压输电线路产生的高压工频电场与强磁场谐波，确保GPS/RTK高精度卫星定位与无线遥测跳频链路零掉线。</p>
                </div>
                
                <div class="qa-card">
                    <div class="qa-step">04</div>
                    <h3>六自由度 (6-DOF) 硬件在环仿真</h3>
                    <p>飞控系统在出厂前全面接入六自由度实时仿真转台，历经超过10,000小时的虚拟极端故障注入测试（包括强风暴、电机断桨、传感器单边失效等），自适应控制算法可在毫秒级重构平衡。</p>
                </div>
            </div>
            
            <div style="background:rgba(11,18,30,0.85); border:1px solid rgba(0,240,255,0.3); border-radius:4px; padding:3mm 5mm; display:flex; justify-content:space-between; align-items:center; margin-top:3mm;">
                <div style="font-family:'Share Tech Mono'; font-size:8.5pt; color:#38bdf8;">
                    CERTIFIED LABORATORIES: CNAS L1082 / ILAC-MRA ACCREDITED FLIGHT TESTING FACILITY
                </div>
                <div style="font-family:'Orbitron'; font-size:9pt; color:#00f0ff; font-weight:bold;">
                    PASS RATE: 99.98%
                </div>
            </div>
        </div>
        
        <div class="page-footer">
            <span class="print-indicator">OBVERSE [展面] · 航空制造标准规范</span>
            <span>QUALITY & RELIABILITY SPECIFICATIONS</span>
            <span class="page-number">PAGE 49 / 50</span>
        </div>
    </div>
    """

def render_back_cover_page():
    return f"""
    <div class="page back-cover-page">
        <div class="tech-grid-overlay"></div>
        <div class="hud-corner tl"></div>
        <div class="hud-corner tr"></div>
        <div class="hud-corner bl"></div>
        <div class="hud-corner br"></div>
        
        <div class="back-cover-container">
            <div class="cover-header-line" style="border-bottom: 1px solid rgba(0,240,255,0.3);">
                <span>DOCUMENT CONTROL: AGY-AERO-2026-FINAL</span>
                <span>RESTRICTED ENGINEERING BLUEPRINT</span>
                <span>GLOBAL ARCHIVE</span>
            </div>
            
            <div class="back-brand-box">
                <h1>AEROSPACE DYNAMICS</h1>
                <div class="motto">REDEFINING AUTONOMOUS FLIGHT // 探索天空的无垠边界</div>
                
                <div class="back-specs-summary">
                    <div class="back-stat">
                        <div class="num">23</div>
                        <div class="lbl">AERO PLATFORMS</div>
                    </div>
                    <div class="back-stat">
                        <div class="num">46</div>
                        <div class="lbl">CAD BLUEPRINTS</div>
                    </div>
                    <div class="back-stat">
                        <div class="num">50</div>
                        <div class="lbl">PAGES ARCHIVE</div>
                    </div>
                    <div class="back-stat">
                        <div class="num">100%</div>
                        <div class="lbl">CARBON COMPOSITE</div>
                    </div>
                </div>
            </div>
            
            <div style="max-width: 600px; margin: 0 auto; color: #94a3b8; font-size: 8.5pt; line-height: 1.6;">
                本画册专为单面高精印刷设计。每张纸正面为超清三维模型视图，背面为深度技术规格解析与装配工程解构。通过背对背冷裱粘接或蝴蝶对裱精装工艺装订成册，翻开即可呈现180度全平摊对开阅读体验。
            </div>
            
            <div class="back-legal-box">
                <div style="color: #38bdf8; margin-bottom: 1mm; font-size: 8.5pt;">
                    COPYRIGHT &copy; 2026-2027 AEROSPACE DYNAMICS FLIGHT LAB. ALL RIGHTS RESERVED.
                </div>
                <div>
                    CONFIDENTIAL & PROPRIETARY BLUEPRINT SPECIFICATION · UNAUTHORIZED DUPLICATION IS STRICTLY PROHIBITED
                </div>
                <div style="margin-top: 2mm; color: #00f0ff; letter-spacing: 2px;">
                    ISO 9001:2015 · AS9100D · CE · FCC CERTIFIED ADVANCED UNMANNED SYSTEMS
                </div>
            </div>
            
            <div class="page-footer" style="border-top: none; padding-top: 0;">
                <span class="print-indicator">REVERSE [封底] · 封底与版权声明</span>
                <span>FINAL PRINT PAGE</span>
                <span class="page-number">PAGE 50 / 50 [BACK COVER]</span>
            </div>
        </div>
    </div>
    """

def generate_full_html():
    """拼接完整的50页HTML代码"""
    pages_html = []
    
    # Page 1: 封面
    pages_html.append(render_cover_page())
    
    # Page 2: 目录与序言
    pages_html.append(render_toc_page())
    
    # Page 3 ~ Page 48: 23个产品专题 (共46页)
    curr_page = 3
    for p in catalog_data.PRODUCTS:
        # 奇数页：正面模型大图
        pages_html.append(render_obverse_page(p, curr_page))
        curr_page += 1
        
        # 偶数页：背面产品介绍
        pages_html.append(render_reverse_page(p, curr_page))
        curr_page += 1
        
    # Page 49: 质量试验体系
    pages_html.append(render_qa_page())
    
    # Page 50: 封底
    pages_html.append(render_back_cover_page())
    
    full_html = f"""<!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>未来飞行 · 航空航天无人系统工程画册 (50P完整版)</title>
        <style>
            {build_css()}
        </style>
    </head>
    <body>
        {''.join(pages_html)}
    </body>
    </html>
    """
    return full_html

async def main():
    print("Generating 50-page brochure HTML content...")
    html_content = generate_full_html()
    
    html_out_path = os.path.join(BASE_DIR, "Aero_UAV_Brochure_Print_Preview.html")
    with open(html_out_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML saved to: {html_out_path}")
    
    pdf_out_path = os.path.join(BASE_DIR, "Aero_UAV_Brochure_50P_Print_Ready.pdf")
    print(f"Rendering print-ready PDF using Playwright Chromium: {pdf_out_path}...")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        html_uri = f"file:///{html_out_path.replace(os.sep, '/')}"
        print(f"Navigating to {html_uri}...")
        await page.goto(html_uri, wait_until="networkidle")
        
        # 等待所有图片完全解码
        await page.wait_for_timeout(2000)
        
        print("Exporting PDF (297mm x 210mm Landscape, 50 Pages)...")
        await page.pdf(
            path=pdf_out_path,
            width="297mm",
            height="210mm",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        await browser.close()
        
    print(f"SUCCESS! 50-page print-ready PDF generated at: {pdf_out_path}")

if __name__ == "__main__":
    asyncio.run(main())
