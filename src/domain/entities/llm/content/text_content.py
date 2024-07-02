"""
text_content.py

This modules defines the text content derived from the base content.
"""
# Imports
from .content import Content, ContentType

# The text content class derived from the base content class
class TextContent(Content):
    def __init__(self, text: str):
        """Textual content that can be included in a model's context.
        
        Args:
            text (str): The text content."""
        super().__init__(ContentType.text)
        self.text = text
    def to_dict(self):
        content_dict = super().to_dict()
        content_dict.update(
            {
                "text": self.text
            }
        )
        return content_dict
