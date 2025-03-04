import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD_TEXT)
		node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
		self.assertEqual(node, node2)
	def test_noteq_types(self):
		node = TextNode("This is a text node", TextType.ITALIC_TEXT)
		node2 = TextNode("This is a text node", TextType.CODE_TEXT)
		self.assertNotEqual(node, node2)
	def test_links_match(self):
		node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev/")
		node2 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev/")
		self.assertEqual(node, node2)
	def test_links_noteq_type(self):
		node = TextNode("This is not a link", TextType.NORMAL_TEXT)
		node2 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev/")
		self.assertNotEqual(node, node2)
	def test_text_noteq(self):
		node = TextNode("This is one text node", TextType.NORMAL_TEXT)
		node2 = TextNode("This is another text node", TextType.NORMAL_TEXT)
		self.assertNotEqual(node, node2)
	def test_null_url_match(self):
		node = TextNode("This is a None url", TextType.LINK, None)
		node2 = TextNode("This is a None url", TextType.LINK)
		self.assertEqual(node, node2)

if __name__ == "__main__":
	unittest.main()
