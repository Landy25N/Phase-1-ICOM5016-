from flask import Flask, jsonify, request
from handler.resources import ResourceHandler
from handler.requests import RequestHandler
from handler.users import UserHandler
from handler.weekly import WeeklyHandler


app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Why hello there! This is a very questionable hard-wired resource app! :<'



@app.route('/users/admin')
def regAdmin():
    return UserHandler().registerAdmin(1, 'Rouon', 'Aro')

@app.route('/users/inneed')
def regNeed():
    return UserHandler().registerNeed(2, 'Kagamine', 'Len')

@app.route('/users/supplier')
def regSupplier():
    return UserHandler().registerSupplier(2, 'Lin', 'Hu')

@app.route('/resources/request/<int:rid>')
def addRequestedResource(rid):
    return RequestHandler().addRequestedResource(5, 1, '10')

@app.route('/resources/<int:rid>')
def getAResource(rid):
    return ResourceHandler().getAResource()

@app.route('/resources/reserve')
def reserveResource():
    return RequestHandler().reserveResource(16, '4')

@app.route('/resources/browse/requested')
def getRequestedResources():
    return RequestHandler().getRequestedResources()

@app.route('/resources/browse/available')
def getAvailableResources():
    return ResourceHandler().getAvailableResources()

@app.route('/resources/browse/requested/<string:keyword>')
def getRequestByKeyword(keyword):
    return RequestHandler().getRequestByKeyword('Bottle')

@app.route('/resources/browse/available/<string:keyword>')
def getAvailableByKeyword(keyword):
    return ResourceHandler().getAvailableByKeyword("Med")

@app.route('/resources/dashboard/daily/needs')
def getDailyNeedsStats():
    return ResourceHandler().getDailyNeedsStats()

@app.route('/resources/dashboard/daily/available')
def getDailyAvailableStats():
    return ResourceHandler().getDailyAvailableStats()

@app.route('/resources/dashboard/daily')
def getAllDailyStats():
    return ResourceHandler().getAllDailyStats()

@app.route('/resources/dashboard/weekly/needs')
def getWeeklyNeedsStats():
    return WeeklyHandler().getWeeklyNeedsStats()

@app.route('/resources/dashboard/weekly/available')
def getWeeklyAvailableStats():
    return WeeklyHandler().getWeeklyAvailableStats()

@app.route('/resources/dashboard/weekly')
def getAllWeeklyStats():
    return WeeklyHandler().getAllWeeklyStats()

@app.route('/resources/dashboard/senate/needs')
def getSenateNeedsStats():
    return ResourceHandler().getSenateNeedsStats()

@app.route('/resources/dashboard/senate/available')
def getSenateAvailableStats():
    return ResourceHandler().getSenateAvailableStats()

@app.route('/resources/dashboard/senate')
def getAllSenateStats():
    return ResourceHandler().getAllSenateStats()


if __name__ == '__main__':
    app.run()