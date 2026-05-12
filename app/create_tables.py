from db import get_cursor

def create_tables(drop_existing=False):
    cursor, conn = get_cursor()
    try:
        if drop_existing:
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

            # Drop in reverse order because of foreign keys
            cursor.execute("DROP TABLE IF EXISTS lead_data_store")
            cursor.execute("DROP TABLE IF EXISTS `LEAD_GET_GOOGLE_MAP`")
            cursor.execute("DROP TABLE IF EXISTS leads")

            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        # 1) Parent table first
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INT NOT NULL AUTO_INCREMENT,
                country VARCHAR(100) DEFAULT NULL,
                business VARCHAR(255) DEFAULT NULL,
                `query` TEXT,
                is_used TINYINT(1) DEFAULT '0',
                tier TINYINT NOT NULL DEFAULT '2',
                PRIMARY KEY (id),
                CONSTRAINT chk_tier CHECK (tier IN (1,2,3))
            ) ENGINE=InnoDB
            DEFAULT CHARSET=utf8mb4
            COLLATE=utf8mb4_0900_ai_ci
        """)

        # 2) Depends on leads(id)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS `LEAD_GET_GOOGLE_MAP` (
                id INT NOT NULL AUTO_INCREMENT,
                query_id INT DEFAULT NULL,
                business_name VARCHAR(100) NOT NULL,
                link VARCHAR(300) NOT NULL,
                IS_USE TINYINT(1) DEFAULT '0',
                PRIMARY KEY (id),
                UNIQUE KEY link (link),
                KEY query_id (query_id),
                CONSTRAINT LEAD_GET_GOOGLE_MAP_ibfk_1
                    FOREIGN KEY (query_id) REFERENCES leads (id)
            ) ENGINE=InnoDB
            DEFAULT CHARSET=utf8mb4
            COLLATE=utf8mb4_0900_ai_ci
        """)

        # 3) Depends on LEAD_GET_GOOGLE_MAP(id)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lead_data_store (
                id INT NOT NULL,
                url TEXT,
                phone VARCHAR(50) DEFAULT 'No Number',
                website TEXT,
                rating VARCHAR(10) DEFAULT NULL,
                is_website TINYINT(1)
                    GENERATED ALWAYS AS (
                        CASE
                            WHEN (website IS NOT NULL) AND (website <> '')
                            THEN TRUE
                            ELSE FALSE
                        END
                    ) STORED,
                PRIMARY KEY (id),
                CONSTRAINT lead_data_store_ibfk_1
                    FOREIGN KEY (id) REFERENCES `LEAD_GET_GOOGLE_MAP` (id)
            ) ENGINE=InnoDB
            DEFAULT CHARSET=utf8mb4
            COLLATE=utf8mb4_0900_ai_ci
        """)

        conn.commit()
        print("Tables created successfully.")

    except Exception as e:
        conn.rollback()
        print(f"Error creating tables: {e}")

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    create_tables(drop_existing=False)