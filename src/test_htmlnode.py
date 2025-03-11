import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
	def test_value_equal(self):
		node = HTMLNode("href", "https://www.testsite.com")
		node2 = HTMLNode("href", "https://www.testsite.com")
		self.assertEqual(node, node2)
	def test_noteq_children(self):
		node = HTMLNode("p", "test paragraphs", ["Paragraph1", "Paragraph2", "Paragraph3"])
		node2 = HTMLNode("p", "test paragraphs")
		self.assertNotEqual(node, node2)
	def test_props_to_html_match(self):
		node = HTMLNode("img", "image links", {"Image1": "Header Image", "Image2": "Main Image"})
		node2 = HTMLNode("img", "image links", {"Image1": "Header Image", "Image2": "Main Image"})
		self.assertEqual(node.props_to_html(), node2.props_to_html())

if __name__ == "__main__":
	unittest.main()

