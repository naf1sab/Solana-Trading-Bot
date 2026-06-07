# Whitelist security module - mages approved withdrawal addresses
# per user with 24hr cooldown before transfers are permitted
def init_whitelist_table():
    """Create whitelist table if not exists"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS whitelist (
            user_id INTEGER,
            address TEXT,
            approved_at REAL,  -- timestamp when added, transfer allowed after 24hrs
            label TEXT,
            PRIMARY KEY (user_id, address)
        )
    ''')
    conn.commit()
    conn.close()

def save_whitelist_address(uid: int, address: str, approved_at: float, label: str = ""):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO whitelist (user_id, address, approved_at, label)
        VALUES (?, ?, ?, ?)
    ''', (uid, address, approved_at, label))
    conn.commit()
    conn.close()

def load_whitelist(uid: int) -> Dict[str, float]:
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT address, approved_at FROM whitelist WHERE user_id = ?', (uid,))
        result = {row[0]: row[1] for row in cursor.fetchall()}
        conn.close()
        return result
    except Exception:
        return {}

def delete_whitelist_address(uid: int, address: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM whitelist WHERE user_id = ? AND address = ?', (uid, address))
    conn.commit()
    conn.close()
