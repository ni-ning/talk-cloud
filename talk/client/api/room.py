# coding: utf-8
from __future__ import absolute_import, unicode_literals

from talk.client.api.base import TalkBaseAPI


class Room(TalkBaseAPI):

    def create(self):

        return self._get(
            '/WebAPI/roomcreate',
            {
                'key': 'xxx',
                'roomname': 'xxx'
            }
        )
