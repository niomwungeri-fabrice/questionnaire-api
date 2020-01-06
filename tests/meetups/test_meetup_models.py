import unittest

test_meet_up_data = {
    "name": "20th Tech Summit",
    "venue": "Telecom House",
    "event_type": "ATTRACTION",
    "tags": ["0bc9be5c-40b7-4247-a0b9-0c068bb5c62b",
             "65d4f7dc-9970-488a-9207-b52dd077a4f7"]
}


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
