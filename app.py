from dotenv import load_dotenv

import tornado.ioloop
import tornado.options
import tornado.web

import json
import logging
import os
import sys

logger = logging.getLogger(__name__)

tornado.options.define(
    "access_to_stdout", default=False, help="Log tornado.access to stdout"
)

load_dotenv()

TORNADO_PORT = int(os.getenv("TORNADO_PORT"))


class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

        self.set_header("Content-Type", "application/json")

    def get(self):
        logger.debug("MainHandler.get")
        logger.info("MainHandler.get")
        logger.warning("MainHandler.get")
        logger.error("MainHandler.get")

        self.write(json.dumps({"response": "Hello, world"}))

    def post(self):
        self.write(json.dumps({"response": "Hello, world"}))

    def options(self):
        self.set_status(204)
        self.finish()


def init_logging(access_to_stdout=False):
    if access_to_stdout:
        access_log = logging.getLogger("tornado.access")
        access_log.propagate = False
        # make sure access log is enabled even if error level is WARNING|ERROR
        access_log.setLevel(logging.INFO)
        stdout_handler = logging.StreamHandler(sys.stdout)
        access_log.addHandler(stdout_handler)


def bootstrap():
    tornado.options.parse_command_line(final=True)
    init_logging(tornado.options.options.access_to_stdout)


def make_app():
    urls = [(r"/", MainHandler)]
    return tornado.web.Application(urls)


def start_server():
    app = make_app()
    app.listen(TORNADO_PORT)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    bootstrap()
    start_server()
