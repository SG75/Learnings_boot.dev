import unittest
from htmlnode import ParentNode
from htmlnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode("p", children)
        expected_result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_result)

    def test_tag_required(self):
        with self.assertRaises(ValueError):
            ParentNode(children=[LeafNode("b", "Bold text")])

    def test_children_required(self):
        with self.assertRaises(ValueError):
            ParentNode("p", [])

if __name__ == "__main__":
    unittest.main()
