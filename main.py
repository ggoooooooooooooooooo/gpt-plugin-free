import wolframalpha

from mtranslate import translate
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from openai import OpenAI
from config import *

def translate_text(text):
    return translate(text, 'en')

def get_responce(message_list, model,):
    client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
    response = client.chat.completions.create(
        messages=message_list,
        model=model,
    )
    return response.choices[0].message.content

def get_wolframalpha(question):
    client = wolframalpha.Client(APP_ID)
    responce = get_responce([{"role": "user", "content": f'{promt}: {question}'}], model="gpt-3.5-turbo")
    text = ""
    for x in responce.splitlines():
        cond = False
        result = client.query(translate_text(x))
        
        for p in result.pods:
            if cond:
                try:
                    text += p.text
                except:print('Неверный тип')
            else:
                cond = True
    return text

def chat():
    message_list = []
    models_list = ['gpt-3.5-turbo', 'gemini-pro', 'code-llama-34b']
    model_end = 'gpt-3.5-turbo'
    
    while True:
        question = textarea("Ваше сообщение:", placeholder="Введите сообщение", type=TEXT)
        model_end = select("Выберите модель", models_list, value=model_end)
        choices = checkbox("Выберите wolframalpha", options=["ДА", 'НЕТ'])
        
        try:
            filex = file_upload("Загрузите файл")['content'].decode('utf-8')
        except:filex = ""
        
        put_text('Вы:', question)

        if question == "чат":
            message_list = []
            continue
        
        if choices == "ДА":
            message_list.append({"role": "user", "content": question+filex+'\n wolframalpha: '+get_wolframalpha(question)})
        else:
            print('НЕТ')
            message_list.append({"role": "user", "content": question+filex})
        #message_list.append({"role": "user", "content": question+filex+'\n wolframalpha: '+get_wolframalpha(question)})  
        put_markdown(get_responce(message_list, model=model_end))

if __name__ == '__main__':
    start_server(chat, port=80)
