import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        expected_result = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_result)

    def test_to_html_without_tag(self):
        node = LeafNode(value="This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")

    def test_to_html_with_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        expected_result = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_result)

    def test_value_required(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p")

if __name__ == "__main__":
    unittest.main()
