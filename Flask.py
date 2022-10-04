from flask import Flask, jsonify, request
app = Flask(__name__)

glucose_inf =[
    {
        "glucose_id" : "0001",
        "glucose" : "99 mg/dL",
        "date" : "2029-01-01"
    },
    {
        "glucose_id" : "0002",
        "glucose" : "120 mg/dL",
        "date" : "2021-03-26"
    }
]


@app.route('/insert', methods=['POST','GET'])
def insert():
    data = request.get_json()
    if data:
        glucose_inf.append(data)
    return "Glucose Information Added Successfully!"


@app.route('/display', methods=['GET'])
def display():
    return jsonify(glucose_inf)


@app.route('/view/<int:index>', methods=['GET'])
def view(index):
    return jsonify(glucose_inf[index])

@app.route('/edit/<int:index>', methods=['PUT', 'GET'])
def edit(index):
    newData = request.get_json()
    glucose_inf[index] = newData
    return 'Glucose Information Updated Successfully', 200

@app.route('/delete/<int:index>', methods=['DELETE'])
def delete(index):
    glucose_inf.pop(index)
    return 'Glucose information Deleted Successfully', 200

if __name__ == '__main__':
    app.run()