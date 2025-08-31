def parse_number(input_string: str, i: int) -> tuple:
    """
    Parser
    Parses given input string for float or int and then returns the
    float + int along with the remaining part
    PS: Handles only one number per string at the start
    """
    if not input_string:
        raise ValueError("Empty input")

    n = len(input_string)
    
    start = i

    # --- Leading Sign
    if input_string[i] == "-":
        i += 1

    # --- Numerical Part
    if i < n and input_string[i] in "0123456789":
        if (
            input_string[i] == "0"
            and i + 1 < n
            and input_string[i + 1] in "0123456789"
        ):
            raise ValueError("Leading zeros not Allowed")
        while i < n and input_string[i] in "0123456789":
            i += 1
    else:
        raise ValueError("Missing Numberical Value")

    # --- Fractional Part
    if i < n and input_string[i] == ".":
        i += 1
        if i < n and input_string[i] in "0123456789":
            while i < n and input_string[i] in "0123456789":
                i += 1
        else:
            raise ValueError("No Numberical Value after decimal")

    # --- Exponent Part
    if i < n and input_string[i] in "eE":
        ckpt = i
        i += 1
        if input_string[i] in "+-":
            i += 1
        if i < n and input_string[i] in "0123456789":
            while i < n and input_string[i] in "0123456789":
                i += 1
        else:
            i = ckpt

    numerical_part = input_string[start:i]
    if "." in numerical_part or "e" in numerical_part or "E" in numerical_part:
        number = float(numerical_part)
    else:
        number = int(numerical_part)
    return (number, i)


if __name__ == "__main__":
    print(parse_number("a123abc", 1))
    print(parse_number("ab45.67,rest", 2))
    print(parse_number("ed-89xyz", 2))
