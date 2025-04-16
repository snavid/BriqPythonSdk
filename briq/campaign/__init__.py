"""
Campaign management module for the Briq API.
"""

class CampaignAPI:
    """
    Campaign management API for Briq.
    
    Provides methods for creating, listing, retrieving, and updating campaigns.
    """
    
    def __init__(self, client):
        """
        Initialize the Campaign API module.
        
        Args:
            client: The Briq client instance
        """
        self.client = client
    
    def create(self, workspace_id, name, description=None, launch_date=None):
        """
        Create a new campaign.
        
        Args:
            workspace_id (str): ID of the workspace to create the campaign in
            name (str): Name of the campaign
            description (str, optional): Description of the campaign
            launch_date (str, optional): Launch date of the campaign in ISO format (e.g., "2023-12-01T00:00:00")
            
        Returns:
            dict: Created campaign data
        """
        data = {
            "workspace_id": workspace_id,
            "name": name
        }
        
        if description:
            data["description"] = description
            
        if launch_date:
            data["launch_date"] = launch_date
            
        return self.client.post("campaign/create/", data=data)
    
    def list(self):
        """
        List all campaigns.
        
        Returns:
            list: List of campaigns
        """
        return self.client.get("campaign/all/")
    
    def get(self, campaign_id):
        """
        Get a campaign by ID.
        
        Args:
            campaign_id (str): ID of the campaign to retrieve
            
        Returns:
            dict: Campaign data
        """
        return self.client.get(f"campaign/{campaign_id}/")
    
    def update(self, campaign_id, name=None, description=None, launch_date=None):
        """
        Update a campaign.
        
        Args:
            campaign_id (str): ID of the campaign to update
            name (str, optional): New name for the campaign
            description (str, optional): New description for the campaign
            launch_date (str, optional): New launch date in ISO format
            
        Returns:
            dict: Updated campaign data
        """
        data = {}
        
        if name:
            data["name"] = name
            
        if description:
            data["description"] = description
            
        if launch_date:
            data["launch_date"] = launch_date
            
        return self.client.patch(f"campaign/update/{campaign_id}", data=data)
