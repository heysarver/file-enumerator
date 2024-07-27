# /file_enumerator.py

import os
import argparse
import fnmatch
import magic

def load_ignore_patterns(directory):
    ignore_patterns = []
    ignore_files = ['.gitignore', '.dockerignore']
    
    for ignore_file in ignore_files:
        ignore_path = os.path.join(directory, ignore_file)
        if os.path.exists(ignore_path):
            with open(ignore_path, 'r') as f:
                ignore_patterns.extend(line.strip() for line in f if line.strip() and not line.startswith('#'))
    
    # Add pattern to ignore .git directory
    ignore_patterns.append('.git/')
    
    return ignore_patterns

def should_ignore(path, base_path, ignore_patterns):
    rel_path = os.path.relpath(path, base_path)
    
    # Ignore .git directory and its contents
    if '.git' in rel_path.split(os.sep):
        return True
    
    for pattern in ignore_patterns:
        if pattern.endswith('/'):
            if fnmatch.fnmatch(rel_path + '/', pattern) or fnmatch.fnmatch(os.path.dirname(rel_path) + '/', pattern):
                return True
        elif fnmatch.fnmatch(rel_path, pattern):
            return True
    return False

def is_text_file(file_path):
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    return file_type.startswith('text/')

def enumerate_files(directory):
    ignore_patterns = load_ignore_patterns(directory)
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), directory, ignore_patterns)]
        
        for file in files:
            file_path = os.path.join(root, file)
            if not should_ignore(file_path, directory, ignore_patterns):
                if is_text_file(file_path):
                    relative_path = os.path.relpath(file_path, directory)
                    print(f"File: {relative_path}")
                    print("-" * 40)
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            print(f.read())
                    except Exception as e:
                        print(f"Error reading file: {e}")
                    
                    print("-" * 40)
                    print("-" * 40)
                    print()

def main():
    parser = argparse.ArgumentParser(description="Directory File Enumerator with Ignore Support")
    parser.add_argument("directory", help="Path to the directory to enumerate")
    args = parser.parse_args()

    directory = os.path.abspath(args.directory)
    
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        return

    enumerate_files(directory)

if __name__ == "__main__":
    main()
