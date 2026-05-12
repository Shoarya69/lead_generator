from connect_mysql_for_123 import get_cursore as gc

def store_data_in_db_lead_by_google_maps(conn,cursor,query_id, names, links):
    # cursor, conn = gc()
    try:
        query = """
            INSERT IGNORE INTO LEAD_GET_GOOGLE_MAP
            (query_id, business_name, link)
            VALUES (%s, %s, %s)
        """

        data = [
            (query_id, name, link)
            for name, link in zip(names, links)
        ]

        before = len(data)
        cursor.executemany(query, data)

        after = cursor.rowcount
        print("row count:- ",after)

        skipped = before - after
        if skipped > 0:
            print(f"⚠️ {skipped} duplicate rows skipped")
        conn.commit()
        print("All set ✅ data saved in DB")
    except Exception as e:
        print(e)
        if conn:
            conn.rollback()
    


def delete_all_dummy_data_from_google_map_table():
    cursor,conn = gc()
    query = "TRUNCATE TABLE LEAD_GET_GOOGLE_MAP"
    cursor.execute(query)
    print("delete all data in table")
    conn.commit()
    conn.close()
    return


