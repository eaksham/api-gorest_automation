"""
conftest.py:
This file contains global fixtures for the API automation project.
Fixtures include the base URL, headers, and an API client instance,
which can be used across all test cases.
"""

import pytest
from utils.api_client import APIClient

# Fixture to provide the base URL for the API tests
@pytest.fixture(scope="session")
def base_url():
    return "https://gorest.co.in/public/v2"

# Fixture to provide headers for all API requests (including authorization token)
@pytest.fixture(scope="session")
def headers():
    return {
        "Authorization": "7e6d373951333152f3a69af545286eef355ebf017390a3a0192f3b06e6376672",  # Add your API token here
        "Content-Type": "application/json"
    }

# Fixture to create an instance of the API client with the base URL and headers
@pytest.fixture(scope="session")
def api_client(base_url, headers):
    return APIClient(base_url, headers)
