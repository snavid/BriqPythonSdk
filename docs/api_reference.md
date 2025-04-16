# Briq Python Client API Reference

This document provides detailed reference information for all classes and methods in the Briq Python client library.

## Table of Contents

- [Client](#client)
- [Config](#config)
- [WorkspaceAPI](#workspaceapi)
- [CampaignAPI](#campaignapi)
- [MessageAPI](#messageapi)
- [Exceptions](#exceptions)

## Client

The `Client` class is the main entry point for interacting with the Briq API.

### Constructor

```python
Client(api_key=None, base_url=None)
```

**Parameters:**
- `api_key` (str, optional): API key for authentication. If not provided, will attempt to load from environment.
- `base_url` (str, optional): Base URL for the API. If not provided, will use the default URL.

### Properties

- `config`: The configuration object for this client.
- `workspace`: The workspace API module.
- `campaign`: The campaign API module.
- `message`: The message API module.

### Methods

#### request

```python
request(method, endpoint, data=None, params=None)
```

Make a request to the Briq API.

**Parameters:**
- `method` (str): HTTP method (GET, POST, PATCH, etc.)
- `endpoint` (str): API endpoint path
- `data` (dict, optional): Request body data
- `params` (dict, optional): Query parameters

**Returns:**
- `dict`: Response data

**Raises:**
- `BriqAPIError`: If the API returns an error
- `BriqAuthError`: If authentication fails
- `BriqRequestError`: If the request fails

#### get

```python
get(endpoint, params=None)
```

Convenience method for GET requests.

**Parameters:**
- `endpoint` (str): API endpoint path
- `params` (dict, optional): Query parameters

**Returns:**
- `dict`: Response data

#### post

```python
post(endpoint, data=None)
```

Convenience method for POST requests.

**Parameters:**
- `endpoint` (str): API endpoint path
- `data` (dict, optional): Request body data

**Returns:**
- `dict`: Response data

#### patch

```python
patch(endpoint, data=None)
```

Convenience method for PATCH requests.

**Parameters:**
- `endpoint` (str): API endpoint path
- `data` (dict, optional): Request body data

**Returns:**
- `dict`: Response data

#### set_api_key

```python
set_api_key(api_key)
```

Set the API key for authentication.

**Parameters:**
- `api_key` (str): The API key to use

## Config

The `Config` class handles configuration for the Briq client.

### Constructor

```python
Config(api_key=None, base_url=None)
```

**Parameters:**
- `api_key` (str, optional): API key for authentication. If not provided, will attempt to load from environment.
- `base_url` (str, optional): Base URL for the API. If not provided, will use the default URL.

### Properties

#### api_key

Get or set the API key.

#### base_url

Get or set the base URL.

#### headers

Get the headers for API requests.

**Returns:**
- `dict`: Headers including the API key.

**Raises:**
- `ValueError`: If API key is not set.

## WorkspaceAPI

The `WorkspaceAPI` class provides methods for managing workspaces.

### Methods

#### create

```python
create(name, description=None)
```

Create a new workspace.

**Parameters:**
- `name` (str): Name of the workspace
- `description` (str, optional): Description of the workspace

**Returns:**
- `dict`: Created workspace data

#### list

```python
list()
```

List all workspaces.

**Returns:**
- `list`: List of workspaces

#### get

```python
get(workspace_id)
```

Get a workspace by ID.

**Parameters:**
- `workspace_id` (str): ID of the workspace to retrieve

**Returns:**
- `dict`: Workspace data

#### update

```python
update(workspace_id, name=None, description=None)
```

Update a workspace.

**Parameters:**
- `workspace_id` (str): ID of the workspace to update
- `name` (str, optional): New name for the workspace
- `description` (str, optional): New description for the workspace

**Returns:**
- `dict`: Updated workspace data

## CampaignAPI

The `CampaignAPI` class provides methods for managing campaigns.

### Methods

#### create

```python
create(workspace_id, name, description=None, launch_date=None)
```

Create a new campaign.

**Parameters:**
- `workspace_id` (str): ID of the workspace to create the campaign in
- `name` (str): Name of the campaign
- `description` (str, optional): Description of the campaign
- `launch_date` (str, optional): Launch date of the campaign in ISO format (e.g., "2023-12-01T00:00:00")

**Returns:**
- `dict`: Created campaign data

#### list

```python
list()
```

List all campaigns.

**Returns:**
- `list`: List of campaigns

#### get

```python
get(campaign_id)
```

Get a campaign by ID.

**Parameters:**
- `campaign_id` (str): ID of the campaign to retrieve

**Returns:**
- `dict`: Campaign data

#### update

```python
update(campaign_id, name=None, description=None, launch_date=None)
```

Update a campaign.

**Parameters:**
- `campaign_id` (str): ID of the campaign to update
- `name` (str, optional): New name for the campaign
- `description` (str, optional): New description for the campaign
- `launch_date` (str, optional): New launch date in ISO format

**Returns:**
- `dict`: Updated campaign data

## MessageAPI

The `MessageAPI` class provides methods for sending and managing messages.

### Methods

#### send_instant

```python
send_instant(content, recipients, sender_id, campaign_id=None)
```

Send an instant message.

**Parameters:**
- `content` (str): Message content
- `recipients` (list): List of recipient phone numbers
- `sender_id` (str): Registered sender ID name
- `campaign_id` (str, optional): Campaign ID to associate the message with

**Returns:**
- `dict`: Message sending result

#### send_campaign

```python
send_campaign(campaign_id, group_id, content, sender_id)
```

Send a campaign message.

**Parameters:**
- `campaign_id` (str): ID of the campaign
- `group_id` (str): ID of the recipient group
- `content` (str): Message content
- `sender_id` (str): Registered sender ID name

**Returns:**
- `dict`: Message sending result

#### get_logs

```python
get_logs()
```

Get message logs.

**Returns:**
- `list`: Message logs

#### get_history

```python
get_history()
```

Get user message history.

**Returns:**
- `list`: Message history

## Exceptions

The Briq client library defines several exception classes for error handling.

### BriqError

Base exception for all Briq-related errors.

### BriqAuthError

Raised when authentication fails.

### BriqAPIError

Raised when the API returns an error.

### BriqRequestError

Raised when a request to the API fails.

### BriqConfigError

Raised when there's a configuration error.
