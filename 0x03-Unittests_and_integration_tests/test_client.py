#!/usr/bin/env python3
""" Client test module """
import unittest
from unittest.mock import Mock, patch, PropertyMock
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

    def test_public_repos_url(self):
        """ test puplic repos property """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"payload": True, "repos_url": "123"}

            client = GithubOrgClient('org')
            res = client._public_repos_url

            self.assertEqual(res, "123")

    @patch('requests.get')
    def test_public_repos(self, mock_request):
        """ test public_repos method """
        mock_resp = Mock()
        payload = {
            'repos_url': "test_url",
            'repos': [{"name": "repo1"}, {"name": "repo2"}]
            }
        mock_resp.json.return_value = payload['repos']
        mock_request.return_value = mock_resp

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = payload["repos_url"]
            obj = GithubOrgClient("org")
            self.assertEqual(obj.public_repos(), ["repo1", "repo2"])

        mock_request.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license, expected):
        """ test has license """
        client = GithubOrgClient('org')
        res = client.has_license(repo, license)
        self.assertEqual(res, expected)
