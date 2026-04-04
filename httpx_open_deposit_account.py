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

# Step 2. Open deposit account for new user
user_id = user_data["user"]["id"]
open_deposit_account_playload = {
  "userId": user_id
}

response = httpx.post(url="http://localhost:8003/api/v1/accounts/open-deposit-account",
                      json=open_deposit_account_playload)

# Step 3. Print result
print(response.json())
print(response.status_code)
