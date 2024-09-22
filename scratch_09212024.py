# Imports
from src.domain.entities.llm.context.context import Context, ContextType
from src.domain.entities.llm.content.text_content import TextContent
from src.domain.services.llm.invoke_chat_model import invoke_chat_model

# Create the starting context window
window = [
    Context(
        [
            TextContent("Hey Claude! How are you doing? Please tell me what color clouds are..."),
            TextContent("Also please tell me when the exact date of the moon landing was? Nothing else.")
        ],
        ContextType.user,
    )
]

# Process it
response = invoke_chat_model(window)

print(response.to_dict())