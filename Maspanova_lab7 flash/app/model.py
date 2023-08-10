class Role:  ##для ролей
    id = 0
    title = ""

    def __init__(self, id, title):
        self.id = id
        self.title = title


class Registration:  ##класс для регистрации
    id = 0
    login = ""
    password = ""
    u_id = 0
    checkPassword = ""

    def __init__(
        self, id=0, login="", password="", u_id=0, checkPassword=""
    ):  ##конструктор
        self.id = id
        self.login = login
        self.password = password
        self.u_id = u_id
        self.checkPassword = checkPassword
