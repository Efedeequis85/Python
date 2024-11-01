import Crud

host="127.0.0.1"
user = ""
passwd = ""
db = ""
tabla = ""


if __name__ == '__main__':
    api = Crud.Api(host, db, tabla, user, passwd)
    crud = Crud.Crud(api)
    crud.iniciarInterfaz()
