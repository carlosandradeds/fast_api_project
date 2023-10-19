from fastapi import FastAPI, APIRouter

from views import user_router, assets_router
from view_sync import sync_router

from database.init_db import create_database


app = FastAPI()
router = APIRouter()

@router.get('/')
def first():
    return 'Hello World'

app.include_router(prefix='/first', router=router)
app.include_router(user_router)
app.include_router(assets_router)
app.include_router(sync_router)

# Define a startup event handler to initialize the database
@app.on_event("startup")
async def startup_event():
    # Initialize the database when the application starts
    await create_database()
