import os
import zipfile

zip_filename = 'Union-Foods-Website.zip'
base_dir = r'C:\Users\ASUS\.gemini\antigravity\scratch\union_foods_website'

# Exclude temporary script files or backups from user zip
exclude_files = {
    'Union-Foods-Website.zip', 'index.html.bak', 'update_index.py',
    'append_css.py', 'update_script_js.py', 'verify_live.py',
    'test_search.js', 'test.py', 'verify.py', 'create_assets.py',
    'generate_more_assets.py', 'build_zip.py'
}

with zipfile.ZipFile(os.path.join(base_dir, zip_filename), 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        # Ignore pycache or hidden dirs
        if '__pycache__' in root or '.git' in root:
            continue
        for file in files:
            if file in exclude_files or file.endswith('.pyc') or file.endswith('.bak'):
                continue
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, base_dir)
            zipf.write(abs_path, rel_path)
            print(f'Added: {rel_path}')

print(f'Successfully built {zip_filename}!')
file_size_kb = os.path.getsize(os.path.join(base_dir, zip_filename)) / 1024
print(f'Archive Size: {file_size_kb:.1f} KB')
