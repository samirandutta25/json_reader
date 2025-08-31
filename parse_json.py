"""
Glue File does the work of parsing
"""

from typing import Any
from tokenizer.json_tokenizer import json_tokenizer
from parsers.value_parser import parse_value


def parse_json(json_str: str) -> Any:
    tokenized_json = json_tokenizer(json_str)
    num_tokens = len(tokenized_json)
    if num_tokens == 0:
        return None
    serialized_value, next_index = parse_value(tokenized_json, 0)
    if next_index >= num_tokens:
        return serialized_value
    raise ValueError(f"Malformed JSON: Invalid json after {next_index}")


if __name__ == "__main__":
    json_str1 = r"""
        {
            "config": {
                "flags": [true, false, null],
                "nested": {
                "arr": [
                    {"key": "value"},
                    {"another": [1, 2, {"deep": "yes"}]}
                ]
                }
            }
        }
    """
    print(parse_json(json_str1))
