import os
from pathlib import Path

from settings.initial_settings import LogParams


def create_necessary_catalogs():
    logs_catalog = Path().resolve().joinpath(LogParams.logs_catalog)
    if not os.path.exists(logs_catalog):
        os.makedirs(logs_catalog, mode=0o755, exist_ok=True)
