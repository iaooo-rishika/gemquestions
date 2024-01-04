import os
import requests


class GeminiPro:
    def __init__(self) -> None:
        pass

    def __call__(self, question: str) -> str:
        # Call the Gemini Pro API to get an answer
        url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={os.getenv("GEMINI_PRO_API_KEY")}'
        data = f'{{"contents": [{{"parts": [{{"text": "You are a Government e-Marketplace (GeM) customer service. Answer the question:\n{question}"}}]}}]}}'
        headers = {'Content-Type': 'application/json'}

        try:
            r = requests.post(url, data=data, headers=headers, timeout=30)
            answer = r.json().get('candidates')[0].get(
                'content').get('parts')[0].get('text')
            return answer.strip()

        except requests.exceptions.Timeout as e:
            print(e)
            return "Timeout error contacting API"

        except TypeError as e:
            print(e)
            return "Error processing response from API"
