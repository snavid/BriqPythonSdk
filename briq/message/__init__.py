"""
Message management module for the Briq API.
"""

class MessageAPI:
    """
    Message management API for Briq.
    
    Provides methods for sending instant messages, campaign messages, and retrieving message logs.
    """
    
    def __init__(self, client):
        """
        Initialize the Message API module.
        
        Args:
            client: The Briq client instance
        """
        self.client = client
    
    def send_instant(self, content, recipients, sender_id, campaign_id=None):
        """
        Send an instant message.
        
        Args:
            content (str): Message content
            recipients (list): List of recipient phone numbers
            sender_id (str): Registered sender ID name
            campaign_id (str, optional): Campaign ID to associate the message with
            
        Returns:
            dict: Message sending result
        """
        data = {
            "content": content,
            "recipients": recipients,
            "sender_id": sender_id
        }
        
        if campaign_id:
            data["campaign_id"] = campaign_id
            
        return self.client.post("message/send-instant", data=data)
    
    def send_campaign(self, campaign_id, group_id, content, sender_id):
        """
        Send a campaign message.
        
        Args:
            campaign_id (str): ID of the campaign
            group_id (str): ID of the recipient group
            content (str): Message content
            sender_id (str): Registered sender ID name
            
        Returns:
            dict: Message sending result
        """
        data = {
            "campaign_id": campaign_id,
            "group_id": group_id,
            "content": content,
            "sender_id": sender_id
        }
            
        return self.client.post("message/send-campaign", data=data)
    
    def get_logs(self):
        """
        Get message logs.
        
        Returns:
            list: Message logs
        """
        return self.client.get("message/logs")
    
    def get_history(self):
        """
        Get user message history.
        
        Returns:
            list: Message history
        """
        return self.client.get("message/history")
