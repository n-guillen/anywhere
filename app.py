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
guidance = "None."
examples = example_roman

response_prompt = f"""
{system_prompt}

<examples>{examples}</examples>

<guidance>{guidance}</guidance>
"""

conversation = f"""
<real>
    {format_conversation(
        Conversation([
            Message("Hey bro! Going to canes with some of my friends!! Tell the fam, love you!! ❤️", MessageType.other),
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