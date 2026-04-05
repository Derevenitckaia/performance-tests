from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client

class DocumentDict(TypedDict):
    """Data structure for document."""
    url: str
    document: str

class GetTariffDocumentResponseDict(TypedDict):
    """Data structure for response when getting tariff document."""
    tariff: DocumentDict

class GetContractDocumentResponseDict(TypedDict):
    """Data structure for response when getting contract documents."""
    tariff: DocumentDict


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

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """Gets tariff document.

        :param account_id: Account ID
        :return: Dictionary with tariff document"""
        return self.get_tariff_document_api(account_id).json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """Gets contract document.

        :param account_id: Account ID
        :return: Dictionary with contract document"""
        return self.get_contract_document_api(account_id).json()

def build_documents_gateway_http_client() -> DocumentsGatewayHttpClient:
    """Builds DocumentsGatewayHttpClient instance."""
    return DocumentsGatewayHttpClient(client=build_gateway_http_client())