"""
context.py

This modules defines the context for a model.
"""

# Imports
from enum import Enum


# The types of context
class ContextType(Enum):
    user = "user"
    assistant = "assistant"

class Context:
    def __init__(self, content: str, type: ContextType):
        """The base input for a model to process.

        Args:
            content: The string content of this context.
            type: A ContextType enum for this context."""
        self.content = content
        self.type = type

    def __str__(self):
        return self.content

    def to_dict(self):
        return {"content": self.content, "type": self.type.name}