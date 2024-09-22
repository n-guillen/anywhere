# Imports
from src.domain.entities.llm.context.context import Context, ContextType
from src.domain.entities.llm.content.text_content import TextContent
from src.domain.services.llm.invoke_chat_model import invoke_chat_model
from src.domain.entities.llm.prompts.prompts import system_prompt, example_mom

# Create the main system prompt and provide examples
guidance = "None."
examples = example_mom

response_prompt = f"""
{system_prompt}

<examples>{examples}</examples>

<guidance>{guidance}</guidance>
"""

conversation = f"""
<real>
    <conversation>
        <other>
            Thank you for taking care of your little brother. You have no idea how much this means.
            You're a sweetheart. Please call if y'all need anything. Love you 🙏❤️
        </other>
        <other>
            He looks good in that car!! 😁
        </other>
    </conversation>
</real>
"""

# Create the starting context window
window = [
    Context([TextContent(conversation)],ContextType.user)
]

# Process it
response = invoke_chat_model(window, response_prompt)

print(response.to_dict())
