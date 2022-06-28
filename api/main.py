import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


app = FastAPI(
    title='Notifications API',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.get('/')
async def root():
    return {'message': 'Hello world'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8001)