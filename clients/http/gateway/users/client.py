from httpx import Response

from clients.http.client import HTTPClient

from typing import TypedDict


class CreateUserRequestDict(TypedDict):
    """Data for creating a new user"""
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class UsersGatewayHTTPClient(HTTPClient):
    """Client for interacting with /api/v1/users http-gateway service."""

    def get_user_api(self, user_id: str) -> Response:
        """Gets a user's data by its user_id"""
        return self.get(url=f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """Creates a new user"""
        return self.post(url="/api/v1/users", json=request)
