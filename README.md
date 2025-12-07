# Custom CSV Reader & Writer

## Overview
This project implements a custom CSV reader and writer in pure Python (no use of the built-in `csv` module inside the implementation).  
The goal is to build a robust parser that:

- Handles quoted fields  
- Escapes embedded quotes (`""`)  
- Supports embedded newlines inside fields  
- Streams rows without loading the entire file into memory  
- Produces CSV output readable by standard CSV readers  

The repository includes:
- `custom_csv_reader.py` — Custom streaming CSV reader  
- `custom_csv_writer.py` — Custom CSV writer with proper quoting rules  
- `benchmark.py` — Generates a dataset and compares performance with Python’s built-in `csv` module  
- `generate_synthetic.py` — Creates synthetic CSV data with edge cases  
- `requirements.txt` — Dependency list (empty for this pure-Python project)

---

## Setup

Requires **Python 3.8+**.

### 1. Clone the repository
```bash
git clone <repo-url>
cd Custom-CSV-Parser-from-Scratch-in-Python
````

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.\.venv\Scripts\activate    # Windows
```

### 3. Install dependencies

(No external libraries required.)

```bash
pip install -r requirements.txt
```

---

## Usage Examples

### Reading CSV using CustomCsvReader

```python
from custom_csv_reader import CustomCsvReader

with CustomCsvReader("input.csv") as reader:
    for row in reader:
        print(row)
```

### Writing CSV using CustomCsvWriter

```python
from custom_csv_writer import CustomCsvWriter

rows = [
    ["hello", "world,with,commas", "text \"quoted\""],
    ["line1\nline2", "value", "test"]
]

with CustomCsvWriter("out.csv") as writer:
    writer.write_rows(rows)
```

---

## Conclusion

This project successfully implements a CSV reader and writer from scratch using pure Python.
It fulfills all functional requirements and demonstrates:

* correct handling of complex CSV cases
* proper escaping of quotes
* support for embedded newlines
* streaming row-by-row parsing
* clean design using Python classes and context managers

The provided implementation offers a clear look into how CSV parsing works internally, without relying on Python’s built-in `csv` module.

```