from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

fourTrainer = ChatterBotCorpusTrainer(chatbot)


fourTrainer.train(
    "./knowledge/4.yml"
)



def brain(input):
    response = chatbot.get_response(input)
    return response
