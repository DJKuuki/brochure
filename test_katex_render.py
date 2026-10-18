import subprocess
import json

formulas = [
    r"C_d = \frac{D}{\frac{1}{2}\rho v^2 A} = 0.045",
    r"EI = \frac{E \cdot b h^3}{12} \quad [E_{\mathrm{T700}} = 230\,\mathrm{GPa}]",
    r"L_{\mathrm{total}} = L_{\mathrm{wing}}(v) + \sum T_{\mathrm{vertical}} = W_{\mathrm{aircraft}}",
    r"\eta_{\mathrm{duct}} = \frac{T_{\mathrm{prop}} + T_{\mathrm{duct}}}{T_{\mathrm{isolated}}} > 1.10",
    r"\begin{bmatrix} \delta_L \\ \delta_R \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} \delta_e \\ \delta_r \end{bmatrix}"
]

js_script = """
const katex = require('katex');
const formulas = JSON.parse(process.argv[1]);
const rendered = formulas.map(f => katex.renderToString(f, { displayMode: true, throwOnError: false }));
console.log(JSON.stringify(rendered));
"""

res = subprocess.run(["node", "-e", js_script, json.dumps(formulas)], capture_output=True, text=True, encoding="utf-8", check=True)
rendered_htmls = json.loads(res.stdout)

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="file:///e:/brochure/node_modules/katex/dist/katex.min.css">
<style>
body {{ background: #0a0a0c; color: #f5f5f7; padding: 40px; font-family: -apple-system, sans-serif; }}
.formula-row {{ margin: 20px 0; padding: 15px 0; border-bottom: 0.5px solid rgba(255,255,255,0.15); }}
.formula-label {{ font-size: 11px; color: #2997ff; letter-spacing: 1px; font-family: monospace; margin-bottom: 8px; }}
</style>
</head>
<body>
<h1>LaTeX KaTeX Aerospace Equations Test</h1>
"""

for i, r in enumerate(rendered_htmls):
    html += f'<div class="formula-row"><div class="formula-label">FORMULA {i+1:02d}</div>{r}</div>'

html += "</body></html>"

with open("test_katex.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved test_katex.html successfully!")
