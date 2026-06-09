import os
import re

def generate_readme():
    # Megkeresi az összes .py fájlt a mappában
    files = [f for f in os.listdir('.') if f.endswith('.py') and f != 'generate_readme.py']
    files.sort()

    content = "# Borsodi Mátrix - Modulok Tára\n\n"
    content += "| Modul neve | Leírás |\n"
    content += "| :--- | :--- |\n"
    
    # A regex itt a tripla idézőjeleket keresi, ami a legbiztonságosabb
    # re.DOTALL: engedi, hogy a szöveg több soros legyen
    pattern = re.compile(r'module_desc\s*=\s*"""(.*?)"""', re.DOTALL)
    
    for f_name in files:
        try:
            with open(f_name, 'r', encoding='utf-8') as f:
                file_content = f.read()
                
                match = pattern.search(file_content)
                
                if match:
                    # Kitisztítjuk a whitespace-t a leírásból
                    desc = match.group(1).strip().replace('\n', ' ')
                else:
                    desc = "---" # Ha nincs leírás, nem akad el, csak jelzi
                
                content += f"| `{f_name}` | {desc} |\n"
        except Exception as e:
            print(f"Hiba a(z) {f_name} feldolgozásakor: {e}")
    
    # A 'w' mód biztosítja, hogy minden futtatáskor tiszta lapot kapj
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("README.md sikeresen generálva! A Mátrix szinkronizálva.")

if __name__ == "__main__":
    generate_readme()
