from config.dbconfig import rg_config
import psycopg2
class UsersDAO:

    def addAdmin(self, uid, type, fname, lname):
        result = 'The admin, ' + fname + ' ' + lname + ', has been successfully registered.'
        return result

    def addNeed(self, uid, type, fname, lname):
        result = 'The person in need, ' + fname + ' ' + lname + ', has been successfully registered.'
        return result

    def addSupplier(self, uid, type, fname, lname):
        result = 'The supplier, ' + fname + ' ' + lname + ', has been successfully registered.'
        return result

    def removeUser(self, uid):
        result = []
        return result