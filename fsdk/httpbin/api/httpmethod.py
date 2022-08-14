#!/usr/bin/env python
# -*- coding:utf-8 -*-

from spell.clients.http.models import HttpRequest, HttpMethod
from spell.clients.service import BaseRpcService


class HttpMethodService(BaseRpcService):
    base_url = "http://httpbin.org/"

    def get(self):
        req = HttpRequest(method="get", path="/get")
        return self.invoker.request(
            req
        )

    def delete(self):
        req = HttpRequest(method="delete", path="/delete")
        return self.invoker.request(
            req
        )

    def put(self):
        req = HttpRequest(method="put", path="/put")
        return self.invoker.request(
            req
        )

    def post(self):
        req = HttpRequest(method=HttpMethod.POST.value, path="/post")
        return self.invoker.request(
            req
        )
