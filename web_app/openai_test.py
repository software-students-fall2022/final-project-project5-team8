import os
import openai

openai.api_key = "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"
message=""
prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman:"
while True:
  message=input()
  if message=="stop":
    break
  prompt=prompt+message+"\nAI:"
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
    )
  answer=response["choices"][0]["text"]
  print(answer)
  prompt=prompt+answer+"\nHuman:"