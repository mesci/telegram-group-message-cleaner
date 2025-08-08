# Telegram Group Message Cleaner

This Python script deletes **all messages** from a Telegram group or channel.

It works in batches (100 messages per request) and automatically waits if Telegram applies a flood limit.

---

## Requirements

- Python 3.8+
- A Telegram account
- Telegram API credentials from [my.telegram.org](https://my.telegram.org).

---

## Installation

1. Clone this repository or download `main.py`.  
2. Install the required library:  
   ```bash
   pip install telethon
   ```  
3. Obtain your API ID and API Hash:  
   - Go to [my.telegram.org](https://my.telegram.org)  
   - Log in and open **API Development Tools**  
   - Create a new app and note your **api_id** and **api_hash**

---

## Usage

1. Open `main.py` and set the following variables:  
   - `api_id`: Your Telegram API ID  
   - `api_hash`: Your Telegram API Hash  
   - `session_name`: A name for your session file (e.g., "delete_session")  
   - `group_id`: The numeric ID of the group or channel that starts with "-100". You can use [@username_to_id_bot](https://t.me/username_to_id_bot) to get yours.  

2. Run the script:  
   ```bash
   python main.py
   ```  
3. On first run, you will be prompted to enter your phone number, the login code sent by Telegram and 2FA password if you set up before.