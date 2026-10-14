# coding: utf-8

import subprocess
import unittest
from unittest.mock import Mock, patch

from winthrop_client_python.exceptions import UnauthorizedException
from winthrop_client_python.refresh_token import WinthropClient


class TestDeviceToken(unittest.TestCase):
    def setUp(self):
        WinthropClient.DeviceToken.clear_cache()
        WinthropClient.DeviceToken.cli_executable = "winthrop"
        WinthropClient.DeviceToken.timeout = 10

    def tearDown(self):
        WinthropClient.DeviceToken.clear_cache()
        WinthropClient.DeviceToken.cli_executable = "winthrop"
        WinthropClient.DeviceToken.timeout = 10

    @patch("winthrop_client_python.refresh_token.subprocess.run")
    def test_access_token_success(self, mock_run):
        mock_run.return_value = Mock(returncode=0, stdout="token-123\n", stderr="")

        token = WinthropClient.DeviceToken.access_token()

        self.assertEqual(token, "token-123")
        mock_run.assert_called_once_with(
            ["winthrop", "token"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )

    @patch("winthrop_client_python.refresh_token.subprocess.run")
    def test_access_token_reuses_cache(self, mock_run):
        mock_run.return_value = Mock(returncode=0, stdout="cached-token\n", stderr="")

        first = WinthropClient.DeviceToken.access_token()
        second = WinthropClient.DeviceToken.access_token()

        self.assertEqual(first, "cached-token")
        self.assertEqual(second, "cached-token")
        mock_run.assert_called_once()

    @patch("winthrop_client_python.refresh_token.subprocess.run")
    def test_clear_cache_fetches_next_token(self, mock_run):
        mock_run.side_effect = [
            Mock(returncode=0, stdout="first-token\n", stderr=""),
            Mock(returncode=0, stdout="second-token\n", stderr=""),
        ]

        first = WinthropClient.DeviceToken.access_token()
        WinthropClient.DeviceToken.clear_cache()
        second = WinthropClient.DeviceToken.access_token()

        self.assertEqual(first, "first-token")
        self.assertEqual(second, "second-token")
        self.assertEqual(mock_run.call_count, 2)

    @patch("winthrop_client_python.refresh_token.subprocess.run")
    def test_configurable_executable_and_timeout(self, mock_run):
        WinthropClient.DeviceToken.cli_executable = "/custom/winthrop"
        WinthropClient.DeviceToken.timeout = 2
        mock_run.return_value = Mock(returncode=0, stdout="token\n", stderr="")

        self.assertEqual(WinthropClient.DeviceToken.access_token(), "token")

        mock_run.assert_called_once_with(
            ["/custom/winthrop", "token"],
            capture_output=True,
            text=True,
            timeout=2,
            check=False,
        )

    @patch("winthrop_client_python.refresh_token.subprocess.run")
    def test_missing_executable(self, mock_run):
        mock_run.side_effect = FileNotFoundError()

        with self.assertRaises(UnauthorizedException) as context:
            WinthropClient.DeviceToken.access_token()

        self.assertIn(
            "Winthrop CLI is not installed. Install it and run `winthrop login`.",
            str(context.exception),
        )

    @patch("winthrop_client_python.refresh_token.subprocess.run")
    def test_non_zero_exit_surfaces_stderr(self, mock_run):
        mock_run.return_value = Mock(
            returncode=1, stdout="", stderr="please run winthrop login\n"
        )

        with self.assertRaises(UnauthorizedException) as context:
            WinthropClient.DeviceToken.access_token()

        self.assertIn("please run winthrop login", str(context.exception))

    @patch("winthrop_client_python.refresh_token.subprocess.run")
    def test_blank_stdout(self, mock_run):
        mock_run.return_value = Mock(returncode=0, stdout="\n", stderr="")

        with self.assertRaises(UnauthorizedException) as context:
            WinthropClient.DeviceToken.access_token()

        self.assertIn("blank access token", str(context.exception))

    @patch("winthrop_client_python.refresh_token.subprocess.run")
    def test_timeout(self, mock_run):
        mock_run.side_effect = subprocess.TimeoutExpired(["winthrop", "token"], 10)

        with self.assertRaises(UnauthorizedException) as context:
            WinthropClient.DeviceToken.access_token()

        self.assertIn("Timed out waiting for Winthrop CLI", str(context.exception))


if __name__ == "__main__":
    unittest.main()
