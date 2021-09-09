import unittest

from libratone.commands import get_volume


class VolumeTests(unittest.TestCase):
    def test_valid_volume(self):
        self.assertEqual(
            b"\x00\x00\x02\x00\x40\x00\x00\x00\x00\x02\x30\x30", get_volume(0)
        )
        self.assertEqual(
            b"\x00\x00\x02\x00\x40\x00\x00\x00\x00\x02\x35\x30", get_volume(50)
        )
        self.assertEqual(
            b"\x00\x00\x02\x00\x40\x00\x00\x00\x00\x03\x31\x30\x30", get_volume(100)
        )

    def test_invalid_volume(self):
        with self.assertRaises(ValueError):
            get_volume(-50)

        with self.assertRaises(ValueError):
            get_volume(-1)

        with self.assertRaises(ValueError):
            get_volume(101)

        with self.assertRaises(ValueError):
            get_volume(150)
