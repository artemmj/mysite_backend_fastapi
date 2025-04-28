from fastapi import FastAPI
from fastapi.responses import Response, HTMLResponse, JSONResponse,  PlainTextResponse, FileResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/")
def root():
    return Response(content="<h1>=== Hello FastAPI! main page ===</h1>", media_type="text/html")

@app.get("/simple", response_class=PlainTextResponse)
def simple_reponse():
    return PlainTextResponse(content="=== simple text ===", media_type="text/plain")

@app.get("/html", response_class=HTMLResponse)
def simple_reponse():
    return HTMLResponse(content="<h1>=== html text ===</h1>")

@app.get("/file", response_class = FileResponse)
def about():
    return FileResponse(path="public/index.html")

@app.get("/json", response_class = JSONResponse)
def json():
    json_data = jsonable_encoder({"message": "success json response!"})
    return JSONResponse(content=json_data)
