from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient

class GetOperationDict(TypedDict):
    """Data for get operation."""
    account_id: str

class MakeOperationRequestDict(TypedDict):
    """Data for make operation request."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """Data for make purchase operation request."""
    category: str

class OperationsGatewayHTTPClient(HTTPClient):
    """Client for interacting with  /api/v1/operations http-gateway service."""

    def get_operation_api(self, operation_id) -> Response:
        """Gets an information about an operation by its id.

        :param operation_id: The id of the operation to get.
        :return response: The response from server."""
        return self.get(url=f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id) -> Response:
        """Gets an information about an operation receipt by operation id.

        :param operation_id: The id of the operation.
        :return response: The response from server."""
        return self.get(url=f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationDict) -> Response:
        """Gets an information about all operations for an account.

        :param query: Dictionary with the id of the account.
        :return response: The response from server."""
        return self.get(url=f"/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationDict) -> Response:
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




