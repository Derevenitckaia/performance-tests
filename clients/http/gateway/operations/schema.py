from datetime import datetime
from enum import StrEnum


from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from tools.fakers import fake


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

class OperationSchema(BaseModel):
    """Data for operation."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class GetOperationsQuerySchema(BaseModel):
    """Data for get operations."""
    accountId: str

class GetOperationResponseSchema(BaseModel):
    """Data for get operation response."""
    operation: OperationSchema

class GetOperationsResponseSchema(BaseModel):
    """Data for get operations response."""
    operations: list[OperationSchema]


class MakeOperationRequestSchema(BaseModel):
    """Base schema for making an operation request."""
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """Request schema for TOP_UP operation."""
    pass


class MakeTopUpOperationResponseSchema(BaseModel):
    """Response schema for TOP_UP operation."""
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """Request schema for PURCHASE operation."""
    category: str = Field(default_factory= lambda: fake.category())


class MakePurchaseOperationResponseSchema(BaseModel):
    """Response schema for PURCHASE operation."""
    operation: OperationSchema


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """Request schema for FEE operation."""
    pass


class MakeFeeOperationResponseSchema(BaseModel):
    """Response schema for FEE operation."""
    operation: OperationSchema


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """Request schema for CASHBACK operation."""
    pass


class MakeCashbackOperationResponseSchema(BaseModel):
    """Response schema for CASHBACK operation."""
    operation: OperationSchema


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """Request schema for TRANSFER operation."""
    pass


class MakeTransferOperationResponseSchema(BaseModel):
    """Response schema for TRANSFER operation."""
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """Request schema for BILL_PAYMENT operation."""
    pass


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """Response schema for BILL_PAYMENT operation."""
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """Request schema for CASH_WITHDRAWAL operation."""
    pass


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """Response schema for CASH_WITHDRAWAL operation."""
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