import fastapi
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "This is the backend for address-fyp"}

from app.api.address import *
from app.api.countries import *
from app.api.regions import *
from app.api.charts import *
from app.api.email_notifications import *
from app.api.analytics import *
from app.api.npl import *
from app.api.finance import *
from app.api.market_segment import *
from app.api.onemap_region_summary import *
