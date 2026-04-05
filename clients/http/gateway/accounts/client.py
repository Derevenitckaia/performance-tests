from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.cards.client import CardDict
from clients.http.gateway.client import build_gateway_http_client

class GetAccountsQueryDict(TypedDict):
    """Data for Get account request."""
    userId: str

class OpenSavingsAccountRequestDict(TypedDict):
    """Data for Open account request."""
    userId: str

class OpenDepositAccountRequestDict(TypedDict):
    """Data for Open account request."""
    userId: str

class OpenCreditCardAccountRequestDict(TypedDict):
    """Data for Open account request."""
    userId: str

class OpenDebitCardAccountRequestDict(TypedDict):
    userId: str

class AccountDict(TypedDict):
    id: str
    type: str
    cards: list[CardDict]  # Вложенная структура: список карт
    status: str
    balance: float

class GetAccountsResponseDict(TypedDict):
    account: AccountDict

class OpenSavingsAccountResponseDict(TypedDict):
    account: AccountDict

class OpenDebitCardAccountResponseDict(TypedDict):
    account: AccountDict

class OpenCreditCardAccountResponseDict(TypedDict):
    account: AccountDict

class OpenDepositAccountResponseDict(TypedDict):
    account: AccountDict


class AccountsGatewayHttpClient(HTTPClient):

    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        """Gets account details.

        :param query: GetAccountsQueryDict
        :return: Response from server"""
        return self.get(url="/api/v1/accounts", params=QueryParams(**query))

    def open_deposit_account_api(self, request: OpenDepositAccountRequestDict) -> Response:
        """Opens deposit account.

        :param request: OpenAccountRequestDict
        :return: Response from server"""
        return self.post(url="/api/v1/accounts/open-deposit-account", json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequestDict) -> Response:
        """Opens savings account.

        :param request: OpenAccountRequestDict
        :return: Response from server"""
        return self.post(url="/api/v1/accounts/open-savings-account", json=request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestDict) -> Response:
        """Opens debit card account.

        :param request: OpenAccountRequestDict
        :return: Response from server"""
        return self.post(url="/api/v1/accounts/open-debit-card-account", json=request)

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestDict) -> Response:
        """Opens credit card account.

        :param request: OpenAccountRequestDict
        :return: Response from server"""
        return self.post(url="/api/v1/accounts/open-credit-card-account", json=request)

    def get_accounts(self, user_id: str) -> GetAccountsResponseDict:
        query = GetAccountsQueryDict(userId=user_id)
        response = self.get_accounts_api(query)
        return response.json()

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseDict:
        request = OpenDepositAccountRequestDict(userId=user_id)
        response = self.open_deposit_account_api(request)
        return response.json()

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseDict:
        request = OpenSavingsAccountRequestDict(userId=user_id)
        response = self.open_savings_account_api(request)
        return response.json()

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseDict:
        request = OpenDebitCardAccountRequestDict(userId=user_id)
        response = self.open_debit_card_account_api(request)
        return response.json()

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseDict:
        request = OpenCreditCardAccountRequestDict(userId=user_id)
        response = self.open_credit_card_account_api(request)
        return response.json()

def build_accounts_gateway_http_client() -> AccountsGatewayHttpClient:
    """Builds AccountsGatewayHttpClient instance."""
    return AccountsGatewayHttpClient(client=build_gateway_http_client())