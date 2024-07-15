import unittest

from textnode import TextNode
from htmlnode import text_to_textnodes

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_eq_different_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("Different text", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_different_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq_different_url(self):
        node = TextNode("This is a text node", "bold", "https://www.example.com")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)
    
    def test_text_to_textnodes():
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        expected_nodes = [
        TextNode("This is ", text_type_text),
        TextNode("text", text_type_bold),
        TextNode(" with an ", text_type_text),
        TextNode("italic", text_type_italic),
        TextNode(" word and a ", text_type_text),
        TextNode("code block", text_type_code),
        TextNode(" and an ", text_type_text),
        TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and a ", text_type_text),
        TextNode("link", text_type_link, "https://boot.dev"),
        ]
        assert text_nodes == expected_nodes
        print("Test text_to_textnodes passed successfully.")


    
if __name__ == "__main__":
    unittest.main()
    

