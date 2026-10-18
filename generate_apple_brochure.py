# -*- coding: utf-8 -*-
"""
Aero UAV Master Catalog (Apple Official Website Design Aesthetic)
98-Page Landscape A4 Print-Ready PDF & Interactive System Generator

Architecture:
- Page 01: Master Cover (Apple Keynote Pristine Typography & Blueprint)
- Page 02: Foreword & Engineering Philosophy (航空工学与极简工业设计哲学)
- Page 03: Table of Contents Part 1 (Exhibits 01 - 23)
- Page 04: Table of Contents Part 2 (Exhibits 24 - 46)
- Pages 05 - 96: 46 Exhibits x 2 Pages = 92 Pages
    * Odd Pages (005, 007, ..., 095): Pure Exhibition Page (Large Hero Image, Studio Pedestal, Ample Negative Space)
    * Even Pages (006, 008, ..., 096): Illustrated In-Depth Editorial (Academic Aerodynamic Theory, Vector SVG, Big Numbers, Specs)
- Page 97: Manufacturing & Quality Engineering Standards (航空级制造工艺与品控标准)
- Page 98: Back Cover & Technical Colophon (极简封底、装订技术说明、工业条码)

Total Pages: Exactly 98 Pages
Single-Sided Print Layout for Butterfly Binding (蝴蝶对裱精装).
"""

import os
import sys
import asyncio
from playwright.async_api import async_playwright
import fitz # PyMuPDF

import catalog_data_v2
import generate_svgs

WORKSPACE_DIR = os.path.abspath("e:/brochure").replace("\\", "/")
IMAGE_DIR = os.path.join(WORKSPACE_DIR, "飞机截图").replace("\\", "/")
OUTPUT_HTML = os.path.join(WORKSPACE_DIR, "Aero_UAV_Catalog_AppleStyle_98P.html").replace("\\", "/")
OUTPUT_PDF = os.path.join(WORKSPACE_DIR, "Aero_UAV_Master_Catalog_AppleStyle_98P.pdf").replace("\\", "/")
OUTPUT_PAGES_DIR = os.path.join(WORKSPACE_DIR, "brochure_pages_v2").replace("\\", "/")

def build_cover_html():
    return '''
<!-- Page 01: Master Cover -->
<div class="page page-cover">
    <div class="cover-technical-grid"></div>
    <div class="cover-top">
        <div class="cover-kicker">AEROSPACE DYNAMICS & ADVANCED AUTONOMOUS SYSTEMS // 2026-2027 COLLECTOR'S EDITION</div>
        <div class="cover-badge">MASTER BLUEPRINT // 98P FULL CATALOG</div>
    </div>
    
    <div class="cover-center">
        <div class="cover-title-group">
            <h1 class="cover-hero-title">未来飞行</h1>
            <h2 class="cover-hero-subtitle">航空航天飞行系统工程图鉴</h2>
            <div class="cover-divider-line"></div>
            <p class="cover-desc">
                46 款全自研工业级飞行器与核心关键部件 · 气动力学与空间飞行动力学深度理论解析<br>
                苹果极简工业美学体系 · 单面高精艺术微喷 · 蝴蝶对裱精装典藏
            </p>
        </div>

        <div class="cover-feature-grid">
            <div class="cover-feature-card">
                <span class="cover-feat-num">46</span>
                <span class="cover-feat-lbl">独立先锋展项</span>
                <span class="cover-feat-sub">多旋翼 / 复合翼 / 动力总成</span>
            </div>
            <div class="cover-feature-card">
                <span class="cover-feat-num">98</span>
                <span class="cover-feat-lbl">完整典藏印张</span>
                <span class="cover-feat-sub">一页纯展 · 一页图文理论解构</span>
            </div>
            <div class="cover-feature-card">
                <span class="cover-feat-num">100%</span>
                <span class="cover-feat-lbl">深度专业理论</span>
                <span class="cover-feat-sub">普朗特 / 纳维-斯托克斯 / 蔡-吴准则</span>
            </div>
            <div class="cover-feature-card">
                <span class="cover-feat-num">180°</span>
                <span class="cover-feat-lbl">展平蝴蝶对裱</span>
                <span class="cover-feat-sub">单面印刷装订 · 厚重刚挺书页</span>
            </div>
        </div>
    </div>

    <div class="cover-bottom">
        <div class="cover-meta-left">
            <div class="cover-meta-brand">AERO-RESEARCH &amp; AUTONOMOUS SYSTEMS LAB</div>
            <div class="cover-meta-sub">AEROSPACE ENGINEERING MONOGRAPH · PUBLISHED IN 2026</div>
        </div>
        <div class="cover-meta-right">
            <div class="cover-barcode-box">
                <div class="barcode-lines">
                    <span style="width:2px;"></span><span style="width:1px;"></span><span style="width:3px;"></span>
                    <span style="width:1px;"></span><span style="width:2px;"></span><span style="width:4px;"></span>
                    <span style="width:1px;"></span><span style="width:2px;"></span><span style="width:1px;"></span>
                    <span style="width:3px;"></span><span style="width:2px;"></span><span style="width:1px;"></span>
                    <span style="width:4px;"></span><span style="width:2px;"></span><span style="width:1px;"></span>
                    <span style="width:3px;"></span><span style="width:1px;"></span><span style="width:2px;"></span>
                </div>
                <span class="barcode-num">ISBN 978-7-900826-46-0</span>
            </div>
            <div class="cover-folio">P.001</div>
        </div>
    </div>
</div>
'''

def build_foreword_html():
    return '''
<!-- Page 02: Foreword & Philosophy -->
<div class="page page-foreword">
    <div class="page-header-row">
        <div class="header-breadcrumb">PREFACE &amp; TAXONOMY // 序言与全书工程架构</div>
        <div class="header-edition">AEROSPACE DYNAMICS // VOL. 01</div>
    </div>

    <div class="foreword-layout">
        <!-- 左列：设计与工程哲学 -->
        <div class="foreword-left">
            <div class="foreword-kicker">ENGINEERING PHILOSOPHY</div>
            <h2 class="foreword-title">极简之道，始于至繁。<br><span style="color:#0071e3;">功能之纯粹，即美学之巅峰。</span></h2>
            
            <p class="foreword-p">
                现代航空航天工程的本质，是在严苛的物理定律与无情的重力场中寻求最优解。飞行器上的每一道微弧曲面，都不是为了装饰而存在，而是由普朗特附面层微分方程、纳维-斯托克斯流场以及蔡-吴复合材料破坏准则严格决定的自然形态。
            </p>
            <p class="foreword-p">
                在这部《未来飞行 · 航空航天飞行系统工程图鉴》中，我们彻底打破了传统工业图录粗粝繁杂的视觉范式，将苹果官网极致严谨的现代工业设计语言（Apple Industrial Aesthetic）全面引入航空领域。我们剔除了所有干扰视线的虚饰线条与暗黑游戏感霓虹，重现纯粹、高贵、理性的工作室（Studio）光影环境。
            </p>
            <p class="foreword-p">
                本书严格按照<strong>“单面印刷、蝴蝶装平展对裱”</strong>工艺设计：全书 46 大核心展项，每一款均以<strong>“跨页对读（Spread）”</strong>的经典节奏呈现——左侧（奇数页）为极致纯粹的沉浸式大幅模型展示，右侧（偶数页）则深度解构其气动流场、动力控制与结构力学专业理论，真正实现艺术典藏级品味与严谨工学深度的无缝统一。
            </p>

            <div class="foreword-sign-box">
                <div class="foreword-sign-name">AERO ADVANCED DYNAMICS COMMITTEE</div>
                <div class="foreword-sign-title">航空航天先进飞行系统工程编委会 · 首席设计工程组</div>
            </div>
        </div>

        <!-- 右列：四大分类架构与装订技术指标 -->
        <div class="foreword-right">
            <div class="foreword-kicker">TAXONOMY &amp; SYSTEMS // 四大核心分类谱系</div>
            
            <div class="taxonomy-list">
                <div class="taxonomy-card">
                    <div class="tax-num">PART I</div>
                    <div class="tax-content">
                        <h4>战术多旋翼与长航时穿越探测平台 (Exhibits 01 - 12)</h4>
                        <p>涵盖流线型航拍无人机、True-X竞技机架、长航时探测平台与环形涵道安防机架，解构附面层低阻与惯量张量解耦理论。</p>
                    </div>
                </div>

                <div class="taxonomy-card">
                    <div class="tax-num">PART II</div>
                    <div class="tax-content">
                        <h4>复合翼垂直起降与微型室内特种构型 (Exhibits 13 - 22)</h4>
                        <p>大展弦比垂直起降复合翼、后推倒V尾巡逻机、反弯飞翼与管桁笼式机架，解析升力过渡转移与颤振气弹抑制。</p>
                    </div>
                </div>

                <div class="taxonomy-card">
                    <div class="tax-num">PART III</div>
                    <div class="tax-content">
                        <h4>重载农业植保与军工级固定翼系统 (Exhibits 23 - 34)</h4>
                        <p>60升重载植保六旋翼、串列双翼、T尾高稳巡线机与直升机单旋翼，解构下洗流场沉积、液压等阻平衡与旋翼倾斜盘动力学。</p>
                    </div>
                </div>

                <div class="taxonomy-card">
                    <div class="tax-num">PART IV</div>
                    <div class="tax-content">
                        <h4>动力总成、倾转构型与一体复材架构 (Exhibits 35 - 46)</h4>
                        <p>大扭矩外转子无刷马达、折叠碳纤螺旋桨、双旋翼倾转推力矢量及热压罐一体共固化纯碳骨架，解析蔡-吴椭球与GD&T动态平衡。</p>
                    </div>
                </div>
            </div>

            <!-- 装订说明小贴士 -->
            <div class="binding-tip-card">
                <div class="tip-badge">PRINT &amp; BINDING SPECIFICATION</div>
                <div class="tip-text"><strong>蝴蝶对裱精装工艺：</strong> 98页单面打印后两两背面涂胶对裱，书脊厚度约 25~30mm，开本展平 180° 完全无缝，纸张挺度高，极具厚重大气典藏质感。</div>
            </div>
        </div>
    </div>

    <div class="page-footer-row">
        <span>AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS // MASTER BLUEPRINT</span>
        <span class="page-folio-num">002</span>
    </div>
</div>
'''

def build_toc_html(part=1):
    items = catalog_data_v2.ITEMS
    if part == 1:
        part_items = items[0:23] # 01 - 23
        title_sub = "PART I : EXHIBITS 01 — 23 // 战术多旋翼、复合翼与室内特种机型"
        page_num_str = "003"
    else:
        part_items = items[23:46] # 24 - 46
        title_sub = "PART II : EXHIBITS 24 — 46 // 重载植保、动力总成、倾转构型与一体复材"
        page_num_str = "004"

    cards_html = ""
    for it in part_items:
        idx = it["index"]
        exhibit_p = 5 + (idx - 1) * 2
        cards_html += f'''
        <div class="toc-item-row">
            <div class="toc-idx">{idx:02d}</div>
            <div class="toc-body">
                <div class="toc-name-row">
                    <span class="toc-name">{it["name_zh"].split("//")[0].strip()}</span>
                    <span class="toc-code">{it["code"]}</span>
                </div>
                <div class="toc-sub">{it["name_en"]}</div>
            </div>
            <div class="toc-pill">{it["category_zh"]}</div>
            <div class="toc-dots"></div>
            <div class="toc-page">P.{exhibit_p:03d} - {exhibit_p+1:03d}</div>
        </div>
        '''

    return f'''
<!-- Page {page_num_str}: TOC Part {part} -->
<div class="page page-toc">
    <div class="page-header-row">
        <div class="header-breadcrumb">MASTER CATALOG INDEX // 全书目录索引 (第 {part} 部分)</div>
        <div class="header-edition">46 EXHIBITS // 98 PAGES BLUEPRINT</div>
    </div>

    <div class="toc-header-block">
        <h2 class="toc-main-title">全书总目录与展项导引</h2>
        <div class="toc-subtitle">{title_sub}</div>
    </div>

    <div class="toc-grid">
        {cards_html}
    </div>

    <div class="page-footer-row">
        <span>AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS // MASTER BLUEPRINT</span>
        <span class="page-folio-num">{page_num_str}</span>
    </div>
</div>
'''

def build_exhibit_pages_html(item):
    idx = item["index"]
    odd_page_num = 5 + (idx - 1) * 2
    even_page_num = odd_page_num + 1

    img_path = os.path.abspath(os.path.join(IMAGE_DIR, item["image"])).replace("\\", "/")
    svg_markup = generate_svgs.get_svg_diagram(item["svg_type"])

    # Hero stats
    hero_stats_html = ""
    for s in item["hero_stats"]:
        hero_stats_html += f'''
        <div class="stat-card">
            <span class="stat-val">{s["val"]}</span>
            <span class="stat-lbl">{s["lbl"]}</span>
        </div>
        '''

    # Specs table
    specs_html = ""
    for sp in item["specs"]:
        specs_html += f'''
        <div class="spec-row">
            <span class="spec-lbl">{sp["label"]}</span>
            <span class="spec-val">{sp["value"]}</span>
        </div>
        '''

    html = f'''
<!-- Page {odd_page_num:03d}: Pure Exhibition Page -->
<div class="page page-exhibition">
    <div class="exhibit-top">
        <div class="exhibit-series">EXHIBIT // {idx:02d} · AERO MASTER BLUEPRINT</div>
        <div class="exhibit-cat-pill">{item["category_zh"]} · {item["category_en"]}</div>
    </div>

    <div class="exhibit-hero">
        <div class="hero-stage">
            <img src="file:///{img_path}" alt="{item["name_zh"]}">
            <div class="stage-watermark">ENGINEERING CAD RENDERING // 3D MODEL ISOMETRIC // {item["code"]}</div>
        </div>
    </div>

    <div class="exhibit-bottom">
        <div class="exhibit-name-block">
            <h2>{item["name_zh"]}</h2>
            <p>{item["name_en"]} — MODEL SPEC: {item["code"]}</p>
        </div>
        <div class="exhibit-folio">{odd_page_num:03d}</div>
    </div>
</div>

<!-- Page {even_page_num:03d}: Illustrated Editorial & Theory Page -->
<div class="page page-editorial">
    <div class="edit-header">
        <div class="edit-badge-row">
            <span class="badge-cat">{item["category_zh"]}</span>
            <span class="badge-code">{item["code"]}</span>
            <span class="badge-folio-tag">EXHIBIT // {idx:02d} OF 46</span>
        </div>
        <h1 class="edit-title">{item["name_zh"]}</h1>
        <div class="edit-tagline">{item["tagline"]}</div>
        <p class="edit-narrative">{item["desc"]}</p>
    </div>

    <!-- 核心理论深度卡片 -->
    <div class="theory-card">
        <div class="theory-card-header">
            <span class="theory-card-tag">◈ FLIGHT DYNAMICS &amp; AERODYNAMICS // 气动流体与飞行动力学解构</span>
            <span class="theory-title">{item["theory_title"]}</span>
        </div>
        <div class="theory-body">
            <div class="theory-text-col">
                <p class="theory-desc">{item["theory_desc"]}</p>
                <div class="theory-formula-box">
                    <span class="formula-tag">GOVERNING EQ:</span>
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
            {hero_stats_html}
        </div>

        <div class="specs-table">
            {specs_html}
        </div>
    </div>

    <div class="edit-footer">
        <span>AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS // MASTER BLUEPRINT</span>
        <span class="page-folio-num">{even_page_num:03d}</span>
    </div>
</div>
'''
    return html

def build_standards_html():
    return '''
<!-- Page 097: Manufacturing & Quality Standards -->
<div class="page page-standards">
    <div class="page-header-row">
        <div class="header-breadcrumb">MANUFACTURING &amp; QUALITY STANDARDS // 航空工程制造工艺与品质检验规范</div>
        <div class="header-edition">AEROSPACE GRADE 2026</div>
    </div>

    <div class="standards-header">
        <h2 class="standards-main-title">精密智造与极端环境可靠性验证体系</h2>
        <div class="standards-subtitle">
            严格遵循航空航天 AS9100D 质量管理规范 · 全闭环数字孪生生产线与毫厘级机加装配公差
        </div>
    </div>

    <div class="standards-grid">
        <div class="std-card">
            <div class="std-badge">01 // COMPOSITES</div>
            <h3>预浸料热压罐一体共固化工艺</h3>
            <div class="std-sub">Prepreg Autoclave Curing Technology</div>
            <p>采用日本东丽航空级 T700/T800 高模量碳纤维预浸布，在精密模具内经历 130℃ 梯度升温与 0.8MPa 恒压环境。树脂固化率达 98.5% 以上，孔隙率严格控制在 0.5% 以下，消除传统常压成型的层间虚粘与微观气孔。</p>
            <div class="std-metric"><span>层间剪切强度:</span> <strong>≥ 85 MPa</strong></div>
        </div>

        <div class="std-card">
            <div class="std-badge">02 // PRECISION CNC</div>
            <h3>五轴高速精密联动数控切削</h3>
            <div class="std-sub">5-Axis High-Precision CNC Machining</div>
            <p>关键金属连接接头、电机座与云台转轴均选用 7075-T651 航空级超硬铝合金。采用瑞士高精五轴联动加工中心单次装夹切削，全三维空间几何公差（GD&T）控制在 ±0.015mm 内，表面经 25μm 硬质阳极氧化封孔防腐处理。</p>
            <div class="std-metric"><span>装配同轴度:</span> <strong>≤ 0.012 mm</strong></div>
        </div>

        <div class="std-card">
            <div class="std-badge">03 // DYNAMIC BALANCE</div>
            <h3>微克级转子动平衡校准系统</h3>
            <div class="std-sub">Dynamic Balancing Class G1.0 Standard</div>
            <p>全系大扭矩无刷电机转子与碳纤折叠螺旋桨，100% 经过德国申克（Schenck）高精动态平衡机在线校准。在高达 28,000 RPM 极限转速下，叶尖残余不平衡偏心量小于 0.5mg·mm，彻底消除飞行器高频果冻振动与轴承疲劳。</p>
            <div class="std-metric"><span>动平衡等级:</span> <strong>ISO G1.0</strong></div>
        </div>

        <div class="std-card">
            <div class="std-badge">04 // WIND TUNNEL</div>
            <h3>气动气弹风洞与颤振边界实测</h3>
            <div class="std-sub">Aeroacoustic & Wind Tunnel Testing</div>
            <p>全机身三维流线模型置于低湍流度航空风洞中，采用六分量测力天平与粒子图像测速技术（PIV）精细标定。全面验证大攻角附面层分离、T尾下洗阻力以及悬臂机翼在 1.5 倍极限平飞空速下的弯扭气弹颤振稳定性。</p>
            <div class="std-metric"><span>颤振临界裕度:</span> <strong>≥ 1.50 V_max</strong></div>
        </div>

        <div class="std-card">
            <div class="std-badge">05 // AVIONICS EMC</div>
            <h3>全频段电磁兼容与滤波屏蔽</h3>
            <div class="std-sub">Full-Spectrum EMC & RF Shielding</div>
            <p>飞控系统、RTK厘米级差分天线与大功率数传图传单元实施多层物理隔离。机载电调配置双重无源 LC 扼流圈与压敏 TVS 防突波抑制，通过严苛的航空标准传导发射（CE102）与辐射敏感度（RS103）测试。</p>
            <div class="std-metric"><span>电源纹波抑制:</span> <strong>≤ 12 mVpp</strong></div>
        </div>

        <div class="std-card">
            <div class="std-badge">06 // CLIMATE ENVELOPE</div>
            <h3>-40℃ 至 +65℃ 极端气候耐受</h3>
            <div class="std-sub">Full-Envelope Environmental Screening</div>
            <p>整机经受高低温湿热交变循环、IP67 级重度暴雨淋水、防尘风沙对吹及高盐雾防腐蚀加速试验。锂离子电池组内置自研 PTC 自加热陶瓷温控膜，确保在极寒高海拔与酷热沙漠极端环境下自主起降。</p>
            <div class="std-metric"><span>环境耐受温度:</span> <strong>-40℃ ~ +65℃</strong></div>
        </div>
    </div>

    <div class="page-footer-row">
        <span>AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS // MASTER BLUEPRINT</span>
        <span class="page-folio-num">097</span>
    </div>
</div>
'''

def build_backcover_html():
    return '''
<!-- Page 098: Back Cover & Technical Colophon -->
<div class="page page-backcover">
    <div class="cover-technical-grid"></div>
    
    <div class="backcover-top">
        <div class="cover-kicker">AEROSPACE DYNAMICS &amp; AUTONOMOUS FLIGHT SYSTEMS // MASTER BLUEPRINT</div>
        <div class="cover-badge">FINAL FOLIO // P.098</div>
    </div>

    <div class="backcover-center">
        <div class="backcover-logo-mark">
            <svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="32" cy="32" r="30" stroke="#1d1d1f" stroke-width="2.5"/>
                <polygon points="32,12 48,50 32,40 16,50" fill="#0071e3"/>
                <circle cx="32" cy="32" r="6" fill="#1d1d1f"/>
            </svg>
        </div>
        <h2 class="backcover-title">未来飞行 · 航空航天飞行系统工程图鉴</h2>
        <div class="backcover-sub">AEROSPACE ENGINEERING &amp; AUTONOMOUS FLIGHT COMPENDIUM</div>
        
        <div class="backcover-colophon-grid">
            <div class="colophon-col">
                <h4>出版与文献信息</h4>
                <p><strong>工程代号:</strong> SPEC-AERO-2026-98P</p>
                <p><strong>文献版本:</strong> 2026-2027 典藏初版</p>
                <p><strong>执行机构:</strong> 航空先进动力与自主系统设计组</p>
                <p><strong>印张规模:</strong> 98页 (46核心展项 + 气动图析)</p>
            </div>
            <div class="colophon-col">
                <h4>装订与印制技术规范</h4>
                <p><strong>印刷工艺:</strong> 单面超高清艺术微喷 (Single-Sided)</p>
                <p><strong>装订形式:</strong> 蝴蝶对裱精装 (Butterfly Mount)</p>
                <p><strong>内页纸张:</strong> 250g 哑光特级白卡对裱 (~1.0mm/张)</p>
                <p><strong>展平开本:</strong> A4 横版 (297mm × 210mm) 180° 完全展平</p>
            </div>
        </div>

        <div class="backcover-quote">
            “航空工程的理性秩序，与极简主义的克制美学，在此达到完美平衡。”
        </div>
    </div>

    <div class="backcover-bottom">
        <div class="backcover-copyright">
            © 2026-2027 AERO DYNAMICS LAB. ALL RIGHTS RESERVED. PRINTED FOR ENGINEERING REFERENCE.
        </div>
        <div class="cover-barcode-box">
            <div class="barcode-lines">
                <span style="width:2px;"></span><span style="width:1px;"></span><span style="width:3px;"></span>
                <span style="width:1px;"></span><span style="width:2px;"></span><span style="width:4px;"></span>
                <span style="width:1px;"></span><span style="width:2px;"></span><span style="width:1px;"></span>
                <span style="width:3px;"></span><span style="width:2px;"></span><span style="width:1px;"></span>
                <span style="width:4px;"></span><span style="width:2px;"></span><span style="width:1px;"></span>
                <span style="width:3px;"></span><span style="width:1px;"></span><span style="width:2px;"></span>
            </div>
            <span class="barcode-num">ISBN 978-7-900826-46-0</span>
        </div>
        <div class="cover-folio">098</div>
    </div>
</div>
'''

def generate_full_html():
    items = catalog_data_v2.ITEMS
    print(f"Generating full HTML with {len(items)} exhibits (98 pages total)...")

    # CSS styles
    css_content = '''
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
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "PingFang SC", "Segoe UI", "Microsoft YaHei", sans-serif;
    background: #fbfbfd;
    color: #1d1d1f;
    -webkit-font-smoothing: antialiased;
}
.page {
    width: 297mm;
    height: 210mm;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    background: #fbfbfd;
}

/* 通用页眉页脚 */
.page-header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #e5e5ea;
    padding-bottom: 8px;
    margin-bottom: 12px;
}
.header-breadcrumb {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #86868b;
    text-transform: uppercase;
}
.header-edition {
    font-size: 10px;
    font-weight: 600;
    color: #0071e3;
    letter-spacing: 1px;
}
.page-footer-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #e5e5ea;
    padding-top: 8px;
    margin-top: 8px;
    font-size: 9.5px;
    color: #86868b;
}
.page-folio-num {
    font-weight: 700;
    color: #1d1d1f;
    font-variant-numeric: tabular-nums;
}

/* ========================================================= */
/* PAGE 01: COVER */
/* ========================================================= */
.page-cover {
    padding: 16mm 22mm 14mm 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: radial-gradient(circle at 50% 40%, #ffffff 0%, #fbfbfd 60%, #f5f5f7 100%);
}
.cover-technical-grid {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: 
        linear-gradient(to right, rgba(0,0,0,0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(0,0,0,0.03) 1px, transparent 1px);
    background-size: 20mm 20mm;
    pointer-events: none;
}
.cover-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 2;
}
.cover-kicker {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.5px;
    color: #0071e3;
}
.cover-badge {
    font-size: 10px;
    font-weight: 700;
    color: #1d1d1f;
    background: #ffffff;
    border: 1px solid #d2d2d7;
    padding: 4px 12px;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.02);
}
.cover-center {
    position: relative;
    z-index: 2;
    margin: auto 0;
}
.cover-title-group {
    text-align: center;
}
.cover-hero-title {
    font-size: 46px;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #1d1d1f;
    line-height: 1.1;
}
.cover-hero-subtitle {
    font-size: 24px;
    font-weight: 600;
    letter-spacing: -0.01em;
    color: #424245;
    margin-top: 8px;
}
.cover-divider-line {
    width: 60px;
    height: 3px;
    background: #0071e3;
    margin: 14px auto;
    border-radius: 2px;
}
.cover-desc {
    font-size: 12px;
    line-height: 1.6;
    color: #6e6e73;
    max-width: 640px;
    margin: 0 auto;
}
.cover-feature-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-top: 32px;
}
.cover-feature-card {
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 12px;
    padding: 14px 16px;
    text-align: center;
    box-shadow: 0 4px 16px rgba(0,0,0,0.02);
}
.cover-feat-num {
    display: block;
    font-size: 26px;
    font-weight: 800;
    color: #1d1d1f;
    letter-spacing: -0.02em;
}
.cover-feat-lbl {
    display: block;
    font-size: 11px;
    font-weight: 700;
    color: #0071e3;
    margin-top: 4px;
}
.cover-feat-sub {
    display: block;
    font-size: 9.5px;
    color: #86868b;
    margin-top: 3px;
}
.cover-bottom {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid #e5e5ea;
    padding-top: 10px;
    position: relative;
    z-index: 2;
}
.cover-meta-left .cover-meta-brand {
    font-size: 11px;
    font-weight: 700;
    color: #1d1d1f;
    letter-spacing: 1px;
}
.cover-meta-left .cover-meta-sub {
    font-size: 9.5px;
    color: #86868b;
    margin-top: 2px;
}
.cover-meta-right {
    display: flex;
    align-items: center;
    gap: 16px;
}
.cover-barcode-box {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.barcode-lines {
    display: flex;
    height: 18px;
    gap: 2px;
    align-items: stretch;
}
.barcode-lines span {
    background: #1d1d1f;
    display: inline-block;
}
.barcode-num {
    font-size: 8.5px;
    font-family: "SF Mono", Consolas, monospace;
    color: #86868b;
    margin-top: 2px;
}
.cover-folio {
    font-size: 14px;
    font-weight: 700;
    color: #86868b;
    font-variant-numeric: tabular-nums;
}

/* ========================================================= */
/* PAGE 02: FOREWORD */
/* ========================================================= */
.page-foreword {
    padding: 14mm 20mm 12mm 20mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.foreword-layout {
    display: grid;
    grid-template-columns: 1.15fr 1fr;
    gap: 24px;
    flex: 1;
    align-items: stretch;
}
.foreword-left {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.foreword-kicker {
    font-size: 10px;
    font-weight: 700;
    color: #0071e3;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.foreword-title {
    font-size: 20px;
    font-weight: 700;
    letter-spacing: -0.015em;
    line-height: 1.3;
    margin-bottom: 12px;
    color: #1d1d1f;
}
.foreword-p {
    font-size: 10.5px;
    line-height: 1.6;
    color: #424245;
    margin-bottom: 10px;
    text-align: justify;
}
.foreword-sign-box {
    border-top: 1px solid #e5e5ea;
    padding-top: 8px;
    margin-top: 8px;
}
.foreword-sign-name {
    font-size: 11px;
    font-weight: 700;
    color: #1d1d1f;
    letter-spacing: 0.5px;
}
.foreword-sign-title {
    font-size: 9.5px;
    color: #86868b;
    margin-top: 2px;
}
.foreword-right {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.taxonomy-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.taxonomy-card {
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    padding: 8px 12px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
}
.tax-num {
    font-size: 10px;
    font-weight: 800;
    color: #0071e3;
    font-family: "SF Mono", Consolas, monospace;
    white-space: nowrap;
    padding-top: 2px;
}
.tax-content h4 {
    font-size: 11px;
    font-weight: 700;
    color: #1d1d1f;
    margin-bottom: 2px;
}
.tax-content p {
    font-size: 9.5px;
    line-height: 1.45;
    color: #6e6e73;
}
.binding-tip-card {
    background: rgba(0, 113, 227, 0.05);
    border: 1px solid rgba(0, 113, 227, 0.2);
    border-radius: 8px;
    padding: 8px 12px;
    margin-top: 8px;
}
.tip-badge {
    font-size: 9px;
    font-weight: 700;
    color: #0071e3;
    letter-spacing: 1px;
    margin-bottom: 3px;
}
.tip-text {
    font-size: 9.5px;
    line-height: 1.45;
    color: #1d1d1f;
}

/* ========================================================= */
/* PAGES 03 - 04: TOC */
/* ========================================================= */
.page-toc {
    padding: 14mm 20mm 12mm 20mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.toc-header-block {
    margin-bottom: 8px;
}
.toc-main-title {
    font-size: 20px;
    font-weight: 700;
    letter-spacing: -0.015em;
    color: #1d1d1f;
}
.toc-subtitle {
    font-size: 11px;
    font-weight: 600;
    color: #0071e3;
    margin-top: 2px;
}
.toc-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 20px;
    row-gap: 3px;
    flex: 1;
    align-content: space-between;
}
.toc-item-row {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 3px 6px;
    background: #ffffff;
    border: 1px solid #f0f0f2;
    border-radius: 6px;
}
.toc-idx {
    font-size: 10px;
    font-weight: 800;
    color: #0071e3;
    font-family: "SF Mono", Consolas, monospace;
    width: 20px;
}
.toc-body {
    flex: 1;
    overflow: hidden;
}
.toc-name-row {
    display: flex;
    align-items: center;
    gap: 6px;
}
.toc-name {
    font-size: 10px;
    font-weight: 700;
    color: #1d1d1f;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.toc-code {
    font-size: 8.5px;
    font-family: "SF Mono", Consolas, monospace;
    color: #86868b;
}
.toc-sub {
    font-size: 8.5px;
    color: #86868b;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.toc-pill {
    font-size: 8.5px;
    color: #515154;
    background: #f5f5f7;
    padding: 2px 6px;
    border-radius: 4px;
    white-space: nowrap;
}
.toc-dots {
    display: none;
}
.toc-page {
    font-size: 9.5px;
    font-weight: 700;
    color: #1d1d1f;
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
}

/* ========================================================= */
/* ODD PAGES: PURE EXHIBITION */
/* ========================================================= */
.page-exhibition {
    width: 297mm;
    height: 210mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 14mm 20mm 12mm 20mm;
    background: #fbfbfd;
}
.exhibit-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.exhibit-series {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #86868b;
}
.exhibit-cat-pill {
    font-size: 10px;
    font-weight: 600;
    color: #0071e3;
    background: #ffffff;
    border: 1px solid #e5e5ea;
    padding: 4px 12px;
    border-radius: 12px;
}
.exhibit-hero {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 8px 0;
}
.hero-stage {
    width: 100%;
    height: 144mm;
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
    position: relative;
    overflow: hidden;
}
.hero-stage img {
    max-width: 95%;
    max-height: 94%;
    object-fit: contain;
    border-radius: 8px;
}
.stage-watermark {
    position: absolute;
    bottom: 10px;
    right: 18px;
    font-size: 9px;
    font-family: "SF Mono", Consolas, monospace;
    font-weight: 600;
    color: #d2d2d7;
    letter-spacing: 1px;
}
.exhibit-bottom {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid #e5e5ea;
    padding-top: 8px;
}
.exhibit-name-block h2 {
    font-size: 17px;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: #1d1d1f;
}
.exhibit-name-block p {
    font-size: 11px;
    color: #86868b;
    margin-top: 2px;
}
.exhibit-folio {
    font-size: 14px;
    font-weight: 600;
    color: #86868b;
    font-variant-numeric: tabular-nums;
}

/* ========================================================= */
/* EVEN PAGES: ILLUSTRATED EDITORIAL & THEORY */
/* ========================================================= */
.page-editorial {
    padding: 13mm 18mm 11mm 18mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #fbfbfd;
}
.edit-header {
    margin-bottom: 6px;
}
.edit-badge-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 4px;
}
.badge-cat {
    font-size: 9.5px;
    font-weight: 600;
    color: #1d1d1f;
    background: #e5e5ea;
    padding: 2px 8px;
    border-radius: 6px;
}
.badge-code {
    font-size: 9.5px;
    font-weight: 700;
    color: #0071e3;
    font-family: "SF Mono", Consolas, monospace;
    background: rgba(0, 113, 227, 0.08);
    padding: 2px 8px;
    border-radius: 6px;
}
.badge-folio-tag {
    font-size: 9.5px;
    font-weight: 600;
    color: #86868b;
    margin-left: auto;
}
.edit-title {
    font-size: 18.5px;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: #1d1d1f;
    line-height: 1.25;
}
.edit-tagline {
    font-size: 11px;
    font-weight: 600;
    color: #0071e3;
    margin-top: 2px;
}
.edit-narrative {
    font-size: 10px;
    line-height: 1.5;
    color: #424245;
    margin-top: 4px;
    text-align: justify;
}

/* 理论卡片 */
.theory-card {
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 10px;
    padding: 10px 12px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.02);
    margin: 6px 0;
}
.theory-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 6px;
    border-bottom: 1px solid #f0f0f2;
    padding-bottom: 4px;
}
.theory-card-tag {
    font-size: 9px;
    font-weight: 700;
    color: #0071e3;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}
.theory-title {
    font-size: 11.5px;
    font-weight: 700;
    color: #1d1d1f;
}
.theory-body {
    display: grid;
    grid-template-columns: 1.15fr 0.95fr;
    gap: 12px;
    align-items: center;
}
.theory-desc {
    font-size: 9.8px;
    line-height: 1.5;
    color: #515154;
    text-align: justify;
}
.theory-formula-box {
    margin-top: 6px;
    background: #f5f5f7;
    border-left: 3px solid #0071e3;
    padding: 5px 8px;
    border-radius: 0 6px 6px 0;
    font-family: "SF Mono", Consolas, monospace;
    font-size: 9px;
    color: #1d1d1f;
}
.formula-tag {
    color: #86868b;
    margin-right: 4px;
}
.theory-diagram-box {
    height: 128px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* 底部指标与规格 */
.edit-bottom-grid {
    display: grid;
    grid-template-columns: 1fr 1.25fr;
    gap: 12px;
    align-items: stretch;
}
.stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
}
.stat-card {
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    padding: 6px 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.stat-val {
    font-size: 16px;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: #1d1d1f;
}
.stat-lbl {
    font-size: 9px;
    color: #86868b;
    margin-top: 1px;
}
.specs-table {
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    padding: 6px 10px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 12px;
    row-gap: 3px;
    align-content: center;
}
.spec-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #f5f5f7;
    padding: 2.5px 0;
    font-size: 9px;
}
.spec-lbl {
    color: #86868b;
}
.spec-val {
    font-weight: 600;
    color: #1d1d1f;
}
.edit-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #e5e5ea;
    padding-top: 6px;
    margin-top: 4px;
    font-size: 9px;
    color: #86868b;
}

/* ========================================================= */
/* PAGE 097: STANDARDS */
/* ========================================================= */
.page-standards {
    padding: 14mm 20mm 12mm 20mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.standards-header {
    margin-bottom: 8px;
}
.standards-main-title {
    font-size: 20px;
    font-weight: 700;
    letter-spacing: -0.015em;
    color: #1d1d1f;
}
.standards-subtitle {
    font-size: 11px;
    font-weight: 600;
    color: #0071e3;
    margin-top: 2px;
}
.standards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    flex: 1;
    align-content: space-between;
}
.std-card {
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 10px;
    padding: 10px 12px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.std-badge {
    font-size: 9px;
    font-weight: 800;
    color: #0071e3;
    letter-spacing: 1px;
}
.std-card h3 {
    font-size: 12px;
    font-weight: 700;
    color: #1d1d1f;
    margin: 4px 0 1px 0;
}
.std-sub {
    font-size: 8.5px;
    color: #86868b;
    margin-bottom: 6px;
}
.std-card p {
    font-size: 9px;
    line-height: 1.45;
    color: #515154;
    text-align: justify;
}
.std-metric {
    border-top: 1px solid #f0f0f2;
    padding-top: 6px;
    margin-top: 6px;
    display: flex;
    justify-content: space-between;
    font-size: 9px;
    color: #86868b;
}
.std-metric strong {
    color: #0071e3;
}

/* ========================================================= */
/* PAGE 098: BACK COVER */
/* ========================================================= */
.page-backcover {
    padding: 16mm 22mm 14mm 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: radial-gradient(circle at 50% 50%, #ffffff 0%, #fbfbfd 60%, #f5f5f7 100%);
}
.backcover-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 2;
}
.backcover-center {
    text-align: center;
    position: relative;
    z-index: 2;
    margin: auto 0;
}
.backcover-logo-mark {
    margin-bottom: 14px;
}
.backcover-title {
    font-size: 22px;
    font-weight: 700;
    letter-spacing: -0.015em;
    color: #1d1d1f;
}
.backcover-sub {
    font-size: 11px;
    font-weight: 600;
    color: #0071e3;
    letter-spacing: 1px;
    margin-top: 4px;
}
.backcover-colophon-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    max-width: 680px;
    margin: 24px auto 16px auto;
    text-align: left;
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 12px;
    padding: 14px 18px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.02);
}
.colophon-col h4 {
    font-size: 11px;
    font-weight: 700;
    color: #1d1d1f;
    margin-bottom: 8px;
    border-bottom: 1px solid #f0f0f2;
    padding-bottom: 4px;
}
.colophon-col p {
    font-size: 9.5px;
    line-height: 1.6;
    color: #515154;
}
.backcover-quote {
    font-size: 11px;
    font-style: italic;
    color: #86868b;
    margin-top: 14px;
}
.backcover-bottom {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid #e5e5ea;
    padding-top: 10px;
    position: relative;
    z-index: 2;
}
.backcover-copyright {
    font-size: 9px;
    color: #86868b;
    letter-spacing: 0.5px;
}
'''

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
        full_body += build_exhibit_pages_html(it)

    # P97: Manufacturing Standards
    full_body += build_standards_html()
    # P98: Back Cover
    full_body += build_backcover_html()

    html_doc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>未来飞行 · 航空航天飞行系统工程图鉴 (98P Master Blueprint)</title>
<style>
{css_content}
</style>
</head>
<body>
{full_body}
</body>
</html>'''

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_doc)
    print(f"Successfully generated HTML: {OUTPUT_HTML} ({len(html_doc)} bytes)")

async def render_pdf():
    print("Launching Playwright to render 98-page print-ready PDF...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Landscape A4 viewport 1400 x 990
        page = await browser.new_page(viewport={"width": 1400, "height": 990})
        html_uri = f"file:///{OUTPUT_HTML}"
        print(f"Loading {html_uri} ...")
        await page.goto(html_uri, wait_until="networkidle")
        await page.wait_for_timeout(2000)

        print(f"Rendering PDF to {OUTPUT_PDF} ...")
        await page.pdf(
            path=OUTPUT_PDF,
            print_background=True,
            prefer_css_page_size=True
        )
        await browser.close()
    print("PDF render completed successfully!")

def export_page_images():
    print(f"Opening PDF with PyMuPDF to export all 98 PNG pages to {OUTPUT_PAGES_DIR} ...")
    os.makedirs(OUTPUT_PAGES_DIR, exist_ok=True)
    doc = fitz.open(OUTPUT_PDF)
    total = len(doc)
    print(f"Total pages in PDF: {total}")
    assert total == 98, f"Expected 98 pages, got {total}"

    # Render at 150 DPI for crisp screen preview and interactive viewer
    zoom = 150.0 / 72.0
    mat = fitz.Matrix(zoom, zoom)

    for i in range(total):
        page = doc[i]
        pix = page.get_pixmap(matrix=mat, alpha=False)
        out_name = os.path.join(OUTPUT_PAGES_DIR, f"page_{i+1:03d}.png")
        pix.save(out_name)
        if (i + 1) % 10 == 0 or i == total - 1:
            print(f"Exported page {i+1:03d} / {total}")
    doc.close()
    print("All 98 page images successfully exported!")

def build_interactive_viewer_html():
    viewer_path = os.path.join(WORKSPACE_DIR, "Apple_Interactive_Viewer.html").replace("\\", "/")
    print(f"Generating Apple interactive flipbook viewer at {viewer_path} ...")

    viewer_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>未来飞行 · 航空航天飞行系统工程图鉴 (Apple 极简设计 98P 典藏画册交互阅览器)</title>
<style>
:root {
    --bg-color: #000000;
    --stage-bg: #111113;
    --card-bg: #1d1d1f;
    --text-primary: #f5f5f7;
    --text-secondary: #86868b;
    --apple-blue: #2997ff;
}
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
body {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "PingFang SC", sans-serif;
    background: var(--bg-color);
    color: var(--text-primary);
    overflow: hidden;
    height: 100vh;
    display: flex;
    flex-direction: column;
    -webkit-font-smoothing: antialiased;
}
/* Top Navigation Bar */
.top-nav {
    height: 52px;
    background: rgba(29, 29, 31, 0.8);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
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
    font-weight: 700;
    background: var(--apple-blue);
    color: #fff;
    padding: 2px 8px;
    border-radius: 4px;
}
.brand-name {
    font-size: 14px;
    font-weight: 600;
    letter-spacing: -0.01em;
}
.nav-controls {
    display: flex;
    align-items: center;
    gap: 16px;
}
.btn-control {
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: #fff;
    padding: 6px 14px;
    border-radius: 18px;
    font-size: 12px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    gap: 6px;
}
.btn-control:hover {
    background: rgba(255, 255, 255, 0.2);
}
.btn-control.active {
    background: var(--apple-blue);
    border-color: var(--apple-blue);
}
.page-indicator {
    font-size: 13px;
    font-variant-numeric: tabular-nums;
    color: var(--text-secondary);
}
.page-indicator strong {
    color: #fff;
}

/* Main Reading Stage */
.stage-container {
    flex: 1;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--stage-bg);
    overflow: hidden;
    padding: 20px;
}
.spread-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 4px;
    max-width: 96vw;
    max-height: 86vh;
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6);
    border-radius: 12px;
    overflow: hidden;
    background: #000;
}
.page-view {
    max-height: 86vh;
    max-width: calc(48vw - 10px);
    object-fit: contain;
    background: #fff;
    display: block;
    user-select: none;
}
.single-mode .page-view {
    max-width: 90vw;
}

/* Floating Navigation Arrows */
.nav-arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    cursor: pointer;
    transition: all 0.2s;
    z-index: 50;
    user-select: none;
}
.nav-arrow:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-50%) scale(1.08);
}
.nav-arrow.prev { left: 24px; }
.nav-arrow.next { right: 24px; }

/* Bottom Drawer Thumbnails */
.bottom-drawer {
    height: 84px;
    background: rgba(29, 29, 31, 0.9);
    backdrop-filter: blur(20px);
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    display: flex;
    align-items: center;
    padding: 0 20px;
    gap: 10px;
    overflow-x: auto;
    scrollbar-width: thin;
    scrollbar-color: rgba(255,255,255,0.2) transparent;
}
.thumb-item {
    height: 60px;
    aspect-ratio: 297 / 210;
    border-radius: 4px;
    overflow: hidden;
    cursor: pointer;
    border: 2px solid transparent;
    opacity: 0.6;
    transition: all 0.2s;
    flex-shrink: 0;
    position: relative;
}
.thumb-item:hover {
    opacity: 0.9;
    transform: translateY(-2px);
}
.thumb-item.active {
    border-color: var(--apple-blue);
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
    right: 4px;
    font-size: 8px;
    font-weight: 700;
    background: rgba(0, 0, 0, 0.7);
    color: #fff;
    padding: 1px 3px;
    border-radius: 2px;
}
</style>
</head>
<body>

<div class="top-nav">
    <div class="brand-title">
        <span class="brand-badge">98P MASTER</span>
        <span class="brand-name">未来飞行 · 航空航天飞行系统工程图鉴 (Apple 极简工业设计体系)</span>
    </div>

    <div class="nav-controls">
        <button class="btn-control active" id="btnSpread" onclick="setViewMode('spread')">
            <span>📖</span> 蝴蝶装对页展开视图 (Spread)
        </button>
        <button class="btn-control" id="btnSingle" onclick="setViewMode('single')">
            <span>📄</span> 单页精细检视 (Single)
        </button>
        <div class="page-indicator" id="pageIndicator">
            页面: <strong>001 / 098</strong>
        </div>
        <a class="btn-control" href="Aero_UAV_Master_Catalog_AppleStyle_98P.pdf" download style="text-decoration:none;">
            <span>⬇</span> 下载高清印刷 PDF (300DPI)
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

<div class="bottom-drawer" id="thumbDrawer">
    <!-- 缩略图由 JS 动态生成 -->
</div>

<script>
const TOTAL_PAGES = 98;
let currentPage = 1;
let viewMode = 'spread'; // 'spread' or 'single'

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
        indicator.innerHTML = `单页阅览: <strong>${String(currentPage).padStart(3, '0')} / 098</strong>`;
        const thumb = document.getElementById(`thumb-${currentPage}`);
        if (thumb) {
            thumb.classList.add('active');
            thumb.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
        }
    } else {
        // 对页展开模式 (Spread)
        // 封面 P1 单独展示，封底 P98 单独展示
        // 内页 P2-P3, P4-P5, ..., P96-P97 对页展示
        spreadWrapper.classList.remove('single-mode');
        if (currentPage === 1) {
            rightImg.style.display = 'none';
            leftImg.src = 'brochure_pages_v2/page_001.png';
            indicator.innerHTML = `封面: <strong>001 / 098</strong> (单页封面)`;
            const thumb = document.getElementById('thumb-1');
            if (thumb) { thumb.classList.add('active'); thumb.scrollIntoView({ behavior: 'smooth', inline: 'center' }); }
        } else if (currentPage >= TOTAL_PAGES) {
            rightImg.style.display = 'none';
            leftImg.src = `brochure_pages_v2/page_098.png`;
            indicator.innerHTML = `封底: <strong>098 / 098</strong> (单页封底)`;
            const thumb = document.getElementById('thumb-98');
            if (thumb) { thumb.classList.add('active'); thumb.scrollIntoView({ behavior: 'smooth', inline: 'center' }); }
        } else {
            // 对页：偶数页在左，奇数页在右
            let leftP = currentPage % 2 === 0 ? currentPage : currentPage - 1;
            let rightP = leftP + 1;
            leftImg.src = `brochure_pages_v2/page_${String(leftP).padStart(3, '0')}.png`;
            rightImg.src = `brochure_pages_v2/page_${String(rightP).padStart(3, '0')}.png`;
            rightImg.style.display = 'block';
            indicator.innerHTML = `蝴蝶装展开对页: <strong>${String(leftP).padStart(3, '0')} — ${String(rightP).padStart(3, '0')}</strong> / 098`;
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

// 键盘快捷键支持
window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {
        nextPage();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        prevPage();
    }
});

// 初始化
initThumbs();
updateView();
</script>

</body>
</html>'''

    with open(viewer_path, "w", encoding="utf-8") as f:
        f.write(viewer_html)
    print(f"Successfully created viewer: {viewer_path}")

async def main():
    print("=== STARTING AERO UAV MASTER CATALOG GENERATION (98 PAGES APPLE V2) ===")
    generate_full_html()
    await render_pdf()
    export_page_images()
    build_interactive_viewer_html()
    print("=== ALL 98-PAGE PRODUCTION PIPELINE TASKS COMPLETED SUCCESSFULLY! ===")

if __name__ == "__main__":
    asyncio.run(main())
