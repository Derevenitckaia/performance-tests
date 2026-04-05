from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class IssueCardDict(TypedDict):
    """Data structure for issue card request."""
    user_id: str
    account_id: str

class CardDict(TypedDict):
    """Card's data structure."""
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str

class IssueVirtualCardResponseDict(TypedDict):
    """Data structure for response when creating issue virtual card request."""
    card: CardDict

class IssuePhysicalCardResponseDict(TypedDict):
    """Data structure for response when creating issue physical card request."""
    card: CardDict


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

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseDict:
        """Create an issue virtual card."""
        request = IssueCardDict(user_id=user_id, account_id=account_id)
        response = self.issue_virtual_card_api(request)
        return response.json()

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseDict:
        """Create an issue physical card."""
        request = IssueCardDict(user_id=user_id, account_id=account_id)
        response = self.issue_physical_card_api(request)
        return response.json()

def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """Builds CardsGatewayHTTPClient instance."""
    return CardsGatewayHTTPClient(client=build_gateway_http_client())