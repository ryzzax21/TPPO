import pytest
import sqlite3
from lab_2.solution import execute_script, get_data, drop_all_tables, write_to_json

@pytest.fixture
def cursor():
    conn = sqlite3.connect('lab_2/test_db.db')
    cur = conn.cursor()
    return cur

def test_execute_script(cursor):
    execute_script(cursor, 'lab_2/lab2_script.sql')
    cursor.execute('SELECT * FROM "lab2_table"')
    rows = cursor.fetchall()
    assert len(rows) == 3
    assert rows[0][0] == 'row1'
    assert rows[0][1] == 'row1'
    assert rows[1][0] == 'row2'
    assert rows[1][1] == 'row2'
    assert rows[2][0] == 'row3'
    assert rows[2][1] == 'row3'