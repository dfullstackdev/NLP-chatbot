from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

zeroTrainer = ChatterBotCorpusTrainer(chatbot)


zeroTrainer.train(
    "./0.yml"
)



def brain(user_input):
    response = chatbot.get_response(user_input)
    return response
