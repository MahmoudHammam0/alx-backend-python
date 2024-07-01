#!/usr/bin/env python3
""" Client test module """
import unittest
from unittest.mock import Mock, patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ test class for GithubOrg """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
        ])
    @patch('requests.get')
    def test_org(self, test_org, expected, mock_get):
        """ test for org method """
        mock_resp = Mock()
        mock_resp.json.return_value = expected
        mock_get.return_value = mock_resp

        obj = GithubOrgClient(test_org)
        res = obj.org

        mock_get.assert_called_once()

        self.assertEqual(res, expected)
