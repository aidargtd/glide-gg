import sqlite3

con = sqlite3.connect(DB_PATH)
cur = con.cursor()


def select_table(table_name, *fields):
    value = f"""SELECT {', '.join(fields)} FROM {table_name}"""
    return cur.execute(value).fetchall()


def select_one_with_aspect(table_name, field, field_value, *fields):
    value = f"""SELECT {', '.join(fields)} FROM {table_name} WHERE {field}=?"""
    return cur.execute(value, (field_value,)).fetchone()


def select_all_with_aspect(table_name, field, field_value, *fields):
    value = f"""SELECT {', '.join(fields)} FROM {table_name} WHERE {field}=?"""
    return cur.execute(value, (field_value,)).fetchall()


def select_all_with_two_aspects(table_name, field1, field_value1, field2, field_value2, *fields):
    value = f"""SELECT {', '.join(fields)} FROM {table_name} WHERE {field1}=? AND {field2}=?"""
    return cur.execute(value, (field_value1, field_value2,)).fetchall()


def select_all_with_three_aspects(table_name, field1, field_value1,
                                  field2, field_value2, field3, field_value3, *fields):
    value = f"""SELECT {', '.join(fields)} FROM {table_name} WHERE {field1}=? AND {field2}=? AND {field3}=?"""
    return cur.execute(value, (field_value1, field_value2, field_value3,)).fetchall()
