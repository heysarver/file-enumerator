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

Create a virtual environment, unless installing on host.

```bash
$ python -m venv venv && source venv/bin/activate
```

Install requirements

```bash
$ pip install -r requirements.txt
```

Run

```bash
$ python file_enumerator.py ~/workspace/path/to/copy
```

## Installation

1. Install the necessary requirements and python libraries as noted above.
2. Alias the script. This can be added to your ~/.bashrc or ~/.zshrc file.

```bash
$ alias file_enum='python /path/to/file_enumerator.py'
```
