from config.dbconfig import rg_config
import psycopg2
class UsersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (rg_config['dbname'],
                                                            rg_config['user'],
                                                            rg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def addAdmin(self, uid, type, fname, lname):
        result = 'The admin, ' + fname + ' ' + lname + ', has been successfully registered.'
        return result

    def addNeed(self, uid, type, fname, lname):
        result = 'The person in need, ' + fname + ' ' + lname + ', has been successfully registered.'
        return result

    def addSupplier(self, uid, type, fname, lname):
        result = 'The supplier, ' + fname + ' ' + lname + ', has been successfully registered.'
        return result

    def ShowAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select uid, fname, lname, city, phone from users natural inner join address where type = 2;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def ShowSupplier(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, fname, lname, city, phone from users natural inner join address where type = 2 and uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getResourcesBySupplierId(self, uid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, qty from resources natural inner join users natural inner join supplies where uid = %s and type = 2;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select pid, pdate, uid, fname, lname, city, phone, rid, rname, pprice, qty, ptotal, cid from users natural inner join address natural inner join resources natural inner join purchases natural inner join creditcards natural inner join resourcesales where uid = %s and type = 3;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSalesByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select pid, pdate, rid, rname, pprice, qty, ptotal from users natural inner join resources natural inner join purchases natural inner join resourcesales where uid = %s and type = 3;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def removeUser(self, uid):
        result = []
        return result