from flask import Flask,request,json
from http import HTTPStatus
# print(__name__)   #__main__
app=Flask(__name__)

"""
In memory database
this ;ist gets back to its original value
what ever we add this will be detele once,when the server is restarted
"""

""" details=[
    {'name':'varnika',
      'education':'btech'
    },
    {'name':'charan',
      'education':'intermediate'
    }
] 
"""
details=[]
def add_id(projects):
    if projects:
        return projects[-1]["id"]+1
    return 1


@app.route("/",methods=["GET"])
#@app.route("/home",method=['GET']) https://127.0.0.1:5000/home
def home():
    return details
 
@app.route("/project/<int:id>",methods=["GET"])
def get_project_id(id):
    # returning the details of person based on id
    for i in details:
        if(i["id"]==id):
            return i
    else:
        return "False"
    

@app.route("/project/<int:id>/<int:update_id>",methods=["PUT"])
def update_project_id(id,update_id):
    # updating id of the person 
    for i in details:
        if(i["id"]==id):
            i['id']=update_id
            return details
    else:
        return False

@app.route("/update/<int:id>",methods=["PUT"])
def update_details(id):
    data=request.get_json()
    for i in details:
        if(i["id"]==id):
            i["Name"]=data["Name"]
            i["id"]=id
            i["age"]=data["age"]
            return details
    else:
        return "NOT FOUND"
@app.route("/add",methods=['post'])
def add_details():
    #Adding the values to the Details list
    data=request.get_json()
    data["id"]=add_id(details)
    details.append(data)
    #HTTPSTATUS.Ok
    return details
@app.route("/delete/<int:id>",methods=["DELETE"])
def delete(id):
    for i in details:
        if(i["id"]==id):
            details.remove(i)
            return "Removed"
    else:
        return "Not found related details"
if __name__=='__main__':
    app.run(debug=True)