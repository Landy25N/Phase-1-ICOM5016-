from config.dbconfig import rg_config
import psycopg2
class RequestsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (rg_config['dbname'],
                                                            rg_config['user'],
                                                            rg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

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
        result = qty + ' bags of ice have been successfully added.'
        return result

    def reserveResource(self, rid, qty):
        result = qty + ' batteries have been successfully requested.'
        return result