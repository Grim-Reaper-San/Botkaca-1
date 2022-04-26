from pyrogram import Client
            bot_token = Config.BOT_TOKEN,
            workers = 20,
            plugins = dict(
                root="Plugins"
            )
autocaption = Client(
    "autocaptionistbot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

    autocaption().run()
