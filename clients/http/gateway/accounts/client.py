from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.accounts.schema import OpenCreditCardAccountRequestSchema, \
    OpenDebitCardAccountRequestSchema, \
    OpenDebitCardAccountResponseSchema, OpenCreditCardAccountResponseSchema, OpenSavingsAccountRequestSchema, \
    OpenSavingsAccountResponseSchema, OpenDepositAccountRequestSchema, OpenDepositAccountResponseSchema, \
    GetAccountsQuerySchema, GetAccountsResponseSchema
from clients.http.gateway.client import build_gateway_http_client

class AccountsGatewayHttpClient(HTTPClient):
    """Client for interacting with /api/v1/accounts http-gateway service."""

    def get_accounts_api(self, query: GetAccountsQuerySchema) -> Response:
        """Gets account details.

        :param query: GetAccountsQuerySchema
        :return: Response from server"""
        return self.get(url="/api/v1/accounts", params=QueryParams(**query.model_dump(by_alias=True)))

    def open_deposit_account_api(self, request: OpenDepositAccountRequestSchema) -> Response:
        """Opens deposit account.

        :param request: OpenAccountRequestSchema
        :return: Response from server"""
        return self.post(url="/api/v1/accounts/open-deposit-account", json=request.model_dump(by_alias=True))

    def open_savings_account_api(self, request: OpenSavingsAccountRequestSchema) -> Response:
        """Opens savings account.

        :param request: OpenAccountRequestSchema
        :return: Response from server"""
        return self.post(url="/api/v1/accounts/open-savings-account", json=request.model_dump(by_alias=True))

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestSchema) -> Response:
        """Opens debit card account.

        :param request: OpenAccountRequestSchema
        :return: Response from server"""
        return self.post(url="/api/v1/accounts/open-debit-card-account", json=request.model_dump(by_alias=True))

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestSchema) -> Response:
        """Opens credit card account.

        :param request: OpenAccountRequestSchema
        :return: Response from server"""
        return self.post(url="/api/v1/accounts/open-credit-card-account", json=request.model_dump(by_alias=True))

    def get_accounts(self, user_id: str) -> GetAccountsResponseSchema:
        """Gets account."""
        query = GetAccountsQuerySchema(user_id=user_id)
        response = self.get_accounts_api(query)
        return GetAccountsResponseSchema.model_validate_json(response.text)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseSchema:
        """Opens deposit account."""
        request = OpenDepositAccountRequestSchema(user_id=user_id)
        response = self.open_deposit_account_api(request)
        return OpenDepositAccountResponseSchema.model_validate_json(response.text)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseSchema:
        """Opens savings account."""
        request = OpenSavingsAccountRequestSchema(user_id=user_id)
        response = self.open_savings_account_api(request)
        return OpenSavingsAccountResponseSchema.model_validate_json(response.text)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseSchema:
        """Opens debit card account."""
        request = OpenDebitCardAccountRequestSchema(user_id=user_id)
        response = self.open_debit_card_account_api(request)
        return OpenDebitCardAccountResponseSchema.model_validate_json(response.text)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseSchema:
        """Opens credit card account."""
        request = OpenCreditCardAccountRequestSchema(user_id=user_id)
        response = self.open_credit_card_account_api(request)
        return OpenCreditCardAccountResponseSchema.model_validate_json(response.text)

def build_accounts_gateway_http_client() -> AccountsGatewayHttpClient:
    """Builds AccountsGatewayHttpClient instance."""
    return AccountsGatewayHttpClient(client=build_gateway_http_client())