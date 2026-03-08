from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


# Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Before Request -> Method: {request.method}, Path: {request.url.path}")

    response = await call_next(request)

    print("After Response Returned")

    return response


# /hello endpoint
@app.get("/hello")
def hello():
    return {
        "message": "Hello, Welcome to FastAPI!"
    }


# Custom 404 Exception Handler
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "message": "The requested resource was not found"
        }
    )