from sanic import Sanic
from sanic.response import json

app = Sanic('Json_example')
@app.route("/json")

def post_json(request):
    return json({"received": True,"message": request.json })

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8000')