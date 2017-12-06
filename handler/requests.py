from flask import jsonify
from dao.requests import RequestsDAO


class RequestHandler:
    def build_request_dict(self, row):
        result = {}
        divide = row.split(' ')
        result['rid'] = divide[0]
        result['rname'] = divide[1]
        result['qty'] = divide[2]
        return result

    def build_add_request_dict(self, string):
        return string

    def getRequestedResources(self):
        dao = RequestsDAO()
        request_list = dao.getRequestedResources()
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestByKeyword(self, keyword):
        dao = RequestsDAO()
        request_list = dao.getRequestByKeyword(keyword)
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def addRequestedResource(self, uid, rid, qty):
        dao = RequestsDAO()
        result = dao.addRequestedResource(uid, rid, qty)
        return jsonify(AddRequest=result)

    def reserveResource(self, rid, qty):
        dao = RequestsDAO()
        result = dao.reserveResource(rid, qty)
        return jsonify(AddReserve=result)