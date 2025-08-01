"""
Provides operations for retrieving an entire product specification that spans multiple
Spira artifacts. This is used by Agentic AI development tools such as Amazon Kiro
for building applications from a formal spec.

A product specification consists of the data in markdown format used by Kiro to generate
the following files:
    - requirements.md - Captures user stories and acceptance criteria in structured EARS notation
    - design.md - Documents technical architecture, sequence diagrams, and implementation considerations
    - tasks.md - Provides a detailed implementation plan with discrete, trackable tasks

This module provides MCP tools for retrieving entire product specifications
"""

from mcp_server_spira.features.formatting import format_requirement
from mcp_server_spira.features.common import get_spira_client
from mcp_server_spira.features.workspaces.tools.products import _get_products_by_id_impl
from typing import Any

def _get_specification_requirements(spira_client, product_id: int, release_id: int | None) -> list[Any]:
    """
    Gets the list of requirements in the product/release

    Args:
        spira_client: The Inflectra Spira API client instance
        product_id: The numeric ID of the product. If the ID is PR:45, just use 45. 
        release_id: The numeric ID of the release. If the ID is RL:12, just use 12. (optional)
                
    Returns:
        List of requirements
    """
    try:
        requirements = []
        starting_row = 1
        number_of_rows = 250
        more_results = True
        while more_results:
            requirements_url = f"projects/{product_id}/requirements?starting_row={starting_row}&number_of_rows={number_of_rows}"
            results = spira_client.make_spira_api_get_request(requirements_url)
            if not results:
                more_results = False
            else:
                starting_row += number_of_rows
            requirements.extend(results)

        return requirements
    except Exception as e:
        raise e

def _get_specification_impl(spira_client, product_id: int, release_id: int | None) -> str:
    """
    Implementation of retrieving the markdown specification for the specified product

    Args:
        spira_client: The Inflectra Spira API client instance
        product_id: The numeric ID of the product. If the ID is PR:45, just use 45. 
        release_id: The numeric ID of the release. If the ID is RL:12, just use 12.
                    If no release is specified, then the specification for the entire
                    project is returned 
                
    Returns:
        Formatted string containing the product specification
    """
    try:
        formatted_specification = []

        # Create the header
        if release_id:
            formatted_specification.append(f'# Specification for Product PR:{product_id}')
        else:
            formatted_specification.append(f'# Specification for Product PR:{product_id}, Release RL:{release_id}')

        # Populate the product overview
        product_overview = _get_products_by_id_impl(spira_client, product_id)
        formatted_specification.append(product_overview)

        # Create the sub-header for the Requirements.md section
        formatted_specification.append(f'# Requirements Document')

        # Get the list of requirements in the product, or just the release
        requirements = _get_specification_requirements(spira_client, product_id, release_id)

        if not requirements:
            return "There are no requirements for the product."

        # Format the requirements into human readable data
        for requirement in requirements:
            requirement_info = format_requirement(requirement)
            formatted_specification.append(requirement_info)

        # Create the sub-header for the Design.md section
        formatted_specification.append(f'# Design Document')

        # Create the sub-header for the Tasks.md section
        formatted_specification.append(f'# Implementation Plan')

        return "\n\n".join(formatted_specification)
    
    except Exception as e:
        return f"There was a problem using this tool: {e}"

def register_tools(mcp) -> None:
    """
    Register product specification tools with the MCP server.
    
    Args:
        mcp: The FastMCP server instance
    """

    @mcp.tool()
    def get_specification(product_id: int, release_id: int | None) -> str:
        """
        Retrieves the complete specification for the requested Spira product,
        with the option to only return the specification for a selected product
        release.
        
        Use this tool when you need to download a full product specification so that
        it can be used in an agentic development environment such as Amazon Kiro

        The returned specification markdown is broken down into the following three sections:
            - Requirements - Captures user stories and acceptance criteria in structured EARS notation
            - Design - Documents technical architecture, sequence diagrams, and implementation considerations
            - Tasks - Provides a detailed implementation plan with discrete, trackable tasks

        Args:
            product_id: The numeric ID of the product. If the ID is PR:45, just use 45.
            release_id: The numeric ID of the release. If the ID is RL:12, just use 12.
                        If no release is specified, then the specification for the entire
                        project is returned 
        
        Returns:
            Formatted string in markdown that contains the full specification for the requested
            Spira product (or just the specific release in that product).
        """
        try:
            spira_client = get_spira_client()
            return _get_specification_impl(spira_client, product_id, release_id)
        except Exception as e:
            return f"Error: {str(e)}"