from datetime import datetime
from enum import Enum
from socket import gethostname
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel
from pydantic import Field


class AppLog(BaseModel):
    application_timestamp: datetime = Field(default_factory=datetime.now)
    document_id: str = Field(default_factory=lambda: str(uuid4()))
    log_message: str
    message: str = 'app_log'
    trace_id: str


class HTTPMethod(Enum):
    CONNECT = 'CONNECT'
    DELETE = 'DELETE'
    GET = 'GET'
    HEAD = 'HEAD'
    OPTIONS = 'OPTIONS'
    PATCH = 'PATCH'
    POST = 'POST'
    PUT = 'PUT'
    TRACE = 'TRACE'


class ServiceLog(BaseModel):
    application_timestamp: datetime = Field(default_factory=datetime.now)
    container_name: str = Field(default_factory=gethostname)
    error_code: Optional[str]
    error_message: Optional[str]
    http_method: Optional[HTTPMethod]
    http_status_code: Optional[int]
    input_data: Optional[str]
    message: str = 'service_log'
    method: str
    output_data: Optional[str]
    processing_time: Optional[float]
    request_headers: Optional[str]
    response_headers: Optional[str]
    sentry_id: Optional[str]
    service_name: str
    trace_id: str
