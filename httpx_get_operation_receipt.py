import time
import httpx

# Step 1. Create user
create_user_payload = {
  "email": f"user{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

create_user_response = httpx.post(url="http://localhost:8003/api/v1/users", json=create_user_payload)
user_data = create_user_response.json()

# Step 2. Open credit account for new user
user_id = user_data["user"]["id"]
open_credit_card_account_payload = {
  "userId": user_id
}
open_credit_card_response = httpx.post(url="http://localhost:8003/api/v1/accounts/open-credit-card-account",
                                       json=open_credit_card_account_payload)
credit_card_data = open_credit_card_response.json()

# Step 3. Make purchase operation
card_id = credit_card_data["account"]["cards"][0]["id"]
account_id = credit_card_data["account"]["id"]
make_purchase_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": card_id,
  "accountId": account_id,
  "category": "taxi"
}

make_purchase_operation_response = httpx.post(url="http://localhost:8003/api/v1/operations/make-purchase-operation",
                                              json=make_purchase_payload)
make_purchase_operation_data = make_purchase_operation_response.json()
operationId = make_purchase_operation_data["operation"]["id"]

# Step 4. Get operation receipt
get_operation_receipt_response = httpx.get(url=f"http://localhost:8003/api/v1/operations/operation-receipt/{operationId}")

print(get_operation_receipt_response.json())
print(get_operation_receipt_response.status_code)