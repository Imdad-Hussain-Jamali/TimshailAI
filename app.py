from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

APIKEY = 'AIzaSyA_OG7LM9zB_auwCXXdNfl1pzE0TdciVbw'  # Replace 'Your_API_Key_Here' with your actual API key

genai.configure(
    api_key=APIKEY
)

app = Flask(__name__)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data['question']
    if question.strip() == "":
        return jsonify({"response": "Please ask a question."})

    response = chat.send_message(question)
    return jsonify({"response": response.text})


if __name__ == '__main__':
    app.run(debug=True)
