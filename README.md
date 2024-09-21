# file-enumerator

Copy code in a folder for use with LLMs.

Aims to honor .gitignore and .dockerignore files and ignore all dev and non-text files.

Perfect for use with pbcopy or outputting to a text file.

## Requirements

- libmagic

  ### macOS
  ```bash
  $ brew install libmagic
  ```

  ### Linux (Debian/Ubuntu)
  ```bash
  $ sudo apt-get install libmagic1
  ```

  ### Windows
  On Windows, you can install the `python-magic-bin` package which includes the necessary binaries.

  ```bash
  $ pip install python-magic-bin
  ```

## Usage

Create a virtual environment, unless installing on host.

### macOS/Linux
```bash
$ python3 -m venv venv && source venv/bin/activate
```

### Windows
```bash
$ python -m venv venv && .\venv\Scripts\activate
```

Install requirements

```bash
$ pip install -r requirements.txt
```

Run.  On macOS this works great in combination with <code>pbcopy</code>

```bash
# macOS/Linux
$ python file_enumerator.py ~/workspace/path/to/copy

# Windows
$ python file_enumerator.py C:\path\to\copy
```

If you do not provide a path to copy, the current directory will be used.

## Installation

1. Install the necessary requirements and python libraries as noted above.
2. Alias the script. This can be added to your ~/.bashrc or ~/.zshrc file on macOS/Linux, or set up as a function in PowerShell on Windows.

### macOS/Linux
```bash
$ alias file_enum='python /path/to/file_enumerator.py'
```

### Windows (PowerShell)
```powershell
function file_enum {
    python C:\path\to\file_enumerator.py $args
}
```
