import os

import uvicorn

from api.api import create_app
from api.hendlers.demo import router

app = create_app()
# Router
app.include_router(router)
