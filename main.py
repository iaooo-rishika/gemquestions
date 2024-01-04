import os
import csv
from pathlib import Path
import sys
from models.gemini_pro import GeminiPro
from models.chat_openai import ChatOpenai


model_name = sys.argv[1]
match model_name:
    case "gemini_pro":
        model = GeminiPro()

    case "chat_openai":
        model = ChatOpenai()


for filename in os.listdir('input'):
    if not filename.endswith('.txt'):
        continue
    input_file_path = f'input/{filename}'
    output_file_path = f'output_{model_name}/{Path(filename).stem}.csv'
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
        answer = model(question)
        writer.writerow([question, answer.strip()])
        output_file.flush()
    output_file.close()
