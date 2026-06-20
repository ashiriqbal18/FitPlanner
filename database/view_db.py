from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.db import get_connection, initialize_database

initialize_database()

with get_connection() as conn:
    rows = conn.execute("SELECT * FROM exercises ORDER BY goal, level, name").fetchall()
    for row in rows:
        print(dict(row))
