# Briq SDK

A Python SDK for interacting with the Briq messaging API.

## Installation

```bash
pip install briq-sdk
```

Or install from source:

```bash
git clone https://github.com/snavid/briq-sdk.git
cd briq-sdk
pip install -e .
```

## Usage

### Authentication

```python
from BriqPythonSdk import BriqClient

# Initialize the client
client = BriqClient(
    username="your_username",
    password="your_password"
)
```

### Get Workspaces

Retrieve all workspaces accessible to the authenticated user:

```python
workspaces = client.get_workspaces()
print(workspaces)
```

### Send a Message

Send an instant message to one or more recipients:

```python
response = client.send_message(
    workspace_id="your_workspace_id",
    recipients=["+255788344348"],
    content="Your message content here",
    sender_id="YourSenderId"
)
print(response)
```

## Error Handling

The SDK provides specific exceptions for different types of errors:

```python
from BriqPythonSdk import BriqAuthenticationError, BriqAPIError, BriqMessageError

try:
    response = client.send_message(...)
except BriqAuthenticationError as e:
    print(f"Authentication error: {e}")
except BriqMessageError as e:
    print(f"Message sending error: {e}")
except BriqAPIError as e:
    print(f"API error: {e}")
```

## API Reference

### BriqClient

```python
BriqClient(username: str, password: str)
```

**Parameters:**
- `username`: The username for authentication
- `password`: The password for authentication

#### Methods

##### get_workspaces()

```python
get_workspaces() -> List[Dict[str, str]]
```

**Returns:**
- List of workspace objects containing details like workspace_id and available sender IDs

**Raises:**
- `BriqAPIError`: If retrieving workspaces fails

##### send_message()

```python
send_message(
    workspace_id: str,
    recipients: List[str],
    content: str,
    sender_id: str
) -> Dict[str, Any]
```

**Parameters:**
- `workspace_id`: The ID of the workspace
- `recipients`: List of recipient phone numbers (with country code)
- `content`: The message content
- `sender_id`: The sender ID to display

**Returns:**
- The API response as a dictionary

**Raises:**
- `BriqMessageError`: If sending the message fails

## License

MIT