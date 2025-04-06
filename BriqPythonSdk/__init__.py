"""
Briq API SDK
~~~~~~~~~~~~

A Python SDK for interacting with the Briq messaging API.

Basic usage:

    >>> from BriqPythonSdk import BriqClient
    >>> client = BriqClient(username="your_username", password="your_password")
    >>> workspaces = client.get_workspaces()
    >>> response = client.send_message(
    ...     workspace_id="your_workspace_id",
    ...     recipients=["+1234567890"],
    ...     content="Hello from Briq SDK!",
    ...     sender_id="YourSenderId"
    ... )

"""

from .client import (
    BriqClient,
    BriqAuthenticationError,
    BriqAPIError,
    BriqMessageError
)

__all__ = [
    'BriqClient',
    'BriqAuthenticationError',
    'BriqAPIError',
    'BriqMessageError'
]

__version__ = '0.1.0'