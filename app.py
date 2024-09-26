# Imports
from src.domain.entities.conversation.conversation import Conversation
from src.domain.entities.conversation.message import Message, MessageType

from src.domain.entities.llm.context.context import Context, ContextType
from src.domain.entities.llm.content.text_content import TextContent
from src.domain.services.llm.invoke_chat_model import invoke_chat_model
from src.domain.entities.llm.prompts.prompts import system_prompt
from src.domain.services.llm.conversation import format_conversation

from conversation_examples import example_roman

# Create the main system prompt and provide examples
mirror = f"""
    <firstname>Noah</firstname>
    <lastname>Guillen</lastname>
    <age>20</age>
    <dob>10/26/2003</dob>
"""
guidance = "my plans changed ill be back soon"
examples = example_roman

response_prompt = f"""
{system_prompt}

<mirror>{mirror}</mirror>

<examples>{examples}</examples>

<guidance>{guidance}</guidance>
"""

conversation = f"""
<real>
    {format_conversation(
        Conversation([
            Message("You all good bro ?", MessageType.other),
        ])
    )}
</real>
"""

# Create the starting context window
window = [
    Context([TextContent(conversation)],ContextType.user)
]

# Process it
response = invoke_chat_model(window, response_prompt)

print(response.to_dict())