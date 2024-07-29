#!/usr/bin/env python3
"""
Module for Testing client
"""
import unittest
import json
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Class that tests git_hub_org_client"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        # Set up the mock response
        mock_get_json.return_value = {'name': org_name}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method and assert the result
        result = client.org()
        endpoint = f'https://api.github.com/orgs/{org_name}'
        self.assertEqual(result, org_name)
        mock_get_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """Function that tests public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        """Function that tests public_repos"""
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_url:

            mocked_url.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_url.assert_called_once()
            mocked_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected_result):
        """Function that tests has_license"""
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expected_result)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class that tests Integration_github_org_client"""
    @classmethod
    def setUpClass(cls):
      """Function that sets up class"""
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
      """Function that clears up class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Function that tests public repos """

    def test_public_repos_with_license(self):
        """Function that tests public with license"""


if __name__ == '__main__':
    unittest.main()
