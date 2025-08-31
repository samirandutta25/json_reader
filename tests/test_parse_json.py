from parse_json import parse_json


def test_single_values():
    json_str1 = """
    42
    """
    json_str2 = """
    "hello"
    """
    json_str3 = """
    true
    """
    json_str4 = """
    null
    """
    assert parse_json(json_str1) == 42
    assert parse_json(json_str2) == "hello"
    assert parse_json(json_str3) == True
    assert parse_json(json_str4) is None


def test_array_values():
    json_str1 = """
    []
    """
    json_str2 = """
    [1, 2, 3]
    """
    json_str3 = """
    ["a", "b", "c", 123, false]
    """
    json_str4 = """
    [[1, 2], [3, 4], [5, 6]]
    """
    assert parse_json(json_str1) == []
    assert parse_json(json_str2) == [1, 2, 3]
    assert parse_json(json_str3) == ["a", "b", "c", 123, False]
    assert parse_json(json_str4) == [[1, 2], [3, 4], [5, 6]]


def test_object_values():
    json_str1 = r"""
    {}
    """
    json_str2 = r"""
    {"a": 1}
    """
    json_str3 = r"""
    {"x": true, "y": null, "z": "test"}
    """
    json_str4 = r"""
    {"person": {"name": "Alice", "age": 30, "active": true}}
    """
    assert parse_json(json_str1) == {}
    assert parse_json(json_str2) == {"a": 1}
    assert parse_json(json_str3) == {"x": True, "y": None, "z": "test"}
    assert parse_json(json_str4) == {
        "person": {"name": "Alice", "age": 30, "active": True}
    }


def test_mixed_values():
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
    assert parse_json(json_str1) == {
        "config": {
            "flags": [True, False, None],
            "nested": {
                "arr": [{"key": "value"}, {"another": [1, 2, {"deep": "yes"}]}]
            },
        }
    }


def test_some_edge_cases():
    json_str1 = r"""
        {"emptyArray": [], "emptyObject": {}}
    """
    json_str2 = r"""
        [{"deep": {"deeper": {"deepest": "done"}}}]
    """
    assert parse_json(json_str1) == {"emptyArray": [], "emptyObject": {}}
    assert parse_json(json_str2) == [{"deep": {"deeper": {"deepest": "done"}}}]
