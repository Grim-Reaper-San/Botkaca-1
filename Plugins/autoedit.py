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


@autocaption.on_message(filters.channel & (filters.photo) & ~filters.edited, group=-1)
async def editing(bot, message):
      try:
         media = message.photo
         caption_text = Config.CAPTION_TEXT
      except:
         caption_text = ""
         pass 
      if (message.photo): 
          if message.caption:                        
             file_caption = f"**{message.caption}**"                
          else:
             fname = media.file_name
             filename = fname.replace("_", ".")
             file_caption = f"`{filename}`"  
      new_file_caption = file_caption.replace(file_caption[:10], "✨")     
      newa_file_caption = new_file_caption.replace("- 0", "Episode 0")  
      newb_file_caption = newa_file_caption.replace("- 1", "Episode 1") 
      newc_file_caption = newb_file_caption.replace("- 2", "Episode 2")
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
                 caption = newc_file_caption.replace(newc_file_caption[-26:], " ") + caption_text,
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
              
                   
      
