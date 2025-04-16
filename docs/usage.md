# Briq Python Client Usage Guide

This guide provides detailed instructions on how to use the Briq Python client library to interact with the Briq messaging platform API.

## Table of Contents

- [Installation](#installation)
- [Authentication](#authentication)
- [Client Initialization](#client-initialization)
- [Workspace Management](#workspace-management)
- [Campaign Management](#campaign-management)
- [Message Management](#message-management)
- [Error Handling](#error-handling)

## Installation

You can install the Briq client library using pip:

```bash
pip install briq
```

## Authentication

The Briq client requires an API key for authentication. You can provide your API key in several ways:

### Environment Variable

Set the `BRIQ_API_KEY` environment variable:

```bash
export BRIQ_API_KEY=your_api_key_here
```

### .env File

Create a `.env` file in your project directory with the following content:

```
BRIQ_API_KEY=your_api_key_here
```

The library will automatically load this file if it exists.

### Manual Configuration

You can also set the API key directly in your code:

```python
import briq

client = briq.Client(api_key="your_api_key_here")

# Or after initialization:
client.set_api_key("your_api_key_here")
```

## Client Initialization

Import the library and create a client instance:

```python
import briq

# Initialize with default settings (loads API key from environment or .env)
client = briq.Client()

# Or specify API key and base URL explicitly
client = briq.Client(
    api_key="your_api_key_here",
    base_url="http://143.198.159.135:8000"
)
```

## Workspace Management

The Briq client provides methods for managing workspaces through the `workspace` module.

### Create a Workspace

```python
workspace = client.workspace.create(
    name="My Workspace",
    description="A workspace for my messaging campaigns"
)
print(f"Created workspace with ID: {workspace['id']}")
```

### List All Workspaces

```python
workspaces = client.workspace.list()
for workspace in workspaces:
    print(f"Workspace: {workspace['name']} (ID: {workspace['id']})")
```

### Get a Workspace by ID

```python
workspace_id = "workspace-uuid"
workspace = client.workspace.get(workspace_id)
print(f"Retrieved workspace: {workspace['name']}")
```

### Update a Workspace

```python
workspace_id = "workspace-uuid"
updated_workspace = client.workspace.update(
    workspace_id,
    name="Updated Workspace Name",
    description="Updated workspace description"
)
print(f"Updated workspace: {updated_workspace['name']}")
```

## Campaign Management

The Briq client provides methods for managing campaigns through the `campaign` module.

### Create a Campaign

```python
campaign = client.campaign.create(
    workspace_id="workspace-uuid",
    name="My Campaign",
    description="A messaging campaign",
    launch_date="2023-12-01T00:00:00"
)
print(f"Created campaign with ID: {campaign['id']}")
```

### List All Campaigns

```python
campaigns = client.campaign.list()
for campaign in campaigns:
    print(f"Campaign: {campaign['name']} (ID: {campaign['id']})")
```

### Get a Campaign by ID

```python
campaign_id = "campaign-uuid"
campaign = client.campaign.get(campaign_id)
print(f"Retrieved campaign: {campaign['name']}")
```

### Update a Campaign

```python
campaign_id = "campaign-uuid"
updated_campaign = client.campaign.update(
    campaign_id,
    name="Updated Campaign Name",
    description="Updated campaign description",
    launch_date="2023-12-15T00:00:00"
)
print(f"Updated campaign: {updated_campaign['name']}")
```

## Message Management

The Briq client provides methods for sending and managing messages through the `message` module.

### Send an Instant Message

```python
result = client.message.send_instant(
    content="Hello from the Briq Python client!",
    recipients=["255788344348"],
    sender_id="my-sender-id",
    campaign_id="optional-campaign-uuid"  # Optional
)
print(f"Message sent with ID: {result['message_id']}")
```

### Send a Campaign Message

```python
result = client.message.send_campaign(
    campaign_id="campaign-uuid",
    group_id="group-uuid",
    content="Campaign message content",
    sender_id="my-sender-id"
)
print(f"Campaign message sent with ID: {result['message_id']}")
```

### Get Message Logs

```python
logs = client.message.get_logs()
for log in logs:
    print(f"Message: {log['content']} - Status: {log['status']}")
```

### Get User Message History

```python
history = client.message.get_history()
for message in history:
    print(f"Message: {message['content']} - Sent at: {message['sent_at']}")
```

## Error Handling

The Briq client raises specific exceptions for different types of errors:

```python
import briq
from briq.exceptions import BriqAuthError, BriqAPIError, BriqRequestError

try:
    # Attempt to use the API
    client = briq.Client()
    workspaces = client.workspace.list()
except BriqAuthError as e:
    print(f"Authentication error: {e}")
except BriqAPIError as e:
    print(f"API error: {e}")
except BriqRequestError as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

Common exceptions:

- `BriqAuthError`: Raised when authentication fails (e.g., invalid API key)
- `BriqAPIError`: Raised when the API returns an error (e.g., invalid request data)
- `BriqRequestError`: Raised when the request fails (e.g., network issues)
- `BriqConfigError`: Raised when there's a configuration error (e.g., missing API key)
