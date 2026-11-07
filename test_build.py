import unittest

from build import render_page


class BuildTests(unittest.TestCase):
    def test_renders_heading(self):
        self.assertIn("<h1>CI/CD</h1>", render_page("CI/CD"))

    def test_escapes_html_in_heading(self):
        self.assertIn("<h1>A &lt; B</h1>", render_page("A < B"))