import time

from httpx import Response, Client

from clients.http.client import HTTPClient

from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.users.schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema


class UsersGatewayHTTPClient(HTTPClient):
    """Client for interacting with /api/v1/users http-gateway service."""

    def get_user_api(self, user_id: str) -> Response:
        """Gets a user's data by its user_id api."""
        return self.get(url=f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """Creates a new user api."""
        return self.post(url="/api/v1/users", json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """Gets a user's data by its user_id."""
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def create_user(self) -> CreateUserResponseSchema:
        """Creates a new user."""
        request = CreateUserRequestSchema()
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """Builds a UsersGatewayHTTPClient instance."""
    return UsersGatewayHTTPClient(client=build_gateway_http_client())

