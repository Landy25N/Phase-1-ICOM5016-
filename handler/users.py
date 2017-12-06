from flask import jsonify
from dao.users import UsersDAO


class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['qty'] = row[2]
        return result

    def registerAdmin(self, uid, fname, lname):
        dao = UsersDAO()
        result = dao.addAdmin(uid, 1, fname, lname)
        return jsonify(Register=result)

    def registerNeed(self, uid, fname, lname):
        dao = UsersDAO()
        result = dao.addNeed(uid, 2, fname, lname)
        return jsonify(Register=result)

    def registerSupplier(self, uid, fname, lname):
        dao = UsersDAO()
        result = dao.addSupplier(uid, 3, fname, lname)
        return jsonify(Register=result)