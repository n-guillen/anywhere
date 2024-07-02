"""
model_response.py

This module defines the services that can be performed on a model's response data.
"""

# Imports
from ....domain.entities.llm.context.context import Context, ContextType
from ....domain.entities.llm.content.text_content import TextContent
from ....domain.entities.llm.content.tool_use_content import ToolUseContent
from anthropic.types.message import Message
from anthropic.types.tool_use_block import ToolUseBlock
from anthropic.types.text_block import TextBlock

# Services
def response_to_context(data: Message) -> Context:
    """Take in a model's response and convert it into context.
    
    Args:
        data (Message): The model's response.
    """
    # Prepare an empty content list, and then collect all the content
    content_list = []
    for content in data.content:
        if isinstance(content, ToolUseBlock): # If the content is a tool use
            content_list.append(ToolUseContent(content.id, content.name, content.input))
        elif isinstance(content, TextBlock): # If the content is normal text
            content_list.append(TextContent(content.text))

    # Create the context to return
    context = Context(content_list, ContextType.assistant)
    return context