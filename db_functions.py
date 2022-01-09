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


def upd_settings_voice(value):
    cur.execute(
        """UPDATE settings SET voice=?""", (value,))
    con.commit()


def select_max_elem(field):
    value = f"""SELECT MAX({field}) FROM Infinity_level_scores"""
    return cur.execute(value).fetchone()


def update_aspect(table_name, field, value_field, parametr, value_parametr):
    value = f'''UPDATE {table_name} SET {field}=? WHERE {parametr} = ?'''
    cur.execute(value, (value_field, value_parametr,))
    con.commit()


def update_availability_item():
    cur.execute(
        """UPDATE ITEM_SHOP SET Availability=?""", (False,))
    con.commit()


def upd_balance(value):
    cur.execute(
        """UPDATE USERS SET coins_amount=?""", (value,))
    con.commit()


def insert_to_locker(*values):
    cur.execute("""INSERT INTO LOCKER(id, path_image, availability, name) 
                        VALUES(?, ?, ?, ?)""", values)
    con.commit()
