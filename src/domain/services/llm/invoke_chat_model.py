"""
invoke_chat_model.py

This modules defines the service for invoking a model.
"""

# Imports
from ...entities.llm.context import Context
import anthropic


# Invoke a chat model
def invoke_chat_model(window: list[Context]):
    """Invoke a chat model and returns its response data.
    
    Args:
        window (list): The context window for a chat model to process a response for."""
    return anthropic.Anthropic().messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=(1024 * 3),
        messages=[
            {"role": context.type.value, "content": context.content}
            for context in window
        ]
    )
