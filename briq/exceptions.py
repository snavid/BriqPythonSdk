"""
Exception classes for the Briq client.
"""

class BriqError(Exception):
    """Base exception for all Briq-related errors."""
    pass

class BriqAuthError(BriqError):
    """Raised when authentication fails."""
    pass

class BriqAPIError(BriqError):
    """Raised when the API returns an error."""
    pass

class BriqRequestError(BriqError):
    """Raised when a request to the API fails."""
    pass

class BriqConfigError(BriqError):
    """Raised when there's a configuration error."""
    pass
