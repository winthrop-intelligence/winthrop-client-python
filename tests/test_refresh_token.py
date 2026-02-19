# coding: utf-8

"""
    Test cases for RefreshToken class

    Tests for OAuth token management with scope support
"""

import json
import time
import unittest
from unittest.mock import Mock, patch, MagicMock
from winthrop_client_python.refresh_token import WinthropClient


class TestRefreshToken(unittest.TestCase):
    """RefreshToken unit test stubs"""

    def setUp(self):
        """Set up test fixtures"""
        # Clear the token cache before each test
        WinthropClient.RefreshToken._token_cache = {}
        
        # Set up test credentials
        WinthropClient.RefreshToken.client_id = "test_client_id"
        WinthropClient.RefreshToken.client_secret = "test_client_secret"
        WinthropClient.RefreshToken.host = "https://test.example.com/oauth/token"

    def tearDown(self):
        """Clean up after each test"""
        WinthropClient.RefreshToken._token_cache = {}
        WinthropClient.RefreshToken.client_id = None
        WinthropClient.RefreshToken.client_secret = None
        WinthropClient.RefreshToken.host = None

    def test_get_cache_key_no_scopes(self):
        """Test cache key generation without scopes"""
        cache_key = WinthropClient.RefreshToken._get_cache_key(None)
        self.assertEqual(cache_key, "no_scopes")

    def test_get_cache_key_with_scopes(self):
        """Test cache key generation with scopes"""
        scopes = ["read", "write"]
        cache_key = WinthropClient.RefreshToken._get_cache_key(scopes)
        self.assertEqual(cache_key, "read,write")

    def test_get_cache_key_sorted_scopes(self):
        """Test cache key generation sorts scopes"""
        scopes1 = ["write", "read"]
        scopes2 = ["read", "write"]
        cache_key1 = WinthropClient.RefreshToken._get_cache_key(scopes1)
        cache_key2 = WinthropClient.RefreshToken._get_cache_key(scopes2)
        self.assertEqual(cache_key1, cache_key2)
        self.assertEqual(cache_key1, "read,write")

    def test_token_params_no_scopes(self):
        """Test token params generation without scopes"""
        params = WinthropClient.RefreshToken._token_params(None)
        expected = {
            "grant_type": "client_credentials",
            "client_id": "test_client_id",
            "client_secret": "test_client_secret",
        }
        self.assertEqual(params, expected)

    def test_token_params_with_scopes(self):
        """Test token params generation with scopes"""
        scopes = ["read", "write", "admin"]
        params = WinthropClient.RefreshToken._token_params(scopes)
        expected = {
            "grant_type": "client_credentials",
            "client_id": "test_client_id",
            "client_secret": "test_client_secret",
            "scope": "read write admin",
        }
        self.assertEqual(params, expected)

    @patch("winthrop_client_python.refresh_token.urllib3.PoolManager")
    def test_access_token_without_scopes(self, mock_pool_manager):
        """Test access token generation without scopes"""
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = json.dumps({
            "access_token": "test_token_123",
            "expires_in": 3600
        }).encode("utf-8")
        
        mock_http = Mock()
        mock_http.request.return_value = mock_response
        mock_pool_manager.return_value = mock_http
        
        # Get access token
        token = WinthropClient.RefreshToken.access_token()
        
        # Verify the token
        self.assertEqual(token, "test_token_123")
        
        # Verify the cache
        cache_key = "no_scopes"
        self.assertIn(cache_key, WinthropClient.RefreshToken._token_cache)
        self.assertEqual(
            WinthropClient.RefreshToken._token_cache[cache_key]["token"],
            "test_token_123"
        )

    @patch("winthrop_client_python.refresh_token.urllib3.PoolManager")
    def test_access_token_with_scopes(self, mock_pool_manager):
        """Test access token generation with scopes"""
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = json.dumps({
            "access_token": "scoped_token_456",
            "expires_in": 3600
        }).encode("utf-8")
        
        mock_http = Mock()
        mock_http.request.return_value = mock_response
        mock_pool_manager.return_value = mock_http
        
        # Get access token with scopes
        scopes = ["read", "write"]
        token = WinthropClient.RefreshToken.access_token(scopes=scopes)
        
        # Verify the token
        self.assertEqual(token, "scoped_token_456")
        
        # Verify the request was made with scopes
        call_args = mock_http.request.call_args
        self.assertIn("scope=read+write", call_args[1]["body"])

    @patch("winthrop_client_python.refresh_token.urllib3.PoolManager")
    def test_multiple_scopes_cached_separately(self, mock_pool_manager):
        """Test that tokens with different scopes are cached separately"""
        # Mock the HTTP response for first scope set
        mock_response1 = Mock()
        mock_response1.status = 200
        mock_response1.data = json.dumps({
            "access_token": "token_read",
            "expires_in": 3600
        }).encode("utf-8")
        
        # Mock the HTTP response for second scope set
        mock_response2 = Mock()
        mock_response2.status = 200
        mock_response2.data = json.dumps({
            "access_token": "token_admin",
            "expires_in": 3600
        }).encode("utf-8")
        
        mock_http = Mock()
        mock_http.request.side_effect = [mock_response1, mock_response2]
        mock_pool_manager.return_value = mock_http
        
        # Get tokens with different scopes
        token1 = WinthropClient.RefreshToken.access_token(scopes=["read"])
        token2 = WinthropClient.RefreshToken.access_token(scopes=["admin"])
        
        # Verify different tokens
        self.assertEqual(token1, "token_read")
        self.assertEqual(token2, "token_admin")
        self.assertNotEqual(token1, token2)
        
        # Verify both are cached
        self.assertEqual(len(WinthropClient.RefreshToken._token_cache), 2)
        self.assertIn("read", WinthropClient.RefreshToken._token_cache)
        self.assertIn("admin", WinthropClient.RefreshToken._token_cache)

    @patch("winthrop_client_python.refresh_token.urllib3.PoolManager")
    @patch("winthrop_client_python.refresh_token.time.time")
    def test_token_caching_and_reuse(self, mock_time, mock_pool_manager):
        """Test that tokens are cached and reused when not expired"""
        # Set initial time
        mock_time.return_value = 1000.0
        
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = json.dumps({
            "access_token": "cached_token",
            "expires_in": 3600
        }).encode("utf-8")
        
        mock_http = Mock()
        mock_http.request.return_value = mock_response
        mock_pool_manager.return_value = mock_http
        
        # First call - should make HTTP request
        token1 = WinthropClient.RefreshToken.access_token()
        self.assertEqual(mock_http.request.call_count, 1)
        
        # Advance time but not past expiration
        mock_time.return_value = 2000.0
        
        # Second call - should use cache, no new HTTP request
        token2 = WinthropClient.RefreshToken.access_token()
        self.assertEqual(mock_http.request.call_count, 1)
        
        # Verify same token
        self.assertEqual(token1, token2)

    @patch("winthrop_client_python.refresh_token.urllib3.PoolManager")
    @patch("winthrop_client_python.refresh_token.time.time")
    def test_token_refresh_on_expiration(self, mock_time, mock_pool_manager):
        """Test that tokens are refreshed when expired"""
        # Set initial time
        mock_time.return_value = 1000.0
        
        # Mock the HTTP responses
        mock_response1 = Mock()
        mock_response1.status = 200
        mock_response1.data = json.dumps({
            "access_token": "token_1",
            "expires_in": 3600
        }).encode("utf-8")
        
        mock_response2 = Mock()
        mock_response2.status = 200
        mock_response2.data = json.dumps({
            "access_token": "token_2",
            "expires_in": 3600
        }).encode("utf-8")
        
        mock_http = Mock()
        mock_http.request.side_effect = [mock_response1, mock_response2]
        mock_pool_manager.return_value = mock_http
        
        # First call
        token1 = WinthropClient.RefreshToken.access_token()
        self.assertEqual(token1, "token_1")
        
        # Advance time past expiration
        mock_time.return_value = 5000.0
        
        # Second call - should refresh
        token2 = WinthropClient.RefreshToken.access_token()
        self.assertEqual(token2, "token_2")
        
        # Verify two HTTP requests were made
        self.assertEqual(mock_http.request.call_count, 2)

    @patch("winthrop_client_python.refresh_token.urllib3.PoolManager")
    def test_error_handling_non_200_response(self, mock_pool_manager):
        """Test error handling for non-200 responses"""
        # Mock a failed HTTP response
        mock_response = Mock()
        mock_response.status = 401
        mock_response.data = b"Unauthorized"
        
        mock_http = Mock()
        mock_http.request.return_value = mock_response
        mock_pool_manager.return_value = mock_http
        
        # Verify exception is raised
        with self.assertRaises(Exception) as context:
            WinthropClient.RefreshToken.access_token()
        
        self.assertIn("Failed to retrieve access token", str(context.exception))
        self.assertIn("401", str(context.exception))

    @patch("winthrop_client_python.refresh_token.urllib3.PoolManager")
    def test_scopes_none_vs_empty_list(self, mock_pool_manager):
        """Test that None scopes and empty list are treated differently"""
        # Mock responses
        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = json.dumps({
            "access_token": "test_token",
            "expires_in": 3600
        }).encode("utf-8")
        
        mock_http = Mock()
        mock_http.request.return_value = mock_response
        mock_pool_manager.return_value = mock_http
        
        # Get token with None scopes
        token1 = WinthropClient.RefreshToken.access_token(scopes=None)
        
        # Get token with empty list scopes
        token2 = WinthropClient.RefreshToken.access_token(scopes=[])
        
        # Both should return tokens
        self.assertEqual(token1, "test_token")
        self.assertEqual(token2, "test_token")
        
        # Verify cache keys are different
        cache_key_none = WinthropClient.RefreshToken._get_cache_key(None)
        cache_key_empty = WinthropClient.RefreshToken._get_cache_key([])
        self.assertNotEqual(cache_key_none, cache_key_empty)


if __name__ == "__main__":
    unittest.main()
