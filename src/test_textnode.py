import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_one(self):
        node = TextNode("some text", TextType.ITALIC,"https://www.boot.dev")
        node2 = TextNode("some text", TextType.LINK,"https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_two(self):
        node = TextNode("bleep",TextType.CODE,"https://www.boot.dev")
        node2 = TextNode("bloop",TextType.CODE,"https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_three(self):
        node = TextNode("Text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("Text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()