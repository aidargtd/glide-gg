import sqlite3
from parametres import *

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


def update_settings_value(value):
    cur.execute(
        """UPDATE settings SET music=?""", (value,))
    con.commit()


def upd_settings_val_effects(value):
    cur.execute(
        """UPDATE settings SET effects=?""", (value,))
    con.commit()


def upd_settings_sound_effects(value):
    cur.execute(
        """UPDATE settings SET sound_effects=?""", (value,))
    con.commit()


def update_aspect(table_name, field, value_field, parametr, value_parametr):
    value = f'''UPDATE {table_name} SET {field}=? WHERE {parametr} = ?'''
    cur.execute(value, (value_field, value_parametr,))
    con.commit()
