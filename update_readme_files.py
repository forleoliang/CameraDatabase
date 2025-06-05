import os
import re

# 定义要处理的文件
readme_files = [
    'doc/README_en.md',
    'doc/README_zh.md',
    'doc/README_ja.md',
    'doc/README_es.md',
    'doc/README_fr.md',
    'doc/README_de.md'
]

# 更新仓库结构部分
def update_repository_structure(content, file_lang):
    # 根据不同语言确定正确的结构部分标题
    structure_titles = {
        'en': '## Repository Structure',
        'zh': '## 仓库结构',
        'ja': '## リポジトリの構造',
        'es': '## Estructura del Repositorio',
        'fr': '## Structure du Dépôt',
        'de': '## Repository-Struktur'
    }
    
    # 获取当前文件的语言
    lang = file_lang
    structure_title = structure_titles.get(lang, structure_titles['en'])
    
    # 确定不同语言的描述文本
    descriptions = {
        'en': {
            'data': 'Data directory',
            'csv': 'CSV format camera specifications',
            'json': 'JSON format camera specifications',
            'images': 'Sample camera images',
            'doc': 'Documentation directory',
            'readme_en': 'English documentation',
            'readme_zh': 'Chinese documentation',
            'readme_ja': 'Japanese documentation',
            'readme_es': 'Spanish documentation',
            'readme_fr': 'French documentation',
            'readme_de': 'German documentation',
            'main_readme': 'Main README'
        },
        'zh': {
            'data': '数据目录',
            'csv': 'CSV格式的相机规格数据',
            'json': 'JSON格式的相机规格数据',
            'images': '相机图像示例',
            'doc': '文档目录',
            'readme_en': '英文文档',
            'readme_zh': '中文文档',
            'readme_ja': '日文文档',
            'readme_es': '西班牙文文档',
            'readme_fr': '法文文档',
            'readme_de': '德文文档',
            'main_readme': '主README文件'
        },
        'ja': {
            'data': 'データディレクトリ',
            'csv': 'CSV形式のカメラ仕様',
            'json': 'JSON形式のカメラ仕様',
            'images': 'カメラ画像サンプル',
            'doc': 'ドキュメントディレクトリ',
            'readme_en': '英語ドキュメント',
            'readme_zh': '中国語ドキュメント',
            'readme_ja': '日本語ドキュメント',
            'readme_es': 'スペイン語ドキュメント',
            'readme_fr': 'フランス語ドキュメント',
            'readme_de': 'ドイツ語ドキュメント',
            'main_readme': 'メインREADMEファイル'
        },
        'es': {
            'data': 'Directorio de datos',
            'csv': 'Especificaciones de cámaras en formato CSV',
            'json': 'Especificaciones de cámaras en formato JSON',
            'images': 'Imágenes de muestra de cámaras',
            'doc': 'Directorio de documentación',
            'readme_en': 'Documentación en inglés',
            'readme_zh': 'Documentación en chino',
            'readme_ja': 'Documentación en japonés',
            'readme_es': 'Documentación en español',
            'readme_fr': 'Documentación en francés',
            'readme_de': 'Documentación en alemán',
            'main_readme': 'README principal'
        },
        'fr': {
            'data': 'Répertoire de données',
            'csv': 'Spécifications des appareils photo au format CSV',
            'json': 'Spécifications des appareils photo au format JSON',
            'images': 'Échantillons d\'images d\'appareils photo',
            'doc': 'Répertoire de documentation',
            'readme_en': 'Documentation en anglais',
            'readme_zh': 'Documentation en chinois',
            'readme_ja': 'Documentation en japonais',
            'readme_es': 'Documentation en espagnol',
            'readme_fr': 'Documentation en français',
            'readme_de': 'Documentation en allemand',
            'main_readme': 'Fichier README principal'
        },
        'de': {
            'data': 'Datenverzeichnis',
            'csv': 'Kameraspezifikationen im CSV-Format',
            'json': 'Kameraspezifikationen im JSON-Format',
            'images': 'Beispielbilder von Kameras',
            'doc': 'Dokumentationsverzeichnis',
            'readme_en': 'Englische Dokumentation',
            'readme_zh': 'Chinesische Dokumentation',
            'readme_ja': 'Japanische Dokumentation',
            'readme_es': 'Spanische Dokumentation',
            'readme_fr': 'Französische Dokumentation',
            'readme_de': 'Deutsche Dokumentation',
            'main_readme': 'Haupt-README-Datei'
        }
    }
    
    desc = descriptions.get(lang, descriptions['en'])
    
    # 标记当前语言文件
    current_file_marker = {
        'en': '(this file)',
        'zh': '（本文件）',
        'ja': '（本ファイル）',
        'es': '(este archivo)',
        'fr': '(ce fichier)',
        'de': '(diese Datei)'
    }
    
    marker = current_file_marker.get(lang, current_file_marker['en'])
    
    # 创建新的仓库结构部分
    this_file = f"README_{lang}.md"
    new_structure = f"""
{structure_title}

```
CameraDatabase/
├── data/                          # {desc['data']}
│   ├── camera_data_cleaned.csv    # {desc['csv']}
│   ├── camera_data_cleaned.json   # {desc['json']}
│   └── images/                    # {desc['images']}
├── doc/                           # {desc['doc']}
│   ├── README_en.md               # {desc['readme_en']}{' ' + marker if this_file == 'README_en.md' else ''}
│   ├── README_zh.md               # {desc['readme_zh']}{' ' + marker if this_file == 'README_zh.md' else ''}
│   ├── README_ja.md               # {desc['readme_ja']}{' ' + marker if this_file == 'README_ja.md' else ''}
│   ├── README_es.md               # {desc['readme_es']}{' ' + marker if this_file == 'README_es.md' else ''}
│   ├── README_fr.md               # {desc['readme_fr']}{' ' + marker if this_file == 'README_fr.md' else ''}
│   └── README_de.md               # {desc['readme_de']}{' ' + marker if this_file == 'README_de.md' else ''}
└── README.md                      # {desc['main_readme']}
```
"""
    
    # 在文件中查找并替换仓库结构部分
    pattern = re.compile(f"{re.escape(structure_title)}.*?```.*?```", re.DOTALL)
    if pattern.search(content):
        return pattern.sub(new_structure, content)
    return content

# 更新导航链接
def update_navigation_links(content):
    # 原始链接模式
    pattern = re.compile(r'\[!\[([^\]]+)\]\([^)]+\)\]\(([^)]+)\)')
    
    # 新链接格式，保持相对路径
    def replace_link(match):
        badge_text = match.group(1)
        badge_link = badge_text.lower()
        if badge_link == 'english':
            file = 'README_en.md'
        elif badge_link == '中文':
            file = 'README_zh.md'
        elif badge_link == '日本語':
            file = 'README_ja.md'
        elif badge_link == 'español':
            file = 'README_es.md'
        elif badge_link == 'français':
            file = 'README_fr.md'
        elif badge_link == 'deutsch':
            file = 'README_de.md'
        else:
            file = f'README_{badge_link}.md'
            
        return f'[![{badge_text}](https://img.shields.io/badge/{badge_text.replace(" ", "%20")}-{file.replace("_", "__")}-{get_badge_color(badge_text)})]({file})'
    
    # 为不同语言设置不同颜色
    def get_badge_color(language):
        colors = {
            'English': 'blue',
            '中文': 'red',
            '日本語': 'green',
            'Español': 'yellow',
            'Français': 'purple',
            'Deutsch': 'orange'
        }
        return colors.get(language, 'gray')
    
    return pattern.sub(replace_link, content)

# 处理所有文件
for file_path in readme_files:
    # 从文件名提取语言代码
    lang_code = file_path.split('_')[-1].split('.')[0]
    
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新内容
    updated_content = update_repository_structure(content, lang_code)
    updated_content = update_navigation_links(updated_content)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"已更新: {file_path}")

print("所有README文件更新完成！") 