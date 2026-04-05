from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import MakeOperationRequestSchema, \
    OperationStatus, MakePurchaseOperationRequestSchema, GetOperationsQuerySchema, GetOperationsSummaryResponseSchema, \
    GetOperationsResponseSchema, GetOperationResponseSchema, GetOperationsReceiptResponseSchema, \
    MakeCashbackOperationResponseSchema, MakeCashbackOperationRequestSchema, MakePurchaseOperationResponseSchema, \
    MakeTransferOperationRequestSchema, MakeTransferOperationResponseSchema, MakeCashWithdrawalOperationResponseSchema, \
    MakeCashWithdrawalOperationRequestSchema, MakeTopUpOperationRequestSchema, MakeTopUpOperationResponseSchema, \
    MakeFeeOperationResponseSchema, MakeFeeOperationRequestSchema


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

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """Gets an information about all operations for an account.

        :param query: Schema with the id of the account.
        :return response: The response from server."""
        return self.get(url=f"/api/v1/operations",
                        params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary_api(self, query: GetOperationsQuerySchema) -> Response:
        """Gets an operations' summary for an account.

        :param query: Schema with the id of the account.
        :return response: The response from server."""
        return self.get(url=f"/api/v1/operations/operations-summary",
                        params=QueryParams(**query.model_dump(by_alias=True)))

    def make_fee_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """Makes a fee operation request.

        :param request: Schema of request data.
        :return: Response from server."""
        return self.post(url="/api/v1/operations/make-fee-operation",
                         json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """Makes a top-up operation request.

        :param request: Schema of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-top-up-operation",
                         json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """Makes a cashback operation request.

        :param request: Schema of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-cashback-operation",
                         json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """Makes a transfer operation request.

        :param request: Schema of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-transfer-operation",
                         json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """Makes a purchase operation request.

        :param request: Schema of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-purchase-operation",
                         json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """Makes a bill payment operation request.

        :param request: Schema of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-bill-payment-operation",
                         json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """Makes a cash withdrawal operation request.

        :param request: Schema of request data.
        :return response: Response from server."""
        return self.post(url="/api/v1/operations/make-cash-withdrawal-operation",
                         json=request.model_dump(by_alias=True))

    def get_operation(self, operation_id) -> GetOperationResponseSchema:
        """Gets operations' data.

        :param operation_id: Operation ID
        :return response: Schema with operation data."""
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id) -> GetOperationsReceiptResponseSchema:
        """Gets operations' receipt.

        :param operation_id: Operation ID
        :return response: Schema with receipt data."""
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationsReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """Gets operations' data.

        :param account_id: Account ID
        :return response: Schema with operations data."""
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """Gets operations' summary.

        :param account_id: Account ID
        :return response: Schema with operations summary data."""
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        """Makes a fee operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Schema with operation data."""
        request = MakeFeeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        """Makes a top-up operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Schema with operation data."""
        request = MakeTopUpOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        """Makes a cashback operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Schema with operation data."""
        request = MakeCashbackOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        """Makes a transfer operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Schema with operation data."""
        request = MakeTransferOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        """Makes a purchase operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Schema with operation data."""
        request = MakePurchaseOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(
            self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        """Makes a cash withdrawal operation request.

        :param card_id: Card ID
        :param account_id: Account ID
        :return response: Schema with operation data."""
        request = MakeCashWithdrawalOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """Builds an OperationsGatewayHTTPClient instance."""
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())


