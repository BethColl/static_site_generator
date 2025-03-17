from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
	TEXT = "normal"
	BOLD_TEXT = "bold"
	ITALIC_TEXT = "italic"
	CODE_TEXT = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text, type, URL=None):
		self.text = text
		self.text_type = type
		self.url = URL

	def __eq__(self, other):
		return self.text == other.text and self.text_type == other.text_type and self.url == other.url

	def __repr__(self):
		return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")

	def text_node_to_html_node(self):
		if self.text_type not in TextType:
			raise ValueError("Not valid Text Type.")
		elif self.text_type == TextType.TEXT:
			return LeafNode(None, self.text)
		elif self.text_type == TextType.BOLD_TEXT:
			return LeafNode('b', self.text)
		elif self.text_type == TextType.ITALIC_TEXT:
			return LeafNode('i', self.text)
		elif self.text_type == TextType.CODE_TEXT:
			return LeafNode('code', self.text)
		elif self.text_type == TextType.LINK:
			return LeafNode('a', self.text, self.url)
		elif self.text_type == TextType.IMAGE:
			return LeafNode('img', '', self.url)
		else: raise ValueError("Text Type not recognized.")
