import os
import re
import unittest
from html.parser import HTMLParser

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILES = [
    os.path.join(REPO_ROOT, name)
    for name in ("index.html", "about.html", "tips.html")
]
JS_FILES = [
    os.path.join(REPO_ROOT, name)
    for name in ("theme-toggle.js", "tips-filter.js")
]
CSS_FILE = os.path.join(REPO_ROOT, "style.css")

CONTENT_SECURITY_POLICY = (
    "default-src 'self'; "
    "img-src 'self' data:; "
    "style-src 'self'; "
    "script-src 'self'; "
    "connect-src 'none'; "
    "font-src 'self'; "
    "media-src 'self'; "
    "object-src 'none'; "
    "base-uri 'self'; "
    "form-action 'self'; "
    "frame-src 'none'; "
    "child-src 'none'; "
    "frame-ancestors 'none'; "
    "worker-src 'none'; "
    "upgrade-insecure-requests; "
    "require-trusted-types-for 'script'"
)

EXPECTED_SECURITY_SNIPPETS = [
    f'http-equiv="Content-Security-Policy" content="{CONTENT_SECURITY_POLICY}"',
    'http-equiv="Referrer-Policy" content="no-referrer"',
    'http-equiv="X-Content-Type-Options" content="nosniff"',
    'http-equiv="Permissions-Policy" content="camera=(), microphone=(), geolocation=()"',
    'http-equiv="Cross-Origin-Opener-Policy" content="same-origin"',
    'http-equiv="Cross-Origin-Resource-Policy" content="same-origin"',
    'http-equiv="Cross-Origin-Embedder-Policy" content="require-corp"',
]

INLINE_EVENT_ATTRIBUTES = (
    "onclick=",
    "onload=",
    "onerror=",
    "onfocus=",
    "onblur=",
    "onmouseover=",
    "onmouseenter=",
    "onmouseleave=",
    "onsubmit=",
    "onreset=",
)

DISALLOWED_SCRIPT_TOKENS = ("innerHTML", "outerHTML", "insertAdjacentHTML")

FILES_DISALLOWING_EXTERNAL_URLS = HTML_FILES + [CSS_FILE]
ALLOWED_EXTERNAL_URLS = {
    "https://instagram.com/fostondiy",
    "https://youtube.com/@fostonmakes",
}


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

    def test_html_documents_include_security_headers(self):
        for html_path in HTML_FILES:
            with self.subTest(html_path=html_path):
                with open(html_path, encoding="utf-8") as f:
                    contents = f.read()
                for snippet in EXPECTED_SECURITY_SNIPPETS:
                    self.assertIn(snippet, contents, f"Missing expected security meta tag fragment: {snippet}")

    def test_html_documents_avoid_inline_event_handlers(self):
        for html_path in HTML_FILES:
            with self.subTest(html_path=html_path):
                with open(html_path, encoding="utf-8") as f:
                    contents = f.read().lower()
                for attribute in INLINE_EVENT_ATTRIBUTES:
                    self.assertNotIn(attribute, contents, f"Inline event handler '{attribute}' found in {html_path}")

    def test_scripts_avoid_html_injection_apis(self):
        for script_path in JS_FILES:
            with self.subTest(script_path=script_path):
                with open(script_path, encoding="utf-8") as f:
                    contents = f.read()
                for token in DISALLOWED_SCRIPT_TOKENS:
                    self.assertNotIn(token, contents, f"Disallowed DOM API '{token}' detected in {script_path}")

    def test_no_external_urls_in_markup_or_styles(self):
        for file_path in FILES_DISALLOWING_EXTERNAL_URLS:
            with self.subTest(file_path=file_path):
                with open(file_path, encoding="utf-8") as f:
                    contents = f.read()
                matches = set(re.findall(r"https://[^'\"\s>]+", contents))
                unexpected = matches - ALLOWED_EXTERNAL_URLS
                self.assertFalse(
                    unexpected,
                    f"External HTTPS references are disallowed: {sorted(unexpected)}",
                )


if __name__ == "__main__":
    unittest.main()
