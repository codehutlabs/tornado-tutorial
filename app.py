import tornado.ioloop
import tornado.web

import json
import os

from dotenv import load_dotenv
load_dotenv()

from tornado.log import enable_pretty_logging, app_log
enable_pretty_logging()


TORNADO_PORT = int(os.getenv("TORNADO_PORT"))


class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def get(self):
        self.write(json.dumps({"response": "Hello, world"}))


def make_app():
    return tornado.web.Application([(r"/", MainHandler)])


if __name__ == "__main__":
    app_log.info(f"Starting Tornado app on port {TORNADO_PORT}.")
    app = make_app()
    app.listen(TORNADO_PORT)
    tornado.ioloop.IOLoop.current().start()
