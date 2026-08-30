from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^]]*\]\(([^)]+)\)")


class RepositoryTests(unittest.TestCase):
    def test_local_markdown_links_exist(self):
        failures = []
        markdown_files = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
        for document in markdown_files:
            text = document.read_text(encoding="utf-8")
            for target in MARKDOWN_LINK.findall(text):
                if target.startswith(("https://", "http://", "mailto:")):
                    continue
                relative_target = target.split("#", 1)[0]
                if not relative_target:
                    continue
                resolved = (document.parent / relative_target).resolve()
                if not resolved.exists():
                    failures.append(f"{document.relative_to(ROOT)} -> {target}")
        self.assertEqual(failures, [], "missing local links: " + ", ".join(failures))

    def test_svg_assets_are_well_formed_xml(self):
        for asset in sorted((ROOT / "assets").glob("*.svg")):
            with self.subTest(asset=asset.name):
                ET.parse(asset)

    def test_test_results_template_has_expected_columns(self):
        header = (ROOT / "templates" / "test-results.csv").read_text(
            encoding="utf-8"
        ).splitlines()[0]
        columns = header.split(",")
        self.assertEqual(len(columns), len(set(columns)))
        self.assertIn("landmark_disruption_0_to_3", columns)
        self.assertIn("visibility_pass", columns)
        self.assertIn("comfort_pass", columns)


if __name__ == "__main__":
    unittest.main()
