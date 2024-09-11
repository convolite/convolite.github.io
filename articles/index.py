import os
import json

folder_path = 'C:\\Users\\veric\\OneDrive\\Desktop\\Website\\new1\\convolite.github.io\\articles'
index_file = 'index.json'

def read_files():
    files = []
    for file in os.listdir(folder_path):
        if file.endswith(".html"):
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                content = f.read()
                title_start = content.find('<title>') + len('<title>')
                title_end = content.find('</title>')
                title = content[title_start:title_end].strip()
                
                # Generate the link in the desired format
                link = f"https://convolite.github.io/articles/{file}"
                
                files.append({
                    'title': title,
                    'link': link
                })
    return files

def write_index_file(files):
    with open(os.path.join(folder_path, index_file), 'w', encoding='utf-8') as f:
        json.dump(files, f, indent=4)

files = read_files()
write_index_file(files)

print(f"Indexed {len(files)} articles. Index file created at {os.path.join(folder_path, index_file)}")
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MKRXXLJQ6D"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-MKRXXLJQ6D');
</script>
