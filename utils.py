#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import logging
import yaml
import re
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Singleton
class Log(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Log, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def getLogger(self):
        return self.logger
    
    def info(self, s):
        self.logger.info(s)

# Singleton
class Config(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        with open("config.yaml", "r") as ymlfile:
            self.config = yaml.safe_load(ymlfile)

    def get_config(self):
        return self.config

    def get_bot_token(self):
        if len(sys.argv) > 1:
            return sys.argv[1]
        elif self.config['TELEGRAM']['TOKEN']:
            return self.config['TELEGRAM']['TOKEN']
        else:
            raise Exception("No Bot-token provided. Use command-line arg or config.yaml")

# Singleton
class MyBot(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MyBot, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.storage = MemoryStorage()
        self.bot = Bot(token=Config().get_bot_token())
        self.dp = Dispatcher(self.bot, storage=self.storage)
        self.cnt = [1]

    def get_bot(self):
        return self.bot, self.dp

    def get_cnt(self):
        return self.cnt

    def set_cnt(self, cnt):
        cnt_list = [int(x) for x in re.findall(r'\d+', cnt)]
        if cnt_list:
            self.cnt = cnt_list
