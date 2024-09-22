"""
prompts.py

This modules defines various prompts used for model generation.
"""

system_prompt = f"""
You are an AI assistant that generates a response(s) mimicking the user's communication style.

Analyze the provided conversation examples between the user and the person you'll be responding to so you can understand the user's tone, vocabulary, and typical message length. These examples are NOT related to the conversation you'll be responding to, they only represent a style to mirror.

You will receive the real conversational context to create a user response for. Ensure the response is contextually appropriate and aligns with any specific guidance provided (if any).
"""

example_mom = f"""
<example>
    <conversation>
        <other>
            Thank you for spending time with your little brother. I'm just laying down not sleeping. Just knock on the door if y'all need anything. Love you.
        </other>
        <user>
            We just got off, it was really fun, love you mom please feel better I'll go and get the tests in a little ❤️
        </user>
    </conversation>
</example>

<example>
    <conversation>
        <other>
            Can you please get some money from your dad and get underwear and medicine for Levi. Thank you.
        </other>
        <user>
            Hey mom dad gave me the card and I got Levi some more packs of underwear and dad some
            cough drops, didn't know we needed any medicine when I went, hope you're feeling better
            love you ❤️
        </user>
        <other>
            Thank you so much!! Love you too 😘
        </other>
        <user>
            Love you mom and I'll do the dishes later too! ❤️
        </user>
    </conversation>
</example>

<example>
    <conversation>
        <other>
            Hey monkey are you feeling better?
        </other>
        <user>
            Hey mom I'm feeling much better it was just bad gas! :) Safely at the apartment ❤️
        </user>
        <other>
            That damn gas will really get you 🤣😂.. Please call me before your trip on Friday. I
            love you. Say your prayers 😇🙏
        </other>
        <user>
            I will let you know mom!! Yes you're right that damn gas🤣🤣 Love you mom get some good
            sleep tonight and make sure you eat! You're beautiful stop worrying about that! Love
            you! ❤️🌏
        </user>
        <other>
            Your sweet thank you. I have to confess, I stopped and got Cheerios. Please don't share
            that . I love you. Say your prayers 😇 🙏
        </other>
        <user>
            Don't worry that'll be between me, you, and God 🙏🏻🤣 Love you mom say your prayers too
            😁❤️
        </user>
        <other>
            Thank you. Love you. Goodnight 😘😴
        </other>
        <user>
            ❤️🌏
        </user>
    </conversation>
</example>
"""
