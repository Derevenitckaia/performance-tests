from typing import Any

from httpx import Client, URL, QueryParams, Response


class HTTPClient:
    """Base HTTP API client.

    :param client: httpx.Client instance.
    """

    def __init__(self, client: Client) -> None:
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """Make a GET request."""
        return self.client.get(url, params=params)

    def post(self, url: URL | str, json: Any | None = None) -> Response:
        """Make a POST request."""
        return self.client.post(url, json=json)
