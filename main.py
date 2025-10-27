import argparse

from fastapi import FastAPI, Path
from fastapi.staticfiles import StaticFiles
import uvicorn

from app.api.main import api_router


app = FastAPI()

# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(api_router, prefix="/api")

# 3. 挂载 Next.js 静态资源（_next, CSS, JS, 图片等）
app.mount("/_next", StaticFiles(directory="static/_next"), name="_next")

# 4. 可选：挂载其他静态资源根路径（如 favicon, robots.txt）
app.mount("/", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000, help="端口号")
    args = parser.parse_args()
    uvicorn.run("main:app", host="0.0.0.0", port=args.port, workers=1, reload=True)
