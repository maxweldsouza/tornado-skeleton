#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import mysqldbhelper
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
    application.listen(config.port)
    print 'Tornado Server running on Port:%s' % config.port
    tornado.ioloop.IOLoop.instance().start()
