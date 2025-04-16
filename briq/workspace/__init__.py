"""
Workspace management module for the Briq API.
"""

class WorkspaceAPI:
    """
    Workspace management API for Briq.
    
    Provides methods for creating, listing, retrieving, and updating workspaces.
    """
    
    def __init__(self, client):
        """
        Initialize the Workspace API module.
        
        Args:
            client: The Briq client instance
        """
        self.client = client
    
    def create(self, name, description=None):
        """
        Create a new workspace.
        
        Args:
            name (str): Name of the workspace
            description (str, optional): Description of the workspace
            
        Returns:
            dict: Created workspace data
        """
        data = {
            "name": name
        }
        
        if description:
            data["description"] = description
            
        return self.client.post("workspace/create/", data=data)
    
    def list(self):
        """
        List all workspaces.
        
        Returns:
            list: List of workspaces
        """
        return self.client.get("workspace/all/")
    
    def get(self, workspace_id):
        """
        Get a workspace by ID.
        
        Args:
            workspace_id (str): ID of the workspace to retrieve
            
        Returns:
            dict: Workspace data
        """
        return self.client.get(f"workspace/{workspace_id}")
    
    def update(self, workspace_id, name=None, description=None):
        """
        Update a workspace.
        
        Args:
            workspace_id (str): ID of the workspace to update
            name (str, optional): New name for the workspace
            description (str, optional): New description for the workspace
            
        Returns:
            dict: Updated workspace data
        """
        data = {}
        
        if name:
            data["name"] = name
            
        if description:
            data["description"] = description
            
        return self.client.patch(f"workspace/update/{workspace_id}", data=data)
