from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_ngrok import run_with_ngrok
from chatterbot.trainers import ListTrainer

# import hyperlink
app = Flask(__name__, template_folder="template")
run_with_ngrok(app)
# english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# trainer = ChatterBotCorpusTrainer(english_bot)
# trainer.train("chatterbot.corpus.english",)
# trainer.train(["Hi there!","Hello"])
# trainer.train(["Greetings!","Hello",])
chatbot = ChatBot('Udaan')
trainer = ListTrainer(chatbot)
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
    "Scheme",
    "Tell me your gender",
    "Male",
    "Age",
    "10",
    "Income group",
    "BPL",
    "Student or Non Student",
    "Non Student"
]
conversation1 = [
    "Hi",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
    "Scheme",
    "Tell me your gender",
    "Female",
    "Age",
    "50",
    "Income group",
    "BPL",
    "Student or Non Student",
    "Non Student"
]
trainer.train(conversation)
trainer.train(conversation1)


# trainer.train(["Hi there!","Hello"])
# trainer.train(["Greetings!","Hello"])
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText == "Policy" or "Scheme":
        return "Which Scheme you are interested in?" + "\n" + "Women/BPL/Student?/Pensioner"
    if userText == 'Bye':
        return "Ok bye!!"
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()