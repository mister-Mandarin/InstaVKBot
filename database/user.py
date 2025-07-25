from database.init import get_connection

def get_user(user_id: int):
    with get_connection() as conn:
        cur = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        return cur.fetchone()

def create_user(user_id: int, first_name: str, last_name: str | None, username: str | None):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO users (user_id, first_name, last_name, username)
            VALUES (?, ?, ?, ?)
        """, (user_id, first_name, last_name, username))
