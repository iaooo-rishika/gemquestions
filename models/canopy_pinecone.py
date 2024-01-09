import requests
import re


class CanopyPinecone:

    def __init__(self) -> None:
        pass

    def __call__(self, question: str) -> str:
        question = question.rstrip("\n")
        url = 'http://localhost:8000/v1/chat/completions'
        data = f'{{"messages": [{{"role": "user","content": "{question}"}} ]}}'
        headers = {'Content-Type': 'application/json'}

        try:
            r = requests.post(url, data=data, headers=headers, timeout=60)
            answer = r.json().get('choices')[0].get('message').get('content')
            answer = re.sub(r'Source.*\n\n', '', answer)
            return answer[:answer.find('Source:')].strip()

        except requests.exceptions.Timeout as e:
            print(e)
            return "Timeout error contacting API"

        except TypeError as e:
            print(e)
            return "Error processing response from API"
