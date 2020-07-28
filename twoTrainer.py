from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

twoTrainer = ChatterBotCorpusTrainer(chatbot)


twoTrainer.train(
    "./knowledge/2.yml"
)



def brain(Uinput):
    response = chatbot.get_response(Uinput)
    return response
