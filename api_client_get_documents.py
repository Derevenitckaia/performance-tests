from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client

# Step 1. Create user
user_gateway_http_client = build_users_gateway_http_client()
user_data = user_gateway_http_client.create_user()
print(f"Create user response: {user_data}")
# Step 2. Open credit card account
accounts_gateway_http_client = build_accounts_gateway_http_client()
credit_card_account_data = accounts_gateway_http_client.open_credit_card_account(user_id=user_data.user.id)
print(f"Open credit card account response: {credit_card_account_data}")
# Step 3. Get tariff document
documents_gateway_http_client = build_documents_gateway_http_client()
tariff_document_data = documents_gateway_http_client.get_tariff_document(account_id=credit_card_account_data.account.id)
print(f"Get tariff document response: {tariff_document_data}")
# Step 4. Get contract document
contract_document_data = documents_gateway_http_client.get_contract_document(account_id=credit_card_account_data.account.id)
print(f"Get contract document response: {contract_document_data}")