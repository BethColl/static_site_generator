class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag #string representing the HTML tag name
		self.value = value #string represtenting the value of the HTML tag (e.g. the text inside a paragraph)
		self.children = children #list of HTMLNode objects representing the children of this node
		self.props = props #dictionary of key-value pairs representing the attributes of the HTML tag

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		if not self.props:
			return ""
		html = ""
		for prop in self.props:
			html = html + (f' {prop}="{self.props[prop]}"')
		return html

	def __eq__(self, other):
		if not isinstance(other, HTMLNode):
			return False
		return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

	def __repr__(self):
		return f' The tag is {self.tag}. The value is {self.value}. The children are {self.children}. The props are {self.props}.'

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if self.tag == None:
			raise ValueError("No tag.")
		elif self.children == None:
			raise ValueError("No child nodes.")
		else:
			result = f'<{self.tag}>'
			for child in self.children:
				if hasattr(child, 'children'):
					result = result + child.to_html()
				else:
					raise ValueError("Improperly defined node.")
		result = result + f'</{self.tag}>'
		return result

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value == None:
			raise ValueError("No tag.")
		elif self.tag == None:
			return self.value
		elif self.tag == "a":
			return f"<a {self.props_to_html().strip(' ')}>{self.value}</a>"
		elif self.tag == "img":
			return f'<img src="{self.value}" />' #Figure out how to add alt-text.
		else:
			return f"<{self.tag}>{self.value}</{self.tag}>"
