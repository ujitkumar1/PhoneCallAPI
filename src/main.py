from call_report import call_report
from initiate_call import initiate_call
from src import app, api

api.add_resource(initiate_call, "/initiate-call")
api.add_resource(call_report, "/call-report/<int:phone>")

if __name__ == "__main__":
    app.run(debug=True)
