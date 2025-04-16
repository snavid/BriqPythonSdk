import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from briq.message import MessageAPI

class TestMessageAPI(unittest.TestCase):
    def setUp(self):
        # Create a mock client
        self.mock_client = MagicMock()
        self.message_api = MessageAPI(self.mock_client)
    
    def test_init(self):
        # Test initialization
        self.assertIsNotNone(self.message_api)
        self.assertEqual(self.message_api.client, self.mock_client)
    
    def test_send_instant(self):
        # Test send_instant method with all parameters
        self.message_api.send_instant(
            "Hello, this is a test message",
            ["255788344348", "255712345678"],
            "test-sender",
            "campaign-1"
        )
        
        # Verify client.post was called with correct arguments
        self.mock_client.post.assert_called_once_with(
            "message/send-instant",
            data={
                "content": "Hello, this is a test message",
                "recipients": ["255788344348", "255712345678"],
                "sender_id": "test-sender",
                "campaign_id": "campaign-1"
            }
        )
        
        # Test send_instant without campaign_id
        self.mock_client.post.reset_mock()
        self.message_api.send_instant(
            "Hello, this is a test message",
            ["255788344348"],
            "test-sender"
        )
        
        # Verify client.post was called with correct arguments
        self.mock_client.post.assert_called_once_with(
            "message/send-instant",
            data={
                "content": "Hello, this is a test message",
                "recipients": ["255788344348"],
                "sender_id": "test-sender"
            }
        )
    
    def test_send_campaign(self):
        # Test send_campaign method
        self.message_api.send_campaign(
            "campaign-1",
            "group-1",
            "Campaign message content",
            "test-sender"
        )
        
        # Verify client.post was called with correct arguments
        self.mock_client.post.assert_called_once_with(
            "message/send-campaign",
            data={
                "campaign_id": "campaign-1",
                "group_id": "group-1",
                "content": "Campaign message content",
                "sender_id": "test-sender"
            }
        )
    
    def test_get_logs(self):
        # Mock response
        mock_response = [
            {"id": "message-1", "content": "Message 1", "status": "delivered"},
            {"id": "message-2", "content": "Message 2", "status": "sent"}
        ]
        self.mock_client.get.return_value = mock_response
        
        # Test get_logs method
        result = self.message_api.get_logs()
        
        # Verify client.get was called with correct arguments
        self.mock_client.get.assert_called_once_with("message/logs")
        
        # Verify result
        self.assertEqual(result, mock_response)
    
    def test_get_history(self):
        # Mock response
        mock_response = [
            {"id": "message-1", "content": "Message 1", "sent_at": "2023-01-01T12:00:00"},
            {"id": "message-2", "content": "Message 2", "sent_at": "2023-01-02T12:00:00"}
        ]
        self.mock_client.get.return_value = mock_response
        
        # Test get_history method
        result = self.message_api.get_history()
        
        # Verify client.get was called with correct arguments
        self.mock_client.get.assert_called_once_with("message/history")
        
        # Verify result
        self.assertEqual(result, mock_response)

if __name__ == '__main__':
    unittest.main()
