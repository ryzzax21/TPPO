import json
import sqlite3
import sys

conn = sqlite3.connect('lab2_database')


def execute_script(cur: sqlite3.Cursor, script: str):
    with open(script, encoding='utf-8') as f:
        cur.executescript(f.read())
        conn.commit()


def get_data(cur: sqlite3.Cursor, table_names: list[str]) -> dict:
    """
    :param cur: db cursor
    :param table_names: get data from these tables
    :return:
    """
    data = dict()
    for table_name in table_names:
        try:
            cur.execute('SELECT * FROM \"{}\"'.format(table_name))
            data[table_name] = cur.fetchall()
        except sqlite3.OperationalError:
            drop_all_tables(cur)
            print(f'{table_name} is not valid table name .!.', file=sys.stderr)
            exit(1)

    return data


def drop_all_tables(cur: sqlite3.Cursor):
    cur.execute('SELECT name FROM sqlite_master WHERE type=\'table\'')
    tables = cur.fetchall()
    for table in tables:
        table_str = ''.join(table)
        cur.execute('DROP TABLE \"{}\"'.format(table_str))
    conn.commit()


def write_to_json(data: dict):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    cur = conn.cursor()
    execute_script(cur, 'lab2_script.sql')
    tables = []
    print('Enter "done" when you are finished entering table names')
    while True:
        table = input('Enter a table name: ')
        if table == 'done':
            break
        tables.append(table)
    data = get_data(cur, tables)
    print(data)
    write_to_json(data)
    drop_all_tables(cur)
    conn.close()


if __name__ == '__main__':
    main()
