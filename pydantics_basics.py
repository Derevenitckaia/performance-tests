from pydantic import BaseModel


class AccountSchema(BaseModel):
    id: str
    type: str
    status: str
    balance: float

# Инициализируем модель AccountSchema через JSON
account_json = """
{
    "id": "account-id",
    "type": "CREDIT_CARD",
    "status": "ACTIVE",
    "balance": 777.11
}
"""
account_json_model = AccountSchema.model_validate_json(account_json)
print('Account JSON model:', account_json_model)
