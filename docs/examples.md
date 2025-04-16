# Briq Python Client Examples

This document provides practical examples of using the Briq Python client library for common tasks.

## Basic Setup

```python
import briq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the client
client = briq.Client()

# Check if API key is set
print(f"API key is {'set' if client.config.api_key else 'not set'}")
```

## Complete Workflow Example

This example demonstrates a complete workflow for creating a workspace, creating a campaign, and sending messages.

```python
import briq
import os
from datetime import datetime, timedelta

# Initialize the client
client = briq.Client()

# 1. Create a workspace
workspace = client.workspace.create(
    name="Marketing Workspace",
    description="Workspace for marketing campaigns"
)
workspace_id = workspace["id"]
print(f"Created workspace: {workspace['name']} (ID: {workspace_id})")

# 2. Create a campaign in the workspace
launch_date = (datetime.now() + timedelta(days=7)).isoformat()
campaign = client.campaign.create(
    workspace_id=workspace_id,
    name="Product Launch Campaign",
    description="Campaign for new product launch",
    launch_date=launch_date
)
campaign_id = campaign["id"]
print(f"Created campaign: {campaign['name']} (ID: {campaign_id})")

# 3. Send an instant message
result = client.message.send_instant(
    content="Hello! We're excited to announce our new product launch next week.",
    recipients=["255788344348", "255712345678"],
    sender_id="COMPANY",
    campaign_id=campaign_id
)
print(f"Sent instant message with ID: {result['message_id']}")

# 4. Get message logs
logs = client.message.get_logs()
print(f"Retrieved {len(logs)} message logs")
```

## Error Handling Example

This example demonstrates how to handle different types of errors that might occur when using the Briq client.

```python
import briq
from briq.exceptions import BriqAuthError, BriqAPIError, BriqRequestError, BriqConfigError

# Try with invalid API key
try:
    client = briq.Client(api_key="invalid_api_key")
    workspaces = client.workspace.list()
except BriqAuthError as e:
    print(f"Authentication error: {e}")
    # Handle authentication error (e.g., prompt for new API key)
    client.set_api_key(input("Enter valid API key: "))

# Try with valid API key but invalid request
try:
    # Attempt to create a workspace with missing required fields
    workspace = client.workspace.create(name="")
except BriqAPIError as e:
    print(f"API error: {e}")
    # Handle API error (e.g., fix request data)
    workspace = client.workspace.create(name="Fixed Workspace Name")

# Try with network issues
try:
    # Set invalid base URL to simulate network issue
    client.config.base_url = "http://invalid-url"
    workspaces = client.workspace.list()
except BriqRequestError as e:
    print(f"Request error: {e}")
    # Handle request error (e.g., retry with correct URL)
    client.config.base_url = "http://143.198.159.135:8000"
    workspaces = client.workspace.list()
```

## Working with Multiple Workspaces

This example demonstrates how to manage multiple workspaces and campaigns.

```python
import briq

# Initialize the client
client = briq.Client()

# List all workspaces
workspaces = client.workspace.list()
print(f"Found {len(workspaces)} workspaces")

# Create a new campaign in each workspace
for workspace in workspaces:
    workspace_id = workspace["id"]
    campaign = client.campaign.create(
        workspace_id=workspace_id,
        name=f"Campaign for {workspace['name']}",
        description=f"Automatically created campaign for {workspace['name']}"
    )
    print(f"Created campaign {campaign['name']} in workspace {workspace['name']}")

# List all campaigns
campaigns = client.campaign.list()
print(f"Total campaigns: {len(campaigns)}")
```

## Sending Messages to Multiple Recipients

This example demonstrates how to send messages to multiple recipients.

```python
import briq
import csv

# Initialize the client
client = briq.Client()

# Load recipients from a CSV file
recipients = []
with open('recipients.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        recipients.append(row[0])  # Assuming phone numbers are in the first column

print(f"Loaded {len(recipients)} recipients")

# Send a message to all recipients
result = client.message.send_instant(
    content="Thank you for subscribing to our newsletter!",
    recipients=recipients,
    sender_id="NEWSLETTER"
)
print(f"Message sent to {len(recipients)} recipients")
```

## Environment Configuration

This example demonstrates different ways to configure the client using environment variables.

```python
import briq
import os
from dotenv import load_dotenv

# Example .env file:
# BRIQ_API_KEY=your_api_key_here
# BRIQ_BASE_URL=http://custom-url:8000

# Method 1: Load from .env file
load_dotenv()
client1 = briq.Client()

# Method 2: Set environment variables programmatically
os.environ["BRIQ_API_KEY"] = "your_api_key_here"
client2 = briq.Client()

# Method 3: Pass values directly
client3 = briq.Client(
    api_key="your_api_key_here",
    base_url="http://custom-url:8000"
)

# Method 4: Set values after initialization
client4 = briq.Client()
client4.config.api_key = "your_api_key_here"
client4.config.base_url = "http://custom-url:8000"
```
