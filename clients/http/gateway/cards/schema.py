from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict


class CardType(StrEnum):
    """Card type."""
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"


class CardStatus(StrEnum):
    """Card status."""
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"


class CardPaymentSystem(StrEnum):
    """Card payment system."""
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"


class CardSchema(BaseModel):
    """Card schema."""
    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str = Field(alias="accountId")
    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: date = Field(alias="expiryDate")
    payment_system: CardPaymentSystem = Field(alias="paymentSystem")


class IssueVirtualCardRequestSchema(BaseModel):
    """Issue virtual card request schema."""
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")


class IssueVirtualCardResponseSchema(BaseModel):
    """Issue virtual card response schema."""
    card: CardSchema


class IssuePhysicalCardRequestSchema(BaseModel):
    """Issue physical card request schema."""
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")


class IssuePhysicalCardResponseSchema(BaseModel):
    """Issue physical card response schema."""
    card: CardSchema