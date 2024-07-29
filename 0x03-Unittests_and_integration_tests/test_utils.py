#!/usr/bin/env python3
""" Utils Module Test
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoiz


class TestAccessNestedMap(unittest.TestCase):
    """A class that tests access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map,
            path, expected):
        """A function that tests
        access_nested_map"""
        self.assertEqual(access_nested_map(nested_map,
            path), expected)
    def test_access_nested_map_exception(self, nested_map, path):
        """test exception of access_nested_map"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(str(err.exception), f"KeyError('{expected}')")


class TestGetJson(unittest.TestCase):
    """A class that tests get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """A function that tests get_json"""
        attr = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **attr)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """A class that tests memoize"""

    def test_memoize(self):
        """A function that tests memoize
        """


        class TestClass:
            """A function that tests Class for wrapping with memoize"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
