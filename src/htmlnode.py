
class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		tag = self.tag #string representing the HTML tag name
		value = self.value #string represtenting the value of the HTML tag (e.g. the text inside a paragraph)
		children = self.children #list of HTMLNode objects representing the children of this node
		props = self.props #dictionary of key-value pairs representing the attributes of the HTML tag

	def to_html(self):
		raise exception NotImplementedError

	def props_to_html(self):
		html = ""
		for prop in self.props:
			html = html + (f' {prop}="{self.props[prop]}"')
		return html

	def __repr__(self):
		return f' The tag is {self.tag}. The value is {self.value}. The children are {self.children}. The props are {self.props}.'
