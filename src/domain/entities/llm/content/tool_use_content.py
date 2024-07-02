"""
tool_use_content.py

This modules defines the tool use content derived from the base content that a model will construct when calling a provided tool.
"""
# Imports
from .content import Content, ContentType

# The tool use content class derived from the base content class
class ToolUseContent(Content):
    def __init__(self, id: str, name: str, input: str):
        """The tool use that a model will construct when calling a provided tool.
        
        Args:
            id (str): The tool use id.
            name (str): The name of the tool being called.
            input (str): The parameters the tool is calling for."""
        super().__init__(ContentType.text)
        self.id = id
        self.name = name
        self.input = input
    def to_dict(self):
        content_dict = super().to_dict()
        content_dict.update(
            {
                "id": self.id,
                "name": self.name,
                "input": self.input
            }
        )
        return content_dict
