import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import autocaption
from config import Config


# =
usercaption_position = Config.CAPTION_POSITION
caption_position = usercaption_position.lower()
caption_text = Config.CAPTION_TEXT


@autocaption.on_message(filters.channel & (filters.text) & ~filters.edited, group=-1)
async def editing(bot, message):
      try:
         media = message.text
         caption_text = Config.CAPTION_TEXT
      except:
         caption_text = ""
         pass 
      if (message.text): 
          if message.text:                        
             message_text = f"{message.text}"
           if message_text.find("magnet"):
             message_text = f"/leech {message.text}"     
             else:
                    return
      try:
          if caption_position == "top":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = caption_text + "\n" + file_caption,
                 parse_mode = "markdown"
             )
          elif caption_position == "bottom":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = f"{message_text}" + "\n" + f"{caption_text}",
                 parse_mode = "markdown"
             )
          elif caption_position == "nil":
             await bot.edit_message_caption(
                 chat_id = message.chat.id,
                 message_id = message.message_id,
                 caption = caption_text, 
                 parse_mode = "markdown"
             ) 
      except:
          pass
             
                   
      
