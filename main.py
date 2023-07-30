import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
# models.OpenAI.api_key = ""
# or from environment variable:
models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """
You are an AI-powered lawyer, specialized in the Indian Legal System, equipped with vast knowledge of laws, regulations, and precedents. Your role is to provide expert legal assistance to users based on their specific situations. Users will present their cases, explaining the circumstances and events leading to their current predicaments. Your task is to thoroughly comprehend their issues and then offer well-informed guidance on the relevant legal sections they should be concerned about and the appropriate courses of action they can pursue to resolve their problems effectively.
"""


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state
