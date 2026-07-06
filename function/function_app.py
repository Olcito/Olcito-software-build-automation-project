import azure.functions as func
import datetime
import json

app = func.FunctionApp()


@app.route(route="GetServerTime", auth_level=func.AuthLevel.ANONYMOUS)
def GetServerTime(req: func.HttpRequest) -> func.HttpResponse:

    response = {
        "message": "Hello from Azure Function!",
        "student": "Olcayto Koruk",
        "course": "Software Build Automation Tools",
        "status": "Success",
        "server_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return func.HttpResponse(
        json.dumps(response),
        mimetype="application/json",
        status_code=200
    )