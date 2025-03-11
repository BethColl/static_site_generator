
class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag #string representing the HTML tag name
		self.value = value #string represtenting the value of the HTML tag (e.g. the text inside a paragraph)
		self.children = children #list of HTMLNode objects representing the children of this node
		self.props = props #dictionary of key-value pairs representing the attributes of the HTML tag

	def to_html(self):
		raise exception(NotImplementedError)

	def props_to_html(self):
		html = ""
		for prop in self.props:
			html = html + (f' {prop}="{self.props[prop]}"')
		return html
        
	def __eq__(self, other):
		return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

	def __repr__(self):
		return f' The tag is {self.tag}. The value is {self.value}. The children are {self.children}. The props are {self.props}.'
