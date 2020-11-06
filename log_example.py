from sanic import Sanic
from sanic.log import logger
from sanic.response import text

app = Sanic('logging_example')

@app.route('/')
async def test(request):
    logger.info('Here is your log')
    return text('Hello Rere')

if __name__ == '__main__':
    app.run(debug=True,access_log=True,host='127.0.0.1',port='8000')