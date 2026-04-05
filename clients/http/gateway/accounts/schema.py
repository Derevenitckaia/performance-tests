from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict

from clients.http.gateway.cards.schema import CardSchema


class AccountType(StrEnum):
    """Account type."""
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"


class AccountStatus(StrEnum):
    """Account status."""
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    PENDING_CLOSURE = "PENDING_CLOSURE"


class AccountSchema(BaseModel):
    """Account schema."""
    id: str
    type: AccountType
    cards: list[CardSchema]
    status: AccountStatus
    balance: float


class GetAccountsQuerySchema(BaseModel):
    """Get accounts query schema."""
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class GetAccountsResponseSchema(BaseModel):
    """Get accounts response schema."""
    accounts: list[AccountSchema]


class OpenDepositAccountRequestSchema(BaseModel):
    """Open deposit account request schema."""
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenDepositAccountResponseSchema(BaseModel):
    """Open deposit account response schema."""
    account: AccountSchema


class OpenSavingsAccountRequestSchema(BaseModel):
    """Open savings account request schema."""
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenSavingsAccountResponseSchema(BaseModel):
    """Open savings account response schema."""
    account: AccountSchema


class OpenDebitCardAccountRequestSchema(BaseModel):
    """Open debit card account request schema."""
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenDebitCardAccountResponseSchema(BaseModel):
    """Open debit card account response schema."""
    account: AccountSchema


class OpenCreditCardAccountRequestSchema(BaseModel):
    """Open credit card account request schema."""
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenCreditCardAccountResponseSchema(BaseModel):
    """Open credit card account response schema."""
    account: AccountSchema