import logging
import os
from http.server import HTTPServer

from dotenv import load_dotenv

from src.server import MyServer


def main() -> None:
    load_dotenv()
    log_level = os.getenv("log_level")
    logging.basicConfig(level=log_level)

    host = os.getenv("host")
    port = int(os.getenv("port"))

    my_server = HTTPServer((host, port), MyServer)
    logging.info("Server started http://%s:%s" % (host, port))

    try:
        my_server.serve_forever()
    except KeyboardInterrupt:
        pass

    my_server.server_close()
    logging.info("Server stopped.")


if __name__ == "__main__":
    main()
