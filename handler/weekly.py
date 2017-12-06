from flask import jsonify
from dao.weekly import WeeklyDAO


class WeeklyHandler:

    def build_weekly_needs_dict(self, row, index):
        result = {}
        if row[index] == '0':
            result['small water bottle'] = row[index]
        if row[index+1] == '0':
            result['1 gallon of water'] = row[index+1]
        if row[index+2] == '0':
            result['medications'] = row[index+2]
        if row[index+3] == '0':
            result['baby food'] = row[index+3]
        if row[index+4] == '0':
            result['canned food'] = row[index+4]
        if row[index+5] == '0':
            result['dry food'] = row[index+5]
        if row[index+6] == '0':
            result['ice'] = row[index+6]
        if row[index+7] == '0':
            result['diesel'] = row[index+7]
        if row[index+8] == '0':
            result['propane'] = row[index+8]
        if row[index+9] == '0':
            result['gasoline'] = row[index+9]
        if row[index+10] == '0':
            result['medical devices'] = row[index+10]
        if row[index+11] == '0':
            result['heavy devices'] = row[index+11]
        if row[index+12] == '0':
            result['tools'] = row[index+12]
        if row[index+13] == '0':
            result['clothing'] = row[index+13]
        if row[index+14] == '0':
            result['power generators'] = row[index+14]
        if row[index+15] == '0':
            result['batteries'] = row[index+15]
        return result

    def build_weekly_available_dict(self, row, index):
        result = {}
        if int(row[index+0]) > 0:
            result['small water bottle'] = row[index+0]
        if int(row[index+1]) > 0:
            result['1 gallon of water'] = row[index+1]
        if int(row[index+2]) > 0:
            result['medications'] = row[index+2]
        if int(row[index+3]) > 0:
            result['baby food'] = row[index+3]
        if int(row[index+4]) > 0:
            result['canned food'] = row[index+4]
        if int(row[index+5]) > 0:
            result['dry food'] = row[index+5]
        if int(row[index+6]) > 0:
            result['ice'] = row[index+6]
        if int(row[index+7]) > 0:
            result['diesel'] = row[index+7]
        if int(row[index+8]) > 0:
            result['propane'] = row[index+8]
        if int(row[index+9]) > 0:
            result['gasoline'] = row[index+9]
        if int(row[index+10]) > 0:
            result['medical devices'] = row[index+10]
        if int(row[index+11]) > 0:
            result['heavy devices'] = row[index+11]
        if int(row[index+12]) > 0:
            result['tools'] = row[index+12]
        if int(row[index+13]) > 0:
            result['clothing'] = row[index+13]
        if int(row[index+14]) > 0:
            result['power generators'] = row[index+14]
        if int(row[index+15]) > 0:
            result['batteries'] = row[index+15]
        return result

    def getWeeklyNeedsStats(self):
        dao = WeeklyDAO()
        weekly_list = dao.getWeeklyStats()
        result_list = []
        for row in range(0, 7):
            result = self.build_weekly_needs_dict(weekly_list, row*16)
            result_list.append(result)
        return jsonify(Dashboard=result_list)

    def getWeeklyAvailableStats(self):
        dao = WeeklyDAO()
        weekly_list = dao.getWeeklyStats()
        result_list = []
        for row in range(0, 7):
            result = self.build_weekly_available_dict(weekly_list, row*16)
            result_list.append(result)
        return jsonify(Dashboard=result_list)

    def getAllWeeklyStats(self):
        dao = WeeklyDAO()
        weekly_list = dao.getWeeklyStats()
        result_list = []
        for row in range(0, 7):
            result1 = self.build_weekly_needs_dict(weekly_list, row*16)
            result_list.append(result1)
        for row in range(0, 7):
            result2 = self.build_weekly_available_dict(weekly_list, row*16)
            result_list.append(result2)
        return jsonify(Dashboard=result_list)