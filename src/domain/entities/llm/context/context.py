"""
context.py

This modules defines the context for a model.
"""

# Imports
from enum import Enum
from ..content.content import Content, ContentType

# The types of context
class ContextType(Enum):
    user = "user"
    assistant = "assistant"

class Context:
    def __init__(self, content: list[Content], type: ContextType):
        """The base input for a model to process.

        Args:
            content: The list of content included in this context.
            type: A ContextType enum for this context."""
        self.content = content
        self.type = type

    def to_dict(self):
        return {"type": self.type.name, "content": [content.to_dict() for content in self.content]}