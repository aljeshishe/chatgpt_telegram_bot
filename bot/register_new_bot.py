from telethon import TelegramClient, events

api_id = 21195270
api_hash = "9c45dc2e764dd0d70431c161628c765f"
client = TelegramClient('session', api_id, api_hash)

BOT_NAME="grachev_test_f2314rf"
BOT_USER_NAME="grachev_test_f2314rf_bot" # must end with -bot

@client.on(events.NewMessage)
async def message_handler(event):
    if 'Please choose a name for your bot' in event.raw_text:
        await event.reply(BOT_NAME)
    elif 'choose a username for your bot' in event.raw_text:
        await event.reply(BOT_USER_NAME)
    elif 'Done! Congratulations on your new bot' in event.raw_text:
        print("Bot created!")
        await client.disconnect()

async def main():
    await client.send_message('botfather', '/newbot')


with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
