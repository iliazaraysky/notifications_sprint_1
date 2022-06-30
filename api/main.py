import aiohttp
import uvicorn
from db import mongodb
from motor.motor_asyncio import AsyncIOMotorClient
from api.v1 import rabbitmq_api, user_event_api
from fastapi import FastAPI, Response, Request
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


# Проверяет Auth сервис. Обращается по адресу.
# Если в заголовке есть валидный токен, предоставляет доступ к контенту
@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    headers = request.headers
    auth_url = 'http://notifications-flask-auth-service:5000/auth/v1/usercheck'
    auth_check = await check_user(auth_url, dict(headers))

    if auth_check.status == 200:
        response = await call_next(request)
        return response
    return Response(status_code=401)


async def check_user(url, headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            return response

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8001)
