import sqlite3
from pathlib import Path

DB_PATH = Path("data.sqlite3")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        '''
        Таблица пользователей
        '''
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id      BIGINT PRIMARY KEY,
                username     TEXT,
                first_name   TEXT NOT NULL,
                last_name    TEXT,
                phone        TEXT,
                vk_id        BIGINT,
                inst_login   TEXT,
                session_data TEXT,
                role         TEXT NOT NULL DEFAULT 'user',
                created_at   TIMESTAMP NOT NULL DEFAULT (datetime('now', '+3 hours')),
                last_update  TIMESTAMP NULL DEFAULT (datetime('now', '+3 hours')),
                active       BOOLEAN NOT NULL DEFAULT TRUE
            );
        """)

        conn.execute('''
            CREATE TABLE IF NOT EXISTS stories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                ig_story_id TEXT,
                url TEXT,
                preview_url TEXT,
                created_at   TIMESTAMP NOT NULL DEFAULT (datetime('now', '+3 hours')),
                status TEXT CHECK(status IN ('new', 'published')) DEFAULT 'new',
                tg_message_id INTEGER,
                vk_story_id TEXT,
                temp_file_path TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
            ''')
