import os
import openai
from flask import Flask, request, render_template  
app = Flask(__name__)  
openai.api_type = "azure"
openai.api_base = "https://openaitestxops.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="test-gpt-35-turbo",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. \n \nHuman: Hello, who are you? \nAI: Hello, I am an AI assistant. I am here to help you with anything you need.\nHuman: I'd like to cancel my subscription. \nAI: Sure thing, I can help you with that. Can you please tell me the name of the subscription and the reason for canceling? \n",
  temperature=0.9,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["Human:","AI:"])