import unittest

from htmlnode import HTMLNode, LeafNode

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
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Test link", {"href": "https://www.testlink.com"})
		self.assertEqual(node.to_html(), '<a href="https://www.testlink.com">Test link</a>')
	def test_leaf_to_html_img(self):
		node = LeafNode("img", "https://www.testimage.com")
		self.assertEqual(node.to_html(), '<img src="https://www.testimage.com" />')
	def test_leaf_to_html_bad_link(self):
		node = LeafNode("img", "Test link", {"href": "https:/www.testlink.com"})
		self.assertNotEqual(node.to_html(), '<a href="https://www.testlink.com">Test link</a>')

if __name__ == "__main__":
	unittest.main()

