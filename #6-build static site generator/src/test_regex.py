import unittest


from htmlnode import extract_markdown_images, extract_markdown_links

def test_extract_markdown_images():
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
    assert extract_markdown_images(text) == [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
    print("Test extract_markdown_images passed successfully.")

def test_extract_markdown_links():
    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    assert extract_markdown_links(text) == [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
    print("Test extract_markdown_links passed successfully.")

if __name__ == "__main__":
     unittest.main()
     test_split_nodes_image()
     test_split_nodes_link()