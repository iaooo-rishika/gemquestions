import requests
import csv
topic = 'seller_reg_pan'
input_file = open("input/seller_reg_pan.txt", "r", encoding="utf-8")
output_file = open(f'output/{topic}.csv', 'w', encoding='utf-8')
writer = csv.writer(output_file)
for line in input_file:
    question = line
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyCfQGKI2XviCyUeZMKrb5q6T05A89K6yxI'
    data = f'{{"contents": [{{"parts": [{{"text": "You are a GeM customer service. Answer the question:\n{question}"}}]}}]}}'
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=data, headers=headers, timeout=10)
    answer = r.json().get('candidates')[0].get(
        'content').get('parts')[0].get('text')
    writer.writerow([question, answer.strip()])
    output_file.flush()
output_file.close()
