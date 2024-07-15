import unittest
from htmlnode import markdown_to_blocks
def test_markdown_to_blocks():
    markdown = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
    expected_blocks = [
        "This is **bolded** paragraph",
        "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
        "* This is a list\n* with items"
    ]
    assert markdown_to_blocks(markdown) == expected_blocks
    print("Test markdown_to_blocks passed successfully.")

if __name__ == "__main__":
    unittest.main()
    test_markdown_to_blocks()