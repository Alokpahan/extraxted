#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7887601981:AAHVDCBa32jWJUwsDoabpT5DJvjgKmAbY-k")
    API_ID = int(os.environ.get("API_ID", "21243428"))
    API_HASH = os.environ.get("API_HASH", "4a1a5ce2583952ae6734b46941c77b38")
    AUTH_USERS = "1411895712"

