import os
import requests
import asyncio
from telegram import Bot

# 1. Setup Keys
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
APIFY_TOKEN = os.getenv('APIFY_TOKEN')

async def get_tiktok_trends():
    bot = Bot(token=TELEGRAM_TOKEN)
    
    # 2. Call Apify to get REAL Malaysian Trends
    # This specifically targets Trending Videos in Malaysia (MY)
    api_url = f"https://api.apify.com/v2/acts/clockworks~tiktok-trends-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"
    
    payload = {
        "type": "videos",
        "region": "MY",  # Focused on Malaysia
        "limit": 5
    }

    try:
        response = requests.post(api_url, json=payload)
        trends = response.json()

        for item in trends:
            title = item.get('videoTitle', 'No Title')
            url = item.get('url', '')
            views = item.get('views', '0')
            
            # 3. Send the real data to Telegram
            message = (
                f"🇲🇾 **Live Malaysia Trend**\n\n"
                f"🎬 **Video:** {title}\n"
                f"👀 **Views:** {views}\n"
                f"🔗 {url}"
            )
            await bot.send_message(chat_id=CHAT_ID, text=message)
            
    except Exception as e:
        print(f"Error fetching trends: {e}")

if __name__ == "__main__":
    asyncio.run(get_tiktok_trends())
