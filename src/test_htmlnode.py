import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p","I am a paragraph", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.boot.dev" target="_blank"')


    def test_props_to_html_2(self):
        node = HTMLNode(props={"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.boot.dev" target="_blank"')


if __name__ == "__main__":
    unittest.main()
