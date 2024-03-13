import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p","I am a paragraph", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')


    def test_props_to_html_2(self):
        node = HTMLNode(props={"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')


class TestLeafNode(unittest.TestCase):
    def test_leaf_render(self):
        node = LeafNode("p","This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')


    def test_leaf_render_notag(self):
        node = LeafNode(value="This is a paragraph of text.", props={"href": "boot.dev"})
        self.assertEqual(node.to_html(), 'This is a paragraph of text.')


    def test_leaf_render_with_prop(self):
        node = LeafNode("p", "This is a paragraph of text.", {"href": "boot.dev"})
        self.assertEqual(node.to_html(), '<p href="boot.dev">This is a paragraph of text.</p>')


    def test_leaf_render_no_value(self):
        node = LeafNode("p", props={"href": "boot.dev"})
        self.assertRaises(ValueError, lambda: node.to_html())
        

if __name__ == "__main__":
    unittest.main()
