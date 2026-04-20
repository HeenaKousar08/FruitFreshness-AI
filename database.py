import sqlite3
from datetime import datetime, timedelta

def init_db():
    conn = sqlite3.connect('fruit_data.db')
    cursor = conn.cursor()
    # Updated table to include financial metrics
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scan_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT,
            freshness TEXT,
            shelf_life TEXT,
            base_price REAL,
            cost_price REAL,
            final_price REAL,
            profit_loss REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

import sqlite3
from datetime import datetime, timedelta

def save_to_db(name, status, days, base_p=0.0, cost_p=0.0, final_p=0.0, pl=0.0):
    conn = sqlite3.connect('fruit_data.db')
    cursor = conn.cursor()
    
    # 60-second window to prevent rapid-fire saving
    one_minute_ago = (datetime.now() - timedelta(seconds=60)).strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''SELECT * FROM scan_history 
                      WHERE item_name = ? AND timestamp > ?''', (name, one_minute_ago))
    
    if not cursor.fetchone():
        cursor.execute('''
            INSERT INTO scan_history 
            (item_name, freshness, shelf_life, base_price, cost_price, final_price, profit_loss) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, status, str(days), base_p, cost_p, final_p, pl))
        conn.commit()
        print(f"✅ Successfully stored: {name}")
    
    conn.close()

if __name__ == "__main__":
    init_db()