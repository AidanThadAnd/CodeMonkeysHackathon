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

    finalResponse = response.choices[0].message.content
    return finalResponse

def common_fixes(prompt):

    messages = [{"role": "user", "content": "What are 3 common problems with " + prompt + " and how can I fix them"}]

    response = client.chat.completions.create(model=model, messages=messages, temperature=0)

    finalResponse = response.choices[0].message.content
    return finalResponse


