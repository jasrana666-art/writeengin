import os, requests
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('OPENROUTER_API_KEY')

# Check account status
resp = requests.get('https://openrouter.ai/api/v1/key', headers={'Authorization': f'Bearer {key}'}, timeout=30)
print('Account status:', resp.status_code)
if resp.status_code == 200:
    data = resp.json()
    print('  Label:', data.get('label'))
    print('  Usage:', data.get('usage'))
    print('  Limit:', data.get('limit'))
else:
    print('  Error:', resp.text[:200])

# Test a paid model
resp2 = requests.post(
    'https://openrouter.ai/api/v1/chat/completions',
    headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
    json={
        'model': 'meta-llama/llama-3.3-70b-instruct',
        'messages': [{'role': 'user', 'content': 'Say hello in one sentence.'}],
        'max_tokens': 30
    },
    timeout=30
)
print('\nPaid model test:', resp2.status_code)
if resp2.status_code == 200:
    content = resp2.json().get('choices', [{}])[0].get('message', {}).get('content', '')
    print('  Response:', content[:100])
else:
    print('  Error:', resp2.text[:200])
