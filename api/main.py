import uvicorn
from db import mongodb
from motor.motor_asyncio import AsyncIOMotorClient
from api.v1 import rabbitmq_api, user_event_api
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


app = FastAPI(
    title='Notifications API',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    mongodb.mongo = AsyncIOMotorClient('mongodb://notifications-mongo-fastapi:27017')


@app.on_event('shutdown')
async def shutdown():
    await mongodb.mongo.stop()


app.include_router(rabbitmq_api.router, prefix='/api/v1/rabbitmq', tags=['rabbitmq_event'])
app.include_router(user_event_api.router, prefix='/api/v1/films', tags=['user_event'])


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8001)
