import json

text = '{"temperature":"23", "humidity": "60", "info":"多云", "wid": "01", "direct": "东风", "power": "4级", "aqi": "58"}'

print('----')
test_json = json.loads(text)
result_json = test_json.get('temperature')

print('1111', test_json.get('temperature'))


