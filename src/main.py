from src import app,api,db
from initiate_call import initiate_call
from call_report import call_report

api.add_resource(initiate_call,"/initiate-call/<int:from_>/<int:to_>")
api.add_resource(call_report,"/call-report/<int:phone>")

if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)