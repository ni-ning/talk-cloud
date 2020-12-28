# coding: utf-8

import inspect
import json
import logging
import requests
import six
from six.moves.urllib.parse import urljoin

from talk.client.api.base import TalkBaseAPI
from talk.core.exceptions import TalkClientException
from talk.core.utils import json_loads

logger = logging.getLogger(__name__)


def _is_api_endpoint(obj):
    return isinstance(obj, TalkBaseAPI)


class BaseClient(object):

    _http = requests.Session()

    API_BASE_URL = 'http://global.talk-cloud.net'

    def __new__(cls, *args, **kwargs):
        self = super(BaseClient, cls).__new__(cls)
        api_endpoints = inspect.getmembers(self, _is_api_endpoint)
        for name, api in api_endpoints:
            api_cls = type(api)
            api = api_cls(self)
            setattr(self, name, api)
        return self

    def __init__(self, timeout=None, auto_retry=True):
        self.timeout = timeout
        self.auto_retry = auto_retry

    @staticmethod
    def parse_talk_params(url, params):
        if not isinstance(params, dict):
            return url
        ret = ['%s/%s' % (key, value) for key, value in params.items()]
        return urljoin(url, '/'.join(ret))

    def _request(self, method, url_or_endpoint, **kwargs):
        if not url_or_endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            url = urljoin(api_base_url, url_or_endpoint)
        else:
            url = url_or_endpoint
        if 'params' not in kwargs:
            kwargs['params'] = {}

        # 拓课云传递参数比较特别 /key1/value1/key2/value2/
        talk_params = kwargs.pop('talk_params') or {}
        url = self.parse_talk_params(url, talk_params)

        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(kwargs['data'], ensure_ascii=False)
            body = body.encode('utf-8')
            kwargs['data'] = body
            if 'headers' not in kwargs:
                kwargs['headers'] = {}
            kwargs['headers']['Content-Type'] = 'application/json'

        kwargs['timeout'] = kwargs.get('timeout', self.timeout)

        res = self._http.request(
            method=method,
            url=url,
            **kwargs
        )
        try:
            res.raise_for_status()
        except requests.RequestException as exc:
            logger.error('\n【请求地址】:%s\n【请求参数】: %s\n%s\n【异常信息】: %s',
                         url, kwargs.get('params', ''), kwargs.get('data', ''), exc)
            raise TalkClientException(
                errcode=None,
                errmsg=None,
                request=exc.request,
                response=exc.response
            )

        result = self._handle_result(res)

        logger.debug("\n【请求地址】: %s\n【请求参数】：%s \n%s\n【响应数据】：%s",
                     url, kwargs.get('params', ''), kwargs.get('data', ''), result)
        return result

    @staticmethod
    def _decode_result(res):
        try:
            result = json_loads(res.content.decode('utf-8', 'ignore'), strict=False)
        except (TypeError, ValueError):
            # Return origin response object if we can not decode it as JSON
            logger.debug('Can not decode response as JSON', exc_info=True)
            return res
        return result

    def _handle_result(self, res):
        result = self._decode_result(res)
        return result

    def _handle_request_except(self, e, func, *args, **kwargs):
        raise e

    def request(self, method, uri, **kwargs):
        try:
            return self._request(method, uri, **kwargs)
        except TalkClientException as exc:
            return self._handle_request_except(exc, self.request, method, uri, **kwargs)

    def get(self, uri, talk_params=None,  params=None, **kwargs):
        """
        get 接口请求

        :param uri: 请求url
        :param talk_params: get 参数（dict 格式）拓课云专用
        :param params: get 参数（dict 格式）
        """
        if params is not None:
            kwargs['params'] = params
        if talk_params is not None:
            kwargs['talk_params'] = talk_params

        return self.request('GET', uri, **kwargs)

