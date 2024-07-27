# file-enumerator

Copy code in a folder for use with LLMs.

Aims to honor .gitignore and .dockerignore files and ignore all dev and non-text files.

## Requirements
- libmagic
  ```bash
  # macOS
  $ brew install libmagic
  ```

## Usage
Create a venv
```bash
$ python -m venv venv && source venv/bin/activate
````

Run with pbcopy
```bash
$ python file_enumerator.py ~/workspace/path/to/copy | pbcopy
```

Output to a file
```bash
$ python file_enumerator.py ~/workspace/path/to/copy > code.txt
```
