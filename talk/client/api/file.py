# coding: utf-8
from __future__ import absolute_import, unicode_literals

from talk.client.api.base import TalkBaseAPI


class File(TalkBaseAPI):

    def delete(self, talk_params=None):
        """
        删除课件

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/deletefile', talk_params)
