import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from briq.client import Client
from briq.exceptions import BriqAuthError, BriqAPIError, BriqRequestError

class TestClient(unittest.TestCase):
    def setUp(self):
        # Create a client with a dummy API key for testing
        self.client = Client(api_key="test_api_key")
    
    def test_init(self):
        # Test client initialization
        self.assertIsNotNone(self.client)
        self.assertEqual(self.client.config.api_key, "test_api_key")
        self.assertEqual(self.client.config.base_url, "http://143.198.159.135:8000")
        
        # Test initialization with custom base URL
        client = Client(api_key="test_api_key", base_url="http://custom-url")
        self.assertEqual(client.config.base_url, "http://custom-url")
    
    def test_set_api_key(self):
        # Test setting API key
        self.client.set_api_key("new_api_key")
        self.assertEqual(self.client.config.api_key, "new_api_key")
    
    @patch('requests.Session.request')
    def test_request_success(self, mock_request):
        # Mock successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'{"key": "value"}'
        mock_response.json.return_value = {"key": "value"}
        mock_request.return_value = mock_response
        
        # Test request method
        result = self.client.request("GET", "test/endpoint")
        
        # Verify request was made correctly
        mock_request.assert_called_once_with(
            method="GET",
            url="http://143.198.159.135:8000/v1/test/endpoint",
            headers=self.client.config.headers,
            json=None,
            params=None
        )
        
        # Verify result
        self.assertEqual(result, {"key": "value"})
    
    @patch('requests.Session.request')
    def test_request_auth_error(self, mock_request):
        # Mock 401 response
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.raise_for_status.side_effect = Exception("401 Client Error")
        mock_request.return_value = mock_response
        
        # Test request method with auth error
        with self.assertRaises(BriqAuthError):
            self.client.request("GET", "test/endpoint")
    
    @patch('requests.Session.request')
    def test_request_api_error(self, mock_request):
        # Mock 400 response
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.content = b'{"error": "Bad request"}'
        mock_response.json.return_value = {"error": "Bad request"}
        mock_response.raise_for_status.side_effect = Exception("400 Client Error")
        mock_request.return_value = mock_response
        
        # Test request method with API error
        with self.assertRaises(BriqAPIError):
            self.client.request("GET", "test/endpoint")
    
    @patch('requests.Session.request')
    def test_request_network_error(self, mock_request):
        # Mock network error
        mock_request.side_effect = Exception("Connection error")
        
        # Test request method with network error
        with self.assertRaises(BriqRequestError):
            self.client.request("GET", "test/endpoint")
    
    @patch('briq.client.Client.request')
    def test_get(self, mock_request):
        # Test get method
        self.client.get("test/endpoint", params={"param": "value"})
        mock_request.assert_called_once_with("GET", "test/endpoint", params={"param": "value"})
    
    @patch('briq.client.Client.request')
    def test_post(self, mock_request):
        # Test post method
        self.client.post("test/endpoint", data={"key": "value"})
        mock_request.assert_called_once_with("POST", "test/endpoint", data={"key": "value"})
    
    @patch('briq.client.Client.request')
    def test_patch(self, mock_request):
        # Test patch method
        self.client.patch("test/endpoint", data={"key": "value"})
        mock_request.assert_called_once_with("PATCH", "test/endpoint", data={"key": "value"})

if __name__ == '__main__':
    unittest.main()
