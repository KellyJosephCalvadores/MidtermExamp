from flask import Flask, jsonify, request
app = Flask(__name__)

hearts = [
]

@app.route('/HeartRecord', methods = ['POST'])
def addHeartRecord():
    NHR = request.get_json() #New Heart Record
    hearts.append(NHR)
    return "Successful added.", 200

@app.route('/HeartRecord', methods = ['GET'])
def getHeartRecord():
    return jsonify(hearts)

@app.route('/HeartRecord/<int:index>', methods = ['GET'])
def getHeartRecordSpecific(index):
    return jsonify(hearts[index]), 200

@app.route('/HeartRecord/<int:index>', methods = ['PUT'])
def updateHeartRecord(index):
    UHR = request.get_json() #Update Heart Request
    hearts[index] = UHR
    return jsonify(hearts[index]), 200

@app.route('/HeartRecord/<int:index>', methods = ['DELETE']) 
def deleteHeartRecordSpecific(index):
    hearts.pop(index)
    return "The records is deleted succesfully.", 200

if __name__ == "__main__":
    app.run()