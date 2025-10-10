import unittest
from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()