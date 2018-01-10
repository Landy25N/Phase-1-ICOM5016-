from flask import jsonify
from dao.resources import ResourcesDAO


class ResourceHandler:
    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rprice'] = row[2]
        result['qty'] = row[3]
        return result

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['fname'] = row[1]
        result['lname'] = row[2]
        result['city'] = row[3]
        result['phone'] = row[4]
        return result

    def build_daily_needs_dict(self, row):
        result = {}
        if row[0] == '0':
            result['small water bottle'] = row[0]
        if row[1] == '0':
            result['1 gallon of water'] = row[1]
        if row[2] == '0':
            result['medications'] = row[2]
        if row[3] == '0':
            result['baby food'] = row[3]
        if row[4] == '0':
            result['canned food'] = row[4]
        if row[5] == '0':
            result['dry food'] = row[5]
        if row[6] == '0':
            result['ice'] = row[6]
        if row[7] == '0':
            result['diesel'] = row[7]
        if row[8] == '0':
            result['propane'] = row[8]
        if row[9] == '0':
            result['gasoline'] = row[9]
        if row[10] == '0':
            result['medical devices'] = row[10]
        if row[11] == '0':
            result['heavy devices'] = row[11]
        if row[12] == '0':
            result['tools'] = row[12]
        if row[13] == '0':
            result['clothing'] = row[13]
        if row[14] == '0':
            result['power generatos'] = row[14]
        if row[15] == '0':
            result['batteries'] = row[15]
        return result

    def build_daily_available_dict(self, row):
        result = {}
        if int(row[0]) > 0:
            result['small water bottle'] = row[0]
        if int(row[1]) > 0:
            result['1 gallon of water'] = row[1]
        if int(row[2]) > 0:
            result['medications'] = row[2]
        if int(row[3]) > 0:
            result['baby food'] = row[3]
        if int(row[4]) > 0:
            result['canned food'] = row[4]
        if int(row[5]) > 0:
            result['dry food'] = row[5]
        if int(row[6]) > 0:
            result['ice'] = row[6]
        if int(row[7]) > 0:
            result['diesel'] = row[7]
        if int(row[8]) > 0:
            result['propane'] = row[8]
        if int(row[9]) > 0:
            result['gasoline'] = row[9]
        if int(row[10]) > 0:
            result['medical devices'] = row[10]
        if int(row[11]) > 0:
            result['heavy devices'] = row[11]
        if int(row[12]) > 0:
            result['tools'] = row[12]
        if int(row[13]) > 0:
            result['clothing'] = row[13]
        if int(row[14]) > 0:
            result['power generatos'] = row[14]
        if int(row[15]) > 0:
            result['batteries'] = row[15]
        return result

    def build_all_daily_dict(self, row):
        result = {}
        result['small water bottle'] = row[0]
        result['1 gallon of water'] = row[1]
        result['medications'] = row[2]
        result['baby food'] = row[3]
        result['canned food'] = row[4]
        result['dry food'] = row[5]
        result['ice'] = row[6]
        result['diesel'] = row[7]
        result['propane'] = row[8]
        result['gasoline'] = row[9]
        result['medical devices'] = row[10]
        result['heavy devices'] = row[11]
        result['tools'] = row[12]
        result['clothing'] = row[13]
        result['power generators'] = row[14]
        result['batteries'] = row[15]
        return result

    def build_senate_needs_dict(self, row, index):
        result = {}
        if index == 0:
            result['region'] = 'San Juan'
        elif index == 16:
            result['region'] = 'Bayamon'
        elif index == 32:
            result['region'] = 'Arecibo'
        elif index == 48:
            result['region'] = 'Mayaguez'
        elif index == 64:
            result['region'] = 'Ponce'
        elif index == 80:
            result['region'] = 'Guayama'
        elif index == 96:
            result['region'] = 'Humacao'
        elif index == 112:
            result['region'] = 'Carolina'
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

    def build_senate_available_dict(self, row, index):
        result = {}
        if index == 0:
            result['region'] = 'San Juan'
        elif index == 16:
            result['region'] = 'Bayamon'
        elif index == 32:
            result['region'] = 'Arecibo'
        elif index == 48:
            result['region'] = 'Mayaguez'
        elif index == 64:
            result['region'] = 'Ponce'
        elif index == 80:
            result['region'] = 'Guayama'
        elif index == 96:
            result['region'] = 'Humacao'
        elif index == 112:
            result['region'] = 'Carolina'
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

    def getAResource(self, rid):
        dao = ResourcesDAO()
        row = dao.getAResource(rid)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            request = self.build_resource_dict(row)
            return jsonify(Resource = request)

    def getAvailableResources(self):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(AvailableResources=result_list)

    def getAvailableByKeyword(self, keyword):
        dao = ResourcesDAO()
        row = dao.getAvailableByKeyword(keyword)
        if not row:
            return jsonify(Error = "Resource Not Available"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(ResourceSearchResult = resource)

    def getSuppliersByResourceId(self, rid):
        dao = ResourcesDAO()
        if not dao.getAResource(rid):
            return jsonify(Error="Resource Not Found"), 404
        suppliers_list = dao.getSuppliersByResourceId(rid)
        result_list = []
        for row in suppliers_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getResourcesByCity(self, city):
        dao = ResourcesDAO()
        suppliers_list = dao.getResourcesByCity(city)
        if len(suppliers_list) == 0:
            return jsonify(Error="City Not Found"), 404
        result_list = []
        for row in suppliers_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getDailyNeedsStats(self):
        dao = ResourcesDAO()
        daily_list = dao.getDailyStats()
        result = self.build_daily_needs_dict(daily_list)
        return jsonify(DailyNeedsDashboard=result)

    def getDailyAvailableStats(self):
        dao = ResourcesDAO()
        daily_list = dao.getDailyStats()
        result = self.build_daily_available_dict(daily_list)
        return jsonify(DailyAvailabilityDashboard=result)

    def getAllDailyStats(self):
        dao = ResourcesDAO()
        daily_list = dao.getDailyStats()
        result = []
        result1 = self.build_daily_needs_dict(daily_list)
        result2 = self.build_daily_available_dict(daily_list)
        result.append(result1)
        result.append(result2)
        return jsonify(DailyDashboard=result)

    def getSenateNeedsStats(self):
        dao = ResourcesDAO()
        weekly_list = dao.getSenateStats()
        result_list = []
        for row in range(0, 8):
            result = self.build_senate_needs_dict(weekly_list, row*16)
            result_list.append(result)
        return jsonify(SenateNeedsDashboard=result_list)

    def getSenateAvailableStats(self):
        dao = ResourcesDAO()
        weekly_list = dao.getSenateStats()
        result_list = []
        for row in range(0, 8):
            result = self.build_senate_available_dict(weekly_list, row*16)
            result_list.append(result)
        return jsonify(SenateAvailabilityDashboard=result_list)

    def getAllSenateStats(self):
        dao = ResourcesDAO()
        weekly_list = dao.getSenateStats()
        result_list = []
        for row in range(0, 8):
            result1 = self.build_senate_needs_dict(weekly_list, row*16)
            result_list.append(result1)
        for row in range(0, 8):
            result2 = self.build_senate_available_dict(weekly_list, row*16)
            result_list.append(result2)
        return jsonify(SenateDashboard=result_list)