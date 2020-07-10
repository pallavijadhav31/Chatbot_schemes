from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_ngrok import run_with_ngrok
from chatterbot.trainers import ListTrainer
app = Flask(_name_,template_folder="templates")
run_with_ngrok(app)
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english",)
#trainer.train(["Hi there!","Hello"])
#trainer.train(["Greetings!","Hello",])
chatbot = ChatBot('Udaan')
trainer = ListTrainer(chatbot)
#trainer.train(["Hi there!","Hello"])
#trainer.train(["Greetings!","Hello"])
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText=="Hi" or userText=="Hello":
      return "How may I help you?"
    if userText=="Schemes" or userText=="Policy":
      return "Which Kind of Scheme you are interested in?"
    if userText=="Pensioners":
      return "Integrated Programme for Older Persons (IPOP),Rashtriya Vayoshri Yojana (RVY),Indira Gandhi National Old Age Pension Scheme (IGNOAPS),The Pradhan Mantri Vaya Vandana Yojana"
    if userText=="Female" or userText=="Women":
      return "Mahila E-haat ,Beti Bachao, Beti Padhao,One Stop Centre Scheme,Working Women Hostels"
    if userText=="Minority":
      return "Schemes"
    if userText=="BPL":
      return "Pradhan Mantri Jan Dhan Yojna (PMJDY),Sukanya Samriddhi Yojna (SSY),Rashtriya Swasthya Bima Yojana (RSBY),National Social Assistance scheme,Pradhan Mantri Mudra Yojana."
    if userText=='Bye':
      return "Ok bye!!"
    return str(chatbot.get_response(userText))
 
 
if _name_ == "_main_":
    app.run()
