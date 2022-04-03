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
      new_file_caption = ' '.join(file_caption.split()[1:])  
      newa_file_caption = new_file_caption.replace("- 0", "| Episode 0")  
      newb_file_caption = newa_file_caption.replace("- 1", "| Episode 1") 
      newc_file_caption = newb_file_caption.replace("- 2", "| Episode 2")
      newd_file_caption = newc_file_caption.replace("- 3", "| Episode 3")
      newe_file_caption = newd_file_caption.replace("- 4", "| Episode 4")
      newf_file_caption = newe_file_caption.replace("- 5", "| Episode 5")
      newg_file_caption = newf_file_caption.replace("- 6", "| Episode 6")
      newh_file_caption = newg_file_caption.replace("- 7", "| Episode 7")
      newi_file_caption = newh_file_caption.replace("- 8", "| Episode 8")
      newj_file_caption = newi_file_caption.replace("- 9", "| Episode 9")
      newk_file_caption = newj_file_caption.replace("S1", "| Season 1")
      newl_file_caption = newk_file_caption.replace("S2", "| Season 2")
      newm_file_caption = newl_file_caption.replace("S3", "| Season 4")
      newn_file_caption = newm_file_caption.replace("S4", "| Season 4")
      newo_file_caption = newn_file_caption.replace("was released!!", "**")
      newp_file_caption = newo_file_caption.seek(0)             # reposition the file pointer to the beginning of the file
      newp_file_caption = newp_file_caption.write('**')
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
                 caption = newo_file_caption.replace(newo_file_caption[-26:], " ") + caption_text,
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
              
                   
      
