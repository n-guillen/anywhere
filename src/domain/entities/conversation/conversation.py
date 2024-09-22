"""
conversation.py

This module defines a conversation.
"""

# Imports
from .message import Message

class Conversation:
    def __init__(self, messages: list[Message] = None):
        self.messages: list[Message] = messages
