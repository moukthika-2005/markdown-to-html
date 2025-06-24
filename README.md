# Markdown to HTML Converter
A simple Python command-line tool that converts `.md` (Markdown) files into clean `.html` files.
It supports standard Markdown syntax, including:
- Headings (#, ##, etc.)
- Bold and italics
- Lists
- Links
- Code blocks with syntax highlighting (like python, java, etc.)

## How to run
**1. Install dependencies**
Make sure Python is installed (Python 3.6+ recommended).Then install required packages:

```bash
pip install -r requirements.txt
```

**2. To convert a markdown file to HTML file**
```bash
python src/converter.py <input.md> <output.html>
```
**3. Example**
```bash
python src/converter.py samples/sample.md samples/sample.html
```
Here my input.md is `sample.md` which is in samples folder and `sample.html` is the output which is generated after running above command
