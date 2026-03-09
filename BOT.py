import os
import requests
import asyncio
from telegram import Bot

# Get secrets from GitHub Environment
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID') 

# This uses a public Trend API (you can swap this for Apify or TikAPI later)
TIKTOK_TREND_API = "https://ads.tiktok.com/marketing_api/creative_center/challenge/get_list"

async def get_trends():
    bot = Bot(token=TELEGRAM_TOKEN)
    
    # Logic to fetch from TikTok Creative Center (Simplified for this example)
    # In a real scenario, you'd use a RapidAPI or Apify URL here
    sample_trends = [
        {"title": "Morning Routine", "growth": "150%", "link": "https://vt.tiktok.com/ZS.../"},
        {"title": "Home Office Setup", "growth": "85%", "link": "https://vt.tiktok.com/ZS.../"}
    ]

    for trend in sample_trends:
        message = (
            f"🚀 **New TikTok Trend Spotted**\n\n"
            f"📌 **Topic:** {trend['title']}\n"
            f"📈 **Growth:** {trend['growth']}\n"
            f"🔗 [Watch Example]({trend['link']})"
        )
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')

if __name__ == "__main__":
    asyncio.run(get_trends())
