#install nltk as well
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import  json
import time
time.clock = time.time #newer version of python

bob=ChatBot('Bob')

with open('newIntent.json', 'r') as f:
    intents = json.load(f)

train=[]

for k, i in enumerate(intents):
    #print(i)
    train.append((i['patterns']))
    train.append(i['responses'])
    #train.append((i['question']))
    #train.append(i['answer'])
    if k>100:
        break

trainer=ListTrainer(bob)

trainer.train(train)

while True:
    while True:
        req = input("You : ")
        response = bob.get_response(req)
        print('Bob : ', response)


'''

trainer=ListTrainer(bot)

trainer.train(intents)

while True:
    req=input("You : ")
    response=bot.get_response(req)
    print('Bob : ',response)
'''
