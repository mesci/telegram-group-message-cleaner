from telethon import TelegramClient
import asyncio
from telethon.errors import FloodWaitError

# Telegram API credentials
api_id = your_api_id
api_hash = "your_api_hash"
session_name = "delete_session" # optional value

# Channel/group id starts with -100
group_id = your_group_id

client = TelegramClient(session_name, api_id, api_hash)


async def delete_all_messages():
    await client.start()
    print("[+] Connection successful, deleting messages...")

    batch = []
    async for message in client.iter_messages(group_id):
        batch.append(message.id)
        if len(batch) >= 100:
            try:
                await client.delete_messages(group_id, batch)
                print(f"[+] {len(batch)} message(s) deleted.")
                batch.clear()
            except FloodWaitError as e:
                print(f"[!] FloodWait: waiting for {e.seconds} seconds...")
                await asyncio.sleep(e.seconds)

    # Remaining messages
    if batch:
        await client.delete_messages(group_id, batch)
        print(f"[+] {len(batch)} message(s) deleted.")

    print("[+] All messages deleted.")


async def main():
    await delete_all_messages()


if __name__ == "__main__":
    asyncio.run(main())
