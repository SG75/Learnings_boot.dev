import unittest


from textnode import TextNode

def test_split_nodes_delimiter():
    # Test with code block delimiter `
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")
    expected_nodes = [
        TextNode("This is text with a ", "text"),
        TextNode("code block", "code"),
        TextNode(" word", "text"),
    ]
    assert new_nodes == expected_nodes

    # Test with bold delimiter **
    node = TextNode("**This is bold text**", "text")
    new_nodes = split_nodes_delimiter([node], "**", "bold")
    expected_nodes = [
        TextNode("", "text"),
        TextNode("This is bold text", "bold"),
        TextNode("", "text"),
    ]
    assert new_nodes == expected_nodes

    # Test with italic delimiter *
    node = TextNode("*This is italic text*", "text")
    new_nodes = split_nodes_delimiter([node], "*", "italic")
    expected_nodes = [
        TextNode("", "text"),
        TextNode("This is italic text", "italic"),
        TextNode("", "text"),
    ]
    assert new_nodes == expected_nodes

    # Test with multiple delimiters in one node
    node = TextNode("This **is bold** and *italic* text", "text")
    new_nodes = split_nodes_delimiter([node], "*", "italic")
    expected_nodes = [
        TextNode("This **is bold** and ", "text"),
        TextNode("italic", "italic"),
        TextNode(" text", "text"),
    ]
    assert new_nodes == expected_nodes

    print("All tests passed successfully.")


if __name__ == "__main__":
     unittest.main()