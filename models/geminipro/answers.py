import os
import csv
import requests
from pathlib import Path

directory = '../../input'

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        input_file_path = f'../../input/{filename}'
        output_file_path = f'../../output/{Path(filename).stem}.csv'
        if not Path(input_file_path).exists() or os.stat(input_file_path).st_size == 0:
            continue
        input_file = open(input_file_path, "r", encoding="utf-8")
        if Path(output_file_path).exists() and os.stat(output_file_path).st_size != 0:
            continue
        print(filename)
        output_file = open(output_file_path, 'w', encoding='utf-8')
        writer = csv.writer(output_file)
        for line in input_file:
            question = line
            url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={os.getenv("GEMINI_PRO_API_KEY")}'
            data = f'{{"contents": [{{"parts": [{{"text": "You are a GeM customer service. Answer the question:\n{question}"}}]}}]}}'
            headers = {'Content-Type': 'application/json'}
            try:
                r = requests.post(url, data=data, headers=headers, timeout=30)
                answer = r.json().get('candidates')[0].get(
                    'content').get('parts')[0].get('text')
                writer.writerow([question, answer.strip()])
                output_file.flush()
            except requests.exceptions.Timeout as e:
                print(e)
            except TypeError as e:
                print(e)
        output_file.close()
