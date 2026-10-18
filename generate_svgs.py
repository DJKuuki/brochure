# -*- coding: utf-8 -*-
"""
Aero UAV 46-Blueprint Master Vector Library
High-precision aerospace blueprints tailored for pure white monograph pages.
Color Palette:
- Structural outlines: #1d1d1f (Apple obsidian graphite)
- Primary flow vectors & axes: #0071e3 (Apple precision blue)
- Secondary stability & laminar flow: #34c759 (aero emerald)
- Loads, moments & caution envelopes: #ff9500 (amber) / #ff3b30 (coral)
- Technical grid & witness lines: #e5e5ea / #86868b
- Mathematical/datum annotations: 7.5px - 9px SF Mono / system sans-serif
"""

def get_svg_diagram(svg_type):
    w, h = 460, 200

    def wrap(inner_content, tag_code=""):
        return f"""<svg viewBox="0 0 {w} {h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="background:transparent; border:none;">
        <defs>
            <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#0071e3" stop-opacity="0.18"/>
                <stop offset="100%" stop-color="#0071e3" stop-opacity="0.02"/>
            </linearGradient>
            <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#ff9500" stop-opacity="0.22"/>
                <stop offset="100%" stop-color="#ff9500" stop-opacity="0.03"/>
            </linearGradient>
            <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#34c759" stop-opacity="0.22"/>
                <stop offset="100%" stop-color="#34c759" stop-opacity="0.03"/>
            </linearGradient>
            <linearGradient id="meshGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#ff3b30" stop-opacity="0.25"/>
                <stop offset="50%" stop-color="#ff9500" stop-opacity="0.15"/>
                <stop offset="100%" stop-color="#0071e3" stop-opacity="0.1"/>
            </linearGradient>
            <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0071e3"/>
            </marker>
            <marker id="arrowDark" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1d1d1f"/>
            </marker>
            <marker id="arrowGreen" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#34c759"/>
            </marker>
            <marker id="arrowAmber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#ff9500"/>
            </marker>
            <pattern id="subgrid" width="10" height="10" patternUnits="userSpaceOnUse">
                <path d="M 10 0 L 0 0 0 10" fill="none" stroke="#f2f2f5" stroke-width="0.4"/>
            </pattern>
            <pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse">
                <rect width="50" height="50" fill="url(#subgrid)"/>
                <path d="M 50 0 L 0 0 0 50" fill="none" stroke="#e6e6eb" stroke-width="0.8"/>
            </pattern>
            <pattern id="hatch" width="6" height="6" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
                <line x1="0" y1="0" x2="0" y2="6" stroke="#86868b" stroke-width="0.8"/>
            </pattern>
        </defs>
        
        <!-- Precision Grid Background -->
        <rect width="{w}" height="{h}" fill="url(#grid)" opacity="0.65"/>
        
        <!-- Architectural Perimeter Ticks -->
        <g stroke="#86868b" stroke-width="0.8" opacity="0.6">
            <path d="M 10 16 L 10 10 L 16 10"/>
            <path d="M 450 16 L 450 10 L 444 10"/>
            <path d="M 10 184 L 10 190 L 16 190"/>
            <path d="M 450 184 L 450 190 L 444 190"/>
        </g>
        
        <!-- Technical Meta Footer in Diagram (Clean Bottom Margin) -->
        <text x="14" y="193" font-family="'SF Mono', Consolas, monospace" font-size="6.2" font-weight="600" fill="#a1a1a6" letter-spacing="0.5">ISO 128-20 // ENGINEERING CAD SCHEMATIC</text>
        <text x="446" y="193" font-family="'SF Mono', Consolas, monospace" font-size="6.2" font-weight="600" fill="#0071e3" text-anchor="end" letter-spacing="0.5">CFD/FEA VALIDATED</text>
        
        {inner_content}
        </svg>"""

    # 1. aerofoil_streamline
    if svg_type == "aerofoil_streamline":
        content = """
        <!-- NACA 64A012 Airfoil Profile -->
        <path d="M 70 115 C 70 78, 170 72, 330 115 C 190 148, 100 142, 70 115 Z" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="2"/>
        <!-- Chord line & Camber line -->
        <line x1="70" y1="115" x2="330" y2="115" stroke="#86868b" stroke-width="0.8" stroke-dasharray="4 2"/>
        <path d="M 70 115 Q 180 104, 330 115" fill="none" stroke="#0071e3" stroke-width="1.2" stroke-dasharray="2 2"/>
        <!-- Thickness dimension line -->
        <line x1="160" y1="80" x2="160" y2="135" stroke="#ff9500" stroke-width="1"/>
        <circle cx="160" cy="80" r="1.5" fill="#ff9500"/>
        <circle cx="160" cy="135" r="1.5" fill="#ff9500"/>
        <text x="165" y="110" font-family="'SF Mono', monospace" font-size="7.5" fill="#ff9500" font-weight="700">t_max = 12% c</text>
        <!-- Stagnation Point & Streamlines -->
        <circle cx="70" cy="115" r="3.5" fill="#0071e3"/>
        <text x="25" y="118" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#0071e3">驻点 Ψ=0</text>
        <path d="M 20 60 C 100 52, 170 54, 430 75" fill="none" stroke="#0071e3" stroke-width="1.5" stroke-dasharray="5 2"/>
        <path d="M 20 85 C 90 75, 170 74, 430 98" fill="none" stroke="#0071e3" stroke-width="1.8"/>
        <path d="M 20 145 C 90 152, 180 150, 430 132" fill="none" stroke="#0071e3" stroke-width="1.8"/>
        <path d="M 20 170 C 100 176, 180 172, 430 155" fill="none" stroke="#0071e3" stroke-width="1.5" stroke-dasharray="5 2"/>
        <!-- Upper Surface Cp Suction Envelope -->
        <path d="M 70 115 C 90 40, 180 50, 330 115" fill="none" stroke="#ff3b30" stroke-width="1.2" stroke-dasharray="3 2"/>
        <text x="125" y="44" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#ff3b30">-Cp_min = 1.42 (负压吸力峰)</text>
        <!-- Laminar to Turbulent Transition Zone -->
        <line x1="210" y1="84" x2="210" y2="70" stroke="#86868b" stroke-width="0.8"/>
        <text x="215" y="74" font-family="'SF Mono', monospace" font-size="7.5" fill="#86868b">转捩点 x_tr/c=0.48</text>
        <!-- Dimension Chord c -->
        <line x1="70" y1="155" x2="330" y2="155" stroke="#1d1d1f" stroke-width="0.8"/>
        <line x1="70" y1="150" x2="70" y2="160" stroke="#1d1d1f" stroke-width="0.8"/>
        <line x1="330" y1="150" x2="330" y2="160" stroke="#1d1d1f" stroke-width="0.8"/>
        <text x="180" y="167" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#1d1d1f" text-anchor="middle">弦长 c = 280 mm</text>
        <!-- Wake Arrow -->
        <line x1="330" y1="115" x2="420" y2="115" stroke="#34c759" stroke-width="1.5" marker-end="url(#arrowGreen)"/>
        <text x="345" y="108" font-family="-apple-system, sans-serif" font-size="8" font-weight="700" fill="#34c759">层流尾流 (Cd=0.012)</text>
        """
        return wrap(content)

    # 2. stress_cantilever
    elif svg_type == "stress_cantilever":
        content = """
        <!-- Root Wall Clamp with Hatching -->
        <rect x="35" y="35" width="22" height="130" fill="url(#hatch)" stroke="#1d1d1f" stroke-width="1.5"/>
        <line x1="57" y1="30" x2="57" y2="170" stroke="#1d1d1f" stroke-width="2.5"/>
        <!-- Deflected Beam under Lift -->
        <line x1="57" y1="95" x2="390" y2="95" stroke="#86868b" stroke-width="0.8" stroke-dasharray="4 3"/>
        <path d="M 57 90 C 160 90, 280 75, 385 60 L 385 74 C 280 89, 160 104, 57 104 Z" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.8"/>
        <!-- Neutral Axis & Stress Profile at Root -->
        <path d="M 65 60 L 85 75 L 85 97 L 65 112 Z" fill="url(#amberGrad)" stroke="#ff9500" stroke-width="1"/>
        <text x="92" y="70" font-family="'SF Mono', monospace" font-size="7.5" fill="#ff3b30" font-weight="700">+σ_拉伸 (380 MPa)</text>
        <text x="92" y="112" font-family="'SF Mono', monospace" font-size="7.5" fill="#0071e3" font-weight="700">-σ_压缩</text>
        <!-- Lift Load Vector -->
        <line x1="385" y1="24" x2="385" y2="56" stroke="#0071e3" stroke-width="2" marker-end="url(#arrow)"/>
        <text x="325" y="26" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3">F_lift = 85.4 N</text>
        <!-- Bending Moment Curve M(x) underneath -->
        <path d="M 57 160 Q 220 160, 385 130" fill="none" stroke="#ff9500" stroke-width="1.5" stroke-dasharray="3 2"/>
        <text x="70" y="155" font-family="'SF Mono', monospace" font-size="8" fill="#ff9500" font-weight="700">M(x) 弯矩包络</text>
        <!-- Max Deflection Callout -->
        <line x1="400" y1="67" x2="400" y2="95" stroke="#1d1d1f" stroke-width="0.8"/>
        <line x1="395" y1="67" x2="405" y2="67" stroke="#1d1d1f" stroke-width="0.8"/>
        <line x1="395" y1="95" x2="405" y2="95" stroke="#1d1d1f" stroke-width="0.8"/>
        <text x="410" y="84" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#1d1d1f">δ &lt; 0.78mm</text>
        <!-- Carbon Layup Callout -->
        <text x="140" y="180" font-family="'SF Mono', monospace" font-size="7.8" fill="#424245" font-weight="600">铺层顺序: 东丽 T800 [0°₄ / ±45°₂ / 90°]s 对称均衡共固化</text>
        """
        return wrap(content)

    # 3. vtol_transition
    elif svg_type == "vtol_transition":
        content = """
        <!-- Calibrated Axes -->
        <line x1="60" y1="165" x2="425" y2="165" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <line x1="60" y1="165" x2="60" y2="35" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <text x="405" y="180" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">空速 V (km/h)</text>
        <text x="25" y="38" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">升力比例 %</text>
        <!-- Rotor Thrust Curve (Cosine decay) -->
        <path d="M 60 55 C 160 55, 230 135, 310 165" fill="none" stroke="#ff9500" stroke-width="2.2"/>
        <text x="75" y="70" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#ff9500">T_rotor (旋翼垂向推力)</text>
        <!-- Wing Aerodynamic Lift (V^2 curve) -->
        <path d="M 90 165 C 190 160, 260 85, 395 55" fill="none" stroke="#0071e3" stroke-width="2.2"/>
        <text x="300" y="50" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3">L_wing = 0.5ρV²S·CL</text>
        <!-- Constant Total Equilibrium -->
        <line x1="60" y1="55" x2="410" y2="55" stroke="#34c759" stroke-width="1.5" stroke-dasharray="3 2"/>
        <text x="180" y="44" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759">恒定总升力 L_total = W_aircraft (100%)</text>
        <!-- Transition Corridor Window -->
        <rect x="180" y="48" width="115" height="117" fill="url(#blueGrad)" stroke="#0071e3" stroke-width="0.8" stroke-dasharray="3 3"/>
        <text x="200" y="110" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#0071e3">模态转换走廊</text>
        <text x="195" y="125" font-family="'SF Mono', monospace" font-size="7.5" fill="#424245">45 km/h ~ 75 km/h</text>
        <!-- Tilt Angle Progression -->
        <text x="65" y="150" font-family="'SF Mono', monospace" font-size="7.5" fill="#86868b">θ=90° (悬停)</text>
        <text x="345" y="150" font-family="'SF Mono', monospace" font-size="7.5" fill="#86868b">θ=0° (巡航)</text>
        """
        return wrap(content)

    # 4. ducted_flow
    elif svg_type == "ducted_flow":
        content = """
        <!-- Ducted Cowl Contours (Upper & Lower) -->
        <path d="M 70 42 C 140 50, 190 68, 250 68 C 310 68, 360 55, 410 48 L 410 32 C 345 38, 290 50, 250 50 C 180 50, 130 32, 70 24 Z" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.8"/>
        <path d="M 70 158 C 140 150, 190 132, 250 132 C 310 132, 360 145, 410 152 L 410 168 C 345 162, 290 150, 250 150 C 180 150, 130 168, 70 176 Z" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.8"/>
        <!-- Rotor Blade Plane -->
        <line x1="250" y1="70" x2="250" y2="130" stroke="#ff9500" stroke-width="3"/>
        <circle cx="250" cy="100" r="9" fill="#1d1d1f"/>
        <circle cx="250" cy="100" r="4" fill="#ffffff"/>
        <!-- Accelerated Streamlines -->
        <path d="M 30 75 C 130 75, 190 85, 250 85 C 310 85, 350 80, 430 80" fill="none" stroke="#0071e3" stroke-width="1.5"/>
        <path d="M 30 125 C 130 125, 190 115, 250 115 C 310 115, 350 120, 430 120" fill="none" stroke="#0071e3" stroke-width="1.5"/>
        <line x1="30" y1="100" x2="430" y2="100" stroke="#0071e3" stroke-width="1" stroke-dasharray="4 2"/>
        <!-- Lip Suction Pressure Vector -->
        <path d="M 120 40 L 95 26" stroke="#ff3b30" stroke-width="1.5" marker-end="url(#arrowDark)"/>
        <text x="65" y="24" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff3b30">唇口增升 ΔT=+18%</text>
        <!-- Tip Clearance Callout -->
        <line x1="250" y1="68" x2="275" y2="68" stroke="#1d1d1f" stroke-width="0.8"/>
        <text x="280" y="72" font-family="'SF Mono', monospace" font-size="7.2" fill="#1d1d1f" font-weight="700">间隙 δ=0.35mm</text>
        <!-- Velocity Inset -->
        <text x="140" y="105" font-family="'SF Mono', monospace" font-size="8" fill="#424245">V_throat &gt; V_in</text>
        <text x="140" y="185" font-family="-apple-system, sans-serif" font-size="7.8" fill="#424245">伯努利文丘里喉道加速 · 消除桨尖涡耗散</text>
        """
        return wrap(content)

    # 5. true_x_inertia
    elif svg_type == "true_x_inertia":
        content = """
        <!-- Coordinate Axes -->
        <line x1="230" y1="20" x2="230" y2="180" stroke="#86868b" stroke-width="0.8" stroke-dasharray="4 3"/>
        <line x1="70" y1="100" x2="390" y2="100" stroke="#86868b" stroke-width="0.8" stroke-dasharray="4 3"/>
        <text x="235" y="30" font-family="'SF Mono', monospace" font-size="8" fill="#86868b">Yb (俯仰轴)</text>
        <text x="375" y="95" font-family="'SF Mono', monospace" font-size="8" fill="#86868b">Xb (横滚轴)</text>
        <!-- True-X Symmetric 45 Deg Arms -->
        <line x1="145" y1="35" x2="315" y2="165" stroke="#1d1d1f" stroke-width="3"/>
        <line x1="145" y1="165" x2="315" y2="35" stroke="#1d1d1f" stroke-width="3"/>
        <!-- 4 Motors -->
        <circle cx="145" cy="35" r="16" fill="url(#blueGrad)" stroke="#0071e3" stroke-width="1.8"/>
        <circle cx="315" cy="35" r="16" fill="url(#blueGrad)" stroke="#0071e3" stroke-width="1.8"/>
        <circle cx="145" cy="165" r="16" fill="url(#blueGrad)" stroke="#0071e3" stroke-width="1.8"/>
        <circle cx="315" cy="165" r="16" fill="url(#blueGrad)" stroke="#0071e3" stroke-width="1.8"/>
        <!-- Rotor Rotation Direction Indicators -->
        <text x="145" y="38" font-family="'SF Mono', monospace" font-size="7" font-weight="700" fill="#0071e3" text-anchor="middle">CW</text>
        <text x="315" y="38" font-family="'SF Mono', monospace" font-size="7" font-weight="700" fill="#0071e3" text-anchor="middle">CCW</text>
        <text x="145" y="168" font-family="'SF Mono', monospace" font-size="7" font-weight="700" fill="#0071e3" text-anchor="middle">CCW</text>
        <text x="315" y="168" font-family="'SF Mono', monospace" font-size="7" font-weight="700" fill="#0071e3" text-anchor="middle">CW</text>
        <!-- Center Concentrated Mass -->
        <circle cx="230" cy="100" r="22" fill="#ffffff" stroke="#1d1d1f" stroke-width="2"/>
        <circle cx="230" cy="100" r="6" fill="#34c759"/>
        <!-- Symmetrical Inertia Circle -->
        <circle cx="230" cy="100" r="55" fill="none" stroke="#34c759" stroke-width="1.2" stroke-dasharray="3 2"/>
        <text x="230" y="145" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759" text-anchor="middle">I_xx = I_yy = 0.0042 kg·m²</text>
        <text x="230" y="178" font-family="-apple-system, sans-serif" font-size="7.8" fill="#424245" text-anchor="middle">45° 完全对角均等惯量 · 横滚与俯仰控制增益完全一致</text>
        """
        return wrap(content)

    # 6. wide_x_vortex
    elif svg_type == "wide_x_vortex":
        content = """
        <!-- Wide-X Geometry Frame (Wider Front, Narrower Rear) -->
        <line x1="230" y1="30" x2="230" y2="170" stroke="#86868b" stroke-width="0.8" stroke-dasharray="3 3"/>
        <!-- Front Wide Arm (Horizontal spread) -->
        <line x1="110" y1="75" x2="230" y2="105" stroke="#1d1d1f" stroke-width="3"/>
        <line x1="350" y1="75" x2="230" y2="105" stroke="#1d1d1f" stroke-width="3"/>
        <!-- Rear Narrow Arm -->
        <line x1="140" y1="145" x2="230" y2="105" stroke="#1d1d1f" stroke-width="3"/>
        <line x1="320" y1="145" x2="230" y2="105" stroke="#1d1d1f" stroke-width="3"/>
        <!-- Camera Lens & 160° Field of View Cone -->
        <circle cx="230" cy="100" r="8" fill="#1d1d1f"/>
        <polygon points="230,95 125,25 335,25" fill="url(#greenGrad)" stroke="#34c759" stroke-width="1.2" stroke-dasharray="4 2"/>
        <text x="230" y="42" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759" text-anchor="middle">160° 超广角透镜无遮挡视野</text>
        <!-- Motor Envelopes -->
        <circle cx="110" cy="75" r="22" fill="url(#blueGrad)" stroke="#0071e3" stroke-width="1.2" stroke-dasharray="2 2"/>
        <circle cx="350" cy="75" r="22" fill="url(#blueGrad)" stroke="#0071e3" stroke-width="1.2" stroke-dasharray="2 2"/>
        <text x="70" y="80" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#0071e3">前桨包络外移</text>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">大宽角布局：彻底消除螺旋桨进入 4K 高动态运镜视野瑕疵</text>
        """
        return wrap(content)

    # 7. circuit_filter
    elif svg_type == "circuit_filter":
        content = """
        <!-- Schematic Rails -->
        <line x1="40" y1="70" x2="260" y2="70" stroke="#1d1d1f" stroke-width="2"/>
        <line x1="40" y1="140" x2="260" y2="140" stroke="#1d1d1f" stroke-width="2"/>
        <!-- Inductor L1 Coil -->
        <path d="M 100 70 A 10 10 0 0 1 120 70 A 10 10 0 0 1 140 70 A 10 10 0 0 1 160 70 A 10 10 0 0 1 180 70" fill="none" stroke="#0071e3" stroke-width="2.5"/>
        <text x="140" y="55" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3" text-anchor="middle">L1 = 4.7μH (40A)</text>
        <!-- Shunt Capacitors C1 & C2 -->
        <g stroke="#1d1d1f" stroke-width="1.5">
            <line x1="85" y1="70" x2="85" y2="98"/>
            <line x1="75" y1="98" x2="95" y2="98"/>
            <line x1="75" y1="104" x2="95" y2="104"/>
            <line x1="85" y1="104" x2="85" y2="140"/>
            <line x1="205" y1="70" x2="205" y2="98"/>
            <line x1="195" y1="98" x2="215" y2="98"/>
            <line x1="195" y1="104" x2="215" y2="104"/>
            <line x1="205" y1="104" x2="205" y2="140"/>
        </g>
        <text x="85" y="125" font-family="'SF Mono', monospace" font-size="7" fill="#86868b" text-anchor="middle">C1 470μF</text>
        <text x="205" y="125" font-family="'SF Mono', monospace" font-size="7" fill="#86868b" text-anchor="middle">C2 470μF</text>
        <!-- TVS Diode -->
        <line x1="240" y1="70" x2="240" y2="140" stroke="#ff9500" stroke-width="1.5"/>
        <text x="245" y="110" font-family="'SF Mono', monospace" font-size="7.5" fill="#ff9500" font-weight="700">TVS 58V</text>
        <!-- Right Inset: Bode Plot -->
        <rect x="290" y="45" width="150" height="95" fill="#fbfbfd" stroke="#d2d2d7" stroke-width="0.8"/>
        <line x1="300" y1="125" x2="430" y2="125" stroke="#86868b" stroke-width="0.8"/>
        <line x1="300" y1="125" x2="300" y2="55" stroke="#86868b" stroke-width="0.8"/>
        <text x="365" y="40" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">Bode 衰减频响</text>
        <!-- -40dB/dec Curve -->
        <path d="M 300 65 L 340 65 Q 360 67, 380 95 L 425 125" fill="none" stroke="#0071e3" stroke-width="2"/>
        <text x="375" y="80" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#0071e3">-40 dB/dec</text>
        <line x1="355" y1="55" x2="355" y2="125" stroke="#ff3b30" stroke-width="0.8" stroke-dasharray="2 2"/>
        <text x="355" y="135" font-family="'SF Mono', monospace" font-size="6.5" fill="#ff3b30" text-anchor="middle">fc=3.4kHz</text>
        <!-- Bottom Spec -->
        <text x="140" y="175" font-family="'SF Mono', monospace" font-size="8" fill="#34c759" font-weight="700">直流母线高频纹波: V_ripple &lt; 12 mVpp (衰减 38 dB)</text>
        """
        return wrap(content)

    # 8. high_aspect_ratio
    elif svg_type == "high_aspect_ratio":
        content = """
        <!-- High Aspect Ratio Wing Planform (Span b=4500mm, AR=26.2) -->
        <path d="M 40 102 L 230 95 L 420 102 L 420 110 L 230 115 L 40 110 Z" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.8"/>
        <!-- Rib Stations along Span -->
        <line x1="90" y1="100" x2="90" y2="111" stroke="#86868b" stroke-width="0.8"/>
        <line x1="150" y1="98" x2="150" y2="112" stroke="#86868b" stroke-width="0.8"/>
        <line x1="210" y1="96" x2="210" y2="114" stroke="#86868b" stroke-width="0.8"/>
        <line x1="250" y1="96" x2="250" y2="114" stroke="#86868b" stroke-width="0.8"/>
        <line x1="310" y1="98" x2="310" y2="112" stroke="#86868b" stroke-width="0.8"/>
        <line x1="370" y1="100" x2="370" y2="111" stroke="#86868b" stroke-width="0.8"/>
        <!-- Prandtl Elliptical Circulation Lift Distribution -->
        <path d="M 40 100 Q 230 25, 420 100" fill="url(#greenGrad)" stroke="#34c759" stroke-width="2"/>
        <text x="230" y="45" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#34c759" text-anchor="middle">普朗特最佳椭圆环量分布 Γ(y)</text>
        <!-- Tip Vortices at Both Tips -->
        <path d="M 40 98 C 22 88, 22 118, 38 108" fill="none" stroke="#ff9500" stroke-width="2"/>
        <path d="M 420 98 C 438 88, 438 118, 422 108" fill="none" stroke="#ff9500" stroke-width="2"/>
        <!-- Wingspan Dimension Line -->
        <line x1="40" y1="135" x2="420" y2="135" stroke="#1d1d1f" stroke-width="0.8"/>
        <line x1="40" y1="130" x2="40" y2="140" stroke="#1d1d1f" stroke-width="0.8"/>
        <line x1="420" y1="130" x2="420" y2="140" stroke="#1d1d1f" stroke-width="0.8"/>
        <text x="230" y="148" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#1d1d1f" text-anchor="middle">总展长 b = 4500 mm // 展弦比 AR = 26.2</text>
        <text x="230" y="175" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">诱导阻力 C_Di = C_L²/(π·e·AR) 降低 82% · 全机滑翔升阻比 L/D = 28.5</text>
        """
        return wrap(content)

    # 9. pid_control
    elif svg_type == "pid_control":
        content = """
        <!-- Oscilloscope Grid & Axes -->
        <line x1="60" y1="165" x2="425" y2="165" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <line x1="60" y1="165" x2="60" y2="35" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <text x="400" y="180" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">时间 t (s)</text>
        <text x="25" y="38" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">角度 θ (°)</text>
        <!-- Step Setpoint Target Line -->
        <line x1="60" y1="75" x2="415" y2="75" stroke="#ff9500" stroke-width="1.5" stroke-dasharray="4 3"/>
        <text x="330" y="68" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#ff9500">期望设定值 r(t) = 1.0</text>
        <!-- Closed Loop Step Response (Fast Rise, D-damped 2.3% overshoot) -->
        <path d="M 60 165 C 105 160, 125 58, 155 58 C 185 58, 205 80, 245 74 C 285 71, 335 75, 415 75" fill="none" stroke="#0071e3" stroke-width="2.5"/>
        <!-- Overshoot Marker -->
        <line x1="155" y1="75" x2="155" y2="58" stroke="#ff3b30" stroke-width="1"/>
        <text x="160" y="52" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff3b30">超调 Mp=2.3%</text>
        <!-- Rise time tr and settling time ts -->
        <line x1="135" y1="75" x2="135" y2="165" stroke="#86868b" stroke-width="0.8" stroke-dasharray="2 2"/>
        <text x="135" y="176" font-family="'SF Mono', monospace" font-size="7" fill="#86868b" text-anchor="middle">tr=28ms</text>
        <line x1="260" y1="75" x2="260" y2="165" stroke="#34c759" stroke-width="0.8" stroke-dasharray="2 2"/>
        <text x="260" y="176" font-family="'SF Mono', monospace" font-size="7" fill="#34c759" text-anchor="middle">ts=85ms</text>
        <text x="200" y="125" font-family="'SF Mono', monospace" font-size="8" fill="#424245">前馈控制 Kf·dr/dt 提前注入 · 消除滞后 2ms</text>
        """
        return wrap(content)

    # 10. topology_stress
    elif svg_type == "topology_stress":
        content = """
        <!-- SIMP Continuum Topology Optimized Frame Core -->
        <rect x="50" y="40" width="360" height="120" rx="4" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.5"/>
        <!-- Optimized Organic Cavities (SIMP density penalization) -->
        <path d="M 120 75 Q 150 65, 175 80 Q 185 105, 165 120 Q 130 130, 115 105 Z" fill="#ffffff" stroke="#1d1d1f" stroke-width="1.8"/>
        <path d="M 230 65 Q 265 60, 280 85 Q 275 110, 250 125 Q 220 120, 215 90 Z" fill="#ffffff" stroke="#1d1d1f" stroke-width="1.8"/>
        <circle cx="340" cy="100" r="24" fill="#ffffff" stroke="#1d1d1f" stroke-width="1.8"/>
        <!-- Principal Stress Flow Vectors (FEA Load Paths) -->
        <path d="M 55 58 C 140 46, 260 48, 405 60" fill="none" stroke="#0071e3" stroke-width="2"/>
        <path d="M 55 142 C 140 154, 260 152, 405 140" fill="none" stroke="#0071e3" stroke-width="2"/>
        <path d="M 185 98 L 225 98" stroke="#ff9500" stroke-width="2.5"/>
        <!-- High Stress Concentration Hotspot at Hinge Pivot -->
        <circle cx="340" cy="100" r="10" fill="none" stroke="#ff3b30" stroke-width="2" stroke-dasharray="3 2"/>
        <text x="340" y="70" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff3b30" text-anchor="middle">σ_max=240MPa</text>
        <text x="210" y="32" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">SIMP 变密度拓扑应力流优化 (7075-T6 铝合金)</text>
        <text x="210" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#34c759" font-weight="700" text-anchor="middle">剔除 42% 低载荷无效死重 · 弯扭抗疲劳极限突破 100,000 次循环</text>
        """
        return wrap(content)

    # 11. stretched_slipstream
    elif svg_type == "stretched_slipstream":
        content = """
        <!-- Stretched-X Coordinate Geometry (Ly > Lx) -->
        <line x1="230" y1="20" x2="230" y2="180" stroke="#86868b" stroke-width="0.8" stroke-dasharray="4 3"/>
        <line x1="70" y1="100" x2="390" y2="100" stroke="#86868b" stroke-width="0.8" stroke-dasharray="4 3"/>
        <!-- Stretched Arms (Narrow width 130mm, Long length 190mm) -->
        <line x1="160" y1="25" x2="300" y2="175" stroke="#1d1d1f" stroke-width="3"/>
        <line x1="300" y1="25" x2="160" y2="175" stroke="#1d1d1f" stroke-width="3"/>
        <!-- 4 Motors -->
        <circle cx="160" cy="25" r="14" fill="url(#blueGrad)" stroke="#0071e3" stroke-width="1.8"/>
        <circle cx="300" cy="25" r="14" fill="url(#blueGrad)" stroke="#0071e3" stroke-width="1.8"/>
        <circle cx="160" cy="175" r="14" fill="url(#greenGrad)" stroke="#34c759" stroke-width="1.8"/>
        <circle cx="300" cy="175" r="14" fill="url(#greenGrad)" stroke="#34c759" stroke-width="1.8"/>
        <!-- Longitudinal High Speed Inflow Corridor (Separated from Wake) -->
        <path d="M 160 39 Q 145 90, 120 175" fill="none" stroke="#ff9500" stroke-width="1.5" stroke-dasharray="4 2"/>
        <path d="M 300 39 Q 315 90, 340 175" fill="none" stroke="#ff9500" stroke-width="1.5" stroke-dasharray="4 2"/>
        <text x="230" y="85" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759" text-anchor="middle">后桨纯净进气流道</text>
        <text x="230" y="100" font-family="'SF Mono', monospace" font-size="7.5" fill="#424245" text-anchor="middle">Ly/Lx = 1.46 (大纵横比)</text>
        <text x="230" y="185" font-family="-apple-system, sans-serif" font-size="8" fill="#1d1d1f" text-anchor="middle">拉伸X构型：高速前飞时后桨彻底摆脱前桨紊流尾迹干扰</text>
        """
        return wrap(content)

    # 12. prop_acoustics
    elif svg_type == "prop_acoustics":
        content = """
        <!-- Acoustic Frequency Spectrum Chart (0 ~ 8000 Hz) -->
        <line x1="60" y1="165" x2="425" y2="165" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <line x1="60" y1="165" x2="60" y2="35" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <text x="400" y="180" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">频率 f (Hz)</text>
        <text x="20" y="38" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">声压级 SPL (dBA)</text>
        <!-- Standard Tonal Spike (BPF blade pass frequency) -->
        <path d="M 60 145 L 140 145 L 150 48 L 160 145 L 290 145 L 295 85 L 300 145 L 420 145" fill="none" stroke="#ff3b30" stroke-width="1.8"/>
        <text x="150" y="40" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff3b30" text-anchor="middle">常规一阶基频峰 (82 dBA)</text>
        <!-- Serrated Trailing Edge Low-Noise Diffused Curve -->
        <path d="M 60 135 Q 150 120, 240 130 T 420 140" fill="url(#greenGrad)" stroke="#34c759" stroke-width="2.5"/>
        <text x="260" y="115" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759">锯齿后缘宽频声能弥散 (-6.5 dBA)</text>
        <!-- Delta SPL annotation -->
        <line x1="150" y1="52" x2="150" y2="122" stroke="#1d1d1f" stroke-width="1" stroke-dasharray="2 2"/>
        <text x="158" y="90" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#1d1d1f">Δ = -6.5 dBA</text>
        <text x="230" y="185" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">非定常后缘脱落涡干涉消除 · 人耳敏感频段 (1kHz~4kHz) 极致静音</text>
        """
        return wrap(content)

    # 13. torque_box
    elif svg_type == "torque_box":
        content = """
        <!-- Bredt-Batho Closed Thin-Walled Box Beam Section -->
        <rect x="90" y="55" width="280" height="90" rx="6" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="2.2"/>
        <!-- Circulating Shear Flow Loop q = tau * t -->
        <g stroke="#0071e3" stroke-width="2">
            <line x1="110" y1="70" x2="350" y2="70" marker-end="url(#arrow)"/>
            <line x1="350" y1="70" x2="350" y2="130" marker-end="url(#arrow)"/>
            <line x1="350" y1="130" x2="110" y2="130" marker-end="url(#arrow)"/>
            <line x1="110" y1="130" x2="110" y2="70" marker-end="url(#arrow)"/>
        </g>
        <text x="230" y="105" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#0071e3" text-anchor="middle">连续剪应力流 q = τ·t = 恒定</text>
        <!-- Torsional Enclosed Area Am Dimension -->
        <text x="230" y="42" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#1d1d1f" text-anchor="middle">布雷特-巴斯 (Bredt-Batho) 闭口抗扭模量 T = 2·Am·q</text>
        <!-- Thickness callout -->
        <line x1="90" y1="152" x2="370" y2="152" stroke="#1d1d1f" stroke-width="0.8"/>
        <line x1="90" y1="147" x2="90" y2="157" stroke="#1d1d1f" stroke-width="0.8"/>
        <line x1="370" y1="147" x2="370" y2="157" stroke="#1d1d1f" stroke-width="0.8"/>
        <text x="230" y="165" font-family="'SF Mono', monospace" font-size="7.5" fill="#424245" text-anchor="middle">壁厚 t = 2.5 mm 碳纤维闭口盒段 // 抗扭刚度 GJ 提升 45 倍</text>
        """
        return wrap(content)

    # 14. stealth_rcs
    elif svg_type == "stealth_rcs":
        content = """
        <!-- Stealth Faceted Airframe Planform (Edge Alignment) -->
        <polygon points="120,135 230,55 340,135 230,112" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="2.2"/>
        <!-- Incident Radar Wavefront (Red) -->
        <g stroke="#ff3b30" stroke-width="1.8">
            <line x1="40" y1="45" x2="155" y2="88" marker-end="url(#arrowDark)"/>
            <line x1="30" y1="65" x2="145" y2="108"/>
            <line x1="50" y1="25" x2="165" y2="68"/>
        </g>
        <text x="40" y="22" font-family="'SF Mono', monospace" font-size="7.8" font-weight="700" fill="#ff3b30">入射雷达电磁波</text>
        <!-- Deflected Specular Reflection into Non-Threatening Sector (Green) -->
        <g stroke="#34c759" stroke-width="2">
            <line x1="155" y1="88" x2="245" y2="25" marker-end="url(#arrowGreen)"/>
            <line x1="145" y1="108" x2="235" y2="45"/>
        </g>
        <text x="250" y="25" font-family="'SF Mono', monospace" font-size="7.8" font-weight="700" fill="#34c759">镜面反射偏折 68°</text>
        <!-- Edge Sweep Angle Lambda -->
        <text x="230" y="160" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#1d1d1f" text-anchor="middle">边缘平行法则: 前后缘后掠角严格一致 Λ = 42°</text>
        <text x="230" y="178" font-family="-apple-system, sans-serif" font-size="8" fill="#0071e3" text-anchor="middle">消除前向单站后向散射 · 雷达截面积 RCS &lt; 0.01 m²</text>
        """
        return wrap(content)

    # 15. maxwell_magnetic
    elif svg_type == "maxwell_magnetic":
        content = """
        <!-- Stator Teeth Profile (0.2mm Kawasaki Silicon Steel) -->
        <path d="M 70 145 L 70 75 L 120 75 L 120 145" fill="none" stroke="#1d1d1f" stroke-width="3"/>
        <path d="M 180 145 L 180 75 L 230 75 L 230 145" fill="none" stroke="#1d1d1f" stroke-width="3"/>
        <path d="M 290 145 L 290 75 L 340 75 L 340 145" fill="none" stroke="#1d1d1f" stroke-width="3"/>
        <!-- Copper Coil Windings with Hatching -->
        <rect x="75" y="85" width="40" height="45" fill="url(#amberGrad)" stroke="#ff9500" stroke-width="1.2"/>
        <rect x="185" y="85" width="40" height="45" fill="url(#amberGrad)" stroke="#ff9500" stroke-width="1.2"/>
        <rect x="295" y="85" width="40" height="45" fill="url(#amberGrad)" stroke="#ff9500" stroke-width="1.2"/>
        <!-- Magnetic Flux Lines Across Airgap -->
        <ellipse cx="95" cy="62" rx="32" ry="20" fill="none" stroke="#0071e3" stroke-width="1.8" stroke-dasharray="4 2"/>
        <ellipse cx="205" cy="62" rx="32" ry="20" fill="none" stroke="#0071e3" stroke-width="1.8" stroke-dasharray="4 2"/>
        <ellipse cx="315" cy="62" rx="32" ry="20" fill="none" stroke="#0071e3" stroke-width="1.8" stroke-dasharray="4 2"/>
        <!-- Permanent Magnets Array Above Airgap -->
        <rect x="65" y="35" width="60" height="12" fill="#d2d2d7" stroke="#1d1d1f" stroke-width="1.2"/>
        <rect x="175" y="35" width="60" height="12" fill="#d2d2d7" stroke="#1d1d1f" stroke-width="1.2"/>
        <rect x="285" y="35" width="60" height="12" fill="#d2d2d7" stroke="#1d1d1f" stroke-width="1.2"/>
        <text x="95" y="44" font-family="'SF Mono', monospace" font-size="7" fill="#ff3b30" text-anchor="middle">N</text>
        <text x="205" y="44" font-family="'SF Mono', monospace" font-size="7" fill="#0071e3" text-anchor="middle">S</text>
        <text x="315" y="44" font-family="'SF Mono', monospace" font-size="7" fill="#ff3b30" text-anchor="middle">N</text>
        <text x="205" y="24" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">气隙磁通密度 B = 1.82 T (高槽满率 92%)</text>
        <text x="205" y="175" font-family="-apple-system, sans-serif" font-size="8" fill="#34c759" font-weight="700" text-anchor="middle">麦克斯韦有限元应力张量寻优 · 消除齿槽转矩脉动与涡流损耗</text>
        """
        return wrap(content)

    # 16. flying_wing_reflex
    elif svg_type == "flying_wing_reflex":
        content = """
        <!-- Reflexed Camber Flying Wing Airfoil -->
        <path d="M 60 115 C 100 80, 210 82, 320 115 C 355 125, 385 120, 405 108 C 365 122, 330 125, 210 116 C 100 116, 75 122, 60 115 Z" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="2.2"/>
        <!-- Reflexed Trailing Edge Camber Line -->
        <line x1="310" y1="118" x2="415" y2="102" stroke="#0071e3" stroke-width="1.5" stroke-dasharray="3 2"/>
        <!-- Aerodynamic Center (AC) vs Center of Gravity (CG) -->
        <circle cx="200" cy="107" r="4" fill="#ff9500"/>
        <text x="190" y="96" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff9500">重心 CG</text>
        <circle cx="230" cy="107" r="4" fill="#0071e3"/>
        <text x="235" y="96" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#0071e3">焦点 AC</text>
        <!-- Static Margin Dimension -->
        <line x1="200" y1="125" x2="230" y2="125" stroke="#1d1d1f" stroke-width="0.8"/>
        <text x="215" y="137" font-family="'SF Mono', monospace" font-size="7" fill="#1d1d1f" text-anchor="middle">Kn = 8.5%</text>
        <!-- Positive Pitching Moment Restoration Arrow -->
        <path d="M 185 130 A 22 22 0 0 1 235 130" fill="none" stroke="#34c759" stroke-width="2" marker-end="url(#arrowGreen)"/>
        <text x="230" y="50" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">反弯后缘提供正零升俯仰力矩 Cm0 &gt; 0</text>
        <text x="230" y="175" font-family="-apple-system, sans-serif" font-size="8" fill="#34c759" font-weight="700" text-anchor="middle">无尾飞翼纵向自配平增稳 · 彻底省去平尾摩擦与干扰阻力</text>
        """
        return wrap(content)

    # 17. downwash_box
    elif svg_type == "downwash_box":
        content = """
        <!-- Spatial Box-Truss Carbon Arm Skeleton -->
        <rect x="70" y="55" width="320" height="90" rx="4" fill="none" stroke="#1d1d1f" stroke-width="2"/>
        <!-- Internal Vertical Posts -->
        <line x1="120" y1="55" x2="120" y2="145" stroke="#0071e3" stroke-width="1.8"/>
        <line x1="230" y1="55" x2="230" y2="145" stroke="#0071e3" stroke-width="1.8"/>
        <line x1="340" y1="55" x2="340" y2="145" stroke="#0071e3" stroke-width="1.8"/>
        <!-- Diagonal Truss Braces -->
        <line x1="70" y1="55" x2="120" y2="145" stroke="#ff9500" stroke-width="1.2"/>
        <line x1="120" y1="55" x2="230" y2="145" stroke="#ff9500" stroke-width="1.2"/>
        <line x1="230" y1="55" x2="340" y2="145" stroke="#ff9500" stroke-width="1.2"/>
        <line x1="340" y1="55" x2="390" y2="145" stroke="#ff9500" stroke-width="1.2"/>
        <!-- Propeller Downwash Arrows Passing Freely Through Center -->
        <g stroke="#34c759" stroke-width="1.8">
            <line x1="175" y1="35" x2="175" y2="165" marker-end="url(#arrowGreen)"/>
            <line x1="285" y1="35" x2="285" y2="165" marker-end="url(#arrowGreen)"/>
        </g>
        <text x="230" y="38" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">空间箱型中空桁架结构</text>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#34c759" font-weight="700" text-anchor="middle">旋翼下洗流直接穿透镂空机臂 · 气动迎风投影面积减少 62%</text>
        """
        return wrap(content)

    # 18. prop_acoustic_waves
    elif svg_type == "prop_acoustic_waves":
        content = """
        <!-- 3-Blade 120 Deg Acoustic Phase Cancellation Waves -->
        <path d="M 50 100 Q 100 35, 150 100 T 250 100 T 350 100" fill="none" stroke="#0071e3" stroke-width="2"/>
        <path d="M 50 100 Q 100 165, 150 100 T 250 100 T 350 100" fill="none" stroke="#ff9500" stroke-width="1.8" stroke-dasharray="4 2"/>
        <!-- Phase Cancelled Resultant Smooth Pressure Line -->
        <line x1="50" y1="100" x2="415" y2="100" stroke="#34c759" stroke-width="2.5"/>
        <text x="230" y="42" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">Gutin 旋转声源与叶梢微后掠三叶相位抵消</text>
        <text x="230" y="130" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759" text-anchor="middle">合成声能干涉相消 // 离散单音尖峰完全平抑</text>
        <text x="230" y="178" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">三叶 120° 旋转几何相位锁定 · 消除二阶谐波抖动</text>
        """
        return wrap(content)

    # 19. flutter_aeroelastic
    elif svg_type == "flutter_aeroelastic":
        content = """
        <!-- Aeroelastic Flutter Bending-Torsion Boundary -->
        <line x1="60" y1="165" x2="425" y2="165" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <line x1="60" y1="165" x2="60" y2="35" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <text x="400" y="180" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">飞行空速 V (m/s)</text>
        <text x="20" y="38" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">阻尼比 ζ</text>
        <!-- Bending mode frequency & Torsion mode frequency curves converging -->
        <path d="M 60 70 C 180 70, 260 78, 350 115" fill="none" stroke="#0071e3" stroke-width="2.2"/>
        <path d="M 60 145 C 180 145, 260 135, 350 115" fill="none" stroke="#ff9500" stroke-width="2.2"/>
        <!-- Flutter Divergence Point -->
        <circle cx="350" cy="115" r="5" fill="#ff3b30"/>
        <text x="355" y="105" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#ff3b30">颤振临界速度 Vf</text>
        <!-- Safe Operating Speed Line -->
        <line x1="220" y1="45" x2="220" y2="165" stroke="#34c759" stroke-width="1.5" stroke-dasharray="3 2"/>
        <text x="220" y="40" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759" text-anchor="middle">V_max 飞行边界 (1.50 安全裕度)</text>
        <text x="230" y="182" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">碳纤大剪切刚度预浸铺层 · 弯扭模态频率彻底解耦</text>
        """
        return wrap(content)

    # 20. t_tail_aerodynamics
    elif svg_type == "t_tail_aerodynamics":
        content = """
        <!-- T-Tail Structural Elevation -->
        <line x1="160" y1="165" x2="230" y2="55" stroke="#1d1d1f" stroke-width="4"/>
        <rect x="130" y="48" width="200" height="14" rx="2" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="2"/>
        <!-- Turbulent Wing Downwash Stream Below -->
        <g stroke="#ff9500" stroke-width="1.5" stroke-dasharray="4 2">
            <path d="M 60 140 C 140 145, 240 155, 380 158"/>
            <path d="M 60 155 C 140 160, 240 168, 380 170"/>
        </g>
        <text x="310" y="145" font-family="'SF Mono', monospace" font-size="7.5" fill="#ff9500">主翼破碎下洗紊流层</text>
        <!-- Clean Free Airflow at T-Tail Top -->
        <g stroke="#0071e3" stroke-width="2">
            <line x1="80" y1="55" x2="380" y2="55" marker-end="url(#arrow)"/>
            <line x1="80" y1="35" x2="380" y2="35" marker-end="url(#arrow)"/>
        </g>
        <text x="390" y="52" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3">纯净未受扰气流</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">T型尾翼气动布局：平尾彻底抬离机身下洗死区</text>
        <text x="230" y="185" font-family="-apple-system, sans-serif" font-size="8" fill="#34c759" font-weight="700" text-anchor="middle">大攻角俯仰操纵舵效提升 34% · 消除深失速失控风险</text>
        """
        return wrap(content)

    # 21. v_tail_decoupling
    elif svg_type == "v_tail_decoupling":
        content = """
        <!-- Inverted V-Tail Dihedral Geometry (110 deg angle) -->
        <line x1="230" y1="140" x2="130" y2="60" stroke="#1d1d1f" stroke-width="3"/>
        <line x1="230" y1="140" x2="330" y2="60" stroke="#1d1d1f" stroke-width="3"/>
        <!-- Ruddervator Force Vector Decomposition -->
        <!-- Left Tail: Combined Force Vector Normal to Fin -->
        <line x1="180" y1="100" x2="140" y2="125" stroke="#ff9500" stroke-width="2.2" marker-end="url(#arrowAmber)"/>
        <!-- Force Decomposed into Fy and Fz -->
        <line x1="140" y1="125" x2="140" y2="100" stroke="#0071e3" stroke-width="1.5" stroke-dasharray="3 2"/>
        <line x1="140" y1="125" x2="180" y2="125" stroke="#34c759" stroke-width="1.5" stroke-dasharray="3 2"/>
        <text x="120" y="115" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#0071e3">F_z (俯仰)</text>
        <text x="160" y="138" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#34c759">F_y (偏航)</text>
        <!-- 110 Deg Dihedral Arc -->
        <path d="M 205 120 A 30 30 0 0 1 255 120" fill="none" stroke="#1d1d1f" stroke-width="1"/>
        <text x="230" y="110" font-family="'SF Mono', monospace" font-size="7.5" fill="#1d1d1f" text-anchor="middle">110°</text>
        <text x="230" y="32" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">倒V尾舵面交叉解耦控制矩阵</text>
        <text x="230" y="178" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">δ_elevator = (δ_L + δ_R)/2 // δ_rudder = (δ_L - δ_R)/2 实时解耦</text>
        """
        return wrap(content)

    # 22. droplet_deposition
    elif svg_type == "droplet_deposition":
        content = """
        <!-- Crop Canopy and Downwash Vortex Spray -->
        <rect x="40" y="145" width="380" height="25" fill="url(#greenGrad)" stroke="#34c759" stroke-width="1.2"/>
        <text x="230" y="162" font-family="-apple-system, sans-serif" font-size="8" font-weight="700" fill="#34c759" text-anchor="middle">农作物树冠层 (叶片正反面双向附着)</text>
        <!-- Centrifugal Nozzle and Atomization Droplet Cone -->
        <circle cx="230" cy="40" r="12" fill="#d2d2d7" stroke="#1d1d1f" stroke-width="1.8"/>
        <!-- Downwash Flow Lines -->
        <path d="M 120 40 C 130 90, 160 135, 170 145" fill="none" stroke="#0071e3" stroke-width="2" marker-end="url(#arrow)"/>
        <path d="M 340 40 C 330 90, 300 135, 290 145" fill="none" stroke="#0071e3" stroke-width="2" marker-end="url(#arrow)"/>
        <!-- Fine Atomized Droplet Particles (VMD = 180 um) -->
        <g fill="#0071e3">
            <circle cx="210" cy="70" r="2"/>
            <circle cx="245" cy="75" r="2.5"/>
            <circle cx="190" cy="100" r="1.8"/>
            <circle cx="270" cy="98" r="2.2"/>
            <circle cx="225" cy="115" r="2"/>
            <circle cx="175" cy="130" r="2.5"/>
            <circle cx="285" cy="128" r="1.8"/>
        </g>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">强风场下压雾化穿透模型 (VMD = 180 μm)</text>
        <text x="230" y="185" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">旋翼大下洗风压彻底吹开冠层 · 农药飘移抑制率达 88%</text>
        """
        return wrap(content)

    # 23. hydraulic_balance
    elif svg_type == "hydraulic_balance":
        content = """
        <!-- Constant Pressure Agricultural Manifold -->
        <line x1="50" y1="100" x2="410" y2="100" stroke="#1d1d1f" stroke-width="4"/>
        <!-- 4 Equal Spacing Spray Nozzles -->
        <g stroke="#0071e3" stroke-width="2">
            <line x1="100" y1="100" x2="100" y2="140" marker-end="url(#arrow)"/>
            <line x1="185" y1="100" x2="185" y2="140" marker-end="url(#arrow)"/>
            <line x1="275" y1="100" x2="275" y2="140" marker-end="url(#arrow)"/>
            <line x1="360" y1="100" x2="360" y2="140" marker-end="url(#arrow)"/>
        </g>
        <!-- Flow meter & Relief Valve -->
        <rect x="50" y="85" width="30" height="30" rx="3" fill="#ffffff" stroke="#ff9500" stroke-width="1.5"/>
        <text x="65" y="103" font-family="'SF Mono', monospace" font-size="6.5" font-weight="700" fill="#ff9500" text-anchor="middle">泵</text>
        <circle cx="230" cy="100" r="14" fill="#ffffff" stroke="#34c759" stroke-width="1.8"/>
        <text x="230" y="103" font-family="'SF Mono', monospace" font-size="6.5" font-weight="700" fill="#34c759" text-anchor="middle">恒压</text>
        <text x="230" y="45" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">闭环电磁恒压配液回流控制回路 (P = 0.45 MPa)</text>
        <text x="230" y="175" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">四通道流量差值 &lt; 1.5% · 彻底杜绝喷杆末端水压衰减断流</text>
        """
        return wrap(content)

    # 24. landing_gear_elasticity
    elif svg_type == "landing_gear_elasticity":
        content = """
        <!-- Parabolic Carbon Composite Leaf Spring Landing Gear -->
        <path d="M 90 60 C 130 60, 160 145, 100 155" fill="none" stroke="#1d1d1f" stroke-width="4"/>
        <path d="M 370 60 C 330 60, 300 145, 360 155" fill="none" stroke="#1d1d1f" stroke-width="4"/>
        <!-- Ground Impact Line -->
        <line x1="60" y1="158" x2="400" y2="158" stroke="#86868b" stroke-width="1.5"/>
        <!-- Deflection Rebound Dynamic Arrow -->
        <path d="M 100 155 Q 120 135, 140 145" fill="none" stroke="#0071e3" stroke-width="2" marker-end="url(#arrow)"/>
        <path d="M 360 155 Q 340 135, 320 145" fill="none" stroke="#0071e3" stroke-width="2" marker-end="url(#arrow)"/>
        <text x="230" y="45" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">复合材料弓形起落架动态吸能 U = ∫(M²/2EI)dx</text>
        <text x="230" y="105" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#ff9500" text-anchor="middle">耐受 3.5G 极限着陆坠撞冲击</text>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#34c759" font-weight="700" text-anchor="middle">大形变非线性弹簧阻尼 · 消除机身硬着陆二次反弹起跳</text>
        """
        return wrap(content)

    # 25. quadrotor_dynamics
    elif svg_type == "quadrotor_dynamics":
        content = """
        <!-- 6-DOF Quadrotor Body Frame (O-Xb, Yb, Zb) -->
        <line x1="230" y1="100" x2="340" y2="100" stroke="#1d1d1f" stroke-width="2" marker-end="url(#arrowDark)"/>
        <line x1="230" y1="100" x2="230" y2="25" stroke="#1d1d1f" stroke-width="2" marker-end="url(#arrowDark)"/>
        <line x1="230" y1="100" x2="160" y2="150" stroke="#1d1d1f" stroke-width="2" marker-end="url(#arrowDark)"/>
        <text x="350" y="104" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#1d1d1f">Xb (Roll φ)</text>
        <text x="235" y="22" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#1d1d1f">Zb (Yaw ψ)</text>
        <text x="145" y="162" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#1d1d1f">Yb (Pitch θ)</text>
        <!-- Rotation Angular Momentum Arrows -->
        <path d="M 310 90 A 15 15 0 0 1 310 110" fill="none" stroke="#0071e3" stroke-width="1.8" marker-end="url(#arrow)"/>
        <path d="M 220 40 A 15 15 0 0 1 240 40" fill="none" stroke="#34c759" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">刚体六自由度牛顿-欧拉非线性解耦运动学方程</text>
        """
        return wrap(content)

    # 26. centrifugal_balance
    elif svg_type == "centrifugal_balance":
        content = """
        <!-- ISO G1.0 Dual Plane Dynamic Balancing Dial -->
        <circle cx="230" cy="100" r="60" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="2"/>
        <line x1="230" y1="35" x2="230" y2="165" stroke="#86868b" stroke-width="0.8" stroke-dasharray="3 3"/>
        <line x1="165" y1="100" x2="295" y2="100" stroke="#86868b" stroke-width="0.8" stroke-dasharray="3 3"/>
        <!-- Imbalance Vector e -->
        <line x1="230" y1="100" x2="270" y2="70" stroke="#ff3b30" stroke-width="2" marker-end="url(#arrowDark)"/>
        <text x="280" y="72" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#ff3b30">偏心偏置 e &lt; 0.5 mg·mm</text>
        <!-- Balancing Counterweight Position -->
        <line x1="230" y1="100" x2="190" y2="130" stroke="#34c759" stroke-width="2" marker-end="url(#arrowGreen)"/>
        <text x="135" y="145" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#34c759">配平质块 Δm</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">Schenck 德国申克双平面动平衡校准 (ISO Class G1.0)</text>
        <text x="230" y="182" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">28,000 RPM 极限转速下振动速度 &lt; 0.35 mm/s · 消除高频抖动</text>
        """
        return wrap(content)

    # 27. efficiency_matching
    elif svg_type == "efficiency_matching":
        content = """
        <!-- Motor Torque-Speed Efficiency Island Contours -->
        <ellipse cx="230" cy="100" rx="145" ry="60" fill="none" stroke="#d2d2d7" stroke-width="1"/>
        <ellipse cx="230" cy="100" rx="95" ry="40" fill="none" stroke="#0071e3" stroke-width="1.5"/>
        <ellipse cx="230" cy="100" rx="50" ry="22" fill="url(#greenGrad)" stroke="#34c759" stroke-width="2"/>
        <circle cx="230" cy="100" r="4" fill="#34c759"/>
        <text x="230" y="104" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759" text-anchor="middle">最高能效点 η=89.2%</text>
        <!-- Propeller Load Power Line P = k*omega^3 -->
        <path d="M 110 150 Q 220 120, 350 45" fill="none" stroke="#ff9500" stroke-width="2.2"/>
        <text x="320" y="38" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#ff9500">负载线 P ∝ ω³</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">电机转矩-转速与螺旋桨气动吸收功率最佳匹配线</text>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">小KV大桨与高阶换向相位角精准咬合 · 续航提升 24%</text>
        """
        return wrap(content)

    # 28. breguet_endurance
    elif svg_type == "breguet_endurance":
        content = """
        <!-- Breguet Endurance Curves (Power Required vs Airspeed) -->
        <line x1="60" y1="165" x2="425" y2="165" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <line x1="60" y1="165" x2="60" y2="35" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <text x="400" y="180" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">空速 V</text>
        <text x="20" y="38" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">需用功率 Preq</text>
        <!-- U-shaped Power Required Curve -->
        <path d="M 85 55 Q 210 160, 395 55" fill="none" stroke="#0071e3" stroke-width="2.5"/>
        <!-- Min Power Point (Max Endurance) -->
        <circle cx="210" cy="133" r="5" fill="#34c759"/>
        <line x1="210" y1="133" x2="210" y2="165" stroke="#34c759" stroke-width="1" stroke-dasharray="3 2"/>
        <text x="210" y="125" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#34c759" text-anchor="middle">V_mp (最大续航航速)</text>
        <!-- Tangent Line from Origin (Max Range) -->
        <line x1="60" y1="165" x2="310" y2="90" stroke="#ff9500" stroke-width="1.5" stroke-dasharray="4 2"/>
        <circle cx="270" cy="108" r="4" fill="#ff9500"/>
        <text x="285" y="102" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff9500">V_mr (最大航程航速)</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">布雷格 (Breguet) 电动长航时航程极值解算</text>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">航程 R = (E_batt·η/g)·(L/D) · 突破 120 分钟单次留空作业</text>
        """
        return wrap(content)

    # 29. supercritical_tip
    elif svg_type == "supercritical_tip":
        content = """
        <!-- Supercritical Blended Winglet Profile -->
        <path d="M 70 120 L 250 120 C 310 120, 360 100, 375 40 L 390 40 C 375 110, 320 135, 250 135 L 70 135 Z" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="2"/>
        <!-- Wingtip Cant and Toe-out Vector -->
        <line x1="375" y1="40" x2="420" y2="35" stroke="#0071e3" stroke-width="1.5" marker-end="url(#arrow)"/>
        <text x="400" y="25" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#0071e3">小翼外倾角 75°</text>
        <!-- Diffused Tip Vortex -->
        <path d="M 375 40 Q 405 55, 385 75 T 395 105" fill="none" stroke="#34c759" stroke-width="1.8" stroke-dasharray="3 2"/>
        <text x="230" y="55" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">超临界微后掠融合式小翼流场</text>
        <text x="230" y="175" font-family="-apple-system, sans-serif" font-size="8" fill="#34c759" font-weight="700" text-anchor="middle">压差涡流扩散至高空层 · 翼梢诱导阻力降低 14.5%</text>
        """
        return wrap(content)

    # 30. joint_contact_stress
    elif svg_type == "joint_contact_stress":
        content = """
        <!-- Lug Eye and High Strength Pin Cylinder -->
        <circle cx="230" cy="100" r="50" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="2"/>
        <circle cx="230" cy="100" r="28" fill="#ffffff" stroke="#1d1d1f" stroke-width="2"/>
        <!-- Hertzian Elliptical Contact Stress Distribution on Pin Surface -->
        <path d="M 202 100 A 28 28 0 0 0 258 100 Q 230 145, 202 100 Z" fill="url(#amberGrad)" stroke="#ff3b30" stroke-width="1.5"/>
        <text x="230" y="125" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff3b30" text-anchor="middle">赫兹接触峰 σ_h=310MPa</text>
        <!-- Clamping Bolt Preload Vector -->
        <line x1="230" y1="35" x2="230" y2="70" stroke="#0071e3" stroke-width="2.5" marker-end="url(#arrow)"/>
        <text x="235" y="52" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3">预紧力 F_pre=12.5kN</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">7075-T651 航空铝关节销轴耳片接触应力计算</text>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">GD&amp;T 配合公差 ±0.010mm · 杜绝折叠机臂长期交变载荷旷量松动</text>
        """
        return wrap(content)

    # 31. tandem_coupling
    elif svg_type == "tandem_coupling":
        content = """
        <!-- Tandem Forward Wing & Aft Wing -->
        <rect x="70" y="85" width="110" height="15" rx="3" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.8"/>
        <rect x="270" y="65" width="140" height="18" rx="3" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.8"/>
        <!-- Forward Wing Lifting Circulation Vortex Inducing Upwash on Aft Wing -->
        <path d="M 180 92 Q 225 105, 270 75" fill="none" stroke="#34c759" stroke-width="2" marker-end="url(#arrowGreen)"/>
        <text x="225" y="118" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#34c759" text-anchor="middle">前翼诱导上洗气流</text>
        <!-- Stagger Dimension Line (h/c) -->
        <line x1="250" y1="74" x2="250" y2="92" stroke="#86868b" stroke-width="0.8"/>
        <text x="255" y="86" font-family="'SF Mono', monospace" font-size="7" fill="#86868b">高差 h</text>
        <text x="230" y="32" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">串列双翼有利气动干涉模型 (Tandem Aero-Coupling)</text>
        <text x="230" y="175" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">后翼利用前翼尾流获得额外有效攻角 · 巡航总升阻比提升 16%</text>
        """
        return wrap(content)

    # 32. dihedral_stability
    elif svg_type == "dihedral_stability":
        content = """
        <!-- Wing Dihedral V-Shape Geometry (Angle Gamma = 4.5 deg) -->
        <line x1="230" y1="125" x2="80" y2="85" stroke="#1d1d1f" stroke-width="3"/>
        <line x1="230" y1="125" x2="380" y2="85" stroke="#1d1d1f" stroke-width="3"/>
        <line x1="80" y1="125" x2="380" y2="125" stroke="#86868b" stroke-width="0.8" stroke-dasharray="3 3"/>
        <!-- Dihedral Angle Arc -->
        <text x="140" y="115" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3">Γ = 4.5°</text>
        <text x="320" y="115" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3">Γ = 4.5°</text>
        <!-- Sideslip Velocity Vector v_slip -->
        <line x1="50" y1="140" x2="110" y2="140" stroke="#ff9500" stroke-width="2" marker-end="url(#arrowAmber)"/>
        <text x="80" y="155" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff9500">侧滑气流 v</text>
        <!-- Restoring Roll Moment Cl_beta Arrow -->
        <path d="M 205 70 A 25 25 0 0 1 255 70" fill="none" stroke="#34c759" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
        <text x="230" y="55" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759" text-anchor="middle">自稳定滚转恢复力矩 Cl_β &lt; 0</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">机翼上反角横向动稳定性几何恢复力矩</text>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">迎风翼有效攻角自增 · 无需副翼干预自动恢复水平姿态</text>
        """
        return wrap(content)

    # 33. helicopter_rotor_dynamics
    elif svg_type == "helicopter_rotor_dynamics":
        content = """
        <!-- Swashplate Cyclic & Collective Pitch Mechanism -->
        <!-- Fixed Swashplate -->
        <line x1="150" y1="120" x2="310" y2="105" stroke="#1d1d1f" stroke-width="3"/>
        <!-- Rotating Swashplate -->
        <line x1="150" y1="110" x2="310" y2="95" stroke="#0071e3" stroke-width="2.5"/>
        <!-- Main Mast Axis -->
        <line x1="230" y1="35" x2="230" y2="165" stroke="#86868b" stroke-width="1.5" stroke-dasharray="4 2"/>
        <!-- Blade Pitch Link Rods -->
        <line x1="170" y1="110" x2="170" y2="55" stroke="#ff9500" stroke-width="1.8"/>
        <line x1="290" y1="95" x2="290" y2="55" stroke="#ff9500" stroke-width="1.8"/>
        <!-- Rotor Blade Grips at Top -->
        <rect x="130" y="50" width="80" height="8" rx="2" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.5"/>
        <rect x="250" y="50" width="80" height="8" rx="2" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.5"/>
        <!-- Swashplate Tilt Angle theta -->
        <text x="325" y="102" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#0071e3">倾斜角 θ=6.2°</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">斜盘周期变距与总距解耦运动学 (90° 相位滞后补偿)</text>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">陀螺进动原理自动补偿 · 实现无刷单旋翼精密六自由度机动</text>
        """
        return wrap(content)

    # 34. reynolds_separation
    elif svg_type == "reynolds_separation":
        content = """
        <!-- Laminar Separation Bubble (LSB) Dynamics -->
        <path d="M 60 135 C 100 80, 200 80, 400 135 Z" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="2"/>
        <!-- Separation Bubble Curve -->
        <path d="M 180 87 Q 240 70, 300 102" fill="url(#amberGrad)" stroke="#ff9500" stroke-width="2"/>
        <!-- Key Points on Airfoil -->
        <circle cx="180" cy="87" r="3" fill="#ff3b30"/>
        <text x="175" y="78" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff3b30" text-anchor="end">层流分离 S</text>
        <circle cx="240" cy="74" r="3" fill="#ff9500"/>
        <text x="240" y="65" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff9500" text-anchor="middle">转捩点 T</text>
        <circle cx="300" cy="102" r="3" fill="#34c759"/>
        <text x="310" y="98" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#34c759">湍流再附 R</text>
        <text x="230" y="32" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">低雷诺数 (Re=1.5×10⁵) 附面层分离泡 (LSB) 再附机制</text>
        <text x="230" y="175" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">微粗糙度边界触发自再附 · 彻底消除低速大攻角气动失速迟滞</text>
        """
        return wrap(content)

    # 35. fault_tolerant_control
    elif svg_type == "fault_tolerant_control":
        content = """
        <!-- Hexarotor Motor Distribution with Motor #3 FAILED -->
        <circle cx="230" cy="100" r="65" fill="none" stroke="#d2d2d7" stroke-width="1.2" stroke-dasharray="3 3"/>
        <!-- 6 Motors at 60 deg intervals -->
        <!-- M1 --> <circle cx="286" cy="67" r="14" fill="url(#greenGrad)" stroke="#34c759" stroke-width="2"/>
        <!-- M2 --> <circle cx="286" cy="133" r="14" fill="url(#greenGrad)" stroke="#34c759" stroke-width="2"/>
        <!-- M3 FAILED (RED X) -->
        <circle cx="230" cy="165" r="14" fill="#ff3b30" fill-opacity="0.2" stroke="#ff3b30" stroke-width="2"/>
        <line x1="222" y1="157" x2="238" y2="173" stroke="#ff3b30" stroke-width="2.5"/>
        <line x1="222" y1="173" x2="238" y2="157" stroke="#ff3b30" stroke-width="2.5"/>
        <text x="230" y="190" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff3b30" text-anchor="middle">M3 故障断电 (T=0)</text>
        <!-- M4 --> <circle cx="174" cy="133" r="14" fill="url(#greenGrad)" stroke="#34c759" stroke-width="2"/>
        <!-- M5 --> <circle cx="174" cy="67" r="14" fill="url(#greenGrad)" stroke="#34c759" stroke-width="2"/>
        <!-- M6 --> <circle cx="230" cy="35" r="14" fill="url(#greenGrad)" stroke="#34c759" stroke-width="2"/>
        <!-- Control Re-allocation Matrix -->
        <text x="230" y="103" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3" text-anchor="middle">B⁺ 动态重构</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">六旋翼单发失效自适应重构容错控制律</text>
        <text x="230" y="178" font-family="-apple-system, sans-serif" font-size="7.8" fill="#424245" text-anchor="middle">对角电机反扭重平衡 · 毫秒级维持姿态受控返航</text>
        """
        return wrap(content)

    # 36. input_shaping_pendulum
    elif svg_type == "input_shaping_pendulum":
        content = """
        <!-- Suspended Payload Anti-Sway Input Shaping -->
        <circle cx="230" cy="45" r="7" fill="#1d1d1f"/>
        <!-- Pendulum Cable and Payload -->
        <line x1="230" y1="45" x2="270" y2="125" stroke="#1d1d1f" stroke-width="1.8"/>
        <circle cx="270" cy="125" r="14" fill="url(#blueGrad)" stroke="#0071e3" stroke-width="2"/>
        <!-- Anti-Sway Impulse Sequence Cancellation -->
        <line x1="230" y1="45" x2="230" y2="140" stroke="#86868b" stroke-width="0.8" stroke-dasharray="3 3"/>
        <path d="M 270 125 Q 230 135, 190 125" fill="none" stroke="#34c759" stroke-width="1.8" stroke-dasharray="2 2"/>
        <text x="230" y="152" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#34c759" text-anchor="middle">零振动输入整形残余摆角 θ &lt; 0.5°</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">吊挂载荷零振动 (Zero-Vibration, ZV) 脉冲整形器</text>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">精确抵消自然摆动半周期 · 加减速机动无残留摆动</text>
        """
        return wrap(content)

    # 37. plate_buckling
    elif svg_type == "plate_buckling":
        content = """
        <!-- Carbon Fiber Sandwich Plate Buckling Under In-Plane Compression -->
        <rect x="70" y="60" width="320" height="80" rx="3" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.8"/>
        <!-- Honeycomb Core Representation -->
        <path d="M 70 100 Q 150 75, 230 100 T 390 100" fill="none" stroke="#ff9500" stroke-width="2.5"/>
        <!-- Compressive In-plane Load Arrows P_cr -->
        <g stroke="#ff3b30" stroke-width="2.5">
            <line x1="30" y1="100" x2="65" y2="100" marker-end="url(#arrowDark)"/>
            <line x1="430" y1="100" x2="395" y2="100" marker-end="url(#arrowDark)"/>
        </g>
        <text x="45" y="85" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#ff3b30">P_cr</text>
        <text x="415" y="85" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#ff3b30">P_cr</text>
        <text x="230" y="42" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">碳纤夹层壁板单半波压缩失稳临界应力 σ_cr = kc·π²D/(b²t)</text>
        <text x="230" y="165" font-family="-apple-system, sans-serif" font-size="8" fill="#34c759" font-weight="700" text-anchor="middle">芳纶蜂窝芯层抗剪支撑 · 临界屈曲载荷提升 320%</text>
        """
        return wrap(content)

    # 38. lidar_slam_ekf
    elif svg_type == "lidar_slam_ekf":
        content = """
        <!-- 3D LiDAR Point Cloud & EKF State Covariance Ellipse -->
        <circle cx="160" cy="110" r="8" fill="#1d1d1f"/>
        <!-- Scanning Rays -->
        <line x1="160" y1="110" x2="90" y2="50" stroke="#0071e3" stroke-width="1" stroke-dasharray="3 2"/>
        <line x1="160" y1="110" x2="160" y2="35" stroke="#0071e3" stroke-width="1" stroke-dasharray="3 2"/>
        <line x1="160" y1="110" x2="240" y2="45" stroke="#0071e3" stroke-width="1" stroke-dasharray="3 2"/>
        <line x1="160" y1="110" x2="280" y2="90" stroke="#0071e3" stroke-width="1" stroke-dasharray="3 2"/>
        <!-- Point Cloud Obstacles -->
        <circle cx="90" cy="50" r="3" fill="#ff9500"/>
        <circle cx="160" cy="35" r="3" fill="#ff9500"/>
        <circle cx="240" cy="45" r="3" fill="#ff9500"/>
        <circle cx="280" cy="90" r="3" fill="#ff9500"/>
        <!-- 3-Sigma EKF Covariance Ellipse -->
        <ellipse cx="160" cy="110" rx="35" ry="20" transform="rotate(-15 160 110)" fill="url(#greenGrad)" stroke="#34c759" stroke-width="1.8"/>
        <text x="160" y="145" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#34c759" text-anchor="middle">3σ 误差不确定性椭圆 P_k|k</text>
        <!-- Trajectory Vector -->
        <path d="M 160 110 Q 220 125, 340 100" fill="none" stroke="#0071e3" stroke-width="2.5" marker-end="url(#arrow)"/>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">激光雷达里程计与扩展卡尔曼滤波 (EKF-SLAM) 融合</text>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">无GPS遮挡室内及森林地下空间自主精准定位 (定位漂移 &lt; 0.8%)</text>
        """
        return wrap(content)

    # 39. space_diversity_rf
    elif svg_type == "space_diversity_rf":
        content = """
        <!-- Space Diversity Dual Antenna Multipath RF Combining -->
        <line x1="130" y1="60" x2="130" y2="120" stroke="#1d1d1f" stroke-width="3"/>
        <line x1="330" y1="60" x2="330" y2="120" stroke="#1d1d1f" stroke-width="3"/>
        <!-- Antenna Separation Distance d >= lambda/2 -->
        <line x1="130" y1="45" x2="330" y2="45" stroke="#0071e3" stroke-width="1"/>
        <text x="230" y="38" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3" text-anchor="middle">天线物理间距 d ≥ λ/2 (空间解相关)</text>
        <!-- Multipath Rayleigh Fading Wavefronts -->
        <path d="M 50 80 Q 90 95, 130 90" fill="none" stroke="#ff3b30" stroke-width="1.8"/>
        <path d="M 50 110 Q 90 85, 130 90" fill="none" stroke="#ff3b30" stroke-width="1.8"/>
        <!-- Maximal Ratio Combining (MRC) -->
        <rect x="200" y="90" width="60" height="40" rx="3" fill="url(#greenGrad)" stroke="#34c759" stroke-width="1.8"/>
        <text x="230" y="114" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#34c759" text-anchor="middle">MRC 合并</text>
        <text x="230" y="155" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759" text-anchor="middle">信噪比增益 SNR +3.8 dB</text>
        <text x="230" y="180" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">双天线空间分集接收：彻底抵抗超远距图传瑞利深衰落断连</text>
        """
        return wrap(content)

    # 40. polymer_impact_absorption
    elif svg_type == "polymer_impact_absorption":
        content = """
        <!-- Polymer Elastomer Stress-Strain Hysteresis Loop -->
        <line x1="80" y1="165" x2="415" y2="165" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <line x1="80" y1="165" x2="80" y2="35" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <text x="390" y="180" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">应变 ε (%)</text>
        <text x="35" y="38" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">应力 σ (MPa)</text>
        <!-- Loading vs Unloading Hysteresis Loop -->
        <path d="M 80 165 C 130 160, 220 90, 360 55 C 240 90, 160 145, 80 165 Z" fill="url(#amberGrad)" stroke="#ff9500" stroke-width="2.2"/>
        <text x="240" y="115" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#ff9500" text-anchor="middle">耗散滞回能量 U_loss = ∮σ dε (85%)</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">高分子记忆聚氨酯撞击能量吸收黏弹性本构响应</text>
        <text x="230" y="182" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">瞬间坠地将动能转化为不可逆热能 · 保护高灵敏机载传感器</text>
        """
        return wrap(content)

    # 41. thrust_line_trim
    elif svg_type == "thrust_line_trim":
        content = """
        <!-- Thrust Line Inclination Passing Through CG -->
        <circle cx="220" cy="110" r="16" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.8"/>
        <circle cx="220" cy="110" r="5" fill="#34c759"/>
        <text x="220" y="138" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#34c759" text-anchor="middle">机体质心 CG</text>
        <!-- Inclined Motor Thrust Vector Line -->
        <line x1="80" y1="130" x2="360" y2="90" stroke="#ff3b30" stroke-width="2.2" marker-end="url(#arrowDark)"/>
        <!-- Inclination Angle Arc -->
        <line x1="80" y1="130" x2="360" y2="130" stroke="#86868b" stroke-width="0.8" stroke-dasharray="3 3"/>
        <text x="300" y="125" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff3b30">θ_tilt = 3.5°</text>
        <text x="230" y="45" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">电机轴线 3.5° 预倾角贯穿质心平衡几何</text>
        <text x="230" y="175" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">全速平飞推力线无零偏力矩臂 · 巡航状态舵机微调功耗降至零</text>
        """
        return wrap(content)

    # 42. lifting_body_cg
    elif svg_type == "lifting_body_cg":
        content = """
        <!-- Blended Wing Body (BWB) Longitudinal Neutral Point vs CG -->
        <polygon points="70,120 230,60 390,120 230,105" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="2"/>
        <circle cx="215" cy="88" r="4" fill="#34c759"/>
        <text x="205" y="80" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#34c759">质心 CG</text>
        <circle cx="245" cy="88" r="4" fill="#0071e3"/>
        <text x="255" y="80" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#0071e3">中立点 NP</text>
        <line x1="215" y1="95" x2="245" y2="95" stroke="#ff9500" stroke-width="1.5"/>
        <text x="230" y="105" font-family="'SF Mono', monospace" font-size="7" font-weight="700" fill="#ff9500" text-anchor="middle">静裕度 9.2%</text>
        <text x="230" y="32" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">翼身融合升力体纵向气动焦点与静稳定裕度校核</text>
        <text x="230" y="175" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">大载重重心前后漂移包络内均保证自稳定恢复能力</text>
        """
        return wrap(content)

    # 43. rtk_differential
    elif svg_type == "rtk_differential":
        content = """
        <!-- RTK Differential GPS/BDS Positioning Geometry -->
        <!-- Satellite Constellation -->
        <polygon points="120,40 125,32 135,32 140,40 130,45" fill="#0071e3"/>
        <text x="130" y="24" font-family="'SF Mono', monospace" font-size="7" fill="#0071e3">GNSS 卫星</text>
        <!-- Ground Base Station -->
        <line x1="100" y1="145" x2="100" y2="105" stroke="#1d1d1f" stroke-width="2"/>
        <circle cx="100" cy="105" r="6" fill="#34c759"/>
        <text x="100" y="160" font-family="'SF Mono', monospace" font-size="7" fill="#34c759" text-anchor="middle">基准站 (已知坐标)</text>
        <!-- Rover UAV -->
        <circle cx="340" cy="85" r="12" fill="url(#blueGrad)" stroke="#1d1d1f" stroke-width="1.8"/>
        <text x="340" y="112" font-family="'SF Mono', monospace" font-size="7" fill="#0071e3" text-anchor="middle">移动站无人机</text>
        <!-- Carrier Phase Signals (Double Difference) -->
        <line x1="130" y1="45" x2="100" y2="105" stroke="#0071e3" stroke-width="1" stroke-dasharray="3 2"/>
        <line x1="130" y1="45" x2="340" y2="85" stroke="#0071e3" stroke-width="1" stroke-dasharray="3 2"/>
        <!-- RTCM Differential Radio Link -->
        <line x1="100" y1="105" x2="340" y2="85" stroke="#ff9500" stroke-width="1.8"/>
        <text x="220" y="80" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff9500" text-anchor="middle">RTCM 3.2 载波相位双差解算</text>
        <text x="230" y="175" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759" text-anchor="middle">厘米级精度: 水平 1.0 cm + 1 ppm // 高程 1.5 cm</text>
        """
        return wrap(content)

    # 44. tilt_rotor_singularity
    elif svg_type == "tilt_rotor_singularity":
        content = """
        <!-- Tilt Rotor Nacelle Conversion Singularity Corridor -->
        <line x1="60" y1="165" x2="425" y2="165" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <line x1="60" y1="165" x2="60" y2="35" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <text x="400" y="180" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">倾转角 β (°)</text>
        <text x="20" y="38" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">操纵效能</text>
        <!-- Rotor Pitch Authority vs Aero Surface Authority -->
        <path d="M 60 55 C 180 55, 250 145, 395 165" fill="none" stroke="#ff9500" stroke-width="2.2"/>
        <path d="M 60 165 C 200 160, 270 70, 395 55" fill="none" stroke="#0071e3" stroke-width="2.2"/>
        <text x="100" y="75" font-family="'SF Mono', monospace" font-size="7.5" fill="#ff9500">旋翼周期变距权重</text>
        <text x="320" y="75" font-family="'SF Mono', monospace" font-size="7.5" fill="#0071e3">气动舵面权重</text>
        <!-- Singularity Avoidance Zone -->
        <rect x="200" y="55" width="80" height="110" fill="url(#greenGrad)" stroke="#34c759" stroke-width="1" stroke-dasharray="3 3"/>
        <text x="240" y="115" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#34c759" text-anchor="middle">平滑无奇异过渡区</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">倾转双旋翼全包线控制权平滑移交分配律</text>
        """
        return wrap(content)

    # 45. tsai_wu_composite
    elif svg_type == "tsai_wu_composite":
        content = """
        <!-- Tsai-Wu Composite Laminate Failure Tensor Ellipse -->
        <line x1="60" y1="100" x2="410" y2="100" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <line x1="230" y1="175" x2="230" y2="25" stroke="#1d1d1f" stroke-width="1.2" marker-end="url(#arrowDark)"/>
        <text x="390" y="115" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">σ₁ (纵向应力)</text>
        <text x="235" y="25" font-family="'SF Mono', monospace" font-size="8" fill="#1d1d1f" font-weight="700">σ₂ (横向应力)</text>
        <!-- Tilted Failure Envelope Ellipse -->
        <ellipse cx="220" cy="95" rx="130" ry="55" transform="rotate(-25 220 95)" fill="url(#greenGrad)" stroke="#34c759" stroke-width="2"/>
        <text x="220" y="98" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#34c759" text-anchor="middle">安全弹性包络 Fi·σi + Fij·σi·σj &lt; 1</text>
        <!-- Operating Load Point -->
        <circle cx="260" cy="75" r="4" fill="#ff3b30"/>
        <text x="270" y="72" font-family="'SF Mono', monospace" font-size="7.5" font-weight="700" fill="#ff3b30">设计载荷点 (安全系数 SF=2.15)</text>
        <text x="230" y="185" font-family="-apple-system, sans-serif" font-size="8" fill="#424245" text-anchor="middle">蔡-吴 (Tsai-Wu) 交互张量多轴应力失效准则校核</text>
        """
        return wrap(content)

    # 46. gdt_cg_balance
    elif svg_type == "gdt_cg_balance":
        content = """
        <!-- ISO GD&T True Position & Datum Balance -->
        <circle cx="230" cy="100" r="55" fill="none" stroke="#d2d2d7" stroke-width="1.2"/>
        <!-- Datum Reference Frame Target -->
        <circle cx="230" cy="100" r="24" fill="url(#blueGrad)" stroke="#0071e3" stroke-width="1.8"/>
        <line x1="230" y1="35" x2="230" y2="165" stroke="#1d1d1f" stroke-width="1" stroke-dasharray="4 2"/>
        <line x1="165" y1="100" x2="295" y2="100" stroke="#1d1d1f" stroke-width="1" stroke-dasharray="4 2"/>
        <!-- GD&T Callout Frame: Position Tolerance 0.02 to Datum [A|B|C] -->
        <rect x="135" y="145" width="190" height="22" fill="#ffffff" stroke="#1d1d1f" stroke-width="1.2"/>
        <text x="145" y="160" font-family="'SF Mono', monospace" font-size="9" fill="#1d1d1f">⌖</text>
        <text x="160" y="159" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#1d1d1f">⌀ 0.020</text>
        <text x="225" y="159" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3">A</text>
        <text x="255" y="159" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3">B</text>
        <text x="285" y="159" font-family="'SF Mono', monospace" font-size="8" font-weight="700" fill="#0071e3">C</text>
        <text x="230" y="24" font-family="'SF Mono', monospace" font-size="8.5" font-weight="700" fill="#1d1d1f" text-anchor="middle">ISO 1101 三维基准位置度与质心包络公差框</text>
        <text x="230" y="182" font-family="-apple-system, sans-serif" font-size="8" fill="#34c759" font-weight="700" text-anchor="middle">整机重心空间球形允差 ⌀ 0.8 mm · 倾转机构动态平衡免配重</text>
        """
        return wrap(content)

    return wrap(content)
