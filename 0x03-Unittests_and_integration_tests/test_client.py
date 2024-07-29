import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
  """Class that test git_hub_org_client"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.GithubOrgClient.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
      """Function that tests git_hub_org_client"""
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, {"payload": True})
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
