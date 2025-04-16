"""
Configuration management for the Briq client.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

class Config:
    """
    Configuration class for the Briq client.
    
    Handles API key management, loading from environment variables or .env files,
    and allows manual setting of configuration values.
    """
    
    def __init__(self, api_key=None, base_url=None):
        """
        Initialize the Config object.
        
        Args:
            api_key (str, optional): API key for authentication. If not provided,
                                     will attempt to load from environment.
            base_url (str, optional): Base URL for the API. If not provided,
                                      will use the default URL.
        """
        # Try to load from .env file if it exists
        env_path = Path('.') / '.env'
        if env_path.exists():
            load_dotenv(dotenv_path=env_path)
        
        self._api_key = api_key or os.environ.get('BRIQ_API_KEY')
        self._base_url = base_url or os.environ.get('BRIQ_BASE_URL', 'http://143.198.159.135:8000')
    
    @property
    def api_key(self):
        """Get the API key."""
        return self._api_key
    
    @api_key.setter
    def api_key(self, value):
        """Set the API key."""
        self._api_key = value
    
    @property
    def base_url(self):
        """Get the base URL."""
        return self._base_url
    
    @base_url.setter
    def base_url(self, value):
        """Set the base URL."""
        self._base_url = value
    
    @property
    def headers(self):
        """
        Get the headers for API requests.
        
        Returns:
            dict: Headers including the API key.
        
        Raises:
            ValueError: If API key is not set.
        """
        if not self._api_key:
            raise ValueError("API key not set. Set it using client.config.api_key = 'your_api_key' or by setting the BRIQ_API_KEY environment variable.")
        
        return {
            "X-API-Key": self._api_key,
            "Content-Type": "application/json"
        }
