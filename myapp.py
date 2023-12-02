from typing import Union
import mysql.connector

from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount('/static', StaticFiles(directory='static', html=True), name='static')
@app.get("/")
def read_root1():
    return {"Hello":"World"}

database = "qldean"

try:
    conn = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password="",
        database=database
    )

    cursor = conn.cursor()

except Exception as e:
    print(f"Loi: {e}")

@app.get("/congviec")
def hello_world(request: Request):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM congviec")
    data = cursor.fetchall()
    cursor.close()
    return templates.TemplateResponse("congviec.html",{"request":request, "data":data})

@app.get("/dean")
def get_dean(request: Request):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dean")
    data = cursor.fetchall()
    cursor.close()
    return templates.TemplateResponse("dean.html",{"request": request, "data": data})

@app.get("/diadiem_phg")
def get_dean(request: Request):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diadiem_phg")
    data = cursor.fetchall()
    cursor.close()
    return templates.TemplateResponse("diadiem_phg.html",{"request": request, "data": data})

@app.get("/nhanvien")
def get_dean(request: Request):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nhanvien")
    data = cursor.fetchall()
    cursor.close()
    return templates.TemplateResponse("nhanvien.html",{"request": request, "data": data})

@app.get("/phancong")
def get_dean(request: Request):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phancong")
    data = cursor.fetchall()
    cursor.close()
    return templates.TemplateResponse("phancong.html",{"request": request, "data": data})

@app.get("/phongban")
def get_dean(request: Request):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phongban")
    data = cursor.fetchall()
    cursor.close()
    return templates.TemplateResponse("phongban.html",{"request": request, "data": data})

@app.get("/thannhan")
def get_dean(request: Request):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM thannhan")
    data = cursor.fetchall()
    cursor.close()
    return templates.TemplateResponse("thannhan.html",{"request": request, "data": data})





