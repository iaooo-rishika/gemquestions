from openai import OpenAI
client = OpenAI()


class ChatOpenai:
    def __init__(self) -> None:
        pass

    def __call__(self, question: str) -> str:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system",
                 "content": "You are a customer service chat bot for Government e-Marketplace (GeM). You only answer customer questions about GeM. Answer questions to help sellers who wish to sell on GeM."},
                {"role": "user", "content": question}
            ]
        )
        return completion.choices[0].message.content.strip()
