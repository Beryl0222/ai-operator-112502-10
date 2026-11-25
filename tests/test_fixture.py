import json
from pathlib import Path
import unittest


class FixtureContractTest(unittest.TestCase):
    def test_scatter_fixture_contains_duplicate_index_and_overlapping_views(self):
        base = Path(__file__).parents[1]
        payload = json.loads((base / "data/input.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["indices"].count(2), 2)
        first, second = payload["views"]
        self.assertLess(max(first["offset"], second["offset"]), min(
            first["offset"] + first["length"], second["offset"] + second["length"]))
        self.assertIn(-1, payload["indices"])

if __name__ == "__main__":
    unittest.main()
