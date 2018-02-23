from flask import jsonify
from dao.users import UsersDAO


class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['fname'] = row[1]
        result['lname'] = row[2]
        result['city'] = row[3]
        result['phone'] = row[4]
        return result

    def build_user_attributes(self, uid, fname, lname, phone, city, street, zcode):
        result = {}
        result['uid'] = uid
        result['fname'] = fname
        result['lname'] = lname
        result['phone'] = phone
        result['city'] = city
        result['street'] = street
        result['zcode'] = zcode
        return result

    def build_supplies_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rprice'] = row[2]
        result['qty'] = row[3]
        return result

    def build_purchases_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pdate'] = row[1]
        result['uid'] = row[2]
        result['fname'] = row[3]
        result['lname'] = row[4]
        result['city'] = row[5]
        result['phone'] = row[6]
        result['rid'] = row[7]
        result['rname'] = row[8]
        result['pprice'] = row[9]
        result['qty'] = row[10]
        result['ptotal'] = row[11]
        result['cid'] = row[12]
        return result

    def build_sales_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pdate'] = row[1]
        result['rid'] = row[2]
        result['rname'] = row[3]
        result['pprice'] = row[4]
        result['qty'] = row[5]
        result['ptotal'] = row[6]
        return result

    def build_creditcard_attributes(self, uid, cnumber, cexpdate, credit_limit):
        result = {}
        result['uid'] = uid
        result['cnumber'] = cnumber
        result['cexpdate'] = cexpdate
        result['credit_limit'] = credit_limit
        return result

    def registerAdmin(self, form):
        if len(form) != 6:
            return jsonify(Error = "Malformed post request"), 400
        else:
            fname = form['fname']
            lname = form['lname']
            phone = form['phone']
            city = form['city']
            street = form['street']
            zcode = form['zcode']
            if fname and lname and phone and city and street and zcode:
                dao = UsersDAO()
                uid = dao.addUser('1', fname, lname, phone)
                dao.addAddress(uid, city, street, zcode)
                result = self.build_user_attributes(uid, fname, lname, phone, city, street, zcode)
                return jsonify(Admin=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def registerNeed(self, form):
        if len(form) != 9:
            return jsonify(Error = "Malformed post request"), 400
        else:
            fname = form['fname']
            lname = form['lname']
            phone = form['phone']
            city = form['city']
            street = form['street']
            zcode = form['zcode']
            cnumber = form['cnumber']
            cexpdate = form['cexpdate']
            credit_limit = form['credit_limit']
            if fname and lname and phone and city and street and zcode and cnumber and cexpdate and credit_limit:
                dao = UsersDAO()
                uid = dao.addUser('3', fname, lname, phone)
                dao.addAddress(uid, city, street, zcode)
                dao.addCreditCard(uid, cnumber, cexpdate, credit_limit)
                result = self.build_user_attributes(uid, fname, lname, phone, city, street, zcode)
                return jsonify(Need=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def registerSupplier(self, form):
        if len(form) != 9:
            return jsonify(Error = "Malformed post request"), 400
        else:
            fname = form['fname']
            lname = form['lname']
            phone = form['phone']
            city = form['city']
            street = form['street']
            zcode = form['zcode']
            cnumber = form['cnumber']
            cexpdate = form['cexpdate']
            credit_limit = form['credit_limit']
            if fname and lname and phone and city and street and zcode and cnumber and cexpdate and credit_limit:
                dao = UsersDAO()
                uid = dao.addUser('2', fname, lname, phone)
                dao.addAddress(uid, city, street, zcode)
                dao.addCreditCard(uid, cnumber, cexpdate, credit_limit)
                result = self.build_user_attributes(uid, fname, lname, phone, city, street, zcode)
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def showAllSuppliers(self):
        dao = UsersDAO()
        request_list = dao.showAllSuppliers()
        result_list = []
        for row in request_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def showSupplier(self, uid):
        dao = UsersDAO()
        row = dao.showSupplier(uid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            supplier = self.build_user_dict(row)
            return jsonify(Supplier = supplier)

    def getResourcesBySupplierId(self, uid):
        dao = UsersDAO()
        if not dao.showSupplier(uid):
            return jsonify(Error="Supplier Not Found"), 404
        resources_list = dao.getResourcesBySupplierId(uid)
        result_list = []
        for row in resources_list:
            result = self.build_supplies_dict(row)
            result_list.append(result)
        return jsonify(ResourcesFromSupplier=result_list)

    def getPurchasesByUserId(self, uid):
        dao = UsersDAO()
        if not dao.showSupplier(uid):
            return jsonify(Error="Supplier Not Found"), 404
        resources_list = dao.getPurchasesByUserId(uid)
        result_list = []
        for row in resources_list:
            result = self.build_purchases_dict(row)
            result_list.append(result)
        return jsonify(PurchasesDoneByUser=result_list)

    def getSalesByUserId(self, uid):
        dao = UsersDAO()
        if not dao.showSupplier(uid):
            return jsonify(Error="Supplier Not Found"), 404
        resources_list = dao.getSalesByUserId(uid)
        result_list = []
        for row in resources_list:
            result = self.build_sales_dict(row)
            result_list.append(result)
        return jsonify(SalesDoneByUser=result_list)

    def getPurchasesByPurchaseId(self, pid):
        dao = UsersDAO()
        resources_list = dao.getPurchasesByPurchaseId(pid)
        result_list = []
        if not result_list:
            return jsonify(Error="Purchase ID Not Found"), 404
        for row in resources_list:
            result = self.build_purchases_dict(row)
            result_list.append(result)
        return jsonify(PurchasesDoneByUser=result_list)

    def registerCreditCard(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            uid = form['uid']
            cnumber = form['cnumber']
            cexpdate = form['cexpdate']
            credit_limit = form['credit_limit']
            if uid and cnumber and cexpdate and credit_limit:
                dao = UsersDAO()
                dao.addCreditCard(uid, cnumber, cexpdate, credit_limit)
                result = self.build_creditcard_attributes(uid, cnumber, cexpdate, credit_limit)
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateCreditCard(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            uid = form['uid']
            cnumber = form['cnumber']
            cexpdate = form['cexpdate']
            credit_limit = form['credit_limit']
            if uid and cnumber and cexpdate and credit_limit:
                dao = UsersDAO()
                dao.updateCreditCard(uid, cnumber, cexpdate, credit_limit)
                result = self.build_creditcard_attributes(uid, cnumber, cexpdate, credit_limit)
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400