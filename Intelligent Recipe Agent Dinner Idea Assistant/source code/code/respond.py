import openai
import os

conversation_history = ["From now on, you will act as my smart kitchen steward and make actionable recipe recommendations for the ingredients I have available (in addition to existing recipes on the Internet, you will also need to consider personal recipes uploaded by users). You need to act natural, like you're talking to me again. After the user really wants to cook a dish, you need to provide him with a detailed recipe, which must be broken down (must contain the required ingredients, and steps) content. In addition, I need you to improvise an opening statement that leads the user to ask you a question, and of course the user can chat if they want to. No need to say of course, I'm happy to be your smart kitchen butler kind of response, just get started. There is no need to imagine that you are who who, because you are now my smart kitchen housekeeper, pay attention to identity. Here is a transcript of our chat:"]

def respond(conver, trans):
    # Set proxy if needed
    os.environ["http_proxy"] = "http://localhost:7890"
    os.environ["https_proxy"] = "http://localhost:7890"

    # Initialize OpenAI client
    client = openai.OpenAI(api_key='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')

    transcript = trans

    conver.append("User: " + transcript)

    # Send the entire conversation history to GPT-3
    full_prompt = "User: " + transcript + "Please use 'Assistance: ' as your opening moniker. "
    print(full_prompt)
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=full_prompt,
        max_tokens= 100
    )

    """
    # Convert GPT-3 response to audio using gTTS
    tts = gTTS(response['choices'][0]['text'])
    tts.save("response.mp3")
    """
    return response.choices[0].text
if __name__ == '__main__':
    respond(conversation_history,'hi')