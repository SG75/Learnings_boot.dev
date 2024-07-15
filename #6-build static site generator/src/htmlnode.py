import re

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses must implement the to_html method")

    def props_to_html(self):
        if not self.props:
            return ""
        props_html = " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        return " " + props_html

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        if children is None or not children:
            raise ValueError("ParentNode must have at least one child.")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not self.children:
            raise ValueError("ParentNode must have at least one child.")

        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"


def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    text = text_node.text
    url = text_node.url

    if text_type == "text":
        return LeafNode(value=text)

    elif text_type == "bold":
        return LeafNode(tag="b", value=text)

    elif text_type == "italic":
        return LeafNode(tag="i", value=text)

    elif text_type == "code":
        return LeafNode(tag="code", value=text)

    elif text_type == "link":
        if url is None:
            raise ValueError("Link TextNode must have a URL.")
        props = {"href": url}
        return LeafNode(tag="a", value=text, props=props)

    elif text_type == "image":
        if url is None:
            raise ValueError("Image TextNode must have a URL.")
        props = {"src": url, "alt": text}
        return LeafNode(tag="img", value="", props=props)

    else:
        raise ValueError("Invalid text type: {}".format(text_type))

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue

        text = node.text
        start_index = 0
        delimiter_start = text.find(delimiter)

        while delimiter_start != -1:
            # Add preceding text as a TextNode
            if delimiter_start > start_index:
                new_nodes.append(TextNode(text[start_index:delimiter_start], text_type))

            # Find the matching closing delimiter
            delimiter_end = text.find(delimiter, delimiter_start + len(delimiter))
            if delimiter_end == -1:
                raise ValueError(f"Invalid Markdown syntax. No matching closing delimiter for '{delimiter}'.")

            # Add the delimited text as a TextNode with the specified text type
            new_nodes.append(TextNode(text[delimiter_start + len(delimiter):delimiter_end], text_type))

            # Update start index for next iteration
            start_index = delimiter_end + len(delimiter)

            # Find next occurrence of delimiter
            delimiter_start = text.find(delimiter, start_index)

        # Add remaining text as a TextNode
        if start_index < len(text):
            new_nodes.append(TextNode(text[start_index:], text_type))

    return new_nodes

def extract_markdown_images(text):
    regex_pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(regex_pattern, text)

def extract_markdown_links(text):
    regex_pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(regex_pattern, text)

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue
        
        text = node.text
        image_tuples = extract_markdown_images(text)
        
        if not image_tuples:
            new_nodes.append(node)
            continue
        
        parts = re.split(r"!\[.*?\]\(.*?\)", text)
        for part in parts:
            if part:
                new_nodes.append(TextNode(part, text_type_text))
        
        for alt_text, url in image_tuples:
            new_nodes.append(TextNode(alt_text, text_type_image, url))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue
        
        text = node.text
        link_tuples = extract_markdown_links(text)
        
        if not link_tuples:
            new_nodes.append(node)
            continue
        
        parts = re.split(r"\[.*?\]\(.*?\)", text)
        for part in parts:
            if part:
                new_nodes.append(TextNode(part, text_type_text))
        
        for anchor_text, url in link_tuples:
            new_nodes.append(TextNode(anchor_text, text_type_link, url))
    
    return new_nodes

def text_to_textnodes(text):
    text_nodes = []
    parts = re.split(r"(\*\*|\*|`|!\[.*?\]\(.*?\)|\[.*?\]\(.*?\))", text)
    
    for part in parts:
        if not part:
            continue
        
        if part.startswith("**"):
            text_nodes.append(TextNode(part[2:], text_type_bold))
        elif part.startswith("*"):
            text_nodes.append(TextNode(part[1:], text_type_italic))
        elif part.startswith("`"):
            text_nodes.append(TextNode(part[1:], text_type_code))
        elif part.startswith("!"):
            images = extract_markdown_images(part)
            for alt_text, url in images:
                text_nodes.append(TextNode(alt_text, text_type_image, url))
        elif part.startswith("["):
            links = extract_markdown_links(part)
            for anchor_text, url in links:
                text_nodes.append(TextNode(anchor_text, text_type_link, url))
        else:
            text_nodes.append(TextNode(part, text_type_text))
    
    return text_nodes

def markdown_to_blocks(markdown):
    # Split the markdown into blocks based on double newlines
    blocks = markdown.split("\n\n")
    
    # Remove leading and trailing whitespace from each block
    blocks = [block.strip() for block in blocks]
    
    # Remove empty blocks
    blocks = [block for block in blocks if block]
    
    return blocks

def block_to_block_type(block):
    if block.startswith("#"):
        return "heading"
    elif block.startswith("```"):
        return "code_block"
    elif block.startswith(">"):
        return "quote_block"
    elif block.startswith("* ") or block.startswith("- "):
        return "unordered_list"
    elif block[0].isdigit() and block[1] == ".":
        return "ordered_list"
    else:
        return "paragraph"