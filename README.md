# ADSA Repository

This repository contains the course materials, lecture notes, practical problems, and supporting scripts for the Advanced Data Structures & Algorithms (ADSA) syllabus.

## What’s inside

- [📚 Course overview and study plan](profile/README.md)
- [📖 Syllabus](syllabus/adsa.md)
- [🧪 Practical experiments and problem notes](lectures/practical)
- [📘 Theory lectures](lectures/theory)
- [💡 Python solutions](solutions)
- [🧰 PDF generation script](main.py)

## Quick start

To generate PDFs for the markdown lecture notes locally:

1. Install [uv](https://docs.astral.sh/uv/) if you do not already have it.
2. From the repository root, run:
   ```bash
   uv sync
   uv run python main.py
   ```
3. Generated PDFs will appear next to their corresponding markdown files.

## Practice Problems by Topic

Curated LeetCode problems for the major DSA topics in this repository are now grouped by topic and ordered from Easy to Hard.

- [Binary Search](profile/README.md#binary-search)
- [Sorting & Divide & Conquer](profile/README.md#sorting--divide--conquer)
- [Linked Lists](profile/README.md#linked-lists)
- [Stacks & Recursion](profile/README.md#stacks--recursion)
- [Queues & Priority Queues](profile/README.md#queues--priority-queues)
- [Graphs & BFS/DFS](profile/README.md#graphs--bfsdfs)
- [Trees & Binary Trees](profile/README.md#trees--binary-trees)
- [Binary Search Trees & Heaps](profile/README.md#binary-search-trees--heaps)
- [Hashing](profile/README.md#hashing)
- [Backtracking](profile/README.md#backtracking)

For the full tables and official problem links, see [profile/README.md](profile/README.md) and [syllabus/adsa.md](syllabus/adsa.md).

## Repository structure

```text
.
├── .github/workflows/   # CI workflow for PDF generation
├── lectures/            # Theory and practical lecture notes
├── presentations/       # Slides and presentation files
├── profile/             # Course landing page and overview
├── solutions/           # Python solutions to selected problems
├── syllabus/            # Main syllabus content
└── main.py              # Markdown-to-PDF generator
```

## Contributing

Contributions are welcome. If you want to improve the content or tooling:

- fix typos or broken links
- add missing practice resources
- improve documentation
- enhance the PDF generation workflow

Please keep changes focused and easy to review.

## Helpful links

- [🛠️ Python DSA Templates](https://github.com/dheereshag/python-dsa-templates)
- [📚 Course Main README](profile/README.md)