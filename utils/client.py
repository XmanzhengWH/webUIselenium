# -*- coding: utf-8 -*-
"""
Python Httpclient for Sending http requests
"""
import os
import json
import requests


class HttpClient(object):
    def __init__(self,
                 host='localhost',
                 port=80,
                 ssl=False,
                 verify_ssl=False,
                 timeout=5,
                 ):
        """Construct a new HttpClient."""
        self._host = host
        self._port = port
        self._timeout = timeout


        self._verify_ssl = verify_ssl


        self._scheme = "http"


        if ssl is True:
            self._scheme = "https"


        self._baseurl = "{0}://{1}:{2}".format(
            self._scheme,
            self._host,
            self._port)


        self._headers = {
            'Content-type': 'application/json',
        }


    def request(self, url, method='GET', params=None, data=None, headers=None):
        url = "{0}{1}".format(self._baseurl, url)
        if headers is None:
            headers = self._headers


        if params is None:
            params = {}


        if isinstance(data, (dict, list)):
            data = json.dumps(data)


        for i in range(0, 3):
            try:
                response = requests.request(
                    method=method,
                    url=url,
                    params=params,
                    data=data,
                    headers=headers,
                    verify=self._verify_ssl,
                    timeout=self._timeout
                )
                break
            except requests.exceptions.ConnectionError as e:
                if i < 2:
                    continue
                else:
                    raise e


        return response




if __name__ == '__main__':
    client = HttpClient('www.baidu.com', 80)
    body = dict(
    )


    resp = client.request("/", method="GET", data=body, headers={"Content-Type":"application/json"})
    print
    resp.status_code
    print
    resp.content
