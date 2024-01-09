import os
import csv
import time
import json
from pathlib import Path
import sys
from models.gemini_pro import GeminiPro
from models.chat_openai import ChatOpenai
from models.canopy_pinecone import CanopyPinecone


model_name = sys.argv[1]
output_format = sys.argv[2]
match model_name:
    case "gemini_pro":
        model = GeminiPro()

    case "chat_openai":
        model = ChatOpenai()

    case "canopy_pinecone":
        model = CanopyPinecone()


for filename in os.listdir('input'):
    if not filename.endswith('.txt'):
        continue
    input_file_path = f'input/{filename}'
    output_folder = f'output/{output_format}/{model_name}/{time.strftime("%Y%m%d")}'
    os.mkdir(output_folder)
    output_file_path = f'{output_folder}/{Path(filename).stem}.{output_format}'
    if not Path(input_file_path).exists() or os.stat(input_file_path).st_size == 0:
        continue
    input_file = open(input_file_path, "r", encoding="utf-8")
    if Path(output_file_path).exists() and os.stat(output_file_path).st_size != 0:
        continue
    print(filename)
    output_file = open(output_file_path, 'w', encoding='utf-8')
    if output_format == 'csv':
        writer = csv.writer(output_file)
    for line in input_file:
        question = line
        answer = model(question)
        if output_format == 'csv':
            writer.writerow([question, answer.strip()])
        elif output_format == 'jsonl'
            json.dump({"question": question, "answer": answer}, output_file)
            output_file.write("\n")
        output_file.flush()
    output_file.close()
