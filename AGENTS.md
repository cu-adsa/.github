# AGENTS.md — Developer & AI Agent Guidelines

Welcome to the **cu-adsa** (Chandigarh University — Advanced Data Structures & Algorithms) repository. This document establishes guidelines, architectural principles, pedagogical standards, and workflows for human contributors and AI coding agents operating on this codebase.

---

## 1. Repository Overview & Mission

The `cu-adsa/.github` repository serves as the central curriculum, documentation, and reference hub for the Advanced Data Structures & Algorithms course. It provides:
- **Theory Lecture Notes**: 45 structured lectures across 3 units paired with compiled PDF deliverables.
- **Practical Lab Experiments**: 15 lab experiments mapped directly to canonical LeetCode problems.
- **Self-Study Modules**: 3 unit-level modules covering advanced algorithmic and analytical topics.
- **Python Reference Implementations**: High-performance, pure Python 3 reference implementations.
- **Presentation Assets**: Complete slide decks for lectures, lab experiments, and self-study modules.
- **Curriculum Alignment**: Strict mapping with Bloom's Taxonomy (BT1–BT6) and Course Outcomes (CO1–CO5).

### Authoritative Reference Textbooks
All theoretical formulations, pseudocode conventions, and asymptotic notations must adhere to the following course references:
1. **[T1] Cormen, Leiserson, Rivest, Stein (CLRS)** — *Introduction to Algorithms* (4th Ed, MIT Press, 2022).
2. **[T2] Antti Laaksonen** — *Guide to Competitive Programming* (3rd Ed, Springer, 2024).
3. **[T3] Steven S. Skiena** — *The Algorithm Design Manual* (3rd Ed, Springer, 2020).
4. **[R1] Halim, Halim, Effendy** — *Competitive Programming 4* (4th Ed, Lulu, 2020).

---

## 2. Directory Architecture

```
cu-adsa/
├── .github/
│   ├── lectures/
│   │   ├── theory/          # 45 Theory lecture notes (<Unit>.<Chapter>.<Lecture>.md + .pdf)
│   │   ├── practical/       # 15 Lab experiments mapped to LeetCode (<id>.md + .pdf)
│   │   └── self-study/      # 3 Autonomous study modules (<Unit>.md + .pdf)
│   ├── presentations/       # Slide decks (.pptx)
│   │   ├── Lecture/         # Lecture presentations (Lecture_01 through Lecture_12)
│   │   ├── Experiments/     # Lab presentations (Exp01 through Exp10)
│   │   └── self-study/      # Self-study slide decks
│   ├── solutions/           # Standalone Python solutions for practicals (<LC#>.py)
│   ├── syllabus/            # Official course syllabus (adsa.md + adsa.pdf)
│   ├── profile/             # GitHub Organization profile (README.md)
│   ├── main.py              # Automated markdown-to-pdf compilation script
│   ├── pyproject.toml       # Python project configuration (uv-managed)
│   ├── uv.lock              # Lockfile for reproducible dependencies
│   ├── README.md            # Repository overview & quick links
│   └── AGENTS.md            # Agent instructions and repository handbook (this file)
└── AGENTS.md                # Mirrored workspace-level agent guidelines
```

---

## 3. Curriculum Structure & Taxonomy Alignment

### 3.1 Course Outcomes (COs)
- **CO1**: Understand and analyze the performance of algorithms using asymptotic notations and time-space tradeoffs.
- **CO2**: Apply linear and non-linear data structures (arrays, linked lists, stacks, queues, trees, graphs) to solve computing problems.
- **CO3**: Design and analyze efficient algorithms for searching, sorting, and optimization paradigms.
- **CO4**: Formulate algorithmic solutions for advanced data engineering challenges including indexing, hashing, and shortest paths.
- **CO5**: Evaluate trade-offs between competing data structures and algorithmic designs for real-world system constraints.

### 3.2 45 Theory Lecture Curriculum Map

#### Unit 1 — Fundamentals of Data Structures & Sorting (15 Lectures)
* **Chapter 1.1: Fundamentals of Data Structures & Arrays**
  * `1.1.1.md` (L1): Concept of data, information, and introduction to data structures `[BT4, CO1]`
  * `1.1.2.md` (L2): Algorithm complexity — time and space; time-space tradeoff `[BT4, CO1]`
  * `1.1.3.md` (L3): Asymptotic notations — Big-O, Big-$\Omega$, Big-$\Theta$ with examples `[BT4, CO1]`
  * `1.1.4.md` (L4): Linear arrays — representation and traversal `[BT4, CO1, CO2]`
  * `1.1.5.md` (L5): Insertion and deletion in arrays `[BT3, CO2]`
  * `1.1.6.md` (L6): Searching — linear search and binary search with complexity analysis `[BT4, CO1, CO5]`
* **Chapter 1.2: Sorting Techniques**
  * `1.2.1.md` (L7): Introduction to sorting; analysis of basic sorting techniques `[BT4, CO1, CO5]`
  * `1.2.2.md` (L8): Bubble sort — algorithm and complexity analysis `[BT4, CO1, CO5]`
  * `1.2.3.md` (L9): Quick sort — algorithm and complexity analysis `[BT4, CO1, CO5]`
  * `1.2.4.md` (L10): Merge sort — merging arrays and complexity analysis `[BT4, CO1, CO5]`
  * `1.2.5.md` (L11): Multi-dimensional arrays — representation and applications `[BT3, CO2]`
  * `1.2.6.md` (L12): Recap and comparative analysis of sorting techniques `[BT4, CO1, CO5]`
* **Chapter 1.3: Pointers, Records & Advanced Arrays**
  * `1.3.1.md` (L13): Pointers and pointer arrays `[BT3, CO2]`
  * `1.3.2.md` (L14): Records — structure and memory representation; parallel arrays `[BT3, CO2]`
  * `1.3.3.md` (L15): Sparse matrices — representation and storage techniques `[BT3, CO2, CO4]`

#### Unit 2 — Linked Lists, Stacks & Queues (14 Lectures)
* **Chapter 2.1: Linked Lists**
  * `2.1.1.md` (L16): Linear linked list — representation in memory `[BT3, CO2]`
  * `2.1.2.md` (L17): Traversal and searching in a linked list `[BT3, CO2, CO5]`
  * `2.1.3.md` (L18): Insertion and deletion in a linked list `[BT3, CO2]`
  * `2.1.4.md` (L19): Header linked list and doubly linked list `[BT3, CO2]`
  * `2.1.5.md` (L20): Circular linked list and circular doubly linked list `[BT3, CO2]`
  * `2.1.6.md` (L21): Operations on doubly linked list; complexity analysis and applications `[BT4, CO1, CO2]`
* **Chapter 2.2: Stacks & Recursion**
  * `2.2.1.md` (L22): Stack — basic terminology, sequential and linked representations `[BT3, CO2]`
  * `2.2.2.md` (L23): Stack operations — PUSH & POP; parenthesis matching `[BT5, CO2, CO3]`
  * `2.2.3.md` (L24): Evaluation of postfix expressions `[BT5, CO2, CO3]`
  * `2.2.4.md` (L25): Infix to postfix conversion `[BT5, CO3]`
  * `2.2.5.md` (L26): Recursion — principles, importance, and implementation `[BT5, CO2, CO3]`
* **Chapter 2.3: Queues**
  * `2.3.1.md` (L27): Queues — introduction and operations `[BT3, CO2]`
  * `2.3.2.md` (L28): Double ended queue (Deque) `[BT3, CO2]`
  * `2.3.3.md` (L29): Priority queue — concept and applications `[BT3, CO2, CO4]`

#### Unit 3 — Graphs, Trees, Hashing & File Organization (16 Lectures)
* **Chapter 3.1: Graphs & Binary Trees**
  * `3.1.1.md` (L30): Graph theory — terminology, adjacency matrix, path matrix `[BT3, CO2]`
  * `3.1.2.md` (L31): Graph traversal — BFS `[BT5, CO2, CO3]`
  * `3.1.3.md` (L32): Graph traversal — DFS and comparison with BFS `[BT5, CO2, CO3, CO5]`
  * `3.1.4.md` (L33): Binary trees — terminology, representation in memory `[BT3, CO2]`
  * `3.1.5.md` (L34): Binary tree traversal algorithms (using stacks) `[BT5, CO2, CO3]`
  * `3.1.6.md` (L35): Shortest path — Dijkstra's Algorithm `[BT5, CO3, CO4]`
* **Chapter 3.2: Binary Search Trees & Advanced Trees**
  * `3.2.1.md` (L36): Shortest path — Bellman-Ford Algorithm `[BT5, CO3, CO4]`
  * `3.2.2.md` (L37): Binary search trees — search, insert, and delete `[BT6, CO2, CO4]`
  * `3.2.3.md` (L38): AVL search trees — rotations and balancing `[BT6, CO2, CO4]`
  * `3.2.4.md` (L39): B-Trees — structure and operations `[BT6, CO2, CO4]`
  * `3.2.5.md` (L40): Heaps — min-heap, max-heap `[BT5, CO2, CO3]`
  * `3.2.6.md` (L41): Heap sort and comparative analysis of tree structures `[BT5, CO3, CO5]`
* **Chapter 3.3: Hashing & File Organization**
  * `3.3.1.md` (L42): Hash tables and hash functions `[BT3, CO2]`
  * `3.3.2.md` (L43): Collision resolution strategies (chaining, linear probing) `[BT5, CO2, CO3]`
  * `3.3.3.md` (L44): File organization — sequential, relative, index sequential, inverted file `[BT6, CO2, CO4]`
  * `3.3.4.md` (L45): Recap — designing efficient data systems (real-world applications) `[BT6, CO4, CO5]`

---

### 3.3 15 Practical Experiments Map

| Exp # | Experiment Title | Target Problem | CO Mapping | BT Level |
| :---: | :--- | :--- | :---: | :---: |
| **E1** | Search in Rotated Sorted Array | [LeetCode #33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | CO1, CO5 | BT4 |
| **E2** | Sort an Array (Merge / Quick Sort) | [LeetCode #912](https://leetcode.com/problems/sort-an-array/) | CO1, CO5 | BT4 |
| **E3** | Group Anagrams (Hashing & Bucketing) | [LeetCode #49](https://leetcode.com/problems/group-anagrams/) | CO2, CO3 | BT5 |
| **E4** | Kth Largest Element in an Array (Quickselect) | [LeetCode #215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | CO3, CO5 | BT5 |
| **E5** | Swap Nodes in Pairs (Linked List) | [LeetCode #24](https://leetcode.com/problems/swap-nodes-in-pairs/) | CO2 | BT3 |
| **E6** | Evaluate Reverse Polish Notation (Stack) | [LeetCode #150](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | CO2, CO3 | BT5 |
| **E7** | Number of Islands (BFS & DFS Graph Traversal) | [LeetCode #200](https://leetcode.com/problems/number-of-islands/) | CO2, CO3 | BT5 |
| **E8** | Network Delay Time (Dijkstra's Algorithm) | [LeetCode #743](https://leetcode.com/problems/network-delay-time/) | CO3, CO4 | BT5 |
| **E9** | Non-overlapping Intervals (Greedy Scheduling) | [LeetCode #435](https://leetcode.com/problems/non-overlapping-intervals/) | CO3, CO4 | BT5 |
| **E10** | Course Schedule (Topological Sorting) | [LeetCode #207](https://leetcode.com/problems/course-schedule/) | CO3, CO4 | BT5 |
| **E11** | Maximum Depth of Binary Tree (Tree Traversal) | [LeetCode #104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | CO2, CO3 | BT5 |
| **E12** | Number of Islands (Disjoint Set Union / Find) | [LeetCode #200](https://leetcode.com/problems/number-of-islands/) | CO2, CO3 | BT5 |
| **E13** | Binary Tree Level Order Traversal (BFS Queue) | [LeetCode #102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | CO2, CO3 | BT5 |
| **E14** | Valid Anagram (Hash Frequency Counter) | [LeetCode #242](https://leetcode.com/problems/valid-anagram/) | CO2, CO3 | BT5 |
| **E15** | Combination Sum (Backtracking & Pruning) | [LeetCode #39](https://leetcode.com/problems/combination-sum/) | CO3, CO4 | BT5 |

---

### 3.4 Self-Study Curriculum Modules

- **Unit 1 (`lectures/self-study/1.md`)**:
  - Amortized Analysis (Aggregate, Accounting/Banker's, Potential Method).
  - Advanced Recurrences (Master Theorem cases, Akra-Bazzi method intuition).
  - Advanced Balanced Trees: Threaded Binary Trees, Red-Black Trees, B-Trees & B+ Trees, Splay Trees, Huffman Encoding, Decision Trees.
  - Space-Time Tradeoffs.
- **Unit 2 (`lectures/self-study/2.md`)**:
  - In-Depth Graph Algorithms: Topological Sorting (Kahn's and Tarjan's), Strongly Connected Components (Kosaraju & Tarjan), Floyd-Warshall All-Pairs Shortest Path, Ford-Fulkerson Network Flow, Advanced Graph Coloring.
  - Advanced Hashing: Perfect Hashing, Double Hashing, Extendible Hashing.
  - Database Indexing: File Indexing, B+ Tree Indexing in Production Relational Engines.
- **Unit 3 (`lectures/self-study/3.md`)**:
  - Algorithmic Paradigms & Advanced Analysis: Randomized Algorithms, Karatsuba Fast Multiplication, Closest Pair Problem (Divide & Conquer).
  - Paradigms Comparative Analysis: Backtracking vs. Divide & Conquer, Greedy vs. Dynamic Programming.
  - Advanced Optimization: 0/1 Knapsack (DP), Disjoint Set Union (Union by Rank & Path Compression), Approximation Algorithms, Branch and Bound.

---

## 4. Pedagogical & Markdown Standards for Theory Notes

Every lecture note in `lectures/theory/` represents an official university study document. All edits or new notes must strictly follow the standard structure below:

### 4.1 Metadata Header
Each file must open with an H1 title and exact curriculum metadata:
```markdown
# L<Lecture_Number> — <Topic Title>

**Unit:** <Unit_Number> | **Chapter:** <Chapter_Name> | **BT Level:** BT<1-6> | **CO:** CO<1-5>

---
```

### 4.2 Required Sections (Strict Order)
1. **Learning Objectives**: 3–5 bullet points using Bloom's action verbs (*Formulate, Implement, Analyze, Evaluate, Construct*).
2. **Conceptual Motivation**: Why does this topic exist? The concrete engineering bottleneck or mathematical limitation it resolves.
3. **Core Theory & Mathematical Formulation**:
   - Precise definitions and mathematical formulas formatted in LaTeX (`$$...$$` and `$..$`).
   - Synonyms, literature contradictions, and conceptual models (e.g., Open Addressing ≡ Closed Hashing).
4. **Step-by-Step Visual Traces**:
   - Structured ASCII diagrams, tables, or trace matrices demonstrating state transitions for concrete input keys.
5. **Python Reference Implementations**:
   - Production-quality, self-contained Python 3 code with complete type annotations and defensive guards.
6. **Complexity & Performance Analysis**:
   - Asymptotic analysis: Best, Average, and Worst-case time, plus Auxiliary Space.
   - Load factor ($\alpha$) formulas and derivations where applicable.
7. **Comparative Matrix**:
   - Clean Markdown tables comparing alternative algorithms/structures across time, space, and hardware locality.
8. **Real-World & Language Realities**:
   - How major production runtimes (CPython, Java HotSpot JVM, C++ libc++/libstdc++, Go runtime, Rust std) implement the concept.
9. **Common Traps & Exam / Interview Gotchas**:
   - Edge cases, recurring student misconceptions, and tricky interview pitfalls.
10. **Summary & Takeaways**:
    - Bulleted synthesis of key architectural insights.
11. **References**:
    - Citations mapped to course textbooks (CLRS, Skiena, Laaksonen).

---

## 5. Practical Lab Notes & Solutions Specification

### 5.1 Lab Notes Format (`lectures/practical/<id>.md`)
- **Metadata**: Experiment number, LeetCode problem link, Course Outcomes, Bloom's level.
- **Problem Statement**: Complete description with formal constraints and boundary inputs.
- **Algorithmic Strategies**:
  - Comparison of naive/brute-force approach vs. optimal approach.
  - Step-by-step logic and invariants.
- **ASCII Visual Traces**: Trace matrices, array pointers, or tree state diagrams.
- **Python Implementation**: Complete solution matching LeetCode signatures with full type annotations.
- **Complexity Breakdown**: Detailed analysis of time complexity and auxiliary space.

### 5.2 Standalone Python Solutions (`solutions/<LC#>.py`)
- **File Naming**: Named strictly by LeetCode problem number (e.g., `33.py`, `217.py`, `496.py`).
- **Standard Signature**: Encapsulated within `class Solution:` matching official LeetCode method names.
- **Zero Third-Party Imports**: Use only standard library modules (e.g., `collections.deque`, `heapq`, `math`).
- **Quality**: Clean, idiomatic Python with descriptive variable names and defensive handling.

---

## 6. Code Quality & Implementation Standards

When authoring Python implementations anywhere in the repository:
- **Target Version**: Python 3.12+ (idiomatic type hinting `list[int]`, pattern matching `match/case`).
- **Zero Third-Party Dependencies**: All data structures must be authored from scratch or use Python standard library modules (`collections`, `heapq`, `dataclasses`, `typing`).
- **Sentinel Object Pattern**: In open addressing or linked structures, never use `None` to denote deleted items. Use explicit sentinels:
  ```python
  DELETED = object()
  ```
- **Defensive Boundary Guards**:
  - Validate non-empty collections before access.
  - Guard against division by zero in hashing modulus operations ($m > 0$).
  - For secondary hash functions, ensure probe steps are strictly coprime to table size ($h_2(k) > 0$ and $\gcd(step, m) = 1$).
  - Guard against infinite loops during open addressing probing cycles.
- **Runnable & Tested**: Code blocks must be free of syntax errors and runnable out-of-the-box.

---

## 7. Build System & Toolchain

The repository relies on **`uv`** as its fast Python package and environment manager.

### 7.1 Environment Setup
```bash
# In the .github directory:
uv sync
```

### 7.2 Compiling Markdown to PDF
Synchronized PDF copies of all lecture notes, lab experiments, self-study modules, and the syllabus are maintained alongside their `.md` sources.

```bash
# Batch compile all curriculum markdown files to PDF:
uv run python main.py

# Compile an individual theory lecture:
uv run python -c "from pathlib import Path; from main import convert_md_to_pdf; convert_md_to_pdf(Path('lectures/theory/3.3.2.md').resolve())"

# Compile an individual practical experiment:
uv run python -c "from pathlib import Path; from main import convert_md_to_pdf; convert_md_to_pdf(Path('lectures/practical/1.md').resolve())"
```

### 7.3 PDF Formatting Constraints (`markdown-pdf`)
The build pipeline utilizes `markdown-pdf` (`MarkdownPdf`, `Section`, `toc_level=2`). To ensure clean compilation without formatting errors:
- **No Complex Raw HTML**: Avoid `<div>`, `<span>`, `<details>`, flexbox, or raw CSS inline styles.
- **GitHub Flavored Markdown Tables**: Standard pipes and hyphens format cleanly into PDF tables.
- **Fenced Code Blocks**: Use standard triple backticks with explicit language indicators (`python`, `text`, `bash`).
- **LaTeX Math Equations**: Provide clear textual formulas or descriptions alongside `$$...$$` blocks to maintain readability across PDF renders.
- **Exclusions**: `main.py` explicitly excludes `README.md`, `agents.md`, `.venv`, and `profile/` from conversion.

---

## 8. Repository Integrity & Link Preservation

- **Curated Cross-Links**: `profile/README.md` and `syllabus/adsa.md` contain curated links to lectures, solutions, and lab experiments. Never delete or rename files without updating corresponding links.
- **Naming Conventions**:
  - Theory: `lectures/theory/<Unit>.<Chapter>.<Lecture>.md` (e.g., `1.1.1.md`, `3.3.2.md`)
  - Practical: `lectures/practical/<Exp_Number>.md` (e.g., `1.md`, `15.md`)
  - Self-Study: `lectures/self-study/<Unit_Number>.md` (e.g., `1.md`, `3.md`)
  - Solutions: `solutions/<LeetCode_Problem_Number>.py` (e.g., `33.py`, `200.py`)
- **PDF Pairing Invariant**: Whenever a `.md` lecture note or syllabus is modified, recompile the corresponding `.pdf` file to keep the deliverables synchronized.

---

## 9. AI Agent Operating Rules & Behavioral Invariants

1. **Verify Before Editing**: Read existing notes within the same chapter or unit before introducing new content to maintain pedagogical continuity and notation consistency.
2. **Pedagogical Rigor**: Never abbreviate, trivialize, or generate surface-level lecture notes. Maintain full mathematical derivations, ASCII visual traces, and production-grade implementations.
3. **No Destructive Operations**: Never run commands that overwrite uncommitted git state or delete lecture directories.
4. **Preserve Synchronized Pairs**: Always verify both the Markdown note and its companion PDF exist and are up to date.
