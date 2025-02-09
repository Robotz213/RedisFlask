"""Module to create a simple extension for Flask | Quart."""

from abc import ABC
from typing import TYPE_CHECKING, Any  # noqa: D104

from redis import Redis as RedisBase  # type: ignore # noqa: I001, PGH003

if TYPE_CHECKING:
    try:
        from flask import Flask  # type: ignore # noqa: F401, I001, PGH003
    except ImportError:
        try:
            from quart import Quart  # type: ignore # noqa: F401, I001, PGH003

        except ImportError:
            raise ImportError("You need to install Flask or Quart to use this library.") from None


class BaseFlaskRedis(RedisBase, ABC):
    """Base of  Redis_Alchemy."""


class Redis(BaseFlaskRedis):
    """A simple extension for Flask | Quart."""

    url_redis = ""

    @property
    def redis_url(self) -> str:
        """Property to get the Redis URL.

        Returns:
            str: Redis URL.

        """
        return self.url_redis

    @redis_url.setter
    def redis_url(self, new_url: str) -> None:
        self.url_redis = new_url

    def __init__(self, app: Any = None) -> None:  # noqa: ANN401
        """Initialize the Redis extension."""
        self.redis_client = None
        if app:
            self.init_app(app)

    def init_app(self, app: Any) -> None:  # noqa: ANN401
        """
        Configure the redis extension.

        Args:
            app (Flask | Quart): Application default (Flask | Quart).

        """
        # Obter configurações individuais
        redis_params = {
            "host": app.config.get("REDIS_HOST", "localhost"),
            "port": int(app.config.get("REDIS_PORT", 6379)),
            "db": int(app.config.get("REDIS_DB", 0)),
            "password": app.config.get("REDIS_PASSWORD"),
            "socket_timeout": app.config.get("REDIS_SOCKET_TIMEOUT"),
            "socket_connect_timeout": app.config.get("REDIS_SOCKET_CONNECT_TIMEOUT"),
            "socket_keepalive": app.config.get("REDIS_SOCKET_KEEPALIVE"),
            "socket_keepalive_options": app.config.get("REDIS_SOCKET_KEEPALIVE_OPTIONS"),
            "retry_on_timeout": app.config.get("REDIS_RETRY_ON_TIMEOUT", False),
            "encoding": app.config.get("REDIS_ENCODING", "utf-8"),
            "decode_responses": app.config.get("REDIS_DECODE_RESPONSES", True),
            "ssl": app.config.get("REDIS_SSL", False),
            "ssl_keyfile": app.config.get("REDIS_SSL_KEYFILE"),
            "ssl_certfile": app.config.get("REDIS_SSL_CERTFILE"),
            "ssl_ca_certs": app.config.get("REDIS_SSL_CA_CERTS"),
            "ssl_check_hostname": app.config.get("REDIS_SSL_CHECK_HOSTNAME"),
            "health_check_interval": app.config.get("REDIS_HEALTH_CHECK_INTERVAL"),
        }

        # Obter URL se fornecida
        redis_url = app.config.get("REDIS_URL")
        if redis_url:
            self.redis_client = RedisBase.from_url(
                redis_url, **{k: v for k, v in redis_params.items() if v is not None}
            )
        else:
            self.redis_client = RedisBase(**{k: v for k, v in redis_params.items() if v is not None})

        # Adicionar a extensão ao app
        app.extensions["redis"] = self

    def __getattr__(self, name: str) -> Any:  # noqa: ANN401
        """Get attribute of the Redis client."""
        return getattr(self.redis_client, name)
