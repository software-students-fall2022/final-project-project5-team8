import os
import openai


def get_response(message,targ):
  openai.api_key = "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"
  prompt="The following is a conversation in "+targ+" between two people. Respond in the according language.\n\nPerson1:"+message+"\n\nPerson2:"
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  )
  answer_targ=response["choices"][0]["text"].replace("\n","")
  prompt="The following sentence is in "+targ+"\n\nPlease translate it into English, the translation should be literal, casual, and grammatically correct.\nSentence:"+answer_targ
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  )
  answer_eng=response["choices"][0]["text"].replace("\n","")
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Correct this to standard English:\n\n"+answer_eng,
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
  answer_eng=response["choices"][0]["text"].replace("\n","")
  return [answer_targ, answer_eng]

print(get_response("我是弱智","Chinese"))