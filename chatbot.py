from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def create_chatbot(name='Synapsea'):
    bot= ChatBot(name)
    return bot

def train_chatbot(bot, corpus_files):
    trainer = ChatterBotCorpusTrainer(bot)
    if isinstance(corpus_files, list):
        for corpus in corpus_files:
            if corpus.endswith('.yml') or corpus.endswith('.yaml'):
                trainer.train(f"./{corpus}")
            else:
                trainer.train(corpus)
    else:
            trainer.train(corpus_files)

def chat_loop(bot):
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Synapsea: Görüşmek üzere!!")
            break
        response = bot.get_response(user_input)
        if float(response.confidence) < 0.5:
            print("Synapsea: üzgünüm, bunu anlamadım. Başka bir şey sorabilir misin?")
        else: 
            print("Synapsea:", response)
import sys

if __name__ == "__main__":
    bot = create_chatbot()
    if len(sys.argv) > 1 and sys.argv[1] == "train":
        train_chatbot(bot, ["chatterbot.corpus.english", "Data/turkce_corpus.yml"])
        print("Training completed.")
    else:
        chat_loop(bot)
    # The chat loop already handles user input and exit logic.
    # No need to duplicate it here.

import yaml

with open("Data/turkce_corpus.yml", encoding="utf-8") as f:
    data = yaml.safe_load(f)
print(data)


