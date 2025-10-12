"""
Inflectra Spira MCP Server

A simple MCP server that exposes Inflectra Spira capabilities.

Prerequisites: You need to have the following environment variables defined:

- INFLECTRA_SPIRA_BASE_URL: The base URL to your Spira instance (e.g. https://mycompany.spiraservice.net)
- INFLECTRA_SPIRA_USERNAME: The login to your Spira instance
- INFLECTRA_SPIRA_API_KEY: The API Key (RSS Token) for your Spira instance

"""
import argparse
import os

from mcp.server.fastmcp import FastMCP

from mcp_server_spira.features import register_all
from mcp_server_spira.utils import register_all_prompts

# Create a FastMCP server instance with a name
mcp = FastMCP("inflectra-spira")

# Get the list of enabled features from the environment variable
# If not set, all features will be enabled by default
enabled_features_str = os.getenv("MCP_SPIRA_ENABLED_FEATURES")
enabled_features = (
    enabled_features_str.split(",") if enabled_features_str else None
)


# Register all features
register_all(mcp, enabled_features)
register_all_prompts(mcp)

def main():
    """Entry point for the command-line script."""
    parser = argparse.ArgumentParser(
        description="Run the Inflectra Spira MCP server")
    # Add more command-line arguments as needed
    
    parser.parse_args()  # Store args if needed later
    
    # Start the server
    mcp.run()

if __name__ == "__main__":
    main()