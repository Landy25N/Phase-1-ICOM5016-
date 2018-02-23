from config.dbconfig import rg_config
import psycopg2
class ResourcesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (rg_config['dbname'],
                                                            rg_config['user'],
                                                            rg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def addResource(self, rname, rprice):
        cursor = self.conn.cursor()
        query = "insert into resources(rname,rprice) values (%s, %s) returning rid;"
        cursor.execute(query, (rname, rprice,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def addSupply(self, uid, rid, qty):
        cursor = self.conn.cursor()
        query = "insert into supplies(uid, rid, qty) values (%s, %s, %s);"
        cursor.execute(query, (uid, rid, qty,))
        self.conn.commit()
        return rid

    def updateResource(self, rid, rname, rprice):
        cursor = self.conn.cursor()
        query = "update resources set rname = %s, rprice = %s where rid = %s;"
        cursor.execute(query, (rname, rprice, rid,))
        self.conn.commit()
        return rid

    def getAResource(self, rid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, qty from resources natural inner join supplies where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getAvailableResources(self):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, qty from resources natural inner join supplies;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAvailableByKeyword(self, keyword):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, qty from resources natural inner join supplies where rname = %s order by rname;"
        cursor.execute(query, (keyword,))
        result = cursor.fetchone()
        return result

    def getSuppliersByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select uid, fname, lname, city, phone from resources natural inner join users natural inner join supplies natural inner join address where rid = %s and type = 2;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCity(self, city):
        cursor = self.conn.cursor()
        query = "rid, rname, rprice, qty from resources natural inner join users natural inner join supplies natural inner join address where city = %s and type = 2;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDailyStats(self):
        result = []
        result.append('9')
        result.append('5')
        result.append('20')
        result.append('0')
        result.append('2')
        result.append('10')
        result.append('0')
        result.append('5')
        result.append('20')
        result.append('0')
        result.append('2')
        result.append('0')
        result.append('5')
        result.append('30')
        result.append('0')
        result.append('8')
        return result

    def getSenateStats(self):

        #San Juan

        result = []
        result.append('1')
        result.append('1')
        result.append('1')
        result.append('1')
        result.append('1')
        result.append('0')
        result.append('0')
        result.append('0')
        result.append('1')
        result.append('1')
        result.append('0')
        result.append('0')
        result.append('1')
        result.append('1')
        result.append('0')
        result.append('8')

        #Bayamon

        result.append('3')
        result.append('4')
        result.append('4')
        result.append('0')
        result.append('1')
        result.append('2')
        result.append('0')
        result.append('0')
        result.append('0')
        result.append('3')
        result.append('2')
        result.append('2')
        result.append('3')
        result.append('2')
        result.append('0')
        result.append('0')

        #Arecibo

        result.append('6')
        result.append('1')
        result.append('5')
        result.append('2')
        result.append('1')
        result.append('0')
        result.append('0')
        result.append('0')
        result.append('0')
        result.append('5')
        result.append('1')
        result.append('5')
        result.append('2')
        result.append('3')
        result.append('1')
        result.append('0')

        #Mayaguez

        result.append('1')
        result.append('3')
        result.append('0')
        result.append('0')
        result.append('2')
        result.append('1')
        result.append('3')
        result.append('0')
        result.append('1')
        result.append('2')
        result.append('0')
        result.append('3')
        result.append('2')
        result.append('0')
        result.append('1')
        result.append('0')

        #Ponce

        result.append('3')
        result.append('5')
        result.append('1')
        result.append('2')
        result.append('0')
        result.append('0')
        result.append('0')
        result.append('4')
        result.append('2')
        result.append('2')
        result.append('4')
        result.append('0')
        result.append('0')
        result.append('1')
        result.append('0')
        result.append('2')

        #Guayama

        result.append('1')
        result.append('3')
        result.append('0')
        result.append('0')
        result.append('0')
        result.append('2')
        result.append('3')
        result.append('5')
        result.append('3')
        result.append('2')
        result.append('1')
        result.append('4')
        result.append('3')
        result.append('2')
        result.append('5')
        result.append('1')

        #Humacao

        result.append('0')
        result.append('0')
        result.append('0')
        result.append('0')
        result.append('0')
        result.append('0')
        result.append('1')
        result.append('2')
        result.append('2')
        result.append('1')
        result.append('0')
        result.append('1')
        result.append('0')
        result.append('1')
        result.append('1')
        result.append('0')

        #Carolina

        result.append('2')
        result.append('3')
        result.append('4')
        result.append('1')
        result.append('2')
        result.append('1')
        result.append('0')
        result.append('1')
        result.append('0')
        result.append('0')
        result.append('2')
        result.append('1')
        result.append('3')
        result.append('0')
        result.append('0')
        result.append('0')

        return result