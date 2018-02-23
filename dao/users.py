from config.dbconfig import rg_config
import psycopg2
class UsersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (rg_config['dbname'],
                                                            rg_config['user'],
                                                            rg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def addUser(self, type, lname, fname, phone):
        cursor = self.conn.cursor()
        query = "insert into users(type, lname, fname, phone) values (%s, %s, %s, %s) returning uid;"
        cursor.execute(query, (type, lname, fname, phone,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def addAddress(self, uid, city, street, zcode):
        cursor = self.conn.cursor()
        query = "insert into address(uid, city, street, zcode) values (%s, %s, %s, %s);"
        cursor.execute(query, (uid, city, street, zcode,))
        self.conn.commit()
        return uid

    def addCreditCard(self, uid, cnumber, cexpdate, credit_limit):
        cursor = self.conn.cursor()
        query = "insert into creditcards(uid, cnumber, cexpdate, credit_limit) values (%s, %s, %s, %s);"
        cursor.execute(query, (uid, cnumber, cexpdate, credit_limit,))
        self.conn.commit()
        return uid

    def updateCreditCard(self, uid, cnumber, cexpdate, credit_limit):
        cursor = self.conn.cursor()
        query = "update creditcards set cnumber = %s, cexpdate = %s, credit_limit = %s where uid = %s;"
        cursor.execute(query, (cnumber, cexpdate, credit_limit, uid,))
        self.conn.commit()
        return uid

    def showAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select uid, fname, lname, city, phone from users natural inner join address where type = 2;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def showSupplier(self, uid):
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

    def getPurchasesByPurchaseId(self, pid):
        cursor = self.conn.cursor()
        query = "select pid, pdate, uid, fname, lname, city, phone, rid, rname, pprice, qty, ptotal, cid from users natural inner join address natural inner join resources natural inner join purchases natural inner join creditcards natural inner join resourcesales where pid = %s;"
        cursor.execute(query, (pid,))
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