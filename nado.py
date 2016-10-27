import os

import requests
import tornado.ioloop
import tornado.web


GEOCODE_FMT = 'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}'


class GeocodeHandler(tornado.web.RequestHandler):
    """Proxy a call to the Google Maps geocode API"""

    def set_default_headers(self):
        # allow cross-origin requests to be made from your app on DroneDeploy to your web server
        self.set_header("Access-Control-Allow-Origin", "https://www.dronedeploy.com")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        # add more allowed methods when adding more handlers (POST, PUT, etc.)
        self.set_header("Access-Control-Allow-Methods", "GET, OPTIONS")

    def get(self):
        api_key = os.environ.get("API_KEY")
        address = self.get_query_argument("address")
        url = GEOCODE_FMT.format(address=address, key=api_key)

        # fetch results of the geocode from Google
        response = requests.get(url)

        # send the results back to the client
        self.write(response.content)

    def options(self):
        # no body
        self.set_status(204)
        self.finish()


def main():
    application = tornado.web.Application([
        (r"/geocode/", GeocodeHandler)
    ])
    port = int(os.environ.get("PORT", 5000))
    application.listen(port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
