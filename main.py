from fastapi import FastAPI, Query, Path, Body, Form
from fastapi.responses import Response, HTMLResponse, JSONResponse,  PlainTextResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index.html")


@app.post("/postdata")
def postdata(username = Form(), userage=Form()):
    return {"name": username, "age": userage}
