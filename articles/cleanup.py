import os

# Define the directory path
directory = r'C:\Users\veric\OneDrive\Desktop\Website\new1\convolite.github.io'

# Define the Google Tag Manager code
gtag_code = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MKRXXLJQ6D"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-MKRXXLJQ6D');
</script>
"""

# Function to check if the file already contains the code
def contains_gtag_code(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return gtag_code.strip() in content
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")
        return False

# Function to append the code to a file
def append_gtag_code(file_path):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(gtag_code)
        print(f"Appended gtag code to {file_path}")
    except Exception as e:
        print(f"Failed to append gtag code to {file_path}: {e}")

# Walk through the directory and process each file
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        if not contains_gtag_code(file_path):
            append_gtag_code(file_path)
        else:
            print(f"Skipped {file_path}, already contains gtag code")
