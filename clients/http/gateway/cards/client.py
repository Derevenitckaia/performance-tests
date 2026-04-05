from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.cards.schema import IssueVirtualCardRequestSchema, IssuePhysicalCardRequestSchema, \
    IssueVirtualCardResponseSchema, IssuePhysicalCardResponseSchema
from clients.http.gateway.client import build_gateway_http_client


class CardsGatewayHTTPClient(HTTPClient):
    """Client for interacting with /api/v1/cards http-gateway service."""

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestSchema) -> Response:
        """Create an issue virtual card request.

        :param request: Schema of request data.
        :return: Response from server."""
        return self.post(url="/api/v1/cards/issue-virtual-card", json=request.model_dump(by_alias=True))

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestSchema) -> Response:
        """Create an issue physical card request.

        :param request: Schema of request data.
        :return: Response from server."""
        return self.post(url="/api/v1/cards/issue-physical-card", json=request.model_dump(by_alias=True))

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseSchema:
        """Create an issue virtual card."""
        request = IssueVirtualCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_virtual_card_api(request)
        return IssueVirtualCardResponseSchema.model_validate_json(response.text)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseSchema:
        """Create an issue physical card."""
        request = IssuePhysicalCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_physical_card_api(request)
        return IssuePhysicalCardResponseSchema.model_validate_json(response.text)

def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """Builds CardsGatewayHTTPClient instance."""
    return CardsGatewayHTTPClient(client=build_gateway_http_client())