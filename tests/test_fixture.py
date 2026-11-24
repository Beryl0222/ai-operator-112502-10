import json
from pathlib import Path
import unittest

class FixtureContractTest(unittest.TestCase):
    def test_fixture_is_valid_json(self):
        base = Path(__file__).parents[1]
        payload = json.loads((base / "data/input.json").read_text())
        schema = json.loads((base / "data/schema.json").read_text())
        self.assertIsInstance(payload, dict)
        self.assertEqual(schema["input_file"], "data/input.json")

if __name__ == "__main__":
    unittest.main()
