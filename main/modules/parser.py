import asyncio
import anitopy
from main.modules.api import AnimePahe
from main.modules.schedule import update_schedule
from main.modules.utils import status_text
from main import status
from main.modules.db import get_animesdb, get_uploads, save_animedb
from main import queue
from main.inline import button1

def trim_title(title: str):
    
    try:
        file_tags = anitopy.parse(title)

        # Check if particular season is mentioned or not
        if "anime_season" in filetags:
            title = file_tags["anime_title"] + " S" + file_tags["anime_season"] + " - " + file_tags["episode_number"]
        else:
            title = file_tags["anime_title"] + " - " + file_tags["episode_number"]
        
        # Check if resolution tag is in title or not
        if "video_resolution" in filetags:
            title += " (" + file_tags["video_resolution"] + ")." + file_tags["file_extension"]
        else:
            title += "." + file_tags["file_extension"]
    
    except:
        # Use the ordinary way in case any error occurs
        title, ext = title.replace("[SubsPlease]","").strip().split("[",maxsplit=2)
        _, ext = ext.split("]",maxsplit=2)
        title = title.strip() + ext
    
    return title

def parse():
    try:
        latest = AnimePahe.get_latest()
    except:
        latest = []
    data = []    

    for i in latest:
        item = {}
        item['title'] = i['anime_title'] + ' - ' + str(i['episode'])
        item['ep_id'] = i['session']
        data.append(item)
    return data

async def auto_parser():
    while True:
        try:
            await status.edit(await status_text("Scrapping Animes..."),reply_markup=button1)
        except:
            pass

        data = parse()
        saved = await get_animesdb()
        uploaded = await get_uploads()

        saved_anime = []
        for i in saved:
            saved_anime.append(i["name"])

        uanimes = []
        for i in uploaded:
            uanimes.append(i["name"])
        
        for i in data:
            if i["title"] not in uanimes and i["title"] not in saved_anime:
                title = i["title"]
                await save_animedb(title,i)

        saved = await get_animesdb()
        for i in saved:
            if i["data"] not in queue:
                queue.append(i["data"])    
                print("Saved -->", i["name"])   

        try:
            await update_schedule()
        except:
            pass
        try:
            await status.edit(await status_text("Idle..."),reply_markup=button1)
        except:
            pass

        await asyncio.sleep(600)
