# -*- coding: utf-8 -*-
"""
合并 build_catalog_v2 与 build_catalog_v2_part2 为完整 catalog_data_v2.py
"""
import build_catalog_v2
import build_catalog_v2_part2

p1 = build_catalog_v2.items_meta
p2 = build_catalog_v2_part2.part2_meta
all_meta = p1 + p2

header = '''# -*- coding: utf-8 -*-
"""
无人机与飞行系统工程典藏画册 (Apple 极简工业设计体系) - 46大展项98P完整数据
每个展项独立占 2 页 (1页纯大图展示 + 1页图文并茂专业理论讲解)，46*2=92页正文
加上 封面(P1)、序言(P2)、目录(P3-P4)、制造检验(P97)、封底(P98)，共98页。
"""

ALBUM_META = {
    "title_zh": "未来飞行 · 航空航天飞行系统工程图鉴",
    "title_en": "Aerospace Dynamics & Autonomous Flight Systems",
    "subtitle": "工业级飞行平台 · 战术飞行器 · 复合翼系统 · 核心动力与飞行物理理论解构",
    "edition": "2026-2027 Master Blueprint Edition",
    "total_pages": 98
}

ITEMS = [
'''

footer = ''']

if __name__ == "__main__":
    print(f"Total items in catalog_data_v2: {len(ITEMS)}")
'''

with open("e:/brochure/catalog_data_v2.py", "w", encoding="utf-8") as f:
    f.write(header)
    for idx, item in enumerate(all_meta, 1):
        img, cat_zh, cat_en, name_zh, name_en, code, tagline, desc, theory_title, theory_desc, theory_formula, svg_type, hero_stats, specs = item
        f.write("    {\n")
        f.write(f'        "index": {idx},\n')
        f.write(f'        "image": {repr(img)},\n')
        f.write(f'        "category_zh": {repr(cat_zh)},\n')
        f.write(f'        "category_en": {repr(cat_en)},\n')
        f.write(f'        "name_zh": {repr(name_zh)},\n')
        f.write(f'        "name_en": {repr(name_en)},\n')
        f.write(f'        "code": {repr(code)},\n')
        f.write(f'        "tagline": {repr(tagline)},\n')
        f.write(f'        "desc": {repr(desc)},\n')
        f.write(f'        "theory_title": {repr(theory_title)},\n')
        f.write(f'        "theory_desc": {repr(theory_desc)},\n')
        f.write(f'        "theory_formula": {repr(theory_formula)},\n')
        f.write(f'        "svg_type": {repr(svg_type)},\n')
        
        # hero_stats
        f.write('        "hero_stats": [\n')
        for val, lbl in hero_stats:
            f.write(f'            {{"val": {repr(val)}, "lbl": {repr(lbl)}}},\n')
        f.write('        ],\n')
        
        # specs
        f.write('        "specs": [\n')
        for lbl, val in specs:
            f.write(f'            {{"label": {repr(lbl)}, "value": {repr(val)}}},\n')
        f.write('        ]\n')
        f.write("    },\n" if idx < len(all_meta) else "    }\n")
    f.write(footer)

print("Successfully written catalog_data_v2.py with 46 items!")
