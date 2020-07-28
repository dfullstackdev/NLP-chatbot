from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

threeTrainer = ChatterBotCorpusTrainer(chatbot)


threeTrainer.train(
    "./knowledge/3.yml"
)



def brain(usr_input):
    response = chatbot.get_response(usr_input)
    return response
