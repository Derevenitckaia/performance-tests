from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client

class DocumentDict(TypedDict):
    url: str
    document: str

class GetTariffDocumentResponseDict(TypedDict):
    tariff: DocumentDict

class GetContractDocumentResponseDict(TypedDict):
    tariff: DocumentDict


class DocumentsGatewayHttpClient(HTTPClient):

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
        """Gets tariff document."""
        return self.get_tariff_document_api(account_id).json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """Gets contract document."""
        return self.get_contract_document_api(account_id).json()

def build_documents_gateway_http_client() -> DocumentsGatewayHttpClient:
    """Builds DocumentsGatewayHttpClient instance."""
    return DocumentsGatewayHttpClient(client=build_gateway_http_client())