from config.dbconfig import rg_config
import psycopg2
class RequestsDAO:

    def getRequestedResources(self):
        result = []
        result.append('1 Small_Bottle 1')
        result.append("2 1_Gallon_Bottle 5")
        result.append('5 Canned_Food 10')
        result.append('7 Ice 15')
        result.append('10 Gasoline 2')
        result.append('12 Heavy_Device 1')
        result.append('15 Power_Generator 1')
        return result

    def getRequestByKeyword(self, keyword):
        result = []
        result.append('2 1_Gallon_Bottle 5')
        result.append('1 Small_Bottle 2')
        return result

    def addRequestedResource(self, uid, rid, qty):
        result = qty + ' bags of ice have been successfully added.'
        return result

    def reserveResource(self, rid, qty):
        result = qty + ' batteries have been successfully requested.'
        return result