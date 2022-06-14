#coding: utf-8 *

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('FICR BOT')

conversa = [
  'Oi', 'Olá', 
  'Tudo bem?', 'Tudo ótimo', 
	'Você gosta de programar?', 'Sim, eu programo em Python'
]

trainer = ListTrainer(bot)
trainer.train(conversa)

def ask_bot(input):
  answer = bot.get_response(input)
  if(float(answer.confidence) > 0.5):
    return f"{bot.name}: {answer}"

  return f"{bot.name}: {answer}"
  