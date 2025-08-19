import uvicorn
from fastapi import FastAPI, Depends

from app.api.endpoints.transfers import transfer_router
from app.api.endpoints.user import user_router
from settings.initial_settings import AppParams
from settings.logging_settings import configure_logger
from fake_db.user_db import get_user_manager
from fake_db.transfer_db import get_transfer_manager
from app.utils import create_necessary_catalogs

app = FastAPI(dependencies=[Depends(get_user_manager),
                            Depends(get_transfer_manager),
                            ],
              )

app.include_router(transfer_router)
app.include_router(user_router)


if __name__ == "__main__":
    create_necessary_catalogs()
    logger = configure_logger(__name__)
    logger.info(f"Starting app with {AppParams}")

    uvicorn.run(AppParams.app,
                host=AppParams.host,
                port=AppParams.port,
                reload=AppParams.reload,
                workers=AppParams.workers,
                )
