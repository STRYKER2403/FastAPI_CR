from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
app = FastAPI()


conn = MongoClient("mongodb+srv://Swapnil:swapnilss@fapicluster.yicv7ee.mongodb.net")


