import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.url.net")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.url.net")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is NOT a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_repr_with_none_url(self):
        node = TextNode("Text without URL", TextType.BOLD)
        self.assertEqual("TextNode(Text without URL, bold, None)", repr(node))

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        node2 = TextNode("", TextType.TEXT)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()