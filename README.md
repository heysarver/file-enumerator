# file-enumerator

Copy code in a folder for use with LLMs.

Aims to honor .gitignore and .dockerignore files and ignore all dev and non-text files.

Perfect for use with pbcopy or outputting to a text file.

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

Run
```bash
$ python file_enumerator.py ~/workspace/path/to/copy
```
