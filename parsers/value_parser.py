"""
Main Parser Flow which calls other parsers
Based on Tokenised String
JSON Grammar
JSON    → VALUE
VALUE   → STRING | NUMBER | OBJECT | ARRAY | TRUE | FALSE | NULL
OBJECT  → '{' MEMBERS? '}'
MEMBERS → PAIR (',' PAIR)*
PAIR    → STRING ':' VALUE
ARRAY   → '[' ELEMENTS? ']'
ELEMENTS→ VALUE (',' VALUE)*
"""

from typing import Any, Tuple


def parse_array(token_list: list, start_index: int) -> Tuple[list, int]:
    """
    Parse a JSON array by recursively parsing its elements.

    Args:
        token_list (list): List of tokens to parse
        start_index (int): Starting index in the token list

    Returns:
        Tuple[list, int]: A tuple containing the parsed array
                        and the next index to process
    """
    parsed_array = []
    curr_idx = start_index + 1
    while curr_idx < len(token_list) and token_list[curr_idx][0] != "RBRACKET":
        try:
            value, next_idx = parse_value(token_list, curr_idx)
            parsed_array.append(value)
            if token_list[next_idx][0] == "COMMA":
                if (
                    next_idx + 1 < len(token_list)
                    and token_list[next_idx + 1][0] == "RBRACKET"
                ):
                    raise ValueError(
                        f"Malformed JSON: Trailing comma in array at {next_idx}"
                    )
                next_idx += 1
            curr_idx = next_idx
        except Exception:
            raise ValueError(f"Malformed JSON: Bad Array at index {curr_idx}")
    if curr_idx >= len(token_list):
        raise ValueError(f"Malformed JSON: Array at {start_index} not closed.")
    return (parsed_array, curr_idx + 1)


def parse_pair(
    token_list: list, start_index: int
) -> Tuple[Tuple[str, Any], int]:
    """
    Parse a Key Value Pair inside an Object.

    Args:
        token_list (list): List of tokens to parse
        start_index (int): Starting index in the token list

    Returns:
        Tuple[tuple, int]: Tuple(Key, Value), next index
    """
    curr_index = start_index

    # Key should be a string
    if token_list[curr_index][0] != "STRING":
        raise ValueError(
            f"Malformed JSON: at {curr_index} \
                         only strings allowed as keys in Objects."
        )
    key = token_list[curr_index][1]
    curr_index += 1

    # Check Colon
    if token_list[curr_index][0] != "COLON":
        raise ValueError(
            f"Malformed JSON: at {curr_index} \
            expected COLON but got {token_list[curr_index]}"
        )
    curr_index += 1

    value, next_idx = parse_value(token_list, curr_index)
    return ((key, value), next_idx)


def parse_object(token_list: list, start_index: int) -> Tuple[dict, int]:
    """
    Parse a JSON Object by recursively parsing its elements.

    Args:
        token_list (list): List of tokens to parse
        start_index (int): Starting index in the token list

    Returns:
        Tuple[dict, int]: A tuple containing the parsed object
                        and the next index to process
    """
    parsed_dict = {}
    curr_idx = start_index + 1
    while curr_idx < len(token_list) and token_list[curr_idx][0] != "RBRACE":
        try:
            data, next_idx = parse_pair(token_list, curr_idx)
            obj_key, obj_value = data
            parsed_dict[obj_key] = obj_value
            if token_list[next_idx][0] == "COMMA":
                if (
                    next_idx + 1 < len(token_list)
                    and token_list[next_idx + 1][0] == "RBRACE"
                ):
                    raise ValueError(
                        f"Malformed JSON: Trailing comma in Object at {next_idx}"
                    )
                next_idx += 1
            curr_idx = next_idx
        except Exception as e:
            raise ValueError(
                f"Malformed JSON: Bad Object at index {curr_idx}: {e}"
            )
    if curr_idx >= len(token_list):
        raise ValueError(
            f"Malformed JSON: Object at {start_index} not closed."
        )
    return (parsed_dict, curr_idx + 1)


def parse_value(token_list: list, start_index: int) -> Tuple[Any, int]:
    """
    Start parsing Object
    return tuple of value and next index
    """
    token_type, token_value = token_list[start_index]
    if token_type == "STRING":
        return (token_value, start_index + 1)
    elif token_type == "NUMBER":
        return (token_value, start_index + 1)
    elif token_type == "LBRACE":
        return parse_object(token_list, start_index)
    elif token_type == "LBRACKET":
        return parse_array(token_list, start_index)
    elif token_type == "LITERAL":
        if token_value == "false":
            return (False, start_index + 1)
        elif token_value == "true":
            return (True, start_index + 1)
        elif token_value == "null":
            return (None, start_index + 1)
        else:
            raise ValueError(f"Literal at {start_index} still not handled.")
    raise ValueError(f"Malformed JSON: Array at {start_index}.")


if __name__ == "__main__":
    print(
        parse_value(
            [
                ("STRING", "deleted"),
            ],
            0,
        )
    )
    print(
        parse_value(
            [
                ("NUMBER", 123),
            ],
            0,
        )
    )
    print(
        parse_value(
            [
                ("LITERAL", "null"),
            ],
            0,
        )
    )
    print(
        parse_value(
            [
                ("LBRACKET", "["),
                ("LBRACKET", "["),
                ("NUMBER", 1),
                ("COMMA", ","),
                ("NUMBER", 2),
                ("RBRACKET", "]"),
                ("COMMA", ","),
                ("LBRACKET", "["),
                ("NUMBER", 3),
                ("COMMA", ","),
                ("NUMBER", 4),
                ("RBRACKET", "]"),
                ("COMMA", ","),
                ("LBRACKET", "["),
                ("NUMBER", 5),
                ("COMMA", ","),
                ("NUMBER", 6),
                ("RBRACKET", "]"),
                ("RBRACKET", "]"),
            ],
            0,
        )
    )
