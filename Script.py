class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {}
𝙸𝙼 <a href=https://t.me/{}>{}</a>,

𝙸𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 + 𝙼𝙾𝚅𝙸𝙴 𝚂𝙴𝙰𝚁𝙲𝙷 + 𝙼𝙰𝙽𝚄𝙰𝙻 𝙵𝙸𝙻𝚃𝙴𝚁 𝙱𝙾𝚃. 𝙸 𝙲𝙰𝙽 𝙶𝙸𝚅𝙴 𝚈𝙾𝚄 𝙼𝙾𝚅𝙸𝙴𝚂 𝙸𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙶𝚁𝙾𝚄𝙿. 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈🔥

𝙼𝚈 𝙶𝚁𝙾𝚄𝙿 : @Hd_moviesmalyalam"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/NJaNu_yir>𝙰𝙱𝙷𝙸</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- This is an open source project. 

<b>╔══ 𝘑𝘰𝘪𝘯 ★ 𝘚𝘩𝘢𝘳𝘦 ★ 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 ══╗
♻️ ᴊᴏɪɴ :- <a href=https://t.me/MWM_Films><b>🔰 Main Group 🔰</b></a>
♻️ ᴊᴏɪɴ :- <a href=https://t.me/MWMFilms><b>🧲 Main Channel🧲</b></a>
╚══ 𝘑𝘰𝘪𝘯 ★ 𝘚𝘩𝘢𝘳𝘦 ★ 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 ══╝</b>

<b>Devoloper:</b>
- <a href=https://t.me/NJaNu_yir>𝙰𝙱𝙷𝙸</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Pooja should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Pooja Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Pooja supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Pooja

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝕿𝖔𝖙𝖆𝖑 𝕱𝖎𝖑𝖊𝖘: <code>{}</code>
★ 𝕿𝖔𝖙𝖆𝖑 𝖀𝖘𝖊𝖗𝖘: <code>{}</code>
★ 𝕿𝖔𝖙𝖆𝖑 𝕮𝖍𝖆𝖙𝖘: <code>{}</code>
★ 𝖀𝖘𝖊𝖉 𝕾𝖙𝖔𝖗𝖆𝖌𝖊: <code>{}</code> 𝙼𝚒𝙱
★ 𝕱𝖗𝖊𝖊 𝕾𝖙𝖔𝖗𝖆𝖌𝖊: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
