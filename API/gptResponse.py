#openai.api_key = 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

import openai
import os
import pandas as pd
import time

openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):


    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(

    model=model,

    messages=messages,

    temperature=0,

)

    return response.choices[0].message["content"]

response = get_completion("say wow")

print(response)

#print(get_completion("Write me a prompt about water"))