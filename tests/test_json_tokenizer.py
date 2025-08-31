import pytest
import sys
import os

from tokenizer.json_tokenizer import json_tokenizer


def test_json_tokenizer_simple():
    json_str = """
    {"a": 1}
    """
    assert json_tokenizer(json_str) == [
        ("LBRACE", "{"),
        ("STRING", "a"),
        ("COLON", ":"),
        ("NUMBER", "1"),
        ("RBRACE", "}"),
    ]


def test_json_tokenizer_nested():
    json_str = """
        {"user": {"id": 101, "roles": ["admin", "editor"]}}
    """
    assert json_tokenizer(json_str) == [
        ("LBRACE", "{"),
        ("STRING", "user"),
        ("COLON", ":"),
        ("LBRACE", "{"),
        ("STRING", "id"),
        ("COLON", ":"),
        ("NUMBER", "101"),
        ("COMMA", ","),
        ("STRING", "roles"),
        ("COLON", ":"),
        ("LBRACKET", "["),
        ("STRING", "admin"),
        ("COMMA", ","),
        ("STRING", "editor"),
        ("RBRACKET", "]"),
        ("RBRACE", "}"),
        ("RBRACE", "}"),
    ]


def test_json_tokenizer_literal():
    json_str = """
        {"active": true, "deleted": false, "meta": null}
    """
    assert json_tokenizer(json_str) == [
        ("LBRACE", "{"),
        ("STRING", "active"),
        ("COLON", ":"),
        ("LITERAL", "true"),
        ("COMMA", ","),
        ("STRING", "deleted"),
        ("COLON", ":"),
        ("LITERAL", "false"),
        ("COMMA", ","),
        ("STRING", "meta"),
        ("COLON", ":"),
        ("LITERAL", "null"),
        ("RBRACE", "}"),
    ]
