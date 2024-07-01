#!/usr/bin/env python3
""" utils test module """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """ test class for access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """ test method for access nested map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected: Any) -> None:
        """ test method for access nested map exceptions """
        self.assertRaises(expected, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """ test class for get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, test_url, expected, mock_request):
        """ mock test for requests.get """
        mock_resp = Mock()
        mock_resp.json.return_value = expected
        mock_request.return_value = mock_resp

        res = get_json(test_url)
        mock_request.assert_called_once_with(test_url)

        self.assertEqual(res, expected)


class TestMemoize(unittest.TestCase):
    """ Memoization test class """
    def test_memoize(self):
        """ test method for memoize """

        class TestClass:

            def a_method(self):
                """ the method to mock """
                return 42

            @memoize
            def a_property(self):
                """ memoized method """
                return self.a_method()

        obj = TestClass()
        with patch.object(obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            first_result = obj.a_property
            second_result = obj.a_property

            mock_method.assert_called_once()

            self.assertEqual(first_result, 42)
            self.assertEqual(second_result, 42)
