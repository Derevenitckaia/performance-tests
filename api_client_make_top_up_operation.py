from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client

# Step 1. Create user
user_gateway_http_client = build_users_gateway_http_client()
user_data = user_gateway_http_client.create_user()
print(f"Create user response: {user_data}")
# Step 2. Open debit card account
accounts_gateway_http_client = build_accounts_gateway_http_client()
debit_card_account_data = accounts_gateway_http_client.open_debit_card_account(user_id=user_data.user.id)
print(f"Open debit card account response:{debit_card_account_data}")
# Step 3. Make top up operation
operations_gateway_http_client = build_operations_gateway_http_client()
card_id = debit_card_account_data.account.cards[0].id
account_id = debit_card_account_data.account.id
top_up_operation_data = operations_gateway_http_client.make_top_up_operation(card_id=card_id, account_id=account_id)
print(f"Make top up operation response: {top_up_operation_data}")