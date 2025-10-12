import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div","Hellom, World", None, {"class": "greeting", "href": "https://example.com"})
        self.assertEqual(node.props_to_html(),' class="greeting" href="https://example.com"')

    def test_values(self):
        node = HTMLNode("div", "Example Text")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Example Text")

    def test_repr(self):
        node = HTMLNode("p", "Example Text", None, {"class": "primary"})
        self.assertEqual(node.__repr__(),"HTMLNode(p, Example Text, children: None, {'class': 'primary'})",)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://google.com"})
        self.assertEqual(node.to_html(),'<a href="https://google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello World")
        self.assertEqual(node.to_html(), "Hello World")

if __name__ == "__main__":
    unittest.main()