"""
invoke_chat_model.py

This modules defines the service for invoking a model.
"""

# Imports
from ...entities.llm.context.context import Context
from .model_response import response_to_context
import anthropic

# Invoke a chat model
def invoke_chat_model(window: list[Context], system: str = None) -> Context:
    """Invoke a chat model and returns its response context.
    
    Args:
        window (list): The context window for a chat model to process a response for."""
    response = anthropic.Anthropic().messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=(1024 * 3),
        system=system or "",
        messages=[
            {
                "role": context.type.value,
                "content": [
                    content.to_dict() for content in context.content
                ]
            }
            for context in window
        ]
    )
    return response_to_context(response)