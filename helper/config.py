#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("4784291", cast=int)
    API_HASH = config("be87fe0a2f987e72f45f7392b9cd3b9d")
    BOT_TOKEN = config("1888088287:AAHFaEAzwtPfK7Q1Fl0PTO8UzkUIZYYKhl0")
    OWNER = config("1601731267", default=1322549723, cast=int)
    LOG = config("-1001417655828", cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
