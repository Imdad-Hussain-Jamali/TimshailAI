import google.generativeai as genai
APIKEY = 'AIzaSyA_OG7LM9zB_auwCXXdNfl1pzE0TdciVbw'

genai.configure(
    api_key = APIKEY
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while (True):
    question = input ("you:")
    if (question.strip()==""):
        break
    response = chat.send_message(question)
    print('\n')
    print (f"Bot:{response.text}")
    print('\n')