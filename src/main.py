from textnode import TextNode, TextType

def main():
    text_node_test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node_test)

main()