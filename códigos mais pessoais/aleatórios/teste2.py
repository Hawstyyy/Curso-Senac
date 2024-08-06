import os
import replicate
import json


os.environ["REPLICATE_API_TOKEN"] = "r8_6BibR9FC5aNVfR5MEpY02uNvTk8TYtm4cIC9K"

# pre_prompt = "oi"
# prompt = input("\n- Insira a pergunta que deseja fazer: ").capitalize()

# output = replicate.run("al6z-infra/llama13b-v1-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a4lcc40061269e5",
# input={"prompt": f"{pre_prompt} {prompt} Assistant: "})

# full_response = ""

# for item in output:
#   full_response += item

# print(full_response)

input = {
    "top_p": 1,
    "prompt": "Tell me how to tailor a men's suit so I look fashionable.",
    "temperature": 0.75,
    "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
    "max_new_tokens": 800,
    "repetition_penalty": 1
}

for event in replicate.stream(
    "meta/llama-2-7b-chat",
    input=input
):
    print(event, end="")