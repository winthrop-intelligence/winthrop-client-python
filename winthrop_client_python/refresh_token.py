import json
import subprocess
import threading
import time
from typing import Optional, List, Dict, Any
from urllib.parse import urlencode
import urllib3

from winthrop_client_python.exceptions import UnauthorizedException


class WinthropClient:
    class RefreshToken:
        _token_cache: Dict[str, Dict[str, Any]] = {}
        _cache_lock = threading.Lock()

        TOKEN_GRANT_TYPE = "client_credentials"
        CONTENT_TYPE = "application/x-www-form-urlencoded"

        client_id: Optional[str] = None
        client_secret: Optional[str] = None
        host: Optional[str] = None

        @classmethod
        def access_token(cls, scopes: Optional[List[str]] = None) -> str:
            cache_key = cls._get_cache_key(scopes)

            with cls._cache_lock:
                cached_token = cls._token_cache.get(cache_key)

                if cached_token is None or time.time() >= cached_token["expires_at"]:
                    cls._generate_access_token(scopes)

                return cls._token_cache[cache_key]["token"]

        @classmethod
        def _get_cache_key(cls, scopes: Optional[List[str]] = None) -> str:
            if scopes is None:
                return "no_scopes"
            if len(scopes) == 0:
                return "empty_scopes"
            return ",".join(sorted(scopes))

        @classmethod
        def _generate_access_token(cls, scopes: Optional[List[str]] = None) -> None:
            response = cls._make_request(scopes)
            cls._handle_response(response, scopes)

        @classmethod
        def _make_request(
            cls, scopes: Optional[List[str]] = None
        ) -> urllib3.BaseHTTPResponse:
            http = urllib3.PoolManager()
            headers = {"Content-Type": cls.CONTENT_TYPE}
            data = cls._token_params(scopes)
            encoded_data = urlencode(data)

            if cls.host is None:
                raise ValueError("host must be set before requesting a token")

            response = http.request(
                "POST", cls.host, headers=headers, body=encoded_data
            )
            return response

        @classmethod
        def _token_params(cls, scopes: Optional[List[str]] = None) -> Dict[str, str]:
            params = {
                "grant_type": cls.TOKEN_GRANT_TYPE,
                "client_id": cls.client_id or "",
                "client_secret": cls.client_secret or "",
            }
            if scopes:
                params["scope"] = " ".join(scopes)
            return params

        @classmethod
        def _handle_response(
            cls,
            response: urllib3.BaseHTTPResponse,
            scopes: Optional[List[str]] = None,
        ) -> None:
            if response.status == 200:
                parsed_response = json.loads(response.data.decode("utf-8"))
                cache_key = cls._get_cache_key(scopes)
                cls._token_cache[cache_key] = {
                    "token": parsed_response["access_token"],
                    "expires_at": time.time() + int(parsed_response["expires_in"])
                }
            else:
                response_data = response.data.decode("utf-8")
                raise Exception(
                    "Failed to retrieve access token: "
                    f"{response.status} - {response_data}"
                )

    class DeviceToken:
        _token_cache: Dict[str, str] = {}
        _cache_lock = threading.Lock()

        cli_executable = "winthrop"
        timeout = 10

        MISSING_CLI_MESSAGE = (
            "Winthrop CLI is not installed. Install it and run `winthrop login`."
        )

        @classmethod
        def access_token(cls, scopes: Optional[List[str]] = None) -> str:
            cache_key = cls._get_cache_key(scopes)

            with cls._cache_lock:
                cached_token = cls._token_cache.get(cache_key)
                if cached_token is None:
                    cached_token = cls._generate_access_token()
                    cls._token_cache[cache_key] = cached_token

                return cached_token

        @classmethod
        def refresh_access_token(cls, scopes: Optional[List[str]] = None) -> str:
            cache_key = cls._get_cache_key(scopes)

            with cls._cache_lock:
                token = cls._generate_access_token()
                cls._token_cache[cache_key] = token
                return token

        @classmethod
        def clear_cache(cls) -> None:
            with cls._cache_lock:
                cls._token_cache = {}

        @classmethod
        def has_cached_token(cls, token: Optional[str]) -> bool:
            if token is None:
                return False

            with cls._cache_lock:
                return token in cls._token_cache.values()

        @classmethod
        def _get_cache_key(cls, scopes: Optional[List[str]] = None) -> str:
            if scopes is None:
                return "no_scopes"
            if len(scopes) == 0:
                return "empty_scopes"
            return ",".join(sorted(scopes))

        @classmethod
        def _generate_access_token(cls) -> str:
            try:
                result = subprocess.run(
                    [cls.cli_executable, "token"],
                    capture_output=True,
                    text=True,
                    timeout=cls.timeout,
                    check=False,
                )
            except FileNotFoundError:
                raise UnauthorizedException(reason=cls.MISSING_CLI_MESSAGE)
            except subprocess.TimeoutExpired:
                raise UnauthorizedException(
                    reason="Timed out waiting for Winthrop CLI token command."
            )

            if result.returncode != 0:
                stderr = (result.stderr or "").strip()
                if stderr:
                    raise UnauthorizedException(reason=stderr)
                raise UnauthorizedException(
                    reason=(
                        "Winthrop CLI token command failed with exit code "
                        f"{result.returncode}."
                    )
                )

            token = (result.stdout or "").strip()
            if not token:
                raise UnauthorizedException(
                    reason="Winthrop CLI returned a blank access token."
                )

            return token
