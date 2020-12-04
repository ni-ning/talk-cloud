# coding: utf-8
from __future__ import absolute_import, unicode_literals

from talk.client.api.base import TalkBaseAPI


class Room(TalkBaseAPI):

    def entry(self, talk_params=None):
        """
        加入房间；直接进入房间（entry）

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/entry', talk_params)

    def create(self, talk_params=None):
        """
        创建房间

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/roomcreate', talk_params)

    def modify(self, talk_params=None):
        """
        修改房间

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/roommodify', talk_params)

    def delete(self, talk_params=None):
        """
        删除房间

        :param talk_params:
        :return:
        """
        return self._get('/WebAPI/roomdelete', talk_params)

    def get_room_by_time(self, talk_params=None):
        """
        得到某时间范围内的房间列表

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/getroombytime', talk_params)

    def get_room(self, talk_params=None):
        """
        得到某个房间的详细信息

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/getroom', talk_params)

    def get_room_list(self, talk_params=None):
        """
        得到房间列表

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/getroomlist', talk_params)

    def bind_file(self, talk_params=None):
        """
        房间关联课件

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/roombindfile', talk_params)

    def delete_file(self, talk_params=None):
        """
        取消房间关联文档

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/roomdeletefile', talk_params)

    def get_login_info(self, talk_params=None):
        """
        获取房间用户登入登出情况

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/getlogininfo', talk_params)

    def get_room_file(self, talk_params=None):
        """
        获取房间的文档列表

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/getroomfile', talk_params)

    def online_num(self, talk_params=None):
        """
        获取房间在线用户数

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/roomonlinenum', talk_params)

    def get_online_user(self, talk_params=None):
        """
        获取房间当前在线用户信息

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/getonlineuser', talk_params)

    def get_chat_list(self, talk_params=None):
        """
        获取房间内聊天记录

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/getchatlist', talk_params)

    def get_user_gift(self, talk_params=None):
        """
        获取用户礼物

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/getuserlist', talk_params)

    def get_live_login_info(self, talk_params=None):
        """
        大班课房间cdn推流用户登录登出情况

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/getLiveLogininfo', talk_params)

    def add_binding_classroom(self, talk_params=None):
        """
        绑定教室

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/addBindingClassroom', talk_params)

    def del_binding_classroom(self, talk_params=None):
        """
        解绑教室

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/delBindingClassroom', talk_params)

    def market_online_num(self, talk_params=None):
        """
        直播带货在线用户数

        :param talk_params: dict
        :return:
        """
        return self._get('/WebAPI/influencerMarketingOnlineNum', talk_params)






