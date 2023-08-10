import mysql.connector as mysql
from app import model


HOST = "91.149.187.115"
DATABASE = "test_shop"
USER = "shopuser"
PASSWORD = "1346792c212C_C"
PORT = "43251"


def getRoles():
    db_connection = mysql.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        port=PORT,
        auth_plugin="mysql_native_password",
    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * from roles")
    result = []
    for i in cursor:
        result.append(model.Role(i[0], i[1]))
    return result


def saveRole(role):
    db_connection = mysql.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        port=PORT,
        auth_plugin="mysql_native_password",
    )
    cursor = db_connection.cursor()
    cursor.execute("insert into roles (r_title) values(%s)", (role,))
    db_connection.commit()


def deleteRole(role):
    db_connection = mysql.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        port=PORT,
        auth_plugin="mysql_native_password",
    )
    cursor = db_connection.cursor()
    cursor.execute("delete from roles where r_id = %s", (role,))
    db_connection.commit()
