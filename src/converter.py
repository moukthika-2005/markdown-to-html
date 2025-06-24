import markdown2
import argparse
import html
import re

def preprocess_code_blocks(text):
    def replacer(match):
        lang = match.group(1)
        code = match.group(2)
        escaped_code = html.escape(code)
        return f'<pre><code class="language-{lang}">{escaped_code}</code></pre>'

    return re.sub(r'```(\w+)\n(.*?)```', replacer, text, flags=re.DOTALL)


def convert_markdown_to_html(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            text = md_file.read()

            # Step 1: Preprocess code blocks with language
            text = preprocess_code_blocks(text)

            # Step 2: Convert Markdown (disable fenced-code-blocks since we handled it)
            html_content = markdown2.markdown(text, extras=['tables'])
            # Step 3: Escape HTML entities
            html_content = html.unescape(html_content)
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print(f"Conversion successful! HTML saved to: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML.")
    parser.add_argument("input", help="Input .md file path")
    parser.add_argument("output", help="Output .html file path")
    args = parser.parse_args()

    convert_markdown_to_html(args.input, args.output)

if __name__ == "__main__":
    main()
