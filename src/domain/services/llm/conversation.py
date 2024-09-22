"""
conversation.py

This module defines conversation functionality for the model.
"""

# Imports
from ...entities.conversation.conversation import Conversation
from ...entities.conversation.message import Message, MessageType

#
def format_conversation(conversation: Conversation) -> str:
    """Format a conversation into an XML structure for the model to interpret easier.

    Args:
        conversation (conversation): The conversation to format."""
    format = ""
    for message in conversation.messages:
        formatted_message = (
            f"<{message.type.value}>{message.text}</{message.type.value}>"
        )
        format += formatted_message
    return f"<conversation>{format}</conversation>"
