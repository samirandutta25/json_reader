def parse_string(input_string: str, i: int) -> tuple:
    """
    Parse a JSON-formatted string starting from a given position.
    The function parses a string that starts
    with a double quote (") and handles escaped characters.
    Valid escape sequences include: \", \\, \b, \f, \n, \r, \t
    Args:
        input_string (str): The input string containing
        a JSON-formatted string. i (int): Starting
        position in the input string where parsing should begin.
    Returns:
        tuple: A tuple containing:
            - str: The parsed string value (without surrounding quotes)
            - int: The index position after the parsed string
    Raises:
        ValueError: If the input is empty, doesn't start with ",
        contains invalid escape sequences,
                   or isn't properly terminated.
    Example:
    parse_string('"Hello\\nWorld"', 0) -> ('Hello\nWorld', 13)
    """
    if not input_string:
        raise ValueError("Empty input")

    n = len(input_string)
    start = i
    if input_string[i] != '"':
        raise ValueError('String must start with " .')
    i += 1
    escaped = False
    ended = False

    while i < n:
        if input_string[i] not in '"\\' and not escaped:
            i += 1
        elif input_string[i] == "\\" and not escaped:
            escaped = True
            i += 1
        elif input_string[i] in '\\bfnrt"' and escaped:
            escaped = False
            i += 1
        elif input_string[i] == '"' and not escaped:
            i += 1
            ended = True
            break
        else:
            raise ValueError("Malformed String")

    if not ended:
        raise ValueError("String Not Ended properly")
    res = input_string[start + 1 : i - 1]
    return (res, i)


if __name__ == "__main__":
    print(parse_string('"a123"abc', 0))
    print(parse_string('"ab45.67",rest"', 0))
    print(parse_string('"89"xyz', 0))
    print(parse_string('"89"', 0))
    print(parse_string(r'"89\n\t3456ty\"xy"z', 0))
    print(parse_string('"89"', 0))
