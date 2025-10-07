from textnode import TextNode, TextType

def main():
    node = TextNode("Anchor text", TextType.LINK, "https://www.youtube.com")
    print(node)

if __name__ == "__main__":
    main()