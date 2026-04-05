from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """Schema for document."""
    url: HttpUrl
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    """Schema for response when getting tariff document."""
    tariff: DocumentSchema

class GetContractDocumentResponseSchema(BaseModel):
    """Schema for response when getting contract documents."""
    contract: DocumentSchema