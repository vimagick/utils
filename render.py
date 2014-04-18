#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libmproxy.flow import Response
from netlib.odict import ODictCaseless
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

def start(ctx, argv):

    global ff
    profile = FirefoxProfile()
    profile.set_preference('permissions.default.stylesheet', 2)
    profile.set_preference('permissions.default.image', 2)
    profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    ff = webdriver.Firefox(profile)
    #ff = webdriver.PhantomJS()

def done(ctx):

    global ff
    ff.quit()

def request(ctx, flow):

    url = flow.request.get_url()
    ff.get(url)
    src = ff.page_source.encode('utf-8')
    res = Response(flow.request, [1,1], 200, 'OK',
        ODictCaseless([['Content-Type', 'text/html; charset=utf-8']]), src, None)
    flow.request.reply(res)
