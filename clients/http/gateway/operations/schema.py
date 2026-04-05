from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class OperationStatus(StrEnum):
    """Operation status."""
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class OperationType(StrEnum):
    """Operation type."""
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"

class GetOperationsQuerySchema(BaseModel):
    """Data for get operations."""
    accountId: str

class MakeOperationRequestSchema(BaseModel):
    """Data for make operation request."""
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """Data for make purchase operation request."""
    category: str

class OperationSchema(BaseModel):
    """Data for operation."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: date = Field(alias="createdAt")
    updated_at: date = Field(alias="updatedAt")
    account_id: str = Field(alias="accountId")

class GetOperationResponseSchema(BaseModel):
    """Data for get operation response."""
    operation: OperationSchema

class GetOperationsResponseSchema(BaseModel):
    """Data for get operations response."""
    operations: list[OperationSchema]

class MakeOperationResponseSchema(BaseModel):
    """Data for make operation response."""
    operation: OperationSchema

class OperationReceiptSchema(BaseModel):
    """Data for operation receipt."""
    url: HttpUrl
    document: str

class GetOperationsReceiptResponseSchema(BaseModel):
    """Data for get operation's receipt response."""
    receipt: OperationReceiptSchema

class OperationsSummarySchema(BaseModel):
    """Data for operation summary."""
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationsSummaryResponseSchema(BaseModel):
    """Data for get operation summary response."""
    summary: OperationsSummarySchema