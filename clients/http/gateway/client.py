from httpx import Client


def build_gateway_http_client() -> Client:
    """Creates httpx.Client instance with base settings for http-gateway service."""
    return Client(timeout=100, base_url="http://localhost:8003")