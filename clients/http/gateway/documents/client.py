from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.documents.schema import GetTariffDocumentResponseSchema, GetContractDocumentResponseSchema


class DocumentsGatewayHttpClient(HTTPClient):
    """Client for interacting with /api/v1/documents http-gateway service."""

    def get_tariff_document_api(self, account_id: str) -> Response:
        """Gets tariff document by account_id.

        :param account_id: Account ID
        :return: Response from server"""
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """Gets contract document by account_id.

        :param account_id: Account ID
        :return: Response from server"""
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseSchema:
        """Gets tariff document.

        :param account_id: Account ID
        :return: Schema with tariff document"""
        response = self.get_tariff_document_api(account_id)
        return GetTariffDocumentResponseSchema.model_validate_json(response.text)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseSchema:
        """Gets contract document.

        :param account_id: Account ID
        :return: Schema with contract document"""
        response = self.get_contract_document_api(account_id)
        return GetContractDocumentResponseSchema.model_validate_json(response.text)

def build_documents_gateway_http_client() -> DocumentsGatewayHttpClient:
    """Builds DocumentsGatewayHttpClient instance."""
    return DocumentsGatewayHttpClient(client=build_gateway_http_client())