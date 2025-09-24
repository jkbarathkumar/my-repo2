import chainlit as cl
@cl.on_message
async def on_message(msg: str):
    await cl.Message(content=f"You said: {msg}").send()
