"""
Example script showing how to use the Briq SDK to send messages
"""

from BriqPythonSdk import BriqClient, BriqAuthenticationError, BriqMessageError

# Replace with your actual credentials
USERNAME = "your_username"
PASSWORD = "your_password"
WORKSPACE_ID = "your_workspace_id"
SENDER_ID = "YourSenderId"

def main():
    # Initialize the client
    client = BriqClient(username=USERNAME, password=PASSWORD)
    
    # List available workspaces
    print("Fetching workspaces...")
    try:
        workspaces = client.get_workspaces()
        print(f"Found {len(workspaces)} workspaces:")
        for workspace in workspaces:
            print(f"  - ID: {workspace.get('workspace_id')}")
            print(f"    Name: {workspace.get('name', 'N/A')}")
    except Exception as e:
        print(f"Failed to fetch workspaces: {e}")
        return
    
    # Send a test message
    recipient = input("Enter recipient phone number (with country code, e.g., +1234567890): ")
    message = input("Enter message to send: ")
    
    print(f"Sending message to {recipient}...")
    try:
        response = client.send_message(
            workspace_id=WORKSPACE_ID,
            recipients=[recipient],
            content=message,
            sender_id=SENDER_ID
        )
        print("Message sent successfully!")
        print(f"Response: {response}")
    except (BriqAuthenticationError, BriqMessageError) as e:
        print(f"Error sending message: {e}")


if __name__ == "__main__":
    main()