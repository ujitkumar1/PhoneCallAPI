from call_report import call_report
from initiate_call import initiate_call
from src import app, api, db

api.add_resource(initiate_call, "/initiate-call")
api.add_resource(call_report, "/call-report")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
