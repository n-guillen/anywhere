# Imports
from src.domain.entities.conversation.conversation import Conversation
from src.domain.entities.conversation.message import Message, MessageType
from src.domain.services.llm.conversation import format_conversation

example_mom = f"""
<example>
    {format_conversation(Conversation([
        Message("Thank you for spending time with your little brother. I'm just laying down not sleeping. Just knock on the door if y'all need anything. Love you.", MessageType.other),
        Message("We just got off, it was really fun, love you mom please feel better I'll go and get the tests in a little ❤️", MessageType.user),
    ]))}
</example>

<example>
    {format_conversation(Conversation([
        Message("Can you please get some money from your dad and get underwear and medicine for Levi. Thank you.", MessageType.other),
        Message("Hey mom dad gave me the card and I got Levi some more packs of underwear and dad some cough drops, didn't know we needed any medicine when I went, hope you're feeling better love you ❤️", MessageType.user),
        Message("Thank you so much!! Love you too 😘", MessageType.other),
        Message("Love you mom and I'll do the dishes later too! ❤️", MessageType.user),
    ]))}
</example>

<example>
    {format_conversation(Conversation([
        Message("Hey monkey are you feeling better?", MessageType.other),
        Message("Hey mom I'm feeling much better it was just bad gas! :) Safely at the apartment ❤️", MessageType.user),
        Message("That damn gas will really get you 🤣😂.. Please call me before your trip on Friday. I love you. Say your prayers 😇🙏", MessageType.other),
        Message("I will let you know mom!! Yes you're right that damn gas🤣🤣 Love you mom get some good sleep tonight and make sure you eat! You're beautiful stop worrying about that! Love you! ❤️🌏", MessageType.user),
        Message("Your sweet thank you. I have to confess, I stopped and got Cheerios. Please don't share that . I love you. Say your prayers 😇 🙏", MessageType.other),
        Message("Don't worry that'll be between me, you, and God 🙏🏻🤣 Love you mom say your prayers too 😁❤️", MessageType.user),
        Message("Thank you. Love you. Goodnight 😘😴", MessageType.other),
        Message("❤️🌏", MessageType.user),
    ]))}
</example>
"""

example_dad = f"""
<example>

</example>
"""

example_roman = f"""
<example>
    {format_conversation(Conversation([
        Message("we 2 hrs away!!", MessageType.user),

        Message("Shoots bro super duper pretty ! Enjoy then next few hours fr homes !", MessageType.other),

        Message("You know it bro! Love you Roman keep everyone good at the house 😁❤️", MessageType.user),

        Message("Gotcha bro! Love you lots Noah have fun ❤️❗", MessageType.other)
    ]))}
</example>

<example>
    {format_conversation(Conversation([
        Message("Hecks yeah!!! I'm off TMR !", MessageType.user),

        Message("forgot to call and say 🤣 when are you going to OH. !", MessageType.user),

        Message("I be going on the 17!!!", MessageType.other),

        Message("Ight!!!! Is mom be there ?!", MessageType.user),

        Message("Mom is be there!", MessageType.other),
    ]))}
</example>

<example>
    {format_conversation(Conversation([
        Message("I appreciate you washing my clothes popps! And thanks for the moola man, you didn't have to do that but it really helps ❗ 🤙❤️", MessageType.other),

        Message("You know it bro it's more than well desevered!! Go out there and have fun today, cheese it up 🤣🤣 Love you Roman, super proud!! 🤙❤️❤️🥁❗", MessageType.user),

        Message("Hey bro what time you thinking for the ride tonight? Rough ETA? Love you ❤️", MessageType.user),

        Message("Around 11!! Love you bro 🥁", MessageType.other),

        Message("Sounds good it will either be me or mom, love you bro light that snare on fire!! 🥁🔥❤️❗", MessageType.user),

        Message("Love you homes !", MessageType.other),

        Message("I'll be there in a hour and 50 min!", MessageType.other),

        Message("Love you bro mom will get you!! Sups proud of you!!", MessageType.user),

        Message("Preesh homes! ❗❗", MessageType.other),
    ]))}
</example>
"""

# {format_conversation(Conversation([
#     Message("-", MessageType.other),

#     Message("-", MessageType.user),

#     Message("-", MessageType.other),

#     Message("-", MessageType.user),

#     Message("-", MessageType.other),

#     Message("-", MessageType.user),
# ]))}
