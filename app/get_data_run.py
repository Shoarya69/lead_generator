from get_main_main_data import main
from connect_mysql_for_123 import get_cursore as gc
import asyncio
import pandas as pd
from data_in_excle_finished import crete_lead_excel_file as clef

async def abc_run():

    cursor = None
    conn = None

    try:

        cursor, conn = gc()

        # GET 100 UNUSED LEADS
        query = """
        SELECT id, business_name, link
        FROM LEAD_GET_GOOGLE_MAP
        WHERE IS_USE = FALSE
        LIMIT 100;
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:

            print("No data in database for lead")
            return

     

        leads = []

        for row in rows:

            leads.append(
                (
                    row[0],   # id
                    row[2]    # url
                )
            )
        res = await main(
            CONCURRENT_PAGES=10,
            URLS=leads
        )

        ids = [row[0] for row in rows]
        format_strings = ",".join(["%s"] * len(ids))
        #THIS QUERY IS FOR UPDATE THE IS_USE STATE TO TRUE 
        update_query = f"""
        UPDATE LEAD_GET_GOOGLE_MAP
        SET IS_USE = TRUE
        WHERE id IN ({format_strings})
        """

        cursor.execute(update_query, ids)

        #THIS QUERY IS FOR STOER THE LEADS IN DATABASE
        save_lead_query= """
                        INSERT INTO lead_data_store
                        (id, url, phone, website, rating)
                        VALUES (%s, %s, %s, %s, %s)
                       """
        data_to_insert = []
        for lead in res:

            phone = lead.get("phone") or "No Number"

            row = (
                lead.get("id"),
                lead.get("url"),
                phone,
                lead.get("website"),
                lead.get("rating")
            )

            data_to_insert.append(row)
        cursor.executemany(save_lead_query,data_to_insert)
        conn.commit()
        # clef(results=res)
        print("IS_USE updated to TRUE")

    except Exception as e:

        print(e)
        print("Something went wrong please try again later")
        conn.rollback()

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()





def data_lead_op():
    cursor = None
    conn = None

    try:

        cursor, conn = gc()

        # GET 100 UNUSED LEADS
        query = """
        SELECT id, business_name, link
        FROM LEAD_GET_GOOGLE_MAP
        WHERE IS_USE = FALSE
        LIMIT 100;
        """

        cursor.execute(query)

        rows = cursor.fetchall()
        urls = []

        
        for row in rows:
            url = row[2]
            urls.append(url)

           
        return urls
    except Exception as e:

        print(e)
        print("Something went wrong please try again later")
        conn.rollback()

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

if __name__ == "__main__":
    asyncio.run(abc_run())