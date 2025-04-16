"""
Client implementation for the Briq API.
"""

import json
import requests
from .config import Config
from .workspace import WorkspaceAPI
from .campaign import CampaignAPI
from .message import MessageAPI

class Client:
    """
    Main client class for interacting with the Briq API.
    
    Provides access to all API endpoints through dedicated modules.
    """
    
    def __init__(self, api_key=None, base_url=None):
        """
        Initialize the Briq client.
        
        Args:
            api_key (str, optional): API key for authentication. If not provided,
                                     will attempt to load from environment.
            base_url (str, optional): Base URL for the API. If not provided,
                                      will use the default URL.
        """
        self.config = Config(api_key=api_key, base_url=base_url)
        self.session = requests.Session()
        
        # Initialize API modules
        self.workspace = WorkspaceAPI(self)
        self.campaign = CampaignAPI(self)
        self.message = MessageAPI(self)
    
    def request(self, method, endpoint, data=None, params=None):
        """
        Make a request to the Briq API.
        
        Args:
            method (str): HTTP method (GET, POST, PATCH, etc.)
            endpoint (str): API endpoint path
            data (dict, optional): Request body data
            params (dict, optional): Query parameters
            
        Returns:
            dict: Response data
            
        Raises:
            BriqAPIError: If the API returns an error
            BriqAuthError: If authentication fails
            BriqRequestError: If the request fails
        """
        from .exceptions import BriqAPIError, BriqAuthError, BriqRequestError
        
        url = f"{self.config.base_url}/v1/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=self.config.headers,
                json=data,
                params=params
            )
            
            response.raise_for_status()
            
            if response.content:
                return response.json()
            return {}
            
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                raise BriqAuthError("Authentication failed. Check your API key.")
            elif response.status_code == 400:
                error_data = response.json() if response.content else {"error": "Bad request"}
                raise BriqAPIError(f"API error: {error_data}")
            else:
                raise BriqAPIError(f"API error: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise BriqRequestError(f"Request failed: {str(e)}")
    
    def get(self, endpoint, params=None):
        """Convenience method for GET requests."""
        return self.request("GET", endpoint, params=params)
    
    def post(self, endpoint, data=None):
        """Convenience method for POST requests."""
        return self.request("POST", endpoint, data=data)
    
    def patch(self, endpoint, data=None):
        """Convenience method for PATCH requests."""
        return self.request("PATCH", endpoint, data=data)
    
    def set_api_key(self, api_key):
        """
        Set the API key for authentication.
        
        Args:
            api_key (str): The API key to use
        """
        self.config.api_key = api_key
