# Inflectra Spira MCP features package
from mcp_server_spira.features import (
    mywork,
    productartifacts,
    programartifacts,
    templateconfiguration,
    workspaces,
    automation,
)

# Map feature names to their registration functions
FEATURE_MAP = {
    "mywork": mywork,
    "productartifacts": productartifacts,
    "programartifacts": programartifacts,
    "templateconfiguration": templateconfiguration,
    "workspaces": workspaces,
    "automation": automation,
}


def register_all(mcp, enabled_features=None):
    """
    Register features with the MCP server.
    If enabled_features is None, all features are registered.
    Otherwise, only the features in the list are registered.

    Args:
        mcp: The FastMCP server instance
        enabled_features: A list of feature names to register.
    """
    if enabled_features is None:
        # If no specific features are requested, register all
        features_to_register = FEATURE_MAP.keys()
    else:
        # Otherwise, only register the requested features
        features_to_register = [
            feature
            for feature in enabled_features
            if feature in FEATURE_MAP
        ]

    for feature_name in features_to_register:
        FEATURE_MAP[feature_name].register(mcp)
