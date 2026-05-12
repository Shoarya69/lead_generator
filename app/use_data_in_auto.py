from connect_mysql_for_123 import get_cursore as gc
from termcolor import colored
def get_lead_value(cursor,conn,to_update=True):
    # cursor,conn = gc()
    try:
        cursor.execute("SELECT * FROM leads WHERE is_used = False LIMIT 1")
        lead = cursor.fetchone()
        
        if not lead:
            print("All the leads already are used create some new lead")
            return 
        else:
            print("Lead alredy fetched and send to the api")
            id = lead[0]
            if to_update:
                update_is_Used_to_True(cursor=cursor,conn=conn,id=id)
            
            return {
                "id": lead[0],
                "Query": lead[3]
            }

    except Exception as e:
        print("error found:- ",e)
  

def update_is_Used_to_True(cursor,conn,id):
    
    try:
        cursor.execute(
            "UPDATE leads SET is_used = TRUE WHERE id = %s",
            (id,)
        )
        print("IS_USED_Update to True")
        conn.commit()
    except Exception as e:
        print(e)
        print("IS_USED_Update Is not set")
        conn.rollback()



def update_is_Used_to_False(cursor,conn,id):
    
    try:
        cursor.execute(
            "UPDATE leads SET is_used = False WHERE id = %s",
            (id,)
        )
        print("IS_USED_Update to True")
        conn.commit()
    except Exception as e:
        print(e)
        print("IS_USED_Update Is not set")
        conn.rollback()

def reset_all_is_used(cursor, conn):
    try:
        cursor.execute(
            "UPDATE leads SET is_used = FALSE"
        )
        conn.commit()
        print("All leads reset: is_used = FALSE ✅")

    except Exception as e:
        print("Reset failed:", e)
        conn.rollback()
if __name__ == "__main__":
    reset_all_is_used()