"""
content.py

This modules defines the base content that a model can processes through context.
"""
# Imports
from enum import Enum

# The types of content
class ContentType(Enum):
    text = "text"
    image = "image"
    tool_use = "tool_use"
    tool_result = "tool_result"

# The base content class
class Content():
    def __init__(self, type: ContentType):
        """The base content a model can input.
        
        Args:
            type (enum): The content type."""
        self.type = type
    
    def to_dict(self):
        """Return this content's attributes."""
        return {
            "type": self.type.value
        }
        