import openai
import gradio

openai.api_key = "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"
#                                 /\
#                                /  \
#                                 |
#enter your Open AI API key here__|

messages = [{"role": "system", "content": "You are an Data structure and algorithms industry expert that have 20 years of experience and have an tremendous knowledge"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "DSA Expert")

demo.launch(share=True)