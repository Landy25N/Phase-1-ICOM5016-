from config.dbconfig import rg_config
import psycopg2
class ResourcesDAO:

    def getAResource(self):
        result = []
        result.append('7 Ice 0')
        return result

    def getAvailableResources(self):
        result = []
        result.append('3 Medications 5')
        result.append('4 Baby_Food 15')
        result.append('6 Dry_Food 10')
        result.append('8 Diesel 5')
        result.append('9 Propane 15')
        result.append('11 Medical_Devices 20')
        result.append('13 Tools 25')
        result.append('14 Clothing 50')
        result.append('16 Batteries 8')
        return result

    def getAvailableByKeyword(self, keyword):
        result = []
        result.append('11 Medical_Devices 20')
        result.append('3 Medications 5')
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