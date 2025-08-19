from dataclasses import dataclass


@dataclass(frozen=True)
class AppParams:
    app: str = "main:app"
    host: str = "0.0.0.0"
    port: int = 8155
    reload: bool = True
    workers: int = 1


@dataclass(frozen=True)
class UserParams:
    start_balance: int = 10


@dataclass(frozen=True)
class LogParams:
    loglevel: int = 10
    log_max_size: int = 10
    log_file_mode: str = "w"
    backup_count: int = 10
    logs_catalog: str = "logs"
    logs_encoding: str = "utf-8"
