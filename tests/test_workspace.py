import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from briq.workspace import WorkspaceAPI

class TestWorkspaceAPI(unittest.TestCase):
    def setUp(self):
        # Create a mock client
        self.mock_client = MagicMock()
        self.workspace_api = WorkspaceAPI(self.mock_client)
    
    def test_init(self):
        # Test initialization
        self.assertIsNotNone(self.workspace_api)
        self.assertEqual(self.workspace_api.client, self.mock_client)
    
    def test_create(self):
        # Test create method
        self.workspace_api.create("Test Workspace", "Test Description")
        
        # Verify client.post was called with correct arguments
        self.mock_client.post.assert_called_once_with(
            "workspace/create/",
            data={"name": "Test Workspace", "description": "Test Description"}
        )
        
        # Test create with only name
        self.mock_client.post.reset_mock()
        self.workspace_api.create("Test Workspace")
        
        # Verify client.post was called with correct arguments
        self.mock_client.post.assert_called_once_with(
            "workspace/create/",
            data={"name": "Test Workspace"}
        )
    
    def test_list(self):
        # Mock response
        mock_response = [
            {"id": "workspace-1", "name": "Workspace 1"},
            {"id": "workspace-2", "name": "Workspace 2"}
        ]
        self.mock_client.get.return_value = mock_response
        
        # Test list method
        result = self.workspace_api.list()
        
        # Verify client.get was called with correct arguments
        self.mock_client.get.assert_called_once_with("workspace/all/")
        
        # Verify result
        self.assertEqual(result, mock_response)
    
    def test_get(self):
        # Mock response
        mock_response = {"id": "workspace-1", "name": "Workspace 1"}
        self.mock_client.get.return_value = mock_response
        
        # Test get method
        result = self.workspace_api.get("workspace-1")
        
        # Verify client.get was called with correct arguments
        self.mock_client.get.assert_called_once_with("workspace/workspace-1")
        
        # Verify result
        self.assertEqual(result, mock_response)
    
    def test_update(self):
        # Test update method with both name and description
        self.workspace_api.update("workspace-1", "Updated Name", "Updated Description")
        
        # Verify client.patch was called with correct arguments
        self.mock_client.patch.assert_called_once_with(
            "workspace/update/workspace-1",
            data={"name": "Updated Name", "description": "Updated Description"}
        )
        
        # Test update with only name
        self.mock_client.patch.reset_mock()
        self.workspace_api.update("workspace-1", "Updated Name")
        
        # Verify client.patch was called with correct arguments
        self.mock_client.patch.assert_called_once_with(
            "workspace/update/workspace-1",
            data={"name": "Updated Name"}
        )
        
        # Test update with only description
        self.mock_client.patch.reset_mock()
        self.workspace_api.update("workspace-1", description="Updated Description")
        
        # Verify client.patch was called with correct arguments
        self.mock_client.patch.assert_called_once_with(
            "workspace/update/workspace-1",
            data={"description": "Updated Description"}
        )
        
        # Test update with no changes
        self.mock_client.patch.reset_mock()
        self.workspace_api.update("workspace-1")
        
        # Verify client.patch was called with correct arguments
        self.mock_client.patch.assert_called_once_with(
            "workspace/update/workspace-1",
            data={}
        )

if __name__ == '__main__':
    unittest.main()
