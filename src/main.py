from textnode import *

print("main.py is running")

def main():
	dummy_text_node = TextNode(("Dummy text"), TextType.LINK, "https://www.boot.dev")
	print(repr(dummy_text_node))

if __name__=="__main__":
	main()
