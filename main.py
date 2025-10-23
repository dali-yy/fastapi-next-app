import argparse

from fastapi import FastAPI
import uvicorn

from app.api.main import api_router


app = FastAPI()

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000, help="端口号")
    args = parser.parse_args()
    uvicorn.run("main:app", host="0.0.0.0", port=args.port, workers=1, reload=True)
