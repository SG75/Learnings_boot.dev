import unittest


from textnode import TextNode

def test_split_nodes_image():
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        text_type_text,
    )
    new_nodes = split_nodes_image([node])
    expected_nodes = [
        TextNode("This is text with an ", text_type_text),
        TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and another ", text_type_text),
        TextNode("second image", text_type_image, "https://i.imgur.com/3elNhQu.png"),
    ]
    assert new_nodes == expected_nodes
    print("Test split_nodes_image passed successfully.")

def test_split_nodes_link():
    node = TextNode(
        "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
        text_type_text,
    )
    new_nodes = split_nodes_link([node])
    expected_nodes = [
        TextNode("This is text with a ", text_type_text),
        TextNode("link", text_type_link, "https://www.example.com"),
        TextNode(" and ", text_type_text),
        TextNode("another", text_type_link, "https://www.example.com/another"),
    ]
    assert new_nodes == expected_nodes
    print("Test split_nodes_link passed successfully.")


if __name__ == "__main__":
     unittest.main()