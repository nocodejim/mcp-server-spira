"""
Tests for the My Task features of the Inflectra Spira MCP Server.
"""
from unittest.mock import MagicMock
from mcp_server_spira.features.mywork.tools.mytasks import _get_my_tasks_impl

# A mock task payload that simulates the data returned by the Spira API
MOCK_TASK = {
    "TaskId": 40,
    "Name": "Test Task",
    "Description": "This is a test task description.",
    "TaskStatusName": "In Progress",
    "TaskTypeName": "Development",
    "TaskPriorityName": "High",
    "EndDate": "2024-12-31",
}

def test_get_my_tasks_impl():
    """
    Tests that we can get the list of my tasks in markdown format using a mock client.
    """
    # Create a mock SpiraClient
    mock_spira_client = MagicMock()

    # Configure the mock to return our mock task data
    mock_spira_client.make_spira_api_get_request.return_value = [MOCK_TASK]

    # Call the implementation function with the mocked client
    results = _get_my_tasks_impl(mock_spira_client)

    # Check that the API was called correctly
    mock_spira_client.make_spira_api_get_request.assert_called_once_with("tasks")

    # Check that the output contains the expected task ID and other details
    assert "[TK:40]" in results
    assert "Test Task" in results
    assert "In Progress" in results
    # assert "Due Date: 2024-12-31" in results