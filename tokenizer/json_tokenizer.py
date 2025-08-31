from parsers.integer_parser import parse_number
from parsers.string_parser import parse_string


def json_tokenizer(json_string: str) -> list[tuple]:
    """
    Tokenize JSON String
    using tokens like LBRACE RBRACE etc
    """
    n = len(json_string)
    i = 0
    json_tokenized_res = []

    while i < n:
        # print(json_tokenized_res, i)
        if json_string[i] == "{":
            json_tokenized_res.append(("LBRACE", json_string[i]))
            i += 1
        elif json_string[i] == "}":
            json_tokenized_res.append(("RBRACE", json_string[i]))
            i += 1
        elif json_string[i] == ":":
            json_tokenized_res.append(("COLON", json_string[i]))
            i += 1
        elif json_string[i] == "[":
            json_tokenized_res.append(("LBRACKET", json_string[i]))
            i += 1
        elif json_string[i] == "]":
            json_tokenized_res.append(("RBRACKET", json_string[i]))
            i += 1
        elif json_string[i] == ",":
            json_tokenized_res.append(("COMMA", json_string[i]))
            i += 1
        elif json_string[i] == " " or json_string[i] == "\n":
            i += 1
        elif json_string[i] == "-" or json_string[i] in "0123456789":
            num, rem = parse_number(json_string, i)
            json_tokenized_res.append(("NUMBER", str(num)))
            i = rem
        elif json_string[i] == '"':
            string, rem = parse_string(json_string, i)
            json_tokenized_res.append(("STRING", string))
            i = rem
        elif (
            json_string[i : i + 4] == "true"
            or json_string[i : i + 4] == "null"
        ):
            json_tokenized_res.append(("LITERAL", json_string[i : i + 4]))
            i += 4
        elif json_string[i : i + 5] == "false":
            json_tokenized_res.append(("LITERAL", json_string[i : i + 5]))
            i += 5
        else:
            ValueError(f"Unexpected character at {i}: {json_string[i]}")

    return json_tokenized_res


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
