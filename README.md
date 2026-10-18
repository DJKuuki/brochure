# GREET AERO // Aero UAV Engineering Monograph (98P)

> **Aero UAV High-Precision Engineering Monograph & Product Blueprint Catalog**  
> 98-Page A4 Landscape Portfolio & Editorial Catalog for Advanced Aerospace Unmanned Systems.

---

## 📖 Overview

This repository contains the complete automated publishing pipeline, vector blueprints, and generated assets for the **GREET AERO** 98-page engineering monograph and product catalog.

Designed with an Apple-inspired Swiss minimalist aesthetic:
- **Pure Exhibition White Palette**: Crisp white background (`#ffffff`) paired with Apple graphite typography (`#1d1d1f`, `#86868b`).
- **46 Aerospace Exhibits**: 46 distinct unmanned aerial vehicles and subsystems across 5 strategic divisions (Strategic High-Altitude, Tactical Reconnaissance, Maritime Patrol, VTOL Urban Mobility, Autonomous Swarm & Electronic Warfare).
- **Two-Page Spread Editorial Cadence**:
  - **Left (Verso)**: Full-bleed high-resolution CAD exhibit rendering with minimalist registration metadata.
  - **Right (Recto)**: Monograph-grade technical essay, engineering specifications, KaTeX pre-rendered LaTeX mathematical formulas, and custom aerospace blueprint vector diagrams.
- **Precision Engineering Diagrams**: 46 SVG blueprints featuring coordinate grids, dimension callouts, stress envelopes, and flight-dynamics diagrams.
- **Zero Web Artifacts**: Built strictly for archival print publication (A4 Landscape, 297mm × 210mm) with exact print CSS page breaks.

---

## 🗂️ Project Structure

```text
.
├── Aero_UAV_Catalog_AppleStyle_98P.html   # 98-page print-ready master HTML document
├── Aero_UAV_Master_Catalog_AppleStyle_98P.pdf # Master 300 DPI PDF monograph export (~18MB)
├── Apple_Interactive_Viewer.html          # Interactive local flipbook viewer for review
├── generate_editorial_brochure.py         # Main automated build pipeline (HTML + PDF + PNGs)
├── generate_svgs.py                       # Vector SVG engineering blueprint generator (46 diagrams)
├── catalog_data_v2.py                     # Structured exhibit database (specs, narratives, titles)
├── catalog_latex_data.py                  # LaTeX mathematical formula definitions
├── pre_rendered_katex.json                # Pre-rendered KaTeX HTML equations cache
├── 飞机截图/                              # 46 source CAD exhibit photographs
├── brochure_pages_v2/                     # Rendered high-res PNG spreads (page_001 to page_098)
├── package.json                           # Node.js dependencies (KaTeX)
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
1. **Python 3.9+**
2. **Node.js 18+**
3. **Playwright** (for headless PDF generation)

```bash
# Install Node dependencies
npm install

# Install Python dependencies
pip install playwright pillow
playwright install chromium
```

### Build & Generate
To recompile all vector diagrams, KaTeX formulas, HTML pages, and export the master PDF:

```bash
python generate_editorial_brochure.py
```

### Preview
Open `Apple_Interactive_Viewer.html` in any modern web browser to navigate the spreads using keyboard arrows or mouse.

---

## 📐 Design Specifications
- **Dimensions**: A4 Landscape (297mm × 210mm)
- **Grid System**: 12-column Swiss typographic grid
- **Typefaces**: SF Pro Display, PingFang SC, Inter, KaTeX_Main, JetBrains Mono
- **Print Compliance**: Standard A4 margin-bleed compliance, CMYK-aligned high-contrast monochrome
