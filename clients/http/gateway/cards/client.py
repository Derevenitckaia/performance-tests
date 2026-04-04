from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient

class IssueCardDict(TypedDict):
    user_id: str
    account_id: str


class CardsGatewayHTTPClient(HTTPClient):
    """Client for interacting with /api/v1/cards http-gateway service."""

    def issue_virtual_card_api(self, request: IssueCardDict) -> Response:
        """Create an issue virtual card request.

        :param request: Dictionary of request data.
        :return: Response from server."""
        return self.post(url="/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardDict) -> Response:
        """Create an issue physical card request.

        :param request: Dictionary of request data.
        :return: Response from server."""
        return self.post(url="/api/v1/cards/issue-physical-card", json=request)

