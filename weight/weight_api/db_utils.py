from sqlite3 import connect
import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE, PORT
from datetime import datetime


class DbConnectionError(Exception):
    pass


# function to connect to the mysql database
def _connect_to_db(db_name):
    connect = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=db_name,
        port=PORT,
        auth_plugin="mysql_native_password",
    )
    return connect


def distinguish_direction(direction):
    if str(direction).lower() == "in":
        return "bruto"
    elif str(direction).lower() == "out":
        return "truckTara"


def check_last_action_from_truck(truck_licence):
    db = _connect_to_db(DATABASE)
    last_action_for_truck = f"SELECT id, direction FROM transactions WHERE truck='{truck_licence}' ORDER BY id DESC LIMIT 1;"
    cursor = db.cursor()
    cursor.execute(last_action_for_truck)
    id_and_direction = cursor.fetchall()
    if id_and_direction:
        return id_and_direction


def generate_new_session_id():
    db = _connect_to_db(DATABASE)
    last_session_id = (
        f"SELECT id, session_id FROM transactions ORDER BY session_id DESC LIMIT 1;"
    )
    cursor = db.cursor()
    cursor.execute(last_session_id)
    id_and_session_id = cursor.fetchall()
    print(f"new session generate new{id_and_session_id}")
    if id_and_session_id == []:
        return 1
    else:

        new_session = id_and_session_id[0][1] + 1
        return new_session


def get_last_session(truck):
    db = _connect_to_db(DATABASE)
    last_session_id = f"SELECT id, session_id, truck FROM transactions WHERE truck='{truck}' ORDER BY session_id DESC LIMIT 1;"
    cursor = db.cursor()
    cursor.execute(last_session_id)
    id_and_session_id_for_existing_truck = cursor.fetchall()
    last_session = [
        id_and_session_id_for_existing_truck[0][0],
        id_and_session_id_for_existing_truck[0][1],
    ]
    return last_session


def get_weight_item(id, t1, t2):
    db = _connect_to_db(DATABASE)
    cursor = db.cursor()
    select_id_truck = f"SELECT * FROM transactions WHERE id='{id}' and datetime BETWEEN '{t1}' AND '{t2}';"
    cursor.execute(select_id_truck)
    output = cursor.fetchall()
    selected_records = []
    if output:
        for record in output:
            weight_truck = {}
            weight_truck["id"] = record[0]
            weight_truck["tara"] = record[6]
            weight_truck["sessions"] = record[9]
            selected_records.append(weight_truck)

        cursor.close()
        return selected_records

    else:

        select_container = (
            f"SELECT * FROM containers_registered WHERE container_id='{id}';"
        )
        cursor.execute(select_container)
        output = cursor.fetchall()

        for record in output:  # is this for necessery?
            weight_container = {}
            weight_container["container_id"] = record[0]
            weight_container["weight"] = record[1]
            weight_container["unit"] = record[2]
            selected_records.append(weight_container)

        cursor.close()
        return selected_records


def get_weight(t1, t2, direction):
    db = _connect_to_db(DATABASE)
    cursor = db.cursor(buffered=True)
    select_direction = f"SELECT * FROM transactions WHERE direction IN ({direction}) AND datetime BETWEEN '{t1}' AND '{t2}';"
    cursor.execute(select_direction)
    output = cursor.fetchall()
    db.commit()
    cursor.close()
    records = []
    for record in output:
        weight_dict = {}
        weight_dict["id"] = record[0]
        weight_dict["direction"] = record[2]
        weight_dict["bruto"] = record[5]
        weight_dict["neto"] = record[7]
        weight_dict["produce"] = record[8]
        weight_dict["containers"] = record[4]
        records.append(weight_dict)
    return records


def get_last_dir_id(truck):
    try:
        last_action_for_truck = check_last_action_from_truck(truck)
        last_id = last_action_for_truck[0][0]
        last_direction = str(last_action_for_truck[0][1])
    except:
        last_direction = "none"
        last_id = 0
    return last_direction, last_id


def swap_dir_value(dir):
    if dir not in ["in", "out", "na"]:
        dir = "na"
    return dir


def post_weight(direction, truck, containers_id, truck_weight, unit, force, produce):
    db = _connect_to_db(DATABASE)
    cur = db.cursor()

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H-%M-%S")

    column = distinguish_direction(direction)

    insert_transactions = ""
    last_direction, last_id = get_last_dir_id(truck)
    direction = swap_dir_value(direction)

    if direction == "in":
        if last_direction != "in":
            new_session_id = generate_new_session_id()
            try:
                insert_transactions = f"INSERT INTO transactions (datetime, direction, truck, containers, {column},  produce, session_id) VALUES ('{timestamp}','{direction}', '{truck}', '{containers_id}', {truck_weight},'{produce}', {new_session_id});"
            except:
                pass
        if direction in last_direction:
            if force.lower() == "true":
                insert_transactions = f"UPDATE transactions SET {column}={truck_weight} where id={last_id};"
            elif force.lower() != "true":
                raise Exception(
                    "this truck has already been weighed on entering, if you want to update last measurement, select force option"
                )
    elif direction == "out":
        if last_direction == "in":
            last_session_id = get_last_session(truck)[1]
            insert_transactions = f"INSERT INTO transactions (datetime, direction, truck, containers, {column}, produce, session_id) VALUES ('{timestamp}', '{direction}', '{truck}', '{containers_id}', {truck_weight}, '{produce}', {last_session_id});"
        if direction in last_direction:
            if force.lower() == "true":
                insert_transactions = f"UPDATE transactions SET {column}={truck_weight} where id={last_id};"
            elif force.lower() != "true":
                raise Exception(
                    "this truck has already been weighed on exiting, if you want to update last measurement, select force option"
                )
        if last_direction == "none":
            insert_transactions = ";"
            raise Exception("Truck can't go out without going in")

    elif direction == "na" and truck != "":
        raise Exception("You have to specify direction for a truck")

    cur.execute(insert_transactions)
    db.commit()
    cur.close()


def health_db():
    db = _connect_to_db(DATABASE)
    cur = db.cursor(buffered=True)
    cur.execute("SELECT 1")
    cur.close()


def batch_weight(id, weight, unit):
    db = _connect_to_db(DATABASE)
    cur = db.cursor()
    insert_tara = f"INSERT INTO containers_registered (container_id, weight, unit) VALUES ('{id}', {weight}, '{unit}');"
    cur.execute(insert_tara)
    db.commit()
    cur.close()


def session_db(sid):
    db = _connect_to_db(DATABASE)
    cur = db.cursor(buffered=True)
    cur.execute(f"SELECT * FROM transactions WHERE session_id = {sid}")
    session_db.output = cur.fetchall()
    cur.close()


def unknown_containers_db():
    db = _connect_to_db(DATABASE)
    cur = db.cursor(buffered=True)
    cur.execute(f"SELECT container_id FROM containers_registered WHERE weight IS NULL")
    output = cur.fetchall()
    unknown_containers_db.list1 = list()
    for id in output:
        unknown_containers_db.list1.append(id[0])
    db.commit()
    cur.close()
