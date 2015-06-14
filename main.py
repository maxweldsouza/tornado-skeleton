#!/usr/bin/env python
import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer
import mysqldbhelper
import os
import config

db = mysqldbhelper.DatabaseConnection(host='localhost',
        user='root',
        passwd='dttmw5d',
        db='new_scantuary')

class MainHandler(tornado.web.RequestHandler):
    def get(self, path):
        self.write('hello world')

settings = {
        'compress_response': True,
        'debug': config.debug
}

application = tornado.web.Application([
    (r"(.*)", MainHandler),
], ** settings)

if __name__ == "__main__":
    print 'Tornado Server running on Port:%s' % config.port
    if config.ssl:
        server = HTTPServer(application, ssl_options = {
            'certfile': os.path.join('ssl/localhost.crt'),
            'keyfile': os.path.join('ssl/localhost.key'),
            })
        server.listen(config.port)
    else:
        application.listen(config.port)
    tornado.ioloop.IOLoop.instance().start()
