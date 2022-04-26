from pyrogram import Client
            api_id = "3845818",
            api_hash = Config.API_HASH,
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
