import os
import sqlite3
from contextlib import closing
from .seed_data import EXERCISES

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "exercises.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    muscle_groups TEXT NOT NULL,
    primary_muscle TEXT NOT NULL,
    equipment TEXT NOT NULL,
    duration_min INTEGER NOT NULL,
    intensity TEXT NOT NULL,
    goal TEXT NOT NULL,
    level TEXT NOT NULL,
    calories_per_min REAL NOT NULL,
    sets INTEGER NOT NULL,
    reps TEXT NOT NULL,
    rest_sec INTEGER NOT NULL,
    description TEXT NOT NULL
)
"""

INSERT_SQL = """
INSERT INTO exercises (
    name, muscle_groups, primary_muscle, equipment,
    duration_min, intensity, goal, level,
    calories_per_min, sets, reps, rest_sec, description
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database(force_reset=False):
    """Create and seed the SQLite database if it is missing or empty."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        cursor = conn.cursor()
        if force_reset:
            cursor.execute("DROP TABLE IF EXISTS exercises")
        cursor.execute(SCHEMA)
        count = cursor.execute("SELECT COUNT(*) FROM exercises").fetchone()[0]
        if force_reset or count == 0:
            cursor.execute("DELETE FROM exercises")
            cursor.executemany(INSERT_SQL, EXERCISES)
        conn.commit()
