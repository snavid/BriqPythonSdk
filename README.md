# Briq Python Client

A Python client library for the Briq messaging platform API.

## Overview

The Briq Python client provides a simple and intuitive interface to interact with the Briq messaging platform API. It allows you to manage workspaces, campaigns, and send messages programmatically from your Python applications.

## Installation

You can install the Briq client library using pip:

```bash
pip install briq
```

## Requirements

- Python 3.7 or higher
- requests
- python-dotenv

## Authentication

The Briq client requires an API key for authentication. You can provide your API key in several ways:

1. Set it in your environment as `BRIQ_API_KEY`
2. Store it in a `.env` file in your project directory
3. Pass it directly when initializing the client

Example `.env` file:
```
BRIQ_API_KEY=your_api_key_here
```

## Quick Start

```python
import briq

# Initialize the client (will load API key from environment or .env file)
client = briq.Client()

# Or set the API key manually
client.set_api_key("your_api_key_here")

# Create a workspace
workspace = client.workspace.create(
    name="My Workspace",
    description="A workspace for my messaging campaigns"
)

# List all workspaces
workspaces = client.workspace.list()

# Send an instant message
result = client.message.send_instant(
    content="Hello from the Briq Python client!",
    recipients=["255788344348"],
    sender_id="my-sender-id"
)
```

## Documentation

For detailed documentation and examples, please refer to the [Usage Guide](docs/usage.md) and [API Reference](docs/api_reference.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
