"""
Briq Python Client Library

A Python client for the Briq messaging platform API.
"""

__version__ = "0.1.0"

from .client import Client
from .config import Config

# Create a default client instance that can be imported directly
client = Client()

__all__ = ["Client", "Config", "client"]
