import os
import unittest
from html.parser import HTMLParser

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILES = [
    os.path.join(REPO_ROOT, name)
    for name in ("index.html", "about.html", "tips.html")
]
CSS_FILE = os.path.join(REPO_ROOT, "style.css")


class SimpleHTMLValidator(HTMLParser):
    def error(self, message):
        raise AssertionError(message)


class TestSiteIntegrity(unittest.TestCase):
    def test_html_documents_have_doctype_and_main(self):
        for html_path in HTML_FILES:
            with self.subTest(html_path=html_path):
                with open(html_path, encoding="utf-8") as f:
                    contents = f.read()
                self.assertTrue(
                    contents.lstrip().lower().startswith("<!doctype html>"),
                    "Expected <!DOCTYPE html> declaration",
                )
                self.assertIn("<main", contents.lower(), "Expected a <main> landmark")

    def test_html_documents_parse_without_errors(self):
        for html_path in HTML_FILES:
            parser = SimpleHTMLValidator()
            with self.subTest(html_path=html_path):
                with open(html_path, encoding="utf-8") as f:
                    parser.feed(f.read())
                parser.close()

    def test_css_has_no_negative_spacing(self):
        with open(CSS_FILE, encoding="utf-8") as f:
            css = f.read()
        disallowed_tokens = ["margin: -", "padding: -", "top: -", "bottom: -", "left: -", "right: -"]
        for token in disallowed_tokens:
            self.assertNotIn(token, css, f"Unexpected negative spacing token '{token}' in stylesheet")


if __name__ == "__main__":
    unittest.main()
