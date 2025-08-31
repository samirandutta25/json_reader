"""
Glue File does the work of parsing
"""
from tokenizer.json_tokenizer import json_tokenizer

if __name__ == "__main__":
    json_str = """
    {"a": 1}
    """
    print(json_tokenizer(json_str))

    json_str2 = """
        [10, 20, 30]
    """
    print(json_tokenizer(json_str2))

    json_str3 = """
        {"name": "Alice", "age": 25}
    """
    print(json_tokenizer(json_str3))

    json_str4 = """
        {"active": true, "deleted": false, "meta": null}
    """
    print(json_tokenizer(json_str4))

    json_str5 = """
        {"user": {"id": 101, "roles": ["admin", "editor"]}}
    """
    print(json_tokenizer(json_str5))
