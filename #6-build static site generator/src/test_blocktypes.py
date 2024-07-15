import unittest
from htmlnode import block_to_block_type
def test_block_to_block_type():
    assert block_to_block_type("# Heading") == "heading"
    assert block_to_block_type("```python\nprint('Hello, world!')\n```") == "code_block"
    assert block_to_block_type("> This is a quote.") == "quote_block"
    assert block_to_block_type("* Item 1\n* Item 2") == "unordered_list"
    assert block_to_block_type("1. Item 1\n2. Item 2") == "ordered_list"
    assert block_to_block_type("This is a paragraph.") == "paragraph"
    print("Test block_to_block_type passed successfully.")

if __name__ == "__main__":
    unittest.main()
    test_block_to_block_type()