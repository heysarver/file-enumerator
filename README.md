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
With pbcopy
```bash
$ python file_enumerator.py ~/workspace/path/to/copy | pbcopy
```
To a file
```bash
$ python file_enumerator.py ~/workspace/path/to/copy > code.txt
```
