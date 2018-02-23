from flask import Flask, jsonify, request
from handler.resources import ResourceHandler
from handler.requests import RequestHandler
from handler.users import UserHandler
from handler.weekly import WeeklyHandler


app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Why hello there! This is a kinda complete resources app'



@app.route('/Resources/register/admin', methods=['POST'])
def regAdmin():
    if request.method == 'POST':
        return UserHandler().registerAdmin(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/register/inneed', methods=['POST'])
def regNeed():
    if request.method == 'POST':
        return UserHandler().registerNeed(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/register/supplier', methods=['POST'])
def regSupplier():
    if request.method == 'POST':
        return UserHandler().registerSupplier(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/suppliers', methods=['GET', 'POST'])
def showAllSuppliers():
    if request.method == 'POST':
        return UserHandler().registerSupplier(request.form)
    elif not request.args:
            return UserHandler().showAllSuppliers()
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/suppliers/<int:uid>', methods=['GET'])
def showSupplier(uid):
    if request.method == 'GET':
        return UserHandler().showSupplier(uid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/request/<int:rid>', methods=['POST'])
def addRequestedResource(rid):
    if request.method == 'POST':
        return RequestHandler().addRequestedResource(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/<int:rid>', methods=['GET', 'PUT'])
def getAResource(rid):
    if request.method == 'GET':
        return ResourceHandler().getAResource(rid)
    elif  request.method == 'PUT':
        return ResourceHandler().updateResource(rid, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/reserve', methods=['POST'])
def reserveFreeResource():
    if request.method == 'POST':
        return RequestHandler().reserveFreeResource(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/purchase', methods=['POST'])
def purchaseResource():
    if request.method == 'POST':
        return RequestHandler().purchaseResource(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/requested', methods=['POST'])
def getRequestedResources():
    if request.method == 'POST':
        return RequestHandler().getRequestedResources()
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources', methods=['POST'])
def getAvailableResources():
    if request.method == 'POST':
        return ResourceHandler().getAvailableResources()
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/requested/<string:keyword>', methods=['POST'])
def getRequestByKeyword(keyword):
    if request.method == 'POST':
        return RequestHandler().getRequestByKeyword(keyword)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/<string:keyword>', methods=['POST'])
def getAvailableByKeyword(keyword):
    if request.method == 'POST':
        return ResourceHandler().getAvailableByKeyword(keyword)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/dashboard/daily/needs')
def getDailyNeedsStats():
    return ResourceHandler().getDailyNeedsStats()

@app.route('/Resources/dashboard/daily/available')
def getDailyAvailableStats():
    return ResourceHandler().getDailyAvailableStats()

@app.route('/Resources/dashboard/daily')
def getAllDailyStats():
    return ResourceHandler().getAllDailyStats()

@app.route('/Resources/dashboard/weekly/needs')
def getWeeklyNeedsStats():
    return WeeklyHandler().getWeeklyNeedsStats()

@app.route('/Resources/dashboard/weekly/available')
def getWeeklyAvailableStats():
    return WeeklyHandler().getWeeklyAvailableStats()

@app.route('/Resources/dashboard/weekly')
def getAllWeeklyStats():
    return WeeklyHandler().getAllWeeklyStats()

@app.route('/Resources/dashboard/senate/needs')
def getSenateNeedsStats():
    return ResourceHandler().getSenateNeedsStats()

@app.route('/Resources/dashboard/senate/available')
def getSenateAvailableStats():
    return ResourceHandler().getSenateAvailableStats()

@app.route('/Resources/dashboard/senate')
def getAllSenateStats():
    return ResourceHandler().getAllSenateStats()

@app.route('/Resources/<int:rid>/supplies', methods=['POST'])
def getResourcesBySupplierId(uid):
    if request.method == 'POST':
        return UserHandler().getResourcesBySupplierId(uid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/<int:rid>/suppliers', methods=['POST'])
def getSuppliersByResourceId(rid):
    if request.method == 'POST':
        return ResourceHandler().getSuppliersByResourceId(rid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/<string:city>/supplies', methods=['POST'])
def getResourcesByCity(city):
    if request.method == 'POST':
        return ResourceHandler().getResourcesByCity(city)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/purchases/<int:uid>', methods=['POST'])
def getPurchasesByUserId(uid):
    if request.method == 'POST':
        return UserHandler().getPurchasesByUserId(uid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/sales/<int:uid>', methods=['POST'])
def getPurchasesByUserId(uid):
    if request.method == 'POST':
        return UserHandler().getSalesByUserId(uid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/purchases/<int:rid>', methods=['POST'])
def getPurchasesByPurchaseId(pid):
    if request.method == 'POST':
        return UserHandler().getPurchasesByPurchaseId(pid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Resources/register/creditcard', methods=['POST', 'PUT'])
def registerCreditCard():
    if request.method == 'POST':
        return UserHandler().registerCreditCard(request.form)
    elif request.method == 'PUT':
        return UserHandler().updateCreditCard(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

if __name__ == '__main__':
    app.run()