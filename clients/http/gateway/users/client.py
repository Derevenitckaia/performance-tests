import time

from httpx import Response, Client

from clients.http.client import HTTPClient

from typing import TypedDict

from clients.http.gateway.client import build_gateway_http_client


class CreateUserRequestDict(TypedDict):
    """Data for creating a new user"""
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str

class UserDict(TypedDict):
    """User's data."""
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class GetUserResponseDict(TypedDict):
    """Response structure when getting a user."""
    user: UserDict

class CreateUserResponseDict(TypedDict):
    """Response structure when creating a user."""
    user: UserDict


class UsersGatewayHTTPClient(HTTPClient):
    """Client for interacting with /api/v1/users http-gateway service."""

    def get_user_api(self, user_id: str) -> Response:
        """Gets a user's data by its user_id api."""
        return self.get(url=f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """Creates a new user api."""
        return self.post(url="/api/v1/users", json=request)

    def get_user(self, user_id: str) -> GetUserResponseDict:
        """Gets a user's data by its user_id."""
        response = self.get_user_api(user_id)
        return response.json()

    def create_user(self) -> CreateUserResponseDict:
        """Creates a new user."""
        request = CreateUserRequestDict(
            email=f"user.{time.time()}@example.com",
            lastName="string",
            firstName="string",
            middleName="string",
            phoneNumber="string"
        )
        response = self.create_user_api(request)
        return response.json()


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """Builds a UsersGatewayHTTPClient instance."""
    return UsersGatewayHTTPClient(client=build_gateway_http_client())

