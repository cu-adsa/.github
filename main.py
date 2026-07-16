from pathlib import Path
from markdown_pdf import MarkdownPdf, Section


def convert_md_to_pdf(md_path: Path) -> None:
    pdf_path = md_path.with_suffix(".pdf")
    content = md_path.read_text(encoding="utf-8")

    pdf = MarkdownPdf(toc_level=2)
    pdf.add_section(Section(content, root=str(md_path.parent)))
    pdf.meta["title"] = md_path.stem
    pdf.save(str(pdf_path))

    print(f"  Created: {pdf_path.relative_to(Path.cwd())}")


def main():
    root = Path(__file__).parent
    excluded_parts = {"profile", ".venv"}
    md_files = [
        p
        for p in root.rglob("*.md")
        if p.stat().st_size > 0
        and p.name.lower() != "readme.md"
        and not any(part in excluded_parts for part in p.parts)
    ]

    if not md_files:
        print("No .md files found.")
        return

    print(f"Found {len(md_files)} markdown file(s). Converting...\n")
    errors = []

    for md_file in sorted(md_files):
        try:
            convert_md_to_pdf(md_file)
        except Exception as exc:
            errors.append((md_file, exc))
            print(f"  ERROR: {md_file.relative_to(root)} — {exc}")

    print(f"\nDone. {len(md_files) - len(errors)} converted, {len(errors)} failed.")


if __name__ == "__main__":
    main()
