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
		node = TextNode("This is not a link", TextType.TEXT)
		node2 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev/")
		self.assertNotEqual(node, node2)
	def test_text_noteq(self):
		node = TextNode("This is one text node", TextType.TEXT)
		node2 = TextNode("This is another text node", TextType.TEXT)
		self.assertNotEqual(node, node2)
	def test_null_url_match(self):
		node = TextNode("This is a None url", TextType.LINK, None)
		node2 = TextNode("This is a None url", TextType.LINK)
		self.assertEqual(node, node2)
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = node.text_node_to_html_node()
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")
	def test_bold(self):
		node = TextNode("This is bolded text", TextType.BOLD_TEXT)
		html_node = node.text_node_to_html_node()
		self.assertEqual(html_node.tag, 'b')
		self.assertEqual(html_node.value, "This is bolded text")
	def test_italic_difference(self):
		node = TextNode("This is italicized text", TextType.ITALIC_TEXT)
		html_node = node.text_node_to_html_node()
		self.assertEqual(html_node.tag, 'i')
		self.assertNotEqual(html_node.value, "This is italic text")

if __name__ == "__main__":
	unittest.main()
