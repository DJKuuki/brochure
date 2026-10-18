# -*- coding: utf-8 -*-
"""
Aero UAV Master Catalog (Pure Swiss Monograph Edition - Exhibition White)
98-Page Print-Ready Client-Facing Engineering Monograph & Interactive System

Design Specifications:
1. Palette: Pure Museum Exhibition White (#ffffff) with Apple deep graphite typography (#1d1d1f, #424245, #6e6e73), precision blue (#0071e3), and aero emerald/amber accents.
2. Architecture: Pure architectural Swiss grid driven by 0.5px hairlines and negative space. ZERO web card containers or nested rounded gray boxes.
3. Formulas: Typeset in authentic LaTeX rendered via KaTeX.
4. Schematics: 46 master-grade vector engineering blueprints with coordinate ticks, dimension markers, and physical stream/stress envelopes.
5. Page 23: Exhibit 10 rotated 90 deg clockwise to fit horizontal landscape layout.
6. Page 97: Balanced engineering layout featuring the AS9100D Aerospace Verification Lifecycle Bar between top and bottom specification grids, completely eliminating voids.
7. Client-Facing Status: Removed fictional ISBN numbers and fake barcodes. Cover features clean slogan "GREET AERO" in wide-spaced pure typography.

Total: Exactly 98 Pages (A4 Landscape, 297mm x 210mm)
"""

import os
import sys
import json
import asyncio
from playwright.async_api import async_playwright
import fitz # PyMuPDF

import catalog_data_v2
import generate_svgs
import catalog_latex_data

WORKSPACE_DIR = os.path.abspath("e:/brochure").replace("\\", "/")
IMAGE_DIR = os.path.join(WORKSPACE_DIR, "飞机截图").replace("\\", "/")
OUTPUT_HTML = os.path.join(WORKSPACE_DIR, "Aero_UAV_Catalog_AppleStyle_98P.html").replace("\\", "/")
OUTPUT_PDF = os.path.join(WORKSPACE_DIR, "Aero_UAV_Master_Catalog_AppleStyle_98P.pdf").replace("\\", "/")
OUTPUT_PAGES_DIR = os.path.join(WORKSPACE_DIR, "brochure_pages_v2").replace("\\", "/")
KATEX_CSS_PATH = f"file:///{WORKSPACE_DIR}/node_modules/katex/dist/katex.min.css"

# 加载 KaTeX 预渲染公式
KATEX_CACHE_FILE = os.path.join(WORKSPACE_DIR, "pre_rendered_katex.json")
if os.path.exists(KATEX_CACHE_FILE):
    with open(KATEX_CACHE_FILE, "r", encoding="utf-8") as f:
        KATEX_FORMULAS_MAP = json.load(f)
else:
    KATEX_FORMULAS_MAP = catalog_latex_data.render_all_katex()
    with open(KATEX_CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(KATEX_FORMULAS_MAP, f, ensure_ascii=False, indent=2)

def get_editorial_svg(svg_markup):
    """矢量图原生适配纯白背景"""
    return svg_markup

def get_section_info(idx):
    if 1 <= idx <= 12:
        return (
            "SECTION 01: TACTICAL & AUTONOMOUS MULTIROTOR PLATFORMS",
            "战术多旋翼与长航时探测系统"
        )
    elif 13 <= idx <= 22:
        return (
            "SECTION 02: HYBRID VTOL & SPECIAL CONFIGURATION UAVS",
            "复合翼垂直起降与特种气动系统"
        )
    elif 23 <= idx <= 34:
        return (
            "SECTION 03: INDUSTRIAL HEAVY-LIFT & FIXED-WING SYSTEMS",
            "工业重载植保与固定翼巡检系统"
        )
    else:
        return (
            "SECTION 04: ADVANCED PROPULSION & MONOCOQUE COMPOSITES",
            "核心动力总成与先进航空材料体系"
        )

# ==============================================================================
# PAGE 01: MASTER COVER (纯粹字体排印封面，无伪ISBN，无胶囊)
# ==============================================================================
def build_cover_html():
    return '''
<!-- Page 01: Master Cover -->
<div class="page page-cover">
    <div class="running-header">
        <div class="rh-title">AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS</div>
        <div class="rh-section">ENGINEERING MONOGRAPH &amp; TECHNICAL COMPENDIUM</div>
    </div>
    
    <div class="cover-hero-center">
        <div class="cover-slogan">G R E E T &nbsp; A E R O</div>
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
            <div class="corp-sub">AEROSPACE MONOGRAPH ARCHIVE // EDITION 2026-2027</div>
        </div>
        <div class="cover-footer-right">
            <div class="cover-doc-id-group">
                <span class="doc-id-label">DOCUMENT CLASSIFICATION</span>
                <span class="doc-id-code">UNPUBLISHED TECHNICAL COMPENDIUM // SPEC-AERO-2026</span>
            </div>
            <div class="page-folio">001</div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# PAGE 02: FOREWORD & ENGINEERING PHILOSOPHY (瑞士网格序言)
# ==============================================================================
def build_foreword_html():
    return '''
<!-- Page 02: Foreword & System Taxonomy -->
<div class="page page-verso" style="padding-top:14mm; padding-bottom:14mm;">
    <div class="running-header">
        <div class="rh-title">PREFACE &amp; TAXONOMY // 序言与全书系统架构</div>
        <div class="rh-section">AEROSPACE MONOGRAPH // VOL. 01</div>
    </div>

    <div class="foreword-grid-layout">
        <!-- 左列：设计与工程哲学 -->
        <div class="foreword-text-col">
            <div class="editorial-kicker">ENGINEERING PHILOSOPHY</div>
            <h2 class="foreword-headline">极简之道，始于至繁。<br><span style="color:#0071e3;">功能之纯粹，即美学之巅峰。</span></h2>
            
            <p class="foreword-paragraph">
                人类对天空的探索，始终是一场对空气动力学极限、结构力学效率与材料物理潜能的无休止求索。本图鉴所收录的四十六款飞行系统与动力总成，代表了我们对现代航空航天工程体系的系统性沉淀与解构。
            </p>
            <p class="foreword-paragraph">
                在这部文献中，我们摒弃了一切浮夸的装饰性修辞，让纯粹的工程数学模型与严谨的物理法则直接对话。每一个机翼截面的微小弯度、每一根碳纤维丝束的铺设角度、每一段涵道唇口的扩张曲率，皆源自对普朗特流动、纳维-斯托克斯方程与欧拉-伯努利梁理论的严苛标定。
            </p>
            <p class="foreword-paragraph">
                我们坚信：最震撼人心的科技力量，绝非来自繁复的机体冗余，而是源于经过千锤百炼后所呈现出的理性秩序与极致克制。
            </p>

            <div class="foreword-signature">
                <div class="sig-name">AERO ADVANCED DYNAMICS &amp; AUTONOMOUS SYSTEMS LAB</div>
                <div class="sig-role">CHIEF ENGINEERING &amp; AEROSPACE DESIGN COUNCIL // 2026</div>
            </div>
        </div>

        <!-- 右列：系统分类体系与工程标准 -->
        <div class="foreword-taxonomy-col">
            <div class="editorial-kicker">SYSTEM TAXONOMY</div>
            
            <div class="tax-item">
                <div class="tax-header">
                    <span class="tax-code">PART I</span>
                    <span class="tax-name">战术多旋翼与长航时探测系统 (Exhibits 01 – 12)</span>
                </div>
                <p>涵盖仿生水滴低阻机身、远距长航时穿越机架、360°全防护文丘里涵道机架及对称True-X竞技平台，深入解构前缘滞止点压强、转动惯量解耦与湍流边界层脉动。</p>
            </div>

            <div class="tax-item">
                <div class="tax-header">
                    <span class="tax-code">PART II</span>
                    <span class="tax-name">复合翼垂直起降与特种气动系统 (Exhibits 13 – 22)</span>
                </div>
                <p>涵盖大展弦比机翼构型、前掠下反翼尖小翼、多旋翼/固定翼模态平滑转换、外倾双垂尾与全动V尾舵面，解析升力分配解耦矩阵、雷达散射截面（RCS）与跨音速附面层激波抑制。</p>
            </div>

            <div class="tax-item">
                <div class="tax-header">
                    <span class="tax-code">PART III</span>
                    <span class="tax-name">工业重载植保与固定翼巡检系统 (Exhibits 23 – 34)</span>
                </div>
                <p>涵盖60升重载植保六旋翼、串列双机翼、经典T尾高稳巡线机与直升机单旋翼，解构下洗流场沉降、管路液压等阻平衡与周期变距动力学。</p>
            </div>

            <div class="tax-item">
                <div class="tax-header">
                    <span class="tax-code">PART IV</span>
                    <span class="tax-name">核心动力总成与先进航空材料 (Exhibits 35 – 46)</span>
                </div>
                <p>涵盖大扭矩外转子电机、折叠碳纤螺旋桨、双旋翼倾转推力矢量及热压罐一体共固化纯碳骨架，解析蔡-吴三维椭球破坏准则与动态重心包线。</p>
            </div>

            <div class="tax-standards-note">
                <div class="std-note-title">AEROSPACE COMPLIANCE &amp; CERTIFICATION</div>
                <div class="std-note-desc">全系型号均严格执行 AS9100D 航空航天质量管理规范，并在低速/跨音速风洞、六分量天平及高低温恶劣气候试验箱中通过全包线可靠性工程验证。</div>
            </div>
        </div>
    </div>

    <div class="verso-footer">
        <div style="font-size:7.5pt; color:#888888; letter-spacing:0.5px;">AEROSPACE MONOGRAPH // PREFACE &amp; TAXONOMY</div>
        <div class="page-folio">002</div>
    </div>
</div>
'''

# ==============================================================================
# PAGES 03 & 04: TABLE OF CONTENTS (双页极简网格目录)
# ==============================================================================
def build_toc_html(part=1):
    items = catalog_data_v2.ITEMS
    if part == 1:
        part_items = items[0:23] # 01 - 23
        subtitle = "SECTION 01: 战术多旋翼与长航时探测系统 &amp; SECTION 02: 复合翼与特种气动系统"
        page_folio = "003"
    else:
        part_items = items[23:46] # 24 - 46
        subtitle = "SECTION 03: 工业重载植保与固定翼巡检系统 &amp; SECTION 04: 核心动力总成与先进航空材料"
        page_folio = "004"

    rows_html = ""
    for it in part_items:
        idx = it["index"]
        p_start = 5 + (idx - 1) * 2
        p_end = p_start + 1
        name_clean = it["name_zh"].split("//")[0].strip()
        rows_html += f'''
        <div class="toc-row">
            <span class="toc-num">{idx:02d}</span>
            <div class="toc-info">
                <span class="toc-title">{name_clean}</span>
                <span class="toc-code">{it["code"]}</span>
            </div>
            <span class="toc-cat">{it["category_zh"]}</span>
            <span class="toc-pages">{p_start:03d} – {p_end:03d}</span>
        </div>
        '''

    return f'''
<!-- Page {page_folio}: TOC Part {part} -->
<div class="page page-verso" style="padding-top:14mm; padding-bottom:14mm;">
    <div class="running-header">
        <div class="rh-title">TABLE OF CONTENTS // 全书总目录索引</div>
        <div class="rh-section">PART 0{part} OF 02</div>
    </div>

    <div class="toc-header-section">
        <h2 class="toc-headline">工程展项总览索引 (Exhibits {part_items[0]["index"]:02d} – {part_items[-1]["index"]:02d})</h2>
        <div class="toc-subheadline">{subtitle}</div>
    </div>

    <div class="toc-two-col-grid">
        {rows_html}
    </div>

    <div class="verso-footer">
        <div style="font-size:7.5pt; color:#888888; letter-spacing:0.5px;">AEROSPACE MONOGRAPH // MASTER CATALOG INDEX</div>
        <div class="page-folio">{page_folio}</div>
    </div>
</div>
'''

# ==============================================================================
# PAGES 05 - 96: 46 EXHIBITS (92 PAGES)
# 四大去卡片化建筑式排版架构，LaTeX 数学排版驱动
# ==============================================================================
def build_exhibit_spread_html(item):
    idx = item["index"]
    verso_page_num = 5 + (idx - 1) * 2
    recto_page_num = verso_page_num + 1

    img_path = os.path.abspath(os.path.join(IMAGE_DIR, item["image"])).replace("\\", "/")
    svg_raw = generate_svgs.get_svg_diagram(item["svg_type"])
    svg_markup = get_editorial_svg(svg_raw)
    sec_en, sec_cn = get_section_info(idx)
    name_clean = item["name_zh"].split("//")[0].strip()
    
    # 获取预渲染 KaTeX LaTeX 公式 HTML
    katex_html = KATEX_FORMULAS_MAP.get(str(idx), "")

    # ──────────────────────────────────────────────────────────
    # 奇数页（左页 Verso）：工程图学安装画框（纯白无缝底板，微细定位十字标）
    # ──────────────────────────────────────────────────────────
    verso_html = f'''
<!-- Page {verso_page_num:03d}: Pure Exhibition (Verso) -->
<div class="page page-verso">
    <div class="running-header">
        <div class="rh-title">AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS</div>
        <div class="rh-section">{sec_en}</div>
    </div>

    <div class="verso-stage">
        <div class="verso-mount">
            <div class="reticle-tick tl"></div>
            <div class="reticle-tick tr"></div>
            <div class="reticle-tick bl"></div>
            <div class="reticle-tick br"></div>
            <div class="mount-meta-top">PLATE {idx:02d}.0 // 3D CAD SURFACE GEOMETRY // ISOMETRIC VIEW</div>
            <div class="mount-meta-bottom">DATUM ZERO // AEROSPACE DIGITAL TWIN // REF: {item["code"]}</div>
            <img src="file:///{img_path}" alt="{name_clean}">
        </div>
    </div>

    <div class="verso-footer">
        <div class="caption-block">
            <div class="caption-title">{idx:02d} / {name_clean}</div>
            <div class="caption-sub">{item["tagline"]}</div>
            <div class="caption-meta">SPECIFICATION REF : {item["code"]} // CATEGORY : {item["category_zh"]} ({item["category_en"]})</div>
        </div>
        <div class="page-folio">{verso_page_num:03d}</div>
    </div>
</div>
'''

    # ──────────────────────────────────────────────────────────
    # 偶数页（右页 Recto）：4 套纯粹印刷学术版式交替呈现（无圆角灰框）
    # ──────────────────────────────────────────────────────────
    arch_type = idx % 4

    if arch_type == 1:
        # ARCHITECTURE 1: 经典双栏气动解构流 (Dissection & Blueprint)
        recto_html = _build_arch_1(item, idx, sec_en, name_clean, svg_markup, katex_html, recto_page_num)
    elif arch_type == 2:
        # ARCHITECTURE 2: 非对称工程亮点流 (Typographic Highlights)
        recto_html = _build_arch_2(item, idx, sec_en, name_clean, svg_markup, katex_html, recto_page_num)
    elif arch_type == 3:
        # ARCHITECTURE 3: 深度数理长文流 (Mathematical Physics & Tri-Column)
        recto_html = _build_arch_3(item, idx, sec_en, name_clean, svg_markup, katex_html, recto_page_num)
    else:
        # ARCHITECTURE 0: 高密工程数据蓝图型 (Blueprint & Metric Matrix)
        recto_html = _build_arch_4(item, idx, sec_en, name_clean, svg_markup, katex_html, recto_page_num)

    return verso_html + recto_html


# ──────────────────────────────────────────────────────────────
# ARCHITECTURE 1: 经典双栏气动解构流 (Dissection & Blueprint)
# ──────────────────────────────────────────────────────────────
def _build_arch_1(item, idx, sec_en, name_clean, svg_markup, katex_html, pn):
    return f'''
<div class="page page-recto">
    <div class="running-header">
        <div class="rh-title">{sec_en}</div>
        <div class="rh-section">PLATE {idx:02d}.1 // {item["code"]}</div>
    </div>

    <div class="arch-header">
        <div class="arch-title-row">
            <h1 class="arch-main-title">{name_clean}</h1>
            <span class="arch-cat-tag">{item["category_zh"]}</span>
        </div>
        <div class="arch-subtitle">{item["name_en"]} — {item["tagline"]}</div>
    </div>

    <!-- 双栏学术正文 -->
    <div class="two-col-text">
        <p>{item["desc"]}</p>
    </div>

    <!-- 科学理论图解与 LaTeX 支配方程 -->
    <div class="blueprint-split-strip">
        <div class="bss-left">
            <div class="plate-label-bar">
                <span class="plb-num">FIG. {idx:02d}.1</span>
                <span class="plb-title">{item["theory_title"]}</span>
            </div>
            <p class="theory-desc-text">{item["theory_desc"]}</p>
            <div class="latex-eq-container">
                <div class="latex-eq-math">{katex_html}</div>
                <span class="latex-eq-tag">[Eq. {idx:02d}.1]</span>
            </div>
        </div>
        <div class="bss-right">
            <div class="floating-vector-diagram">
                {svg_markup}
            </div>
        </div>
    </div>

    <!-- 四大浮动指标与 Booktabs 规格矩阵 -->
    <div class="hero-and-table-row">
        <div class="hero-stat-strip-4">
            <div class="hss-item"><span class="hss-idx">// 01</span><span class="hss-val">{item["hero_stats"][0]["val"]}</span><span class="hss-lbl">{item["hero_stats"][0]["lbl"]}</span></div>
            <div class="hss-item"><span class="hss-idx">// 02</span><span class="hss-val">{item["hero_stats"][1]["val"]}</span><span class="hss-lbl">{item["hero_stats"][1]["lbl"]}</span></div>
            <div class="hss-item"><span class="hss-idx">// 03</span><span class="hss-val">{item["hero_stats"][2]["val"]}</span><span class="hss-lbl">{item["hero_stats"][2]["lbl"]}</span></div>
            <div class="hss-item"><span class="hss-idx">// 04</span><span class="hss-val">{item["hero_stats"][3]["val"]}</span><span class="hss-lbl">{item["hero_stats"][3]["lbl"]}</span></div>
        </div>

        <table class="monograph-booktabs">
            <thead>
                <tr><th>技术参数指标</th><th>工程标定值</th><th>分系统配置</th><th>设计规范</th></tr>
            </thead>
            <tbody>
                <tr><td>{item["specs"][0]["label"]}</td><td class="bv">{item["specs"][0]["value"]}</td><td>{item["specs"][4]["label"]}</td><td class="bv">{item["specs"][4]["value"]}</td></tr>
                <tr><td>{item["specs"][1]["label"]}</td><td class="bv">{item["specs"][1]["value"]}</td><td>{item["specs"][5]["label"]}</td><td class="bv">{item["specs"][5]["value"]}</td></tr>
                <tr><td>{item["specs"][2]["label"]}</td><td class="bv">{item["specs"][2]["value"]}</td><td>{item["specs"][6]["label"]}</td><td class="bv">{item["specs"][6]["value"]}</td></tr>
                <tr><td>{item["specs"][3]["label"]}</td><td class="bv">{item["specs"][3]["value"]}</td><td>{item["specs"][7]["label"]}</td><td class="bv">{item["specs"][7]["value"]}</td></tr>
            </tbody>
        </table>
    </div>

    <div class="verso-footer">
        <div style="font-size:7.5pt; color:#888888; letter-spacing:0.5px;">AEROSPACE MONOGRAPH // SCIENTIFIC DISSECTION MATRIX</div>
        <div class="page-folio">{pn:03d}</div>
    </div>
</div>
'''


# ──────────────────────────────────────────────────────────────
# ARCHITECTURE 2: 非对称工程亮点流 (Typographic Highlights)
# ──────────────────────────────────────────────────────────────
def _build_arch_2(item, idx, sec_en, name_clean, svg_markup, katex_html, pn):
    desc_sentences = item["desc"].replace("。", "。|").split("|")
    desc_sentences = [s.strip() for s in desc_sentences if len(s.strip()) > 8]
    th_sentences = item["theory_desc"].replace("。", "。|").split("|")
    th_sentences = [s.strip() for s in th_sentences if len(s.strip()) > 8]

    hl_titles = [
        item["tagline"].split("·")[0].strip() if "·" in item["tagline"] else item["category_zh"],
        item["theory_title"].split("·")[-1].strip() if "·" in item["theory_title"] else item["theory_title"],
        item["specs"][4]["label"],
    ]
    hl_descs = [
        desc_sentences[0] if len(desc_sentences) > 0 else item["desc"][:110],
        th_sentences[0] if len(th_sentences) > 0 else item["theory_desc"][:110],
        desc_sentences[-1] if len(desc_sentences) > 1 else (th_sentences[-1] if len(th_sentences) > 1 else item["tagline"]),
    ]

    return f'''
<div class="page page-recto">
    <div class="running-header">
        <div class="rh-title">{sec_en}</div>
        <div class="rh-section">ENGINEERING HIGHLIGHTS // {item["code"]}</div>
    </div>

    <div class="arch-header">
        <div class="arch-title-row">
            <h1 class="arch-main-title">{name_clean}</h1>
            <span class="arch-cat-tag">{item["category_zh"]}</span>
        </div>
        <div class="arch-subtitle">{item["name_en"]} — {item["tagline"]}</div>
    </div>

    <!-- 纯字体排印三列工程亮点 (无背景卡片，纯发丝标线) -->
    <div class="pure-highlights-strip">
        <div class="ph-col">
            <div class="ph-num">01</div>
            <div class="ph-title">{hl_titles[0]}</div>
            <p class="ph-desc">{hl_descs[0]}</p>
            <div class="ph-metric-row">
                <span class="ph-m-val">{item["hero_stats"][0]["val"]}</span>
                <span class="ph-m-lbl">{item["hero_stats"][0]["lbl"]}</span>
            </div>
        </div>
        <div class="ph-col">
            <div class="ph-num">02</div>
            <div class="ph-title">{hl_titles[1]}</div>
            <p class="ph-desc">{hl_descs[1]}</p>
            <div class="ph-metric-row">
                <span class="ph-m-val">{item["hero_stats"][1]["val"]}</span>
                <span class="ph-m-lbl">{item["hero_stats"][1]["lbl"]}</span>
            </div>
        </div>
        <div class="ph-col">
            <div class="ph-num">03</div>
            <div class="ph-title">{hl_titles[2]}</div>
            <p class="ph-desc">{hl_descs[2]}</p>
            <div class="ph-metric-row">
                <span class="ph-m-val">{item["hero_stats"][2]["val"]}</span>
                <span class="ph-m-lbl">{item["hero_stats"][2]["lbl"]}</span>
            </div>
        </div>
    </div>

    <!-- 宽幅无边框透明工程矢量图解 -->
    <div class="pure-wide-diagram-strip">
        <div class="pw-svg-col">
            {svg_markup}
        </div>
        <div class="pw-math-col">
            <div class="plate-label-bar">
                <span class="plb-num">FIG. {idx:02d}.1</span>
                <span class="plb-title">{item["theory_title"]}</span>
            </div>
            <div class="latex-eq-container" style="margin-top:2mm;">
                <div class="latex-eq-math">{katex_html}</div>
                <span class="latex-eq-tag">[Eq. {idx:02d}.1]</span>
            </div>
            <p class="theory-desc-text" style="margin-top:2mm;">{item["theory_desc"]}</p>
        </div>
    </div>

    <!-- 紧凑单行参数带 -->
    <div class="linear-specs-ribbon">
        <div class="lsr-item"><span>{item["specs"][0]["label"]}</span><strong>{item["specs"][0]["value"]}</strong></div>
        <div class="lsr-item"><span>{item["specs"][1]["label"]}</span><strong>{item["specs"][1]["value"]}</strong></div>
        <div class="lsr-item"><span>{item["specs"][2]["label"]}</span><strong>{item["specs"][2]["value"]}</strong></div>
        <div class="lsr-item"><span>{item["specs"][3]["label"]}</span><strong>{item["specs"][3]["value"]}</strong></div>
        <div class="lsr-item"><span>{item["specs"][4]["label"]}</span><strong>{item["specs"][4]["value"]}</strong></div>
        <div class="lsr-item"><span>{item["specs"][5]["label"]}</span><strong>{item["specs"][5]["value"]}</strong></div>
    </div>

    <div class="verso-footer">
        <div style="font-size:7.5pt; color:#888888; letter-spacing:0.5px;">AEROSPACE MONOGRAPH // ENGINEERING HIGHLIGHTS &amp; MECHANICS</div>
        <div class="page-folio">{pn:03d}</div>
    </div>
</div>
'''


# ──────────────────────────────────────────────────────────────
# ARCHITECTURE 3: 深度数理长文流 (Mathematical Physics & Tri-Column)
# ──────────────────────────────────────────────────────────────
def _build_arch_3(item, idx, sec_en, name_clean, svg_markup, katex_html, pn):
    tagline_parts = item["tagline"].split("·")
    pull_quote = tagline_parts[0].strip() if tagline_parts else item["tagline"]

    return f'''
<div class="page page-recto">
    <div class="running-header">
        <div class="rh-title">{sec_en}</div>
        <div class="rh-section">MATHEMATICAL PHYSICS // {item["code"]}</div>
    </div>

    <div class="arch-header">
        <div class="arch-title-row">
            <h1 class="arch-main-title">{name_clean}</h1>
            <span class="arch-cat-tag">{item["category_zh"]}</span>
        </div>
        <div class="arch-subtitle">{item["name_en"]}</div>
    </div>

    <!-- 权威引述条 (纯左侧发丝线条标引) -->
    <div class="editorial-quote-line">
        <span class="eql-bar"></span>
        <div class="eql-content">
            <span class="eql-tag">DESIGN THESIS :</span>
            <span class="eql-quote">“{pull_quote} — 以纯粹结构数学响应复杂动力工况。”</span>
        </div>
    </div>

    <!-- 三栏学术长文 (无背景框，纯正文排列) -->
    <div class="tri-narrative-grid">
        <div class="tng-col">
            <span class="tng-header">01 // SYSTEM OVERVIEW</span>
            <p>{item["desc"]}</p>
        </div>
        <div class="tng-col">
            <span class="tng-header">02 // FLIGHT DYNAMICS</span>
            <p>{item["theory_desc"]}</p>
        </div>
        <div class="tng-col">
            <span class="tng-header">03 // KEY BENCHMARKS</span>
            <div class="tng-stat-grid">
                <div class="tng-stat-cell">
                    <span class="ts-val">{item["hero_stats"][0]["val"]}</span>
                    <span class="ts-lbl">{item["hero_stats"][0]["lbl"]}</span>
                </div>
                <div class="tng-stat-cell">
                    <span class="ts-val">{item["hero_stats"][1]["val"]}</span>
                    <span class="ts-lbl">{item["hero_stats"][1]["lbl"]}</span>
                </div>
                <div class="tng-stat-cell">
                    <span class="ts-val">{item["hero_stats"][2]["val"]}</span>
                    <span class="ts-lbl">{item["hero_stats"][2]["lbl"]}</span>
                </div>
                <div class="tng-stat-cell">
                    <span class="ts-val">{item["hero_stats"][3]["val"]}</span>
                    <span class="ts-lbl">{item["hero_stats"][3]["lbl"]}</span>
                </div>
            </div>
        </div>
    </div>

    <!-- 醒目全宽 LaTeX 数学模型居中展台 -->
    <div class="central-latex-stage">
        <div class="cls-header">
            <span class="plb-num">FIG. {idx:02d}.1</span>
            <span class="plb-title">GOVERNING AERODYNAMIC EQUATION // {item["theory_title"]}</span>
            <span class="latex-eq-tag" style="margin-left:auto;">[Eq. {idx:02d}.1]</span>
        </div>
        <div class="cls-math">
            {katex_html}
        </div>
    </div>

    <!-- 紧凑双行规格矩阵 -->
    <div class="compact-matrix-footer">
        <div class="cmf-row">
            <span class="cmf-k">{item["specs"][0]["label"]}:</span><span class="cmf-v">{item["specs"][0]["value"]}</span>
            <span class="cmf-k">{item["specs"][1]["label"]}:</span><span class="cmf-v">{item["specs"][1]["value"]}</span>
            <span class="cmf-k">{item["specs"][2]["label"]}:</span><span class="cmf-v">{item["specs"][2]["value"]}</span>
            <span class="cmf-k">{item["specs"][3]["label"]}:</span><span class="cmf-v">{item["specs"][3]["value"]}</span>
        </div>
        <div class="cmf-row" style="margin-top:1.5mm;">
            <span class="cmf-k">{item["specs"][4]["label"]}:</span><span class="cmf-v">{item["specs"][4]["value"]}</span>
            <span class="cmf-k">{item["specs"][5]["label"]}:</span><span class="cmf-v">{item["specs"][5]["value"]}</span>
            <span class="cmf-k">{item["specs"][6]["label"]}:</span><span class="cmf-v">{item["specs"][6]["value"]}</span>
            <span class="cmf-k">{item["specs"][7]["label"]}:</span><span class="cmf-v">{item["specs"][7]["value"]}</span>
        </div>
    </div>

    <div class="verso-footer">
        <div style="font-size:7.5pt; color:#888888; letter-spacing:0.5px;">AEROSPACE MONOGRAPH // MATHEMATICAL GOVERNING EQUATIONS</div>
        <div class="page-folio">{pn:03d}</div>
    </div>
</div>
'''


# ──────────────────────────────────────────────────────────────
# ARCHITECTURE 4: 高密工程数据蓝图型 (Blueprint & Metric Matrix)
# ──────────────────────────────────────────────────────────────
def _build_arch_4(item, idx, sec_en, name_clean, svg_markup, katex_html, pn):
    return f'''
<div class="page page-recto">
    <div class="running-header">
        <div class="rh-title">{sec_en}</div>
        <div class="rh-section">BLUEPRINT MATRIX // {item["code"]}</div>
    </div>

    <div class="arch-header">
        <div class="arch-title-row">
            <h1 class="arch-main-title">{name_clean}</h1>
            <span class="arch-cat-tag">{item["category_zh"]}</span>
        </div>
        <div class="arch-subtitle">{item["name_en"]} — {item["tagline"]}</div>
    </div>

    <!-- 顶部单段精悍导读 -->
    <div class="single-lead-text">
        <p>{item["desc"]}</p>
    </div>

    <!-- 全宽工程物理图解与公式一体台 -->
    <div class="diagram-and-math-monolith">
        <div class="dam-header">
            <span class="plb-num">FIG. {idx:02d}.1 // {item["theory_title"]}</span>
            <span class="latex-eq-tag">[Eq. {idx:02d}.1]</span>
        </div>
        <div class="dam-svg-box">
            {svg_markup}
        </div>
        <div class="dam-math-row">
            <div class="latex-eq-math">{katex_html}</div>
            <p class="dam-desc">{item["theory_desc"]}</p>
        </div>
    </div>

    <!-- 8 项开放式水平数据网格 (无卡片，纯发丝网格) -->
    <div class="open-matrix-8">
        <div class="om-cell"><span class="om-lbl">{item["hero_stats"][0]["lbl"]}</span><span class="om-val">{item["hero_stats"][0]["val"]}</span></div>
        <div class="om-cell"><span class="om-lbl">{item["hero_stats"][1]["lbl"]}</span><span class="om-val">{item["hero_stats"][1]["val"]}</span></div>
        <div class="om-cell"><span class="om-lbl">{item["hero_stats"][2]["lbl"]}</span><span class="om-val">{item["hero_stats"][2]["val"]}</span></div>
        <div class="om-cell"><span class="om-lbl">{item["hero_stats"][3]["lbl"]}</span><span class="om-val">{item["hero_stats"][3]["val"]}</span></div>
        <div class="om-cell"><span class="om-lbl">{item["specs"][0]["label"]}</span><span class="om-sub">{item["specs"][0]["value"]}</span></div>
        <div class="om-cell"><span class="om-lbl">{item["specs"][1]["label"]}</span><span class="om-sub">{item["specs"][1]["value"]}</span></div>
        <div class="om-cell"><span class="om-lbl">{item["specs"][4]["label"]}</span><span class="om-sub">{item["specs"][4]["value"]}</span></div>
        <div class="om-cell"><span class="om-lbl">{item["specs"][5]["label"]}</span><span class="om-sub">{item["specs"][5]["value"]}</span></div>
    </div>

    <div class="verso-footer">
        <div style="font-size:7.5pt; color:#888888; letter-spacing:0.5px;">AEROSPACE MONOGRAPH // DATA MATRIX &amp; PHYSICAL SPECIFICATION</div>
        <div class="page-folio">{pn:03d}</div>
    </div>
</div>
'''

# ==============================================================================
# PAGE 097: MANUFACTURING & QUALITY STANDARDS (无卡片纯净网格 + 流程连贯条)
# ==============================================================================
def build_standards_html():
    return '''
<!-- Page 097: Manufacturing & Quality Standards -->
<div class="page page-verso" style="padding-top:14mm; padding-bottom:14mm;">
    <div class="running-header">
        <div class="rh-title">MANUFACTURING &amp; QUALITY STANDARDS // 航空工程制造工艺与品质检验规范</div>
        <div class="rh-section">AEROSPACE GRADE AS9100D</div>
    </div>

    <div class="standards-header-block">
        <h2 class="standards-headline">精密制造工艺与极端环境可靠性验证体系</h2>
        <div class="standards-subheadline">
            遵循航空航天 AS9100D 质量管理体系标准 · 六维全流程闭环可追溯验证 (GB/T 38058 · MIL-STD-810H · RTCA/DO-160G)
        </div>
    </div>

    <div class="standards-editorial-wrapper">
        <!-- Top Row: Specs 01 - 03 -->
        <div class="standards-grid-row">
            <div class="std-box">
                <div class="std-header">
                    <span class="std-code">SPEC 01 // COMPOSITES</span>
                    <h4>预浸料热压罐一体共固化工艺</h4>
                    <div class="std-en">Prepreg Autoclave Curing Technology</div>
                </div>
                <p>采用日本东丽航空级 T700/T800 高模量碳纤维预浸布，在精密金属对开模内经历 130℃ 梯度升温与 0.8MPa 恒压环境。树脂固化率达 98.5% 以上，孔隙率控制在 0.45% 以下，彻底消除传统常压工艺层间虚粘与微气孔隐患。</p>
                <div class="std-bench-row"><span>层间剪切强度:</span> <strong>≥ 85 MPa</strong></div>
                <div class="std-bench-row"><span>微观孔隙率:</span> <strong>≤ 0.45% (GB/T 33501)</strong></div>
            </div>

            <div class="std-box">
                <div class="std-header">
                    <span class="std-code">SPEC 02 // PRECISION CNC</span>
                    <h4>五轴高速精密联动数控切削</h4>
                    <div class="std-en">5-Axis High-Precision CNC Machining</div>
                </div>
                <p>关键金属连接接头、电机机座与云台转轴均选用 7075-T651 航空级超硬铝合金。采用瑞士米克朗五轴联动加工中心单次装夹切削，几何公差（GD&amp;T）严格控制在 ±0.015mm 内，表面经 25μm 硬质阳极氧化封孔防腐处理。</p>
                <div class="std-bench-row"><span>装配同轴度:</span> <strong>≤ 0.012 mm</strong></div>
                <div class="std-bench-row"><span>表面形位公差:</span> <strong>±0.015 mm (ISO 2768)</strong></div>
            </div>

            <div class="std-box">
                <div class="std-header">
                    <span class="std-code">SPEC 03 // DYNAMIC BALANCE</span>
                    <h4>微克级转子动平衡校准系统</h4>
                    <div class="std-en">Dynamic Balancing Class G1.0 Standard</div>
                </div>
                <p>全系大扭矩无刷电机转子与碳纤折叠螺旋桨，100% 经过德国申克（Schenck）高精动态平衡机在线校准。在高达 28,000 RPM 极限转速下，叶尖残余不平衡偏心量小于 0.5mg·mm，彻底消除飞行器高频抖动与轴承疲劳。</p>
                <div class="std-bench-row"><span>动平衡等级:</span> <strong>ISO Class G1.0</strong></div>
                <div class="std-bench-row"><span>残余不平衡偏心:</span> <strong>≤ 0.5 mg·mm</strong></div>
            </div>
        </div>

        <!-- Middle Lifecycle Verification Pipeline Bar (Eliminating the vertical void!) -->
        <div class="as9100d-lifecycle-bar">
            <div class="as9100d-lifecycle-title-row">
                <div class="as9100d-lifecycle-title">AS9100D 全生命周期闭环质量可追溯验证序列 // VERIFICATION &amp; TRACEABILITY PIPELINE</div>
                <div style="font-size:6.5pt; font-family:'SF Mono',monospace; color:#0071e3; font-weight:700;">100% LOT INSPECTED · ZERO DEFECT QA</div>
            </div>
            <div class="as9100d-lifecycle-steps">
                <div class="al-step">
                    <span class="al-step-num">PHASE 01</span>
                    <span class="al-step-name">原料光谱理化</span>
                    <span class="al-step-metric">T800碳丝拉伸/树脂固化</span>
                </div>
                <div class="al-step">
                    <span class="al-step-num">PHASE 02</span>
                    <span class="al-step-name">五轴微米数控</span>
                    <span class="al-step-metric">蔡司三坐标检测 ±0.015mm</span>
                </div>
                <div class="al-step">
                    <span class="al-step-num">PHASE 03</span>
                    <span class="al-step-name">动平衡校准</span>
                    <span class="al-step-metric">Schenck G1.0 偏心&lt;0.5mg</span>
                </div>
                <div class="al-step">
                    <span class="al-step-num">PHASE 04</span>
                    <span class="al-step-name">低湍流风洞</span>
                    <span class="al-step-metric">PIV六分量天平/颤振裕度</span>
                </div>
                <div class="al-step">
                    <span class="al-step-num">PHASE 05</span>
                    <span class="al-step-name">全频暗室EMC</span>
                    <span class="al-step-metric">CE102/RS103 纹波≤12mV</span>
                </div>
                <div class="al-step">
                    <span class="al-step-num">PHASE 06</span>
                    <span class="al-step-name">极端环境应力</span>
                    <span class="al-step-metric">-40℃~+65℃/IP67重度暴雨</span>
                </div>
            </div>
        </div>

        <!-- Bottom Row: Specs 04 - 06 -->
        <div class="standards-grid-row">
            <div class="std-box">
                <div class="std-header">
                    <span class="std-code">SPEC 04 // WIND TUNNEL</span>
                    <h4>气动气弹风洞与颤振边界实测</h4>
                    <div class="std-en">Aeroacoustic &amp; Wind Tunnel Testing</div>
                </div>
                <p>全机身三维流线模型置于低湍流度航空风洞中，采用六分量测力天平与粒子图像测速技术（PIV）精细标定。全面验证大攻角附面层分离、T尾下洗阻力以及悬臂机翼在 1.5 倍极限平飞空速下的弯扭气弹颤振稳定性。</p>
                <div class="std-bench-row"><span>颤振临界裕度:</span> <strong>≥ 1.50 V_max</strong></div>
                <div class="std-bench-row"><span>风洞天平标定精度:</span> <strong>±0.5% (AIAA S-071)</strong></div>
            </div>

            <div class="std-box">
                <div class="std-header">
                    <span class="std-code">SPEC 05 // AVIONICS EMC</span>
                    <h4>全频段电磁兼容与滤波屏蔽</h4>
                    <div class="std-en">Full-Spectrum EMC &amp; RF Shielding</div>
                </div>
                <p>飞控系统、RTK厘米级差分天线与大功率数传图传单元实施多层物理隔离。机载电调配置双重无源 LC 扼流圈与压敏 TVS 防突波抑制，通过严苛的航空标准传导发射（CE102）与辐射敏感度（RS103）测试。</p>
                <div class="std-bench-row"><span>电源纹波抑制:</span> <strong>≤ 12 mVpp</strong></div>
                <div class="std-bench-row"><span>电磁辐射屏蔽:</span> <strong>≥ 65 dB (MIL-STD-461G)</strong></div>
            </div>

            <div class="std-box">
                <div class="std-header">
                    <span class="std-code">SPEC 06 // CLIMATE ENVELOPE</span>
                    <h4>-40℃ 至 +65℃ 极端气候耐受</h4>
                    <div class="std-en">Full-Envelope Environmental Screening</div>
                </div>
                <p>整机经受高低温湿热交变循环、IP67 级重度暴雨淋水、防尘风沙对吹及高盐雾防腐蚀加速试验。锂离子电池组内置自研 PTC 自加热陶瓷温控膜，确保在极寒高海拔与酷热沙漠极端环境下自主起降。</p>
                <div class="std-bench-row"><span>环境耐受温度:</span> <strong>-40℃ ~ +65℃</strong></div>
                <div class="std-bench-row"><span>密封防护等级:</span> <strong>IP67 (GB/T 4208-2017)</strong></div>
            </div>
        </div>
    </div>

    <div class="verso-footer">
        <div style="font-size:7.5pt; color:#888888; letter-spacing:0.5px;">AEROSPACE MONOGRAPH // MANUFACTURING &amp; QUALITY STANDARDS</div>
        <div class="page-folio">097</div>
    </div>
</div>
'''

# ==============================================================================
# PAGE 098: BACK COVER (纯粹工程封底，无伪ISBN)
# ==============================================================================
def build_backcover_html():
    return '''
<!-- Page 098: Back Cover & Technical Colophon -->
<div class="page page-cover">
    <div class="running-header" style="border-bottom: 0.5px solid rgba(0, 0, 0, 0.12);">
        <div class="rh-title">AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS</div>
        <div class="rh-section">TECHNICAL COLOPHON // SPEC-AERO-2026</div>
    </div>

    <div class="cover-hero-center">
        <div class="backcover-emblem">
            <svg width="56" height="56" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="32" cy="32" r="30" stroke="#1d1d1f" stroke-width="1.5"/>
                <polygon points="32,14 46,48 32,40 18,48" fill="#1d1d1f"/>
                <circle cx="32" cy="32" r="3.5" fill="#0071e3"/>
            </svg>
        </div>
        <h2 class="backcover-headline">未来飞行 · 航空航天飞行系统工程图鉴</h2>
        <div class="backcover-subline">AEROSPACE ENGINEERING &amp; AUTONOMOUS FLIGHT COMPENDIUM</div>

        <div class="colophon-document-box">
            <div class="colophon-cell">
                <span class="col-lbl">文献工程编号</span>
                <span class="col-val">TECH-SPEC-AERO-2026-ENG</span>
            </div>
            <div class="colophon-cell">
                <span class="col-lbl">文献出版级别</span>
                <span class="col-val">UNPUBLISHED ENGINEERING MONOGRAPH</span>
            </div>
            <div class="colophon-cell">
                <span class="col-lbl">研发与设计机构</span>
                <span class="col-val">AERO ADVANCED DYNAMICS &amp; AUTONOMOUS SYSTEMS LAB</span>
            </div>
            <div class="colophon-cell">
                <span class="col-lbl">质量认证准则</span>
                <span class="col-val">AS9100D / ISO 9001:2015 AEROSPACE CERTIFIED</span>
            </div>
        </div>

        <div class="backcover-quote-line">
            “航空工程的理性秩序，与极简主义的克制美学，在此达到完美平衡。”
        </div>
    </div>

    <div class="cover-footer-row">
        <div class="cover-footer-left">
            <div class="corp-brand">© 2026-2027 AERO DYNAMICS ENGINEERING GROUP. ALL RIGHTS RESERVED.</div>
            <div class="corp-sub">RESTRICTED ENGINEERING REFERENCE MONOGRAPH // NOT FOR COMMERCIAL RESALE</div>
        </div>
        <div class="cover-footer-right">
            <div class="cover-doc-id-group">
                <span class="doc-id-label">DOCUMENT CLASSIFICATION</span>
                <span class="doc-id-code">RESTRICTED TECHNICAL ARCHIVE // EDITION 2026</span>
            </div>
            <div class="page-folio">098</div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# CSS STYLESHEET (Pure Swiss Monograph Edition - Pure Exhibition White)
# ==============================================================================
def get_editorial_css():
    return '''
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
    background: #f5f5f7;
    color: #1d1d1f;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    -webkit-font-smoothing: antialiased;
}
.page {
    width: 297mm;
    height: 210mm;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    background: #ffffff;
}

/* 顶部与底部运行眉线 (Running Header / Footer) */
.running-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.12);
    padding-bottom: 3.5mm;
}
.rh-title {
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #1d1d1f;
}
.rh-section {
    font-size: 7.5pt;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #86868b;
}
.verso-footer {
    border-top: 0.5px solid rgba(0, 0, 0, 0.12);
    padding-top: 3.5mm;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}
.page-folio {
    font-size: 10pt;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
    color: #1d1d1f;
    font-family: "SF Mono", Menlo, Consolas, monospace;
}

/* ========================================================= */
/* COVER (PAGE 01 & 098) */
/* ========================================================= */
.page-cover {
    padding: 16mm 22mm 14mm 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #ffffff;
}
.cover-hero-center {
    margin: auto 0;
    text-align: center;
}
.cover-slogan {
    font-size: 13pt;
    font-weight: 400;
    letter-spacing: 14px;
    color: #86868b;
    text-transform: uppercase;
    text-indent: 14px;
    margin-bottom: 7mm;
}
.cover-main-title {
    font-size: 46pt;
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1.1;
    color: #1d1d1f;
}
.cover-sub-title {
    font-size: 20pt;
    font-weight: 600;
    letter-spacing: -0.01em;
    color: #424245;
    margin-top: 3mm;
}
.cover-hairline {
    width: 60px;
    height: 1.5px;
    background: #0071e3;
    margin: 5mm auto;
}
.cover-scope-desc {
    font-size: 9.5pt;
    line-height: 1.6;
    color: #6e6e73;
    max-width: 620px;
    margin: 0 auto;
}
.cover-four-disciplines {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8mm;
    margin-top: 10mm;
    text-align: left;
    border-top: 0.5px solid rgba(0, 0, 0, 0.12);
    padding-top: 5mm;
}
.discipline-col {
    display: flex;
    flex-direction: column;
}
.disc-num {
    font-size: 11pt;
    font-weight: 800;
    color: #0071e3;
    font-family: "SF Mono", Menlo, Consolas, monospace;
}
.disc-title {
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #1d1d1f;
    margin-top: 1mm;
}
.disc-cn {
    font-size: 8pt;
    font-weight: 600;
    color: #424245;
    margin-top: 0.5mm;
}
.discipline-col p {
    font-size: 7.5pt;
    line-height: 1.45;
    color: #86868b;
    margin-top: 1.5mm;
}
.cover-footer-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 0.5px solid rgba(0, 0, 0, 0.12);
    padding-top: 4mm;
}
.cover-footer-left .corp-brand {
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #1d1d1f;
}
.cover-footer-left .corp-sub {
    font-size: 7.2pt;
    color: #86868b;
    margin-top: 1mm;
}
.cover-doc-id-group {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.doc-id-label {
    font-size: 6.5pt;
    font-weight: 800;
    letter-spacing: 1px;
    color: #0071e3;
    font-family: "SF Mono", monospace;
}
.doc-id-code {
    font-size: 7pt;
    color: #86868b;
    font-family: "SF Mono", monospace;
    margin-top: 0.5mm;
}

/* ========================================================= */
/* FOREWORD (PAGE 02) */
/* ========================================================= */
.foreword-grid-layout {
    display: grid;
    grid-template-columns: 1.18fr 1fr;
    gap: 12mm;
    flex: 1;
    margin-top: 5mm;
    margin-bottom: 4mm;
    align-items: stretch;
}
.foreword-text-col {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.editorial-kicker {
    font-size: 7.8pt;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #0071e3;
    margin-bottom: 2mm;
    font-family: "SF Mono", monospace;
}
.foreword-headline {
    font-size: 19pt;
    font-weight: 800;
    letter-spacing: -0.015em;
    line-height: 1.25;
    margin-bottom: 4mm;
    color: #1d1d1f;
}
.foreword-paragraph {
    font-size: 8.8pt;
    line-height: 1.6;
    color: #424245;
    text-align: justify;
    margin-bottom: 3.5mm;
}
.foreword-signature {
    border-top: 0.5px solid rgba(0, 0, 0, 0.12);
    padding-top: 3mm;
    margin-top: 3mm;
}
.sig-name {
    font-size: 8pt;
    font-weight: 700;
    color: #1d1d1f;
    letter-spacing: 0.5px;
}
.sig-role {
    font-size: 7pt;
    color: #86868b;
    margin-top: 1mm;
}
.foreword-taxonomy-col {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border-left: 0.5px solid rgba(0, 0, 0, 0.12);
    padding-left: 8mm;
}
.tax-item {
    margin-bottom: 2.5mm;
}
.tax-header {
    display: flex;
    gap: 3mm;
    align-items: baseline;
}
.tax-code {
    font-size: 8pt;
    font-weight: 800;
    color: #0071e3;
    font-family: "SF Mono", Consolas, monospace;
}
.tax-name {
    font-size: 8.2pt;
    font-weight: 700;
    color: #1d1d1f;
}
.tax-item p {
    font-size: 7.6pt;
    line-height: 1.45;
    color: #6e6e73;
    margin-top: 1mm;
}
.tax-standards-note {
    border-top: 0.5px solid rgba(0, 0, 0, 0.12);
    padding-top: 2.5mm;
    margin-top: 2mm;
}
.std-note-title {
    font-size: 7.2pt;
    font-weight: 800;
    color: #1d1d1f;
    letter-spacing: 0.8px;
    font-family: "SF Mono", monospace;
}
.std-note-desc {
    font-size: 7.2pt;
    line-height: 1.45;
    color: #86868b;
    margin-top: 1mm;
}

/* ========================================================= */
/* TOC (PAGES 03 & 04) */
/* ========================================================= */
.toc-header-section {
    margin-top: 4mm;
    margin-bottom: 4mm;
}
.toc-headline {
    font-size: 18pt;
    font-weight: 800;
    letter-spacing: -0.015em;
    color: #1d1d1f;
}
.toc-subheadline {
    font-size: 8.5pt;
    font-weight: 600;
    color: #0071e3;
    margin-top: 1.5mm;
}
.toc-two-col-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 12mm;
    row-gap: 1.8mm;
    flex: 1;
    align-content: space-between;
}
.toc-row {
    display: flex;
    align-items: baseline;
    gap: 2.5mm;
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.08);
    padding-bottom: 1.2mm;
}
.toc-num {
    font-size: 8.5pt;
    font-weight: 800;
    color: #0071e3;
    font-family: "SF Mono", Consolas, monospace;
    width: 18px;
}
.toc-info {
    flex: 1;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}
.toc-title {
    font-size: 8.5pt;
    font-weight: 700;
    color: #1d1d1f;
    margin-right: 4px;
}
.toc-code {
    font-size: 7.5pt;
    font-family: "SF Mono", Consolas, monospace;
    color: #86868b;
}
.toc-cat {
    font-size: 7.5pt;
    color: #6e6e73;
    white-space: nowrap;
}
.toc-pages {
    font-size: 8pt;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
    color: #1d1d1f;
    white-space: nowrap;
    font-family: "SF Mono", monospace;
}

/* ========================================================= */
/* EXHIBITION (VERSO / ODD PAGES) - 去圆角灰框，工程定位标 */
/* ========================================================= */
.page-verso {
    padding: 16mm 22mm 16mm 24mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #ffffff;
}
.verso-stage {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2mm 0;
}
.verso-mount {
    position: relative;
    border: 0.5px solid rgba(0, 0, 0, 0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    background: #ffffff;
}
.verso-mount img {
    max-width: 236mm;
    max-height: 134mm;
    object-fit: contain;
    display: block;
}
/* 工程定位十字标线 (Architectural reticles) */
.reticle-tick {
    position: absolute;
    width: 10px;
    height: 10px;
    border-color: #0071e3;
    border-style: solid;
    pointer-events: none;
}
.reticle-tick.tl { top: -1px; left: -1px; border-width: 2px 0 0 2px; }
.reticle-tick.tr { top: -1px; right: -1px; border-width: 2px 2px 0 0; }
.reticle-tick.bl { bottom: -1px; left: -1px; border-width: 0 0 2px 2px; }
.reticle-tick.br { bottom: -1px; right: -1px; border-width: 0 2px 2px 0; }

.mount-meta-top {
    position: absolute;
    top: -2.8mm;
    left: 12px;
    font-size: 6pt;
    font-family: "SF Mono", monospace;
    font-weight: 700;
    color: #0071e3;
    background: #ffffff;
    padding: 0 4px;
    letter-spacing: 0.8px;
}
.mount-meta-bottom {
    position: absolute;
    bottom: -2.8mm;
    right: 12px;
    font-size: 6pt;
    font-family: "SF Mono", monospace;
    color: #86868b;
    background: #ffffff;
    padding: 0 4px;
    letter-spacing: 0.5px;
}
.caption-block {
    display: flex;
    flex-direction: column;
    gap: 1.5px;
}
.caption-title {
    font-size: 11pt;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: #1d1d1f;
}
.caption-sub {
    font-size: 8pt;
    color: #6e6e73;
    letter-spacing: 0.5px;
}
.caption-meta {
    font-size: 7.2pt;
    font-family: "SF Mono", Menlo, Consolas, monospace;
    color: #86868b;
    margin-top: 1px;
}

/* ========================================================= */
/* EDITORIAL (RECTO / EVEN PAGES) - 四大多态学术版式体系 */
/* ========================================================= */
.page-recto {
    padding: 16mm 24mm 16mm 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #ffffff;
}

/* 公共标题头 */
.arch-header {
    margin-top: 2.5mm;
    margin-bottom: 3.5mm;
}
.arch-title-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
.arch-main-title {
    font-size: 19pt;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #1d1d1f;
    line-height: 1.15;
}
.arch-cat-tag {
    font-size: 7.8pt;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #0071e3;
    font-family: "SF Mono", monospace;
}
.arch-subtitle {
    font-size: 8.8pt;
    font-weight: 500;
    color: #6e6e73;
    margin-top: 1.5px;
}

/* 图解标题与 LaTeX 公式公共类 */
.plate-label-bar {
    display: flex;
    align-items: baseline;
    gap: 3mm;
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.12);
    padding-bottom: 1.5mm;
    margin-bottom: 2mm;
}
.plb-num {
    font-size: 7.8pt;
    font-weight: 800;
    letter-spacing: 0.8px;
    color: #0071e3;
    font-family: "SF Mono", monospace;
}
.plb-title {
    font-size: 7.8pt;
    font-weight: 700;
    color: #1d1d1f;
    letter-spacing: 0.3px;
}
.theory-desc-text {
    font-size: 7.8pt;
    line-height: 1.55;
    color: #424245;
    text-align: justify;
}
.latex-eq-container {
    border-top: 0.5px solid rgba(0, 113, 227, 0.4);
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.12);
    padding: 2.5mm 0;
    margin: 2.5mm 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.latex-eq-math {
    flex: 1;
    overflow-x: auto;
    color: #1d1d1f;
}
.latex-eq-tag {
    font-size: 7.2pt;
    font-family: "SF Mono", monospace;
    color: #0071e3;
    margin-left: 4mm;
    white-space: nowrap;
}

/* --- ARCHITECTURE 1 SPECIFICS --- */
.two-col-text {
    column-count: 2;
    column-gap: 8mm;
    text-align: justify;
    margin-bottom: 3.5mm;
}
.two-col-text p {
    font-size: 8.2pt;
    line-height: 1.55;
    color: #333336;
}
.blueprint-split-strip {
    display: grid;
    grid-template-columns: 1fr 1.05fr;
    gap: 6mm;
    border-top: 0.5px solid rgba(0, 0, 0, 0.12);
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.12);
    padding: 3.5mm 0;
    margin-bottom: 3.5mm;
    align-items: center;
}
.bss-left {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.bss-right {
    height: 48mm;
    display: flex;
    align-items: center;
    justify-content: center;
}
.floating-vector-diagram {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.hero-and-table-row {
    display: grid;
    grid-template-columns: 0.85fr 1.45fr;
    gap: 6mm;
    align-items: stretch;
}
.hero-stat-strip-4 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3mm 4mm;
    align-content: center;
}
.hss-item {
    border-left: 1.5px solid #0071e3;
    padding-left: 2.5mm;
    display: flex;
    flex-direction: column;
}
.hss-idx {
    font-size: 6pt;
    font-family: "SF Mono", monospace;
    color: #0071e3;
    font-weight: 700;
}
.hss-val {
    font-size: 13.5pt;
    font-weight: 800;
    color: #1d1d1f;
    letter-spacing: -0.02em;
    line-height: 1.1;
    margin: 0.5mm 0;
}
.hss-lbl {
    font-size: 6.8pt;
    color: #6e6e73;
    text-transform: uppercase;
}
.monograph-booktabs {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.2pt;
}
.monograph-booktabs thead tr {
    border-top: 1.5px solid #1d1d1f;
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.2);
}
.monograph-booktabs th {
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    padding: 1.2mm 0;
    color: #6e6e73;
    font-size: 6.8pt;
}
.monograph-booktabs td {
    padding: 1.4mm 0;
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.06);
    color: #424245;
}
.monograph-booktabs td.bv {
    color: #1d1d1f;
    font-weight: 600;
}
.monograph-booktabs tbody tr:last-child td {
    border-bottom: 1.5px solid #1d1d1f;
}

/* --- ARCHITECTURE 2 SPECIFICS --- */
.pure-highlights-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6mm;
    border-top: 0.5px solid rgba(0, 0, 0, 0.12);
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.12);
    padding: 4mm 0;
    margin-bottom: 4mm;
}
.ph-col {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border-right: 0.5px solid rgba(0, 0, 0, 0.08);
    padding-right: 5mm;
}
.ph-col:last-child {
    border-right: none;
    padding-right: 0;
}
.ph-num {
    font-size: 26pt;
    font-weight: 200;
    color: #0071e3;
    font-family: "SF Mono", monospace;
    line-height: 0.9;
    letter-spacing: -1px;
}
.ph-title {
    font-size: 8.5pt;
    font-weight: 700;
    color: #1d1d1f;
    margin: 2mm 0 1.5mm 0;
}
.ph-desc {
    font-size: 7.5pt;
    line-height: 1.5;
    color: #424245;
    text-align: justify;
    flex: 1;
}
.ph-metric-row {
    border-top: 0.5px solid rgba(0, 0, 0, 0.08);
    padding-top: 2mm;
    margin-top: 2.5mm;
    display: flex;
    align-items: baseline;
    gap: 2mm;
}
.ph-m-val {
    font-size: 13pt;
    font-weight: 800;
    color: #1d1d1f;
}
.ph-m-lbl {
    font-size: 6.8pt;
    color: #86868b;
    text-transform: uppercase;
}
.pure-wide-diagram-strip {
    display: grid;
    grid-template-columns: 1.35fr 1fr;
    gap: 6mm;
    align-items: center;
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.12);
    padding-bottom: 3.5mm;
    margin-bottom: 3.5mm;
}
.pw-svg-col {
    height: 48mm;
    display: flex;
    align-items: center;
    justify-content: center;
}
.pw-math-col {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.linear-specs-ribbon {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 2mm 4mm;
    padding: 1mm 0;
}
.lsr-item {
    display: flex;
    flex-direction: column;
    border-left: 0.5px solid rgba(0, 0, 0, 0.12);
    padding-left: 2mm;
}
.lsr-item span {
    font-size: 6.5pt;
    color: #86868b;
}
.lsr-item strong {
    font-size: 7.8pt;
    color: #1d1d1f;
    margin-top: 0.5mm;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* --- ARCHITECTURE 3 SPECIFICS --- */
.editorial-quote-line {
    display: flex;
    gap: 3mm;
    align-items: center;
    border-top: 0.5px solid rgba(0, 0, 0, 0.12);
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.12);
    padding: 2.5mm 0;
    margin-bottom: 3.5mm;
}
.eql-bar {
    width: 3px;
    height: 16px;
    background: #0071e3;
    flex-shrink: 0;
}
.eql-content {
    display: flex;
    gap: 2mm;
    align-items: baseline;
}
.eql-tag {
    font-size: 7pt;
    font-weight: 800;
    color: #0071e3;
    font-family: "SF Mono", monospace;
}
.eql-quote {
    font-size: 8.8pt;
    font-weight: 600;
    color: #1d1d1f;
    letter-spacing: 0.2px;
}
.tri-narrative-grid {
    display: grid;
    grid-template-columns: 1.15fr 1.15fr 0.95fr;
    gap: 6mm;
    margin-bottom: 3.5mm;
}
.tng-col {
    display: flex;
    flex-direction: column;
}
.tng-header {
    font-size: 7.2pt;
    font-weight: 800;
    color: #0071e3;
    letter-spacing: 1px;
    font-family: "SF Mono", monospace;
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.1);
    padding-bottom: 1.5mm;
    margin-bottom: 2mm;
}
.tng-col p {
    font-size: 7.8pt;
    line-height: 1.55;
    color: #424245;
    text-align: justify;
}
.tng-stat-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3mm 2mm;
}
.tng-stat-cell {
    border-left: 1.5px solid rgba(0, 113, 227, 0.6);
    padding-left: 2mm;
    display: flex;
    flex-direction: column;
}
.ts-val {
    font-size: 14pt;
    font-weight: 800;
    color: #1d1d1f;
    line-height: 1.1;
}
.ts-lbl {
    font-size: 6.5pt;
    color: #86868b;
    text-transform: uppercase;
}
.central-latex-stage {
    border-top: 1px solid rgba(0, 113, 227, 0.4);
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.12);
    padding: 3mm 0;
    margin-bottom: 3.5mm;
}
.cls-header {
    display: flex;
    align-items: baseline;
    gap: 3mm;
    margin-bottom: 2mm;
}
.cls-math {
    color: #1d1d1f;
    padding: 1mm 0;
}
.compact-matrix-footer {
    display: flex;
    flex-direction: column;
    padding: 1.5mm 0;
}
.cmf-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr 1fr);
    column-gap: 2mm;
    font-size: 7.2pt;
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.06);
    padding-bottom: 1mm;
}
.cmf-k { color: #86868b; }
.cmf-v { color: #1d1d1f; font-weight: 600; }

/* --- ARCHITECTURE 4 SPECIFICS --- */
.single-lead-text {
    margin-bottom: 3.5mm;
}
.single-lead-text p {
    font-size: 8.5pt;
    line-height: 1.6;
    color: #333336;
    text-align: justify;
    max-width: 90%;
}
.diagram-and-math-monolith {
    border-top: 0.5px solid rgba(0, 0, 0, 0.12);
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.12);
    padding: 3.5mm 0;
    margin-bottom: 3.5mm;
}
.dam-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 2mm;
}
.dam-svg-box {
    height: 48mm;
    display: flex;
    align-items: center;
    justify-content: center;
}
.dam-math-row {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 6mm;
    align-items: center;
    border-top: 0.5px solid rgba(0, 113, 227, 0.3);
    padding-top: 2.5mm;
    margin-top: 2.5mm;
}
.dam-desc {
    font-size: 7.6pt;
    line-height: 1.5;
    color: #424245;
    text-align: justify;
}
.open-matrix-8 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 3mm 6mm;
    padding: 1.5mm 0;
}
.om-cell {
    border-top: 0.5px solid rgba(0, 0, 0, 0.1);
    padding-top: 1.5mm;
    display: flex;
    flex-direction: column;
}
.om-lbl {
    font-size: 6.5pt;
    color: #86868b;
    text-transform: uppercase;
}
.om-val {
    font-size: 13.5pt;
    font-weight: 800;
    color: #1d1d1f;
    margin-top: 0.5mm;
}
.om-sub {
    font-size: 7.8pt;
    font-weight: 600;
    color: #0071e3;
    margin-top: 1mm;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* ========================================================= */
/* STANDARDS (PAGE 097) - BALANCED FLOW WITH ZERO VOIDS */
/* ========================================================= */
.standards-header-block {
    margin-top: 3mm;
    margin-bottom: 3mm;
}
.standards-headline {
    font-size: 18pt;
    font-weight: 800;
    letter-spacing: -0.015em;
    color: #1d1d1f;
}
.standards-subheadline {
    font-size: 8.5pt;
    font-weight: 600;
    color: #0071e3;
    margin-top: 1.5mm;
}
.standards-editorial-wrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin: 1mm 0;
}
.standards-grid-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 4mm 8mm;
}
.std-box {
    border-top: 0.5px solid rgba(0, 0, 0, 0.15);
    padding-top: 2mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.std-header .std-code {
    font-size: 6.8pt;
    font-weight: 800;
    color: #0071e3;
    font-family: "SF Mono", Consolas, monospace;
    letter-spacing: 0.5px;
}
.std-header h4 {
    font-size: 9.5pt;
    font-weight: 700;
    color: #1d1d1f;
    margin-top: 0.8mm;
}
.std-header .std-en {
    font-size: 7pt;
    color: #86868b;
    margin-bottom: 1.5mm;
}
.std-box p {
    font-size: 7.5pt;
    line-height: 1.45;
    color: #424245;
    text-align: justify;
}
.std-bench-row {
    border-top: 0.5px solid rgba(0, 0, 0, 0.08);
    padding-top: 1.2mm;
    margin-top: 1.5mm;
    display: flex;
    justify-content: space-between;
    font-size: 7pt;
    color: #6e6e73;
}
.std-bench-row strong {
    color: #0071e3;
    font-family: "SF Mono", monospace;
}

/* AS9100D Central Lifecycle Bar */
.as9100d-lifecycle-bar {
    border-top: 0.5px solid rgba(0, 0, 0, 0.15);
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.15);
    background: #fbfbfd;
    padding: 2.5mm 4mm;
    margin: 2mm 0;
}
.as9100d-lifecycle-title-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 2mm;
}
.as9100d-lifecycle-title {
    font-size: 7pt;
    font-weight: 800;
    color: #1d1d1f;
    letter-spacing: 0.8px;
    font-family: "SF Mono", monospace;
}
.as9100d-lifecycle-steps {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 3mm;
}
.al-step {
    border-left: 2px solid #0071e3;
    padding-left: 2mm;
    display: flex;
    flex-direction: column;
}
.al-step-num {
    font-size: 6.2pt;
    font-family: "SF Mono", monospace;
    font-weight: 800;
    color: #0071e3;
}
.al-step-name {
    font-size: 7.2pt;
    font-weight: 700;
    color: #1d1d1f;
    margin-top: 0.5mm;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.al-step-metric {
    font-size: 6.5pt;
    color: #86868b;
    margin-top: 0.5mm;
}

/* ========================================================= */
/* BACK COVER (PAGE 098) */
/* ========================================================= */
.backcover-emblem {
    margin-bottom: 4mm;
}
.backcover-headline {
    font-size: 20pt;
    font-weight: 800;
    letter-spacing: -0.015em;
    color: #1d1d1f;
}
.backcover-subline {
    font-size: 9pt;
    font-weight: 600;
    color: #0071e3;
    letter-spacing: 1px;
    margin-top: 1.5mm;
}
.colophon-document-box {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4mm 8mm;
    max-width: 620px;
    margin: 8mm auto 4mm auto;
    text-align: left;
    border-top: 0.5px solid rgba(0, 0, 0, 0.12);
    border-bottom: 0.5px solid rgba(0, 0, 0, 0.12);
    padding: 4mm 0;
}
.colophon-cell {
    display: flex;
    flex-direction: column;
}
.col-lbl {
    font-size: 6.8pt;
    font-weight: 700;
    text-transform: uppercase;
    color: #86868b;
    letter-spacing: 0.5px;
}
.col-val {
    font-size: 8.2pt;
    font-weight: 700;
    color: #1d1d1f;
    margin-top: 1mm;
}
.backcover-quote-line {
    font-size: 9.5pt;
    font-style: italic;
    color: #6e6e73;
    margin-top: 5mm;
}

/* KaTeX Global Light Styling */
.katex {
    font-size: 1.05em !important;
    text-rendering: geometricPrecision;
    color: #1d1d1f !important;
}
.katex-display {
    margin: 0.2em 0 !important;
}
'''

# ==============================================================================
# PIPELINE RUNNER
# ==============================================================================
def generate_full_html():
    items = catalog_data_v2.ITEMS
    print(f"Generating Pure Swiss Monograph HTML (Exhibition White) for {len(items)} exhibits (98 pages total)...")

    full_body = ""
    # P1: Cover
    full_body += build_cover_html()
    # P2: Foreword
    full_body += build_foreword_html()
    # P3: TOC Part 1
    full_body += build_toc_html(part=1)
    # P4: TOC Part 2
    full_body += build_toc_html(part=2)

    # P5 - P96: 46 Exhibits x 2 = 92 Pages
    for it in items:
        full_body += build_exhibit_spread_html(it)

    # P97: Manufacturing Standards
    full_body += build_standards_html()
    # P98: Back Cover
    full_body += build_backcover_html()

    html_doc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>未来飞行 · 航空航天飞行系统工程图鉴 (Swiss Monograph White Edition)</title>
<link rel="stylesheet" href="{KATEX_CSS_PATH}">
<style>
{get_editorial_css()}
</style>
</head>
<body>
{full_body}
</body>
</html>'''

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_doc)
    print(f"Successfully generated Master HTML: {OUTPUT_HTML} ({len(html_doc)} bytes)")

async def render_pdf():
    print("Launching Chromium via Playwright to generate Print-Ready PDF...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2
        )
        page = await context.new_page()

        file_url = f"file:///{OUTPUT_HTML}"
        print(f"Navigating to {file_url}...")
        await page.goto(file_url, wait_until="networkidle", timeout=120000)

        # 等待 KaTeX 字体加载就绪
        await page.wait_for_selector(".katex", timeout=15000)
        await asyncio.sleep(2)

        print("Generating PDF (A4 Landscape, print background enabled)...")
        await page.pdf(
            path=OUTPUT_PDF,
            width="297mm",
            height="210mm",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            prefer_css_page_size=True
        )
        await browser.close()
    print(f"Successfully generated PDF: {OUTPUT_PDF}")

def export_page_images():
    print(f"Rendering high-res page PNGs from {OUTPUT_PDF}...")
    os.makedirs(OUTPUT_PAGES_DIR, exist_ok=True)
    doc = fitz.open(OUTPUT_PDF)
    print(f"Total pages in PDF: {len(doc)}")
    assert len(doc) == 98, f"Expected 98 pages, got {len(doc)}"

    zoom = 1.5 # 150 DPI for crisp interactive viewer
    mat = fitz.Matrix(zoom, zoom)

    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        p_num = i + 1
        out_png = os.path.join(OUTPUT_PAGES_DIR, f"page_{p_num:03d}.png")
        pix.save(out_png)
        if p_num % 20 == 0 or p_num == 98:
            print(f"  Rendered page {p_num:03d}/098 -> {out_png}")

    print("All 98 page images successfully exported!")

def build_interactive_viewer_html():
    viewer_path = os.path.join(WORKSPACE_DIR, "Apple_Interactive_Viewer.html").replace("\\", "/")
    print(f"Building Apple Interactive Spread Viewer at {viewer_path}...")

    viewer_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>未来飞行 · 航空航天飞行系统工程图鉴 (Swiss Monograph 98P Viewer)</title>
<style>
:root {
    --bg-color: #141416;
    --stage-bg: #18181b;
    --text-primary: #f5f5f7;
    --text-secondary: #8e8e93;
    --accent: #2997ff;
    --spine-color: #d2d2d7;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    background: var(--bg-color);
    color: var(--text-primary);
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", sans-serif;
    height: 100vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}
.top-nav {
    height: 52px;
    background: rgba(20, 20, 22, 0.9);
    backdrop-filter: blur(20px);
    border-bottom: 0.5px solid rgba(255, 255, 255, 0.12);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px;
    z-index: 100;
}
.brand-title {
    display: flex;
    align-items: center;
    gap: 12px;
}
.brand-badge {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2.5px;
    color: #fff;
    background: #0071e3;
    padding: 3px 8px;
    border-radius: 4px;
    font-family: "SF Mono", monospace;
}
.brand-name {
    font-size: 14px;
    font-weight: 600;
    letter-spacing: -0.2px;
    color: var(--text-primary);
}
.nav-controls {
    display: flex;
    align-items: center;
    gap: 12px;
}
.btn-control {
    background: rgba(255, 255, 255, 0.08);
    border: 0.5px solid rgba(255, 255, 255, 0.15);
    color: #fff;
    padding: 6px 14px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    gap: 6px;
}
.btn-control:hover {
    background: rgba(255, 255, 255, 0.16);
}
.btn-control.active {
    background: #0071e3;
    border-color: #0071e3;
}
.page-indicator {
    font-size: 12px;
    font-variant-numeric: tabular-nums;
    color: var(--text-secondary);
    font-family: "SF Mono", monospace;
}
.page-indicator strong {
    color: #fff;
}
.stage-container {
    flex: 1;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--stage-bg);
    overflow: hidden;
    padding: 16px;
}
.spread-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1px;
    max-width: 96vw;
    max-height: 87vh;
    box-shadow: 0 30px 80px rgba(0, 0, 0, 0.6), 0 4px 16px rgba(0, 0, 0, 0.3);
    background: var(--spine-color);
}
.page-view {
    max-height: 87vh;
    max-width: calc(48vw - 8px);
    object-fit: contain;
    background: #ffffff;
    display: block;
    user-select: none;
}
.single-mode .page-view {
    max-width: 90vw;
}
.nav-arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 44px;
    height: 44px;
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    border: 0.5px solid rgba(255, 255, 255, 0.2);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    cursor: pointer;
    transition: all 0.2s;
    z-index: 50;
    user-select: none;
}
.nav-arrow:hover {
    background: rgba(255, 255, 255, 0.22);
    transform: translateY(-50%) scale(1.05);
}
.nav-arrow.prev { left: 24px; }
.nav-arrow.next { right: 24px; }
.bottom-drawer {
    height: 80px;
    background: rgba(18, 18, 20, 0.95);
    backdrop-filter: blur(20px);
    border-top: 0.5px solid rgba(255, 255, 255, 0.1);
    display: flex;
    align-items: center;
    padding: 0 20px;
    gap: 8px;
    overflow-x: auto;
    scrollbar-width: thin;
    scrollbar-color: rgba(255,255,255,0.2) transparent;
}
.thumb-item {
    height: 56px;
    aspect-ratio: 297 / 210;
    overflow: hidden;
    cursor: pointer;
    border: 1px solid rgba(255, 255, 255, 0.12);
    opacity: 0.55;
    transition: all 0.2s;
    flex-shrink: 0;
    position: relative;
    background: #ffffff;
}
.thumb-item:hover {
    opacity: 0.95;
    transform: translateY(-2px);
}
.thumb-item.active {
    border-color: #0071e3;
    opacity: 1;
}
.thumb-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.thumb-folio {
    position: absolute;
    bottom: 2px;
    right: 3px;
    font-size: 8px;
    font-weight: 700;
    background: rgba(0, 0, 0, 0.75);
    color: #fff;
    padding: 1px 3px;
    font-family: monospace;
}
</style>
</head>
<body>

<div class="top-nav">
    <div class="brand-title">
        <span class="brand-badge">GREET AERO</span>
        <span class="brand-name">未来飞行 · 航空航天飞行系统工程图鉴 (Swiss Monograph White 98P)</span>
    </div>

    <div class="nav-controls">
        <button class="btn-control active" id="btnSpread" onclick="setViewMode('spread')">
            <span>📖</span> 跨页对展阅读 (Spread View)
        </button>
        <button class="btn-control" id="btnSingle" onclick="setViewMode('single')">
            <span>📄</span> 单页精细检视 (Single View)
        </button>
        <div class="page-indicator" id="pageIndicator">
            页面: <strong>001 / 098</strong>
        </div>
        <a class="btn-control" href="Aero_UAV_Master_Catalog_AppleStyle_98P.pdf" download style="text-decoration:none;">
            <span>⬇</span> 下载典藏印刷 PDF
        </a>
    </div>
</div>

<div class="stage-container" id="stageContainer">
    <div class="nav-arrow prev" onclick="prevPage()">‹</div>
    
    <div class="spread-wrapper" id="spreadWrapper">
        <img src="brochure_pages_v2/page_001.png" class="page-view" id="leftPage" alt="Page Left">
        <img src="brochure_pages_v2/page_002.png" class="page-view" id="rightPage" alt="Page Right" style="display:none;">
    </div>

    <div class="nav-arrow next" onclick="nextPage()">›</div>
</div>

<div class="bottom-drawer" id="thumbDrawer"></div>

<script>
const TOTAL_PAGES = 98;
let currentPage = 1;
let viewMode = 'spread';

function initThumbs() {
    const drawer = document.getElementById('thumbDrawer');
    let html = '';
    for (let i = 1; i <= TOTAL_PAGES; i++) {
        const pNum = String(i).padStart(3, '0');
        html += `
        <div class="thumb-item ${i === 1 ? 'active' : ''}" id="thumb-${i}" onclick="jumpToPage(${i})">
            <img src="brochure_pages_v2/page_${pNum}.png" loading="lazy" alt="P.${pNum}">
            <span class="thumb-folio">${pNum}</span>
        </div>
        `;
    }
    drawer.innerHTML = html;
}

function updateView() {
    const leftImg = document.getElementById('leftPage');
    const rightImg = document.getElementById('rightPage');
    const indicator = document.getElementById('pageIndicator');
    const spreadWrapper = document.getElementById('spreadWrapper');

    document.querySelectorAll('.thumb-item').forEach(el => el.classList.remove('active'));

    if (viewMode === 'single') {
        spreadWrapper.classList.add('single-mode');
        rightImg.style.display = 'none';
        leftImg.src = `brochure_pages_v2/page_${String(currentPage).padStart(3, '0')}.png`;
        indicator.innerHTML = `单页检视: <strong>${String(currentPage).padStart(3, '0')} / 098</strong>`;
        const thumb = document.getElementById(`thumb-${currentPage}`);
        if (thumb) {
            thumb.classList.add('active');
            thumb.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
        }
    } else {
        spreadWrapper.classList.remove('single-mode');
        if (currentPage === 1) {
            rightImg.style.display = 'none';
            leftImg.src = 'brochure_pages_v2/page_001.png';
            indicator.innerHTML = `封面: <strong>001 / 098</strong> (GREET AERO)`;
            const thumb = document.getElementById('thumb-1');
            if (thumb) { thumb.classList.add('active'); thumb.scrollIntoView({ behavior: 'smooth', inline: 'center' }); }
        } else if (currentPage >= TOTAL_PAGES) {
            rightImg.style.display = 'none';
            leftImg.src = `brochure_pages_v2/page_098.png`;
            indicator.innerHTML = `封底: <strong>098 / 098</strong>`;
            const thumb = document.getElementById('thumb-98');
            if (thumb) { thumb.classList.add('active'); thumb.scrollIntoView({ behavior: 'smooth', inline: 'center' }); }
        } else {
            let leftP = currentPage % 2 === 0 ? currentPage : currentPage - 1;
            let rightP = leftP + 1;
            leftImg.src = `brochure_pages_v2/page_${String(leftP).padStart(3, '0')}.png`;
            rightImg.src = `brochure_pages_v2/page_${String(rightP).padStart(3, '0')}.png`;
            rightImg.style.display = 'block';
            indicator.innerHTML = `跨页对展: <strong>${String(leftP).padStart(3, '0')} — ${String(rightP).padStart(3, '0')}</strong> / 098`;
            const thumbL = document.getElementById(`thumb-${leftP}`);
            if (thumbL) { thumbL.classList.add('active'); thumbL.scrollIntoView({ behavior: 'smooth', inline: 'center' }); }
            const thumbR = document.getElementById(`thumb-${rightP}`);
            if (thumbR) thumbR.classList.add('active');
        }
    }
}

function setViewMode(mode) {
    viewMode = mode;
    document.getElementById('btnSpread').classList.toggle('active', mode === 'spread');
    document.getElementById('btnSingle').classList.toggle('active', mode === 'single');
    updateView();
}

function prevPage() {
    if (viewMode === 'single') {
        if (currentPage > 1) currentPage--;
    } else {
        if (currentPage === 1) return;
        if (currentPage <= 3) currentPage = 1;
        else currentPage -= 2;
    }
    updateView();
}

function nextPage() {
    if (viewMode === 'single') {
        if (currentPage < TOTAL_PAGES) currentPage++;
    } else {
        if (currentPage === 1) currentPage = 2;
        else if (currentPage >= TOTAL_PAGES - 1) currentPage = TOTAL_PAGES;
        else currentPage += 2;
    }
    updateView();
}

function jumpToPage(p) {
    currentPage = p;
    updateView();
}

window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {
        nextPage();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        prevPage();
    }
});

initThumbs();
updateView();
</script>

</body>
</html>'''

    with open(viewer_path, "w", encoding="utf-8") as f:
        f.write(viewer_html)
    print(f"Successfully created viewer: {viewer_path}")

async def main():
    print("=== STARTING PURE SWISS MONOGRAPH PRODUCTION (WHITE EDITION + NEW BLUEPRINTS) ===")
    generate_full_html()
    await render_pdf()
    export_page_images()
    build_interactive_viewer_html()
    print("=== PRODUCTION COMPLETED SUCCESSFULLY! ===")

if __name__ == "__main__":
    asyncio.run(main())
