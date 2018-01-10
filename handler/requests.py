from flask import jsonify
from dao.requests import RequestsDAO


class RequestHandler:
    def build_request_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rprice'] = row[2]
        result['qty'] = row[3]
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
        row = dao.getRequestByKeyword(keyword)
        if not row:
            return jsonify(Error = "Request Not Found"), 404
        else:
            request = self.build_request_dict(row)
            return jsonify(RequestsSearchResult = request)

    def addRequestedResource(self, uid, rid, qty):
        dao = RequestsDAO()
        result = dao.addRequestedResource(uid, rid, qty)
        return jsonify(AddRequest=result)

    def reserveResource(self, rid, qty):
        dao = RequestsDAO()
        result = dao.reserveResource(rid, qty)
        return jsonify(AddReserve=result)