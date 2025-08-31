# Simple JSON Parser

This project aims to implement a simple JSON parser in Python, following the specifications defined at [https://www.json.org/json-en.html](https://www.json.org/json-en.html).

## Features

- Parses JSON strings into Python data structures (dict for objects, list for arrays, str for strings, int/float for numbers, bool for booleans, None for null)
- Handles objects, arrays, strings, numbers, booleans, and null

## Usage

```python
from json_parser import parse_json

# Parse JSON string
json_str = '{"name": "test", "values": [1, 2, 3]}'
result = parse_json(json_str)
```

## Testing

Run the tests using:
```bash
# Add the project root to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Run tests with pytest from tests dir
# For Linux/macOS:
pytest test_json_parser.py

# For Windows(from project root):
$env:PYTHONPATH="."; pytest .\tests\test_parse_json.py
```

The test suite includes various cases for:
- Object parsing
- Array parsing
- String handling
- Number validation
- Boolean values
- Null values

## Getting Started

1. Clone the repository.
2. Install dependencies (if any).
3. Run the parser with your JSON input.

## Specification

Refer to [https://www.json.org/json-en.html](https://www.json.org/json-en.html) for the JSON format specification.

## License

MIT License