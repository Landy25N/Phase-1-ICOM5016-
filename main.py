from flask import Flask, jsonify, request
from handler.resources import ResourceHandler
from handler.requests import RequestHandler
from handler.users import UserHandler
from handler.weekly import WeeklyHandler


app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Why hello there! This is a semicomplete, semihard-wired resources app! :<'



@app.route('/Resources/register/admin')
def regAdmin():
    return UserHandler().registerAdmin(1, 'Rouon', 'Aro')

@app.route('/Resources/register/inneed')
def regNeed():
    return UserHandler().registerNeed(5, 'Akagami', 'Hero')

@app.route('/Resources/register/supplier')
def regSupplier():
    return UserHandler().registerSupplier(4, 'Kemonone', 'Rou')

@app.route('/Resources/suppliers')
def showAllSuppliers():
    return UserHandler().ShowAllSuppliers()

@app.route('/Resources/suppliers/<int:uid>')
def showSupplier(uid):
    return UserHandler().ShowSupplier(uid)

@app.route('/Resources/request/<int:rid>')
def addRequestedResource(rid):
    return RequestHandler().addRequestedResource(5, 1, '10')

@app.route('/Resources/<int:rid>')
def getAResource(rid):
    return ResourceHandler().getAResource(rid)

@app.route('/Resources/reserve')
def reserveResource():
    return RequestHandler().reserveResource(16, '4')

@app.route('/Resources/purchase')
def purchaseResource():
    return RequestHandler().reserveResource(16, '4')

@app.route('/Resources/requested')
def getRequestedResources():
    return RequestHandler().getRequestedResources()

@app.route('/Resources')
def getAvailableResources():
    return ResourceHandler().getAvailableResources()

@app.route('/Resources/requested/<string:keyword>')
def getRequestByKeyword(keyword):
    return RequestHandler().getRequestByKeyword(keyword)

@app.route('/Resources/<string:keyword>')
def getAvailableByKeyword(keyword):
    return ResourceHandler().getAvailableByKeyword(keyword)

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

@app.route('/Resources/<int:rid>/supplies')
def getResourcesBySupplierId(uid):
    return UserHandler().getResourcesBySupplierId(uid)

@app.route('/Resources/<int:rid>/suppliers')
def getSuppliersByResourceId(rid):
    return ResourceHandler().getSuppliersByResourceId(rid)

@app.route('/Resources/<string:city>/supplies')
def getResourcesByCity(city):
    return ResourceHandler().getResourcesByCity(city)

@app.route('/Resources/purchases/<int:uid>')
def getPurchasesByUserId(uid):
    return UserHandler().getPurchasesByUserId(uid)

@app.route('/Resources/sales/<int:uid>')
def getPurchasesByUserId(uid):
    return UserHandler().getSalesByUserId(uid)


if __name__ == '__main__':
    app.run()