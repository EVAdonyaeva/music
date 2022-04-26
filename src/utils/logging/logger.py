import decimal
import json
import logging
import uuid
from datetime import date
from datetime import datetime
from sys import stdout
from typing import Any
from typing import Dict

from pydantic import ValidationError

from .log_scheme import AppLog
from .log_scheme import ServiceLog


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args,
                **kwargs,
            )
        return cls._instances[cls]


class JsonStdOutLogger(metaclass=Singleton):
    def __init__(
            self,
            logger_name: str,
    ) -> None:
        self.logger = logging.getLogger(logger_name)

        self.logger.addHandler(logging.StreamHandler(stdout))

    def app_log(self, data: Dict[str, Any]) -> None:
        """
        Запись лога приложения в формате json
        :param data: Payload сообщения
        :return: None
        """
        if not isinstance(data, dict):
            logging.error(f'Logging data is {type(data)} - not a dictionary')
            return

        try:
            app_log: AppLog = AppLog(**data)
        except ValidationError as err:
            logging.error(str(err))
            return

        self.logger.info(app_log.json(by_alias=True, ensure_ascii=False))

    def service_log(self, data: Dict[str, Any]) -> None:
        """
        Запись лога запроса в формате json
        :param data: Payload сообщения
        :return: None
        """

        if not isinstance(data, dict):
            logging.error(f'Logging data is {type(data)} - not a dictionary')
            return

        try:
            service_log: ServiceLog = ServiceLog(**data)
        except ValidationError as err:
            logging.error(str(err))
            return

        self.logger.info(service_log.json(by_alias=True, ensure_ascii=False))

    @staticmethod
    def get_dump_data(data: Dict) -> str:
        def json_serial(obj):
            if isinstance(obj, (datetime, date)):
                return obj.isoformat()
            if isinstance(obj, uuid.UUID):
                return obj.hex
            if isinstance(obj, decimal.Decimal):
                return (str(o) for o in [obj])
            raise TypeError("Type %s not serializable" % type(obj))

        return json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2, default=json_serial,
                          iterable_as_array=True)
