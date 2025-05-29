#!/usr/bin/env python3
r"""
Script to (re)generate LaTeX labels for sections, subsections and subsubsections.

- **Removes** any existing labels matching our generated prefixes (sec:, subsec:, subsubsec:).
- **Generates** fresh labels based on the heading text:
  - \label{sec:<slug>} after each \section{...}
  - \label{subsec:<slug>} after each \subsection{...}
  - \label{subsubsec:<subsec-slug>:<subsubsec-slug>} after each \subsubsection{...}

Leaves any other \label (e.g., for figures, tables) untouched.

Usage:
    python add_labels.py input.tex output.tex
"""
import re
import argparse


def slugify(text):
    """Convert text to a lowercase slug with hyphens."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text.strip())


def process_lines(lines):
    new_lines = []
    current_subsec = None
    i = 0
    n = len(lines)

    # Regex to detect old sectioning labels only
    old_label_re = re.compile(r"^\s*\\label\s*\{(?:sec|subsec|subsubsec|app):.*\}")

    while i < n:
        line = lines[i]

        # Remove any old generated sectioning labels
        if old_label_re.match(line):
            i += 1
            continue

        # SECTION
        m_sec = re.match(r"^(\s*)\\section\{(.+?)\}", line)
        if m_sec:
            indent, title = m_sec.groups()
            slug = slugify(title)
            # keep original line (with newline)
            new_lines.append(f"{indent}\\section{{{title}}}\\label{{sec:{slug}}}\n")
            current_subsec = None
            i += 1
            continue

        # SUBSECTION
        m_sub = re.match(r"^(\s*)\\subsection\{(.+?)\}", line)
        if m_sub:
            indent, title = m_sub.groups()
            slug = slugify(title)
            new_lines.append(f"{indent}\\subsection{{{title}}}\\label{{subsec:{slug}}}\n")
            current_subsec = slug
            i += 1
            continue

        # SUBSUBSECTION
        m_ssub = re.match(r"^(\s*)\\subsubsection\{(.+?)\}", line)
        if m_ssub:
            indent, title = m_ssub.groups()
            slug2 = slugify(title)
            full = f"{current_subsec}:{slug2}" if current_subsec else slug2
            new_lines.append(f"{indent}\\subsubsection{{{title}}}\\label{{subsubsec:{full}}}\n")
            i += 1
            continue

        # default: keep everything else (including figure/table labels)
        new_lines.append(line)
        i += 1

    return new_lines


def main():
    parser = argparse.ArgumentParser(description="Re-add LaTeX sectioning labels, removing old ones.")
    parser.add_argument('input', help='Input .tex file')
    parser.add_argument('output', help='Output .tex file')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        lines = f.readlines()

    new_lines = process_lines(lines)

    with open(args.output, 'w') as f:
        f.writelines(new_lines)
    print(f"Processed labels written to {args.output}")


if __name__ == '__main__':
    main()
