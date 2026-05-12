from data_store_in_db_lead import store_data_in_db_lead_by_google_maps
from main_2_scrrapper import as_main_scrapper as scrpper
from use_data_in_auto import get_lead_value
from playwright.async_api import async_playwright
import asyncio
import random
import pandas as pd
from connect_mysql_for_123 import get_cursore as gc
import pandas as pd

async def fucntion_run_scrapper(time:int):
    async with async_playwright() as p:

        context = await p.chromium.launch_persistent_context(
            user_data_dir="./playwright_profile_3",     # ✅ ROOT folder
            headless=False,
            args=[
                
                "--start-maximized",
                "--disable-blink-features=AutomationControlled"
            ]
        )


        page = await context.new_page()
        try:
            cursor, conn = gc()
            for i in range(time):
                value = get_lead_value(cursor=cursor,conn=conn)
                print(value['Query'])
                await page.mouse.wheel(0, random.randint(300, 800))
                df = await scrpper(page=page,query=value['Query'])
                print(df.head())
                if df.empty:
                    print("❌ DataFrame hi empty hai")
                    continue

                title_count = df['title'].notna().sum()
                link_count = df['link'].notna().sum()

                print(f"title count: {title_count}, link count: {link_count}")

                if title_count == 0:
                    print("❌ title column empty hai")
                    continue
                if link_count == 0:
                    print("❌ link column empty hai")
                    continue
                if title_count != link_count:
                    print("⚠️ title aur link ka count match nahi kar raha")
                    continue
                store_data_in_db_lead_by_google_maps(conn,cursor,value['id'],names=df['title'],links=df['link'])
                print("end of the scrapping process times: - ",i)
            await context.close()
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()




async def custome_run_scrapper(query):
    async with async_playwright() as p:

        context = await p.chromium.launch_persistent_context(
            user_data_dir="./playwright_profile_3",     # ✅ ROOT folder
            headless=False,
            args=[
                
                "--start-maximized",
                "--disable-blink-features=AutomationControlled"
            ]
        )


        page = await context.new_page()
        data = pd.DataFrame(columns=["title", "link"])
        a=0
        for i in query:
            a=a+1
            value = i
            print(value)
            await page.mouse.wheel(0, random.randint(300, 800))
            df = await scrpper(page=page,query=value)
            print(df.head())
            if df.empty:
                print("❌ DataFrame hi empty hai")
                return pd.DataFrame(columns=["title", "link"])

            title_count = df['title'].notna().sum()
            link_count = df['link'].notna().sum()

            print(f"title count: {title_count}, link count: {link_count}")

            if title_count == 0:
                print("❌ title column empty hai")

            if link_count == 0:
                print("❌ link column empty hai")

            if title_count != link_count:
                print("⚠️ title aur link ka count match nahi kar raha")
                return
           
            data = pd.concat([data, df], ignore_index=True)
            data = data.drop_duplicates()
            data = data.drop_duplicates(subset=["link"])
            print("end of the scrapping process times: - ",a)
        await context.close()
        return data


if __name__ == "__main__":
    asyncio.run(fucntion_run_scrapper(2))