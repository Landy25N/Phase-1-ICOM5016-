from config.dbconfig import rg_config
import psycopg2

class WeeklyDAO:

    def getWeeklyStats(self):
        #Latest day

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

        #2nd day

        result.append('0')
        result.append('0')
        result.append('4')
        result.append('0')
        result.append('4')
        result.append('3')
        result.append('0')
        result.append('1')
        result.append('5')
        result.append('1')
        result.append('6')
        result.append('8')
        result.append('0')
        result.append('10')
        result.append('0')
        result.append('5')

        #3rd day

        result.append('10')
        result.append('23')
        result.append('10')
        result.append('15')
        result.append('0')
        result.append('1')
        result.append('6')
        result.append('8')
        result.append('0')
        result.append('2')
        result.append('8')
        result.append('1')
        result.append('0')
        result.append('10')
        result.append('3')
        result.append('5')

        #4th day

        result.append('0')
        result.append('6')
        result.append('8')
        result.append('0')
        result.append('7')
        result.append('5')
        result.append('4')
        result.append('2')
        result.append('10')
        result.append('6')
        result.append('0')
        result.append('7')
        result.append('4')
        result.append('0')
        result.append('0')
        result.append('7')

        #5th day

        result.append('6')
        result.append('2')
        result.append('1')
        result.append('9')
        result.append('0')
        result.append('8')
        result.append('2')
        result.append('6')
        result.append('25')
        result.append('8')
        result.append('10')
        result.append('16')
        result.append('1')
        result.append('5')
        result.append('8')
        result.append('7')

        #6th day

        result.append('10')
        result.append('20')
        result.append('14')
        result.append('12')
        result.append('19')
        result.append('0')
        result.append('7')
        result.append('10')
        result.append('23')
        result.append('12')
        result.append('5')
        result.append('11')
        result.append('4')
        result.append('7')
        result.append('10')
        result.append('7')

        #7th day

        result.append('1')
        result.append('5')
        result.append('0')
        result.append('0')
        result.append('0')
        result.append('0')
        result.append('2')
        result.append('4')
        result.append('6')
        result.append('3')
        result.append('2')
        result.append('0')
        result.append('2')
        result.append('1')
        result.append('1')
        result.append('0')

        return result