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

    def build_request_attributes(self, uid, rid, rname, qty):
        result = {}
        result['uid'] = uid
        result['rid'] = rid
        result['rname'] = rname
        result['qty'] = qty
        return result

    def build_purchase_attributes(self, uid, cid, ptotal, pdate):
        result = {}
        result['uid'] = uid
        result['cid'] = cid
        result['ptotal'] = ptotal
        result['pdate'] = pdate
        return result

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

    def addRequestedResource(self, form):
        if len(form) != 3:
            return jsonify(Error = "Malformed post request"), 400
        else:
            uid = form['uid']
            rid = form['rid']
            qty = form['qty']
            if uid and rid and qty:
                dao = RequestsDAO()
                if not dao.confirmAResource(rid):
                    return jsonify(Error = "Resource not found."), 404
                else:
                    rname = dao.confirmAResource(rid)[0]
                    dao.addRequestedResource(uid, rid, qty)
                    result = self.build_request_attributes(uid, rid, rname, qty)
                    return jsonify(AddRequest=result), 201

    def reserveFreeResource(self, form):
        if len(form) != 8:
            return jsonify(Error = "Malformed post request"), 400
        else:
            pdate = form['pdate']
            uid = form['uid']
            sellerid = form['sellerid']
            cid = form['cid']
            rid = form['rid']
            pprice = form['pprice']
            qty = form['qty']
            ptotal = form['ptotal']
            if pdate and uid and sellerid and cid == 'null' and rid and pprice and qty and ptotal:
                dao = RequestsDAO()
                if not dao.confirmAResource(rid):
                    return jsonify(Error = "Resource not found."), 404
                else:
                    rname = dao.confirmAResource(rid)[0]
                    productPrice = dao.getResourcesPrice(cid)[0]
                    if productPrice > 0:
                        return jsonify(Error = "This resource isn't free, thus can't be reserved. It must be purchased"), 400
                    sellerQty = dao.getSellersQty(sellerid, rid)[0]
                    if sellerQty < qty:
                        return jsonify(Error = "Seller doesn't have the amount of resources requested"), 400
                    pid = dao.addPurchase(sellerid, uid, cid, ptotal, pdate)
                    dao.addResourceSales(pid, rid, qty, pprice)
                    dao. updateSellersQty(qty, sellerid, rid)
                    result = self.build_purchase_attributes(uid, cid, ptotal, pdate)
                    return jsonify(Purchase=result), 201

    def purchaseResource(self, form):
        if len(form) != 8:
            return jsonify(Error = "Malformed post request"), 400
        else:
            pdate = form['pdate']
            uid = form['uid']
            sellerid = form['sellerid']
            cid = form['cid']
            rid = form['rid']
            pprice = form['pprice']
            qty = form['qty']
            ptotal = form['ptotal']
            if pdate and uid and sellerid and cid and rid and pprice and qty and ptotal:
                dao = RequestsDAO()
                if not dao.confirmAResource(rid):
                    return jsonify(Error = "Resource not found."), 404
                else:
                    rname = dao.confirmAResource(rid)[0]
                    productPrice = dao.getResourcesPrice(uid, cid)[0]
                    if productPrice == 0:
                        return jsonify(Error = "This resource is free, thus can't be purchased. It must be reserved"), 400
                    sellerQty = dao.getSellersQty(sellerid, rid)[0]
                    if sellerQty < qty:
                        return jsonify(Error = "Seller doesn't have the amount of resources requested"), 400
                    pid = dao.addPurchase(sellerid, uid, cid, ptotal, pdate)
                    dao.addResourceSales(pid, rid, qty, pprice)
                    dao. updateSellersQty(qty, sellerid, rid)
                    result = self.build_purchase_attributes(uid, cid, ptotal, pdate)
                    return jsonify(Purchase=result), 201