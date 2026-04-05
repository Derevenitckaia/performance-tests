from typing import TypedDict, Literal

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class GetOperationsQueryDict(TypedDict):
    """Data for get operations."""
    accountId: str

class MakeOperationRequestDict(TypedDict):
    """Data for make operation request."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """Data for make purchase operation request."""
    category: str

class OperationDict(TypedDict):
    """Data for operation."""
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class GetOperationResponseDict(TypedDict):
    """Data for get operation response."""
    operation: OperationDict

class GetOperationsResponseDict(TypedDict):
    """Data for get operations response."""
    operations: list[OperationDict]

class MakeOperationResponseDict(TypedDict):
    """Data for make operation response."""
    operation: OperationDict

class OperationReceiptDict(TypedDict):
    """Data for operation receipt."""
    url: str
    document: str

class GetOperationsReceiptResponseDict(TypedDict):
    """Data for get operation's receipt response."""
    receipt: OperationReceiptDict

class OperationsSummaryDict(TypedDict):
    """Data for operation summary."""
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationsSummaryResponseDict(TypedDict):
    """Data for get operation summary response."""
    summary: OperationsSummaryDict

class OperationsGatewayHTTPClient(HTTPClient):
    """Client for interacting with  /api/v1/operations http-gateway service."""

    def get_operation_api(self, operation_id: str) -> Response:
        """Gets an information about an operation by its id.

        :param operation_id: The id of the operation to get.
        :return response: The response from server."""
        return self.get(url=f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """Gets an information about an operation receipt by operation id.

        :param operation_id: The id of the operation.
        :return response: The response from server."""
        return self.get(url=f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """Gets an information about all operations for an account.

        :param query: Dictionary with the id of the account.
        :return response: The response from server."""
        return self.get(url=f"/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsQueryDict) -> Response:
        """Gets an operations' summary for an account.

        :param query: Dictionary with the id of the account.
        :return response: The response from server."""
        return self.get(url=f"/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """Makes a fee operation request.

        :param request: Dictionary of request data.
        :return: Response from server."""
        return self.post(url="/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """Makes a top-up operation request.

        :param request: Dictionary of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """Makes a cashback operation request.

        :param request: Dictionary of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """Makes a transfer operation request.

        :param request: Dictionary of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """Makes a purchase operation request.

        :param request: Dictionary of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """Makes a bill payment operation request.

        :param request: Dictionary of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """Makes a cash withdrawal operation request.

        :param request: Dictionary of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id):
        """Gets operations' data.

        :param operation_id: Operation ID
        :return response: Dictionary with operation data."""
        response = self.get_operations_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id):
        """Gets operations' receipt.

        :param operation_id: Operation ID
        :return response: Dictionary with receipt data."""
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """Gets operations' data.

        :param account_id: Account ID
        :return response: Dictionary with operations data."""
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """Gets operations' summary.

        :param account_id: Account ID
        :return response: Dictionary with operations summary data."""
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """Makes a fee operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Dictionary with operation data."""
        request = MakeOperationRequestDict(
            status="IN_PROGRESS",
            amount=100,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """Makes a top-up operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Dictionary with operation data."""
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """Makes a cashback operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Dictionary with operation data."""
        request = MakeOperationRequestDict(
            status="IN_PROGRESS",
            amount=200,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """Makes a transfer operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Dictionary with operation data."""
        request = MakeOperationRequestDict(
            status="IN_PROGRESS",
            amount=300,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """Makes a purchase operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Dictionary with operation data."""
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=101,
            cardId=card_id,
            accountId=account_id,
            category="beauty"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """Makes a cash withdrawal operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Dictionary with operation data."""
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=201,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """Builds an OperationsGatewayHTTPClient instance."""
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())


