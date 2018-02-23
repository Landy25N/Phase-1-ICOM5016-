from config.dbconfig import rg_config
import psycopg2
class RequestsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (rg_config['dbname'],
                                                            rg_config['user'],
                                                            rg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def confirmAResource(self, rid):
        cursor = self.conn.cursor()
        query = "select rname from resources where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getARequestedResource(self, rid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, qty from resources natural inner join requests where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getRequestedResources(self):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, qty from resources natural inner join requests;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByKeyword(self, keyword):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, qty from resources natural inner join requests where rname = %s order by rname;"
        cursor.execute(query, (keyword,))
        result = cursor.fetchone()
        return result

    def addRequestedResource(self, uid, rid, qty):
        cursor = self.conn.cursor()
        query = "insert into requests(uid, rid, qty) values (%s, %s, %s);"
        cursor.execute(query, (uid, rid, qty,))
        self.conn.commit()
        return uid

    def addPurchase(self, sellerid, uid, cid, ptotal, pdate):
        cursor = self.conn.cursor()
        query = "insert into purchases(sellerid, uid, cid, ptotal, pdate) values (%s, %s, %s, %s, %s) returning pid;"
        cursor.execute(query, (sellerid, uid, cid, ptotal, pdate,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def addResourceSales(self, pid, rid, qty, pprice):
        cursor = self.conn.cursor()
        query = "insert into resourcesales(pid, rid, qty, pprice) values (%s, %s, %s, %s);"
        cursor.execute(query, (pid, rid, qty, pprice,))
        self.conn.commit()
        return pid

    def getResourcesPrice(self, uid, rid):
        cursor = self.conn.cursor()
        query = "select pprice from supplies where uid = %s and rid = %s;"
        cursor.execute(query, (uid, rid,))
        result = cursor.fetchone()
        return result

    def getSellersQty(self, uid, rid):
        cursor = self.conn.cursor()
        query = "select qty from supplies where uid = %s and rid = %s;"
        cursor.execute(query, (uid, rid,))
        result = cursor.fetchone()
        return result

    def updateSellersQty(self, sub, uid, rid):
        cursor = self.conn.cursor()
        query = "update supplies set qty = (qty - %s) where uid = %s and rid = %s;"
        cursor.execute(query, (sub, uid, rid,))
        self.conn.commit()
        return rid