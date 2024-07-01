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
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"payload": True, "repos_url": "123"}

            client = GithubOrgClient('org')
            res = client._public_repos_url

            self.assertEqual(res, "123")

    @patch('requests.get')
    def test_public_repos(self, mock_request):
        """ test public_repos method """
        mock_resp = Mock()
        payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_resp.json.return_value = payload['repos']
        mock_request.return_value = mock_resp

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = payload["repos_url"]
            self.assertEqual(GithubOrgClient("google").public_repos(), ["episodes.dart", "kratu",])
            mock_repos.assert_called_once()
        mock_request.assert_called_once()
