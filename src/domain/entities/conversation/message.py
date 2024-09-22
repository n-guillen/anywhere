"""
message.py

This module defines a message.
"""
# Imports
from enum import Enum

# The types of messages
class MessageType(Enum):
    user = "user"
    other = "other"

class Message:
    def __init__(self, text: str, type: MessageType):
        self.text = text
        self.type = type