# coding: utf-8

import unittest
from unittest.mock import Mock, patch

from winthrop_client_python.api_client import ApiClient
from winthrop_client_python.configuration import Configuration
from winthrop_client_python.exceptions import UnauthorizedException
from winthrop_client_python.refresh_token import WinthropClient


class Response:
    def __init__(self, status):
        self.status = status
        self.reason = "Unauthorized" if status == 401 else "OK"
        self.data = b""
        self.headers = {}


class TestApiClientDeviceToken(unittest.TestCase):
    def setUp(self):
        WinthropClient.DeviceToken.clear_cache()

    def tearDown(self):
        WinthropClient.DeviceToken.clear_cache()

    @patch("winthrop_client_python.refresh_token.subprocess.run")
    def test_401_refreshes_device_token_and_retries_once(self, mock_run):
        mock_run.side_effect = [
            Mock(returncode=0, stdout="old-token\n", stderr=""),
            Mock(returncode=0, stdout="new-token\n", stderr=""),
        ]
        configuration = Configuration(access_token=WinthropClient.DeviceToken.access_token())
        api_client = ApiClient(configuration)
        api_client.rest_client = Mock()
        api_client.rest_client.request.side_effect = [Response(401), Response(200)]

        response = api_client.call_api(
            "GET",
            "https://example.test/resource",
            header_params={"Authorization": "Bearer old-token"},
        )

        self.assertEqual(response.status, 200)
        self.assertEqual(configuration.access_token, "new-token")
        self.assertEqual(api_client.rest_client.request.call_count, 2)
        retry_headers = api_client.rest_client.request.call_args.kwargs["headers"]
        self.assertEqual(retry_headers["Authorization"], "Bearer new-token")

    @patch("winthrop_client_python.refresh_token.subprocess.run")
    def test_401_retry_raises_auth_error_if_still_401(self, mock_run):
        mock_run.side_effect = [
            Mock(returncode=0, stdout="old-token\n", stderr=""),
            Mock(returncode=0, stdout="new-token\n", stderr=""),
        ]
        configuration = Configuration(access_token=WinthropClient.DeviceToken.access_token())
        api_client = ApiClient(configuration)
        api_client.rest_client = Mock()
        api_client.rest_client.request.side_effect = [Response(401), Response(401)]

        with self.assertRaises(UnauthorizedException):
            api_client.call_api(
                "GET",
                "https://example.test/resource",
                header_params={"Authorization": "Bearer old-token"},
            )

        self.assertEqual(api_client.rest_client.request.call_count, 2)

    def test_401_does_not_retry_static_access_token(self):
        configuration = Configuration(access_token="static-token")
        api_client = ApiClient(configuration)
        api_client.rest_client = Mock()
        api_client.rest_client.request.return_value = Response(401)

        response = api_client.call_api(
            "GET",
            "https://example.test/resource",
            header_params={"Authorization": "Bearer static-token"},
        )

        self.assertEqual(response.status, 401)
        api_client.rest_client.request.assert_called_once()


if __name__ == "__main__":
    unittest.main()
