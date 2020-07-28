from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

oneTrainer = ChatterBotCorpusTrainer(chatbot)


oneTrainer.train(
    "./knowledge/1.yml"
)



def brain(u_input):
    response = chatbot.get_response(u_input)
    return response
