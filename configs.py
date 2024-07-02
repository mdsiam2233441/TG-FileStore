# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("9815122"))
	API_HASH = os.environ.get("0b6f3e4a98948a2be450ed198784d614")
	BOT_TOKEN = os.environ.get("7266995978:AAHoibpxfuQ7IlOPQgvq_iQAOIL1ZOBrF1A")
	BOT_USERNAME = os.environ.get("Filestoragepybot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002246272311"))
	SHORTLINK_URL = os.environ.get('instantearn.in')
	SHORTLINK_API = os.environ.get('fe76f8810ff923d8a6aff21cc743153a2a958c1e')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1399928285"))
	DATABASE_URL = os.environ.get("mongodb+srv://ziknerefye:q8hIQ2q682gzvk5j@cluster0.t0njh9r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	UPDATES_CHANNEL = os.environ.get("-1002246272311")
	LOG_CHANNEL = os.environ.get("-1002122392950", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "-1002122392950").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1002246272311").split()))
	OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE","-1002246272311").split(",") if id.strip()]
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/Filestoragepybot)
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [render](https://render.com)
│
├🔸 **Developer:** [Predator HackerzZ](https://t.me/Star_Jalshatvskr) 
│
├🔹 **Bot Support:** [Support Group](https://t.me/Star_Jalshatvskr)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/Star_Jalshatvskr)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@Star_Jalshatvskr](https://github.com/PredatorHackerzZ)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Filestoragepybot) or ``````
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
