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


def checkLogin(login):
    db_connection = mysql.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        port=PORT,
        auth_plugin="mysql_native_password",
    )
    cursor = db_connection.cursor()
    cursor.execute("select * from credentials where c_login= %s", (login,))
    row = cursor.fetchone()
    if row == None:
        return True
    else:
        return False


def saveRegistration(registration):
    db_connection = mysql.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        port=PORT,
        auth_plugin="mysql_native_password",
    )
    cursor = db_connection.cursor()
    cursor.execute(
        "insert into users() values();"
    )  # создаю в таблице users пользователья с id
    user_id = cursor.lastrowid  # возвращает индификатор последней добавленной строки
    cursor.execute(
        "insert into credentials (c_login, c_password, u_id) values(%s, %s, %s);",
        (registration.login, registration.password, user_id),
    )
    db_connection.commit()


def login(login, password):
    db_connection = mysql.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        port=PORT,
        auth_plugin="mysql_native_password",
    )
    cursor = db_connection.cursor()
    cursor.execute(
        "select u_id from credentials where c_login = %s and c_password = %s",
        (login, password),
    )
    data = cursor.fetchone()
    if data != None:
        user_id = data[0]
        cursor.execute("select * from users where u_id=%s;", (user_id,))
        user_data = cursor.fetchone()
        if user_data != None:
            new_user = model.User(
                user_data[0], user_data[1], user_data[2], user_data[3]
            )
            return new_user
        else:
            return None
    else:
        return None
    return None


def load_user_by_id(user_id):
    db_connection = mysql.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        port=PORT,
        auth_plugin="mysql_native_password",
    )
    cursor = db_connection.cursor()
    cursor.execute("select * from users where u_id=%s;", (user_id,))
    user_data = cursor.fetchone()
    if user_data != None:
        new_user = model.User(user_data[0], user_data[1], user_data[2], user_data[3])
        return new_user
    else:
        return None
