# -*- coding: utf-8 -*-
"""
Pre-rendered LaTeX formulas for all 46 aerospace exhibits using KaTeX
"""
import subprocess
import json

LATEX_FORMULAS = {
    1: r"C_d = \frac{D}{\frac{1}{2}\rho v^2 A} = 0.045",
    2: r"EI = \frac{E \cdot b h^3}{12} \quad [E_{\mathrm{T700}} = 230\,\mathrm{GPa}]",
    3: r"L_{\mathrm{total}} = L_{\mathrm{wing}}(v) + \sum T_{\mathrm{vertical}} = W_{\mathrm{aircraft}}",
    4: r"\eta_{\mathrm{duct}} = \frac{T_{\mathrm{prop}} + T_{\mathrm{duct}}}{T_{\mathrm{isolated}}} > 1.10",
    5: r"I_{xx} = I_{yy} \quad [I_{xy} = 0]",
    6: r"\Delta T_{\mathrm{loss}} = f\left(\frac{\Delta y}{R_{\mathrm{rotor}}}\right) < 4\%",
    7: r"V_{\mathrm{ripple}} = \frac{I_{\mathrm{peak}}}{2\pi f_{\mathrm{pwm}} C} < 15\,\mathrm{mV}",
    8: r"C_{Di} = \frac{C_L^2}{\pi e \cdot \mathrm{AR}} \quad \left[\mathrm{AR} = \frac{b^2}{S} = 26.2\right]",
    9: r"u(t) = K_p e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de}{dt} + K_f \frac{dr}{dt}",
    10: r"\min_{\mathbf{x}} C(\mathbf{x}) = \mathbf{U}^{\mathsf{T}}\mathbf{K}\mathbf{U} \quad \text{s.t.} \quad \frac{V(\mathbf{x})}{V_0} \le f",
    11: r"R_{\mathrm{slip}}(x) = R_{\mathrm{prop}} \sqrt{\frac{1 + a}{1 + 2a}}",
    12: r"W_{\mathrm{acoustic}} = k \left(\frac{\rho v_{\mathrm{tip}}^5 D^2}{a_0^3}\right) \frac{1}{B^2}",
    13: r"T_{\mathrm{torsion}} = 2 A_{\mathrm{enclosed}} \, q_{\mathrm{shear}} \quad [J_{\mathrm{box}} \gg \sum J_{\mathrm{plate}}]",
    14: r"\sigma_{\mathrm{RCS}} = \lim_{R \to \infty} 4\pi R^2 \frac{|\mathbf{E}_s|^2}{|\mathbf{E}_i|^2}",
    15: r"\Phi_{\mathrm{diff}} = \rho_{\mathrm{geom}} + \lambda N + \varepsilon_{\mathrm{phase}} \quad [\Delta < 1\,\mathrm{cm}]",
    16: r"C_m = C_{m0} + C_{m\alpha}\alpha \quad [C_{m0} > 0,\, C_{m\alpha} < 0]",
    17: r"F_{\mathrm{drag}} = \frac{1}{2} C_{d,\mathrm{box}} \rho v_{\mathrm{downwash}}^2 A_{\mathrm{proj}}",
    18: r"T_{em} = \left(\frac{\pi D^2 L}{4}\right) B_{\mathrm{gap}} A_{\mathrm{linear}} \cos\theta",
    19: r"W_{\mathrm{sound}} \propto \rho c^3 D^2 M_{\mathrm{tip}}^6 C_T^2",
    20: r"v_{\mathrm{flutter}} \propto \sqrt{\frac{GJ}{I_\alpha (x_\alpha - x_{ea})}}",
    21: r"C_{m\delta_e} = - C_{L\alpha,\mathrm{tail}} \left(\frac{S_{\mathrm{tail}} l_{\mathrm{tail}}}{S \bar{c}}\right) \eta_{\mathrm{tail}}",
    22: r"\begin{bmatrix} \delta_L \\ \delta_R \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} \delta_e \\ \delta_r \end{bmatrix}",
    23: r"v_{\mathrm{terminal}} = \frac{(\rho_{\mathrm{drop}} - \rho_{\mathrm{air}}) g d^2}{18 \mu_{\mathrm{air}}}",
    24: r"\Delta P_{\mathrm{pipe}} = \lambda \left(\frac{L}{D}\right) \left(\frac{\rho v^2}{2}\right) \quad [\Delta_{\mathrm{bal}} < 2\%]",
    25: r"E_{\mathrm{kinetic}} = \frac{1}{2} m v_{\mathrm{drop}}^2 \le \int F_{\mathrm{spring}} \, dx",
    26: r"m \frac{d^2\mathbf{r}}{dt^2} = \mathbf{R} \mathbf{T} - m\mathbf{g} - \mathbf{D}",
    27: r"F_{\mathrm{centrifugal}} = m_{\mathrm{blade}} r_{cg} \omega^2 \quad [\Delta_{\mathrm{res}} < 0.05\,\mathrm{g}]",
    28: r"\eta_{\mathrm{system}} = \frac{T_{\mathrm{thrust}}}{V_{\mathrm{bus}} I_{\mathrm{bus}}} = 11.8\,\mathrm{g/W}",
    29: r"E_{\mathrm{endurance}} = \frac{\eta_{\mathrm{prop}}}{\mathrm{SFC}} \frac{C_L}{C_D} \ln\left(\frac{W_{\mathrm{initial}}}{W_{\mathrm{final}}}\right)",
    30: r"C_{p,\mathrm{tip}} = 1 - \left(\frac{v_{\mathrm{tip}}}{v_{\mathrm{sound}}}\right)^2",
    31: r"\sigma_{\mathrm{contact}} = \sqrt{\frac{F_{\mathrm{clamp}} E_{\mathrm{composite}}}{\pi R_{\mathrm{pipe}} L_{\mathrm{contact}}}}",
    32: r"C_{L,\mathrm{tandem}} = C_{L1}(\alpha) + \frac{S_2}{S_1} C_{L2}(\alpha - \varepsilon(\alpha))",
    33: r"C_{l\beta} \propto - \Gamma \left(\frac{C_{L,\mathrm{wing}}}{6}\right)",
    34: r"T_{\mathrm{hover}} = \sqrt{2\rho A_{\mathrm{disk}} P_{\mathrm{shaft}} \eta_{\mathrm{FM}}}",
    35: r"\mathrm{Re} = \frac{\rho v c}{\mu} \quad [\text{Separation Controlled by VG}]",
    36: r"\mathbf{u}_{\mathrm{actuators}} = \mathbf{B}^\dagger \mathbf{v}_{\mathrm{virtual}}",
    37: r"\frac{A_{n+1}}{A_n} = \exp\left(-\frac{\zeta \pi}{\sqrt{1 - \zeta^2}}\right)",
    38: r"\sigma_{\mathrm{crit}} = \frac{k_{\mathrm{buckling}} \pi^2 E}{12(1 - \nu^2)} \left(\frac{t}{b}\right)^2",
    39: r"\mathbf{r}_k(\mathbf{x}) = \mathbf{p}_{\mathrm{point\text{-}to\text{-}plane}}(\mathbf{T}_{wb} \mathbf{p}_{\mathrm{lidar}})",
    40: r"P_{\mathrm{outage,div}} = P_{\mathrm{outage}}^2 \quad [\mathrm{SNR}_{\mathrm{mrc}} = \mathrm{SNR}_1 + \mathrm{SNR}_2]",
    41: r"E_{\mathrm{dissipated}} = \int \sigma(\varepsilon, \dot{\varepsilon})\,d\varepsilon > 0.85\,E_k",
    42: r"\Delta M_{\mathrm{thrust}} = T_{\mathrm{cruise}} \cdot z_{\mathrm{thrust\_offset}}",
    43: r"x_{\mathrm{margin}} = \frac{x_{\mathrm{NP}} - x_{\mathrm{CG}}}{\mathrm{MAC}} \in [15\%, 38\%]",
    44: r"\tau_{\mathrm{yaw}} = T_L \sin(\delta_L) \cdot d - T_R \sin(\delta_R) \cdot d",
    45: r"F_i \sigma_i + F_{ij} \sigma_i \sigma_j \le 1.0 \quad [\text{Tsai-Wu Criterion}]",
    46: r"x_{\mathrm{cg}}(\theta) = \frac{m_{\mathrm{fuse}}x_{\mathrm{fuse}} + 2m_{\mathrm{motor}}x_{\mathrm{rot}}(\theta)}{M_{\mathrm{total}}}"
}

def render_all_katex():
    js_script = """
    const katex = require('katex');
    const input = JSON.parse(process.argv[1]);
    const output = {};
    for (const [k, v] of Object.entries(input)) {
        output[k] = katex.renderToString(v, { displayMode: true, throwOnError: false });
    }
    console.log(JSON.stringify(output));
    """
    res = subprocess.run(
        ["node", "-e", js_script, json.dumps(LATEX_FORMULAS)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True
    )
    return json.loads(res.stdout)

if __name__ == "__main__":
    rendered = render_all_katex()
    print(f"Successfully pre-rendered {len(rendered)} LaTeX formulas via KaTeX!")
    with open("pre_rendered_katex.json", "w", encoding="utf-8") as f:
        json.dump(rendered, f, ensure_ascii=False, indent=2)
    print("Saved pre_rendered_katex.json!")
