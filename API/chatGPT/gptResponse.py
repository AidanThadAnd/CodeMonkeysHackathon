#openai.api_key = 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

from openai import OpenAI
import os
import pandas as pd
import time

api_key = "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"

client = OpenAI(api_key=api_key)

model="gpt-3.5-turbo"




def how_to_dispose(prompt):

    messages = [{"role": "user", "content": "How should I dispose of " + prompt}]

    response = client.chat.completions.create(model=model, messages=messages, temperature=0,)

    return response.choices[0].message.content

def problems_and_fixes(prompt):

    messages = [{"role": "user", "content": "What are common problems with " + prompt + " and how can I fix them"}]

    response = client.chat.completions.create(model=model, messages=messages, temperature=0)

    return response.choices[0].message.content


responseDisposal = how_to_dispose("Battery")

responseProblems = problems_and_fixes("battery")

print(responseDisposal)

print(responseProblems)

