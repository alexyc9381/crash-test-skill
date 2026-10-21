import json
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SKILL = os.path.join(ROOT, "skills", "crash-test", "SKILL.md")


class SkillTest(unittest.TestCase):
    def setUp(self):
        with open(SKILL) as f:
            self.text = f.read()

    def test_frontmatter(self):
        self.assertTrue(self.text.startswith("---\nname: crash-test\n"))
        for key in ("description:", "argument-hint:", "license: MIT"):
            self.assertIn(key, self.text.split("---")[1])

    def test_seven_disasters(self):
        for who in ("The Recession", "The Copycat", "The Lawsuit", "Bad Reviews", "The Price War",
                    "No Customers", "The Broken Link"):
            self.assertIn(f"**{who}.**", self.text)
        self.assertIn("Start seven sub-agents at once", self.text)
        self.assertIn("Nobody sees anybody else's notes", self.text)

    def test_engineer_and_retest(self):
        self.assertIn("## 3. The damage report (the lead engineer)", self.text)
        self.assertIn("**The fix plan.**", self.text)
        self.assertIn("## 4. Re-test", self.text)
        self.assertIn("Call the plan BULLETPROOF only if every dummy now SURVIVES", self.text)

    def test_never_invents(self):
        self.assertIn("Never invent market sizes, statistics, competitor names or survey results", self.text)
        self.assertIn("not a forecast", self.text)

    def test_credit_line(self):
        self.assertIn("Made with /crash-test by Alex Chen (@nocodealex) · chen.media", self.text)

    def test_plugin_files(self):
        for name in ("plugin.json", "marketplace.json"):
            with open(os.path.join(ROOT, ".claude-plugin", name)) as f:
                json.load(f)


if __name__ == "__main__":
    unittest.main()
