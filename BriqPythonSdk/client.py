import requests
import json
from typing import List, Dict, Any


class BriqClient:
    """
    SDK for interacting with the Briq API.
    Handles authentication and caching of access tokens.
    """
    
    BASE_URL = "https://heading-to-paris-op.briq.tz"
    
    def __init__(self, username: str, password: str):
        """
        Initialize the Briq client with credentials.
        
        Args:
            username: The username for authentication
            password: The password for authentication
        """
        self.username = username
        self.password = password
        self.cached_token = None
        self.token_type = None
    
    def _authenticate(self) -> None:
        """
        Authenticate with the Briq API and cache the access token.
        """
        url = f"{self.BASE_URL}/auth/login"
        
        payload = {
            'username': self.username,
            'password': self.password
        }
        
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            
            response_data = response.json()
            self.cached_token = response_data['access_token']
            self.token_type = response_data['token_type']
        except requests.exceptions.RequestException as e:
            raise BriqAuthenticationError(f"Authentication failed: {str(e)}")
    
    def _get_headers(self) -> Dict[str, str]:
        """
        Get headers with authentication token.
        
        Returns:
            Dict containing the authorization headers
        """
        if not self.cached_token:
            self._authenticate()
            
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.cached_token}'
        }
    
    def get_workspaces(self) -> List[Dict[str, str]]:
        """
        Get all workspaces accessible to the authenticated user.
        
        Returns:
            List of workspace objects containing details like workspace_id and available sender IDs
            
        Raises:
            BriqAPIError: If retrieving workspaces fails
        """
        url = f"{self.BASE_URL}/workspaces/"

        try:
            headers = self._get_headers()
            response = requests.get(url, headers=headers)
            
            # Check if token is invalid and retry with fresh token if needed
            if response.status_code == 401 and "Invalid token" in response.text:
                self.cached_token = None
                headers = self._get_headers()  # This will re-authenticate
                response = requests.get(url, headers=headers)
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise BriqAPIError(f"Failed to get workspaces: {str(e)}")
    
    def send_message(self, 
                     workspace_id: str, 
                     recipients: List[str], 
                     content: str, 
                     sender_id: str) -> Dict[str, Any]:
        """
        Send an instant message to specified recipients.
        
        Args:
            workspace_id: The ID of the workspace
            recipients: List of recipient phone numbers (with country code)
            content: The message content
            sender_id: The sender ID to display
            
        Returns:
            The API response as a dictionary
            
        Raises:
            BriqMessageError: If sending the message fails
        """
        url = f"{self.BASE_URL}/messages/send-instant"
        
        payload = json.dumps({
            "workspace_id": workspace_id,
            "recipients": recipients,
            "content": content,
            "sender_id": sender_id
        })
        
        try:
            headers = self._get_headers()
            response = requests.post(url, headers=headers, data=payload)
            
            # Check if token is invalid and retry with fresh token if needed
            if response.status_code == 401 and "Invalid token" in response.text:
                self.cached_token = None
                headers = self._get_headers()  # This will re-authenticate
                response = requests.post(url, headers=headers, data=payload)
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise BriqMessageError(f"Failed to send message: {str(e)}")


class BriqAuthenticationError(Exception):
    """Exception raised for authentication errors with the Briq API."""
    pass


class BriqAPIError(Exception):
    """Exception raised for general API errors with the Briq API."""
    pass


class BriqMessageError(Exception):
    """Exception raised for errors when sending messages via the Briq API."""
    pass