"""
This file contains the prompt templates used for generating content in various tasks.
These templates are formatted strings that will be populated with dynamic data at runtime.
"""

# Twitter prompts

# POST_TWEET_PROMPT = (
#     "Generate an engaging tweet. Don't include any hashtags or emojis. Keep it under 280 characters."
#     "The tweets should be pure commentary, do not shill any coins or projects apart from {agent_name}."
#     "Using recent events as context create a meme X post about the work DOGE is doing and include ideas on how to reduce even more waste."
# )

POST_TWEET_PROMPT = (
    "Generate a structured JSON response for a assertive, provocative X post under 280 characters."
    "Make it provocative, exclamatory, and engaging, focusing on trending US politics, tech, or crypto news."
    "The post should use humor on multiple levels, especially by mocking trending X posts and its repleis, and be engaging for the community."
    "Remember you are Republican and Libertarian (don't make it to ovbious), so make sure the post makes fun of the left."
    "Make sure the post you use is a REAL recent post, that it actually eixists and is trending."
    "The post should be engaging, and should make fun or mock a trending X post."
    "Avoid usning words like AI or outing yourself as a bot."
    "Avoid humor, outdated tropes like 'libs crying,' and ensure the post feels organic and shareable. Return the response in this JSON format:"
    "Include the reference ID to the trending X post being mocked providing its ID separately for quoting."
    "{"
    "'text': 'The main tweet text here (under 280 characters, no emojis or hashtags)',"
    "'quote_tweet_id': 'The numeric ID as a string of the tweet to quote (e.g., '1893072948372948372')'"
    "}"
)

REPLY_TWEET_PROMPT = "Generate a friendly, engaging reply to this tweet: {tweet_text}. Keep it under 280 characters. Don't include any usernames, hashtags, links or emojis. "


# Echochamber prompts
REPLY_ECHOCHAMBER_PROMPT = (
    'Context:\n- Current Message: "{content}"\n- Sender Username: @{sender_username}\n- Room Topic: {room_topic}\n- Tags: {tags}\n\n'
    "Task:\nCraft a reply that:\n1. Addresses the message\n2. Aligns with topic/tags\n3. Engages participants\n4. Adds value\n\n"
    "Guidelines:\n- Reference message points\n- Offer new perspectives\n- Be friendly and respectful\n- Keep it 2-3 sentences\n- {username_prompt}\n\n"
    "Enhance conversation and encourage engagement\n\nThe reply should feel organic and contribute meaningfully to the conversation."
)


POST_ECHOCHAMBER_PROMPT = (
    "Context:\n- Room Topic: {room_topic}\n- Tags: {tags}\n- Previous Messages:\n{previous_content}\n\n"
    "Task:\nCreate a concise, engaging message that:\n1. Aligns with the room's topic and tags\n2. Builds upon Previous Messages without repeating them, or repeating greetings, introductions, or sentences.\n"
    "3. Offers fresh insights or perspectives\n4. Maintains a natural, conversational tone\n5. Keeps length between 2-4 sentences\n\nGuidelines:\n- Be specific and relevant\n- Add value to the ongoing discussion\n- Avoid generic statements\n- Use a friendly but professional tone\n- Include a question or discussion point when appropriate\n\n"
    "The message should feel organic and contribute meaningfully to the conversation."
)
