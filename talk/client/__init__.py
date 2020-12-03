# coding: utf-8
from __future__ import absolute_import, unicode_literals

import logging

from talk.client.base import BaseClient
from talk.client import api

logger = logging.getLogger(__name__)


class TalkClient(BaseClient):

    room = api.Room()

    def __init__(self, *args, **kwargs):
        super(TalkClient, self).__init__(*args, **kwargs)
