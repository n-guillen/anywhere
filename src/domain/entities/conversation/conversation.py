"""
conversation.py

This module defines a conversation.
"""

# Imports
from .message import Message

class Conversation:
    def __init__(self):
        self.messages: list[Message]
