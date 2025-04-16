import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from briq.campaign import CampaignAPI

class TestCampaignAPI(unittest.TestCase):
    def setUp(self):
        # Create a mock client
        self.mock_client = MagicMock()
        self.campaign_api = CampaignAPI(self.mock_client)
    
    def test_init(self):
        # Test initialization
        self.assertIsNotNone(self.campaign_api)
        self.assertEqual(self.campaign_api.client, self.mock_client)
    
    def test_create(self):
        # Test create method with all parameters
        self.campaign_api.create(
            "workspace-1", 
            "Test Campaign", 
            "Test Description", 
            "2023-12-01T00:00:00"
        )
        
        # Verify client.post was called with correct arguments
        self.mock_client.post.assert_called_once_with(
            "campaign/create/",
            data={
                "workspace_id": "workspace-1",
                "name": "Test Campaign",
                "description": "Test Description",
                "launch_date": "2023-12-01T00:00:00"
            }
        )
        
        # Test create with only required parameters
        self.mock_client.post.reset_mock()
        self.campaign_api.create("workspace-1", "Test Campaign")
        
        # Verify client.post was called with correct arguments
        self.mock_client.post.assert_called_once_with(
            "campaign/create/",
            data={
                "workspace_id": "workspace-1",
                "name": "Test Campaign"
            }
        )
    
    def test_list(self):
        # Mock response
        mock_response = [
            {"id": "campaign-1", "name": "Campaign 1"},
            {"id": "campaign-2", "name": "Campaign 2"}
        ]
        self.mock_client.get.return_value = mock_response
        
        # Test list method
        result = self.campaign_api.list()
        
        # Verify client.get was called with correct arguments
        self.mock_client.get.assert_called_once_with("campaign/all/")
        
        # Verify result
        self.assertEqual(result, mock_response)
    
    def test_get(self):
        # Mock response
        mock_response = {"id": "campaign-1", "name": "Campaign 1"}
        self.mock_client.get.return_value = mock_response
        
        # Test get method
        result = self.campaign_api.get("campaign-1")
        
        # Verify client.get was called with correct arguments
        self.mock_client.get.assert_called_once_with("campaign/campaign-1/")
        
        # Verify result
        self.assertEqual(result, mock_response)
    
    def test_update(self):
        # Test update method with all parameters
        self.campaign_api.update(
            "campaign-1", 
            "Updated Name", 
            "Updated Description", 
            "2023-12-15T00:00:00"
        )
        
        # Verify client.patch was called with correct arguments
        self.mock_client.patch.assert_called_once_with(
            "campaign/update/campaign-1",
            data={
                "name": "Updated Name",
                "description": "Updated Description",
                "launch_date": "2023-12-15T00:00:00"
            }
        )
        
        # Test update with only name
        self.mock_client.patch.reset_mock()
        self.campaign_api.update("campaign-1", "Updated Name")
        
        # Verify client.patch was called with correct arguments
        self.mock_client.patch.assert_called_once_with(
            "campaign/update/campaign-1",
            data={"name": "Updated Name"}
        )
        
        # Test update with only description
        self.mock_client.patch.reset_mock()
        self.campaign_api.update("campaign-1", description="Updated Description")
        
        # Verify client.patch was called with correct arguments
        self.mock_client.patch.assert_called_once_with(
            "campaign/update/campaign-1",
            data={"description": "Updated Description"}
        )
        
        # Test update with only launch_date
        self.mock_client.patch.reset_mock()
        self.campaign_api.update("campaign-1", launch_date="2023-12-15T00:00:00")
        
        # Verify client.patch was called with correct arguments
        self.mock_client.patch.assert_called_once_with(
            "campaign/update/campaign-1",
            data={"launch_date": "2023-12-15T00:00:00"}
        )
        
        # Test update with no changes
        self.mock_client.patch.reset_mock()
        self.campaign_api.update("campaign-1")
        
        # Verify client.patch was called with correct arguments
        self.mock_client.patch.assert_called_once_with(
            "campaign/update/campaign-1",
            data={}
        )

if __name__ == '__main__':
    unittest.main()
