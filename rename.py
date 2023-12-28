"""
                            BISMILLAHIRRAHMANIRRAHIM

                        FREE PALESTINE  &&  TERRORIST ISRAEL

"""







import re
import os

def check_and_rename_for_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            check_and_rename(file_path)


def check_and_rename(file_path):
    try:
        new_extension = ""
        with open(file_path, 'r') as file:
            content = file.read()
            jsx_pattern = re.compile(r'<[a-zA-Z0-9_]+\s*[^>]*>\s*(<\/[a-zA-Z0-9_]+>)?')
            if jsx_pattern.search(content):
                original_extension = os.path.splitext(file_path)[1]
                new_extension = '.tsx' if original_extension == '.ts' else '.jsx'
            else:
                print(f"File {file_path} does not contain JSX code.")
                return
        new_file_path = os.path.splitext(file_path)[0] + new_extension
        os.rename(file_path, new_file_path)
        print(f"File extension changed to {new_extension} for file: {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"---------------Error processing file: {file_path}")

# Replace 'your_folder_path' with the actual path to your folder
check_and_rename_for_folder(r'your_folder_path')

