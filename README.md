# Sample DroneDeploy App Server

A sample Tornado server for working in concert with a DroneDeploy app.

You can proxy geocode requests to the Google Maps API by querying the geocode endpoint of this server.

For example, https://your-sample-dronedeploy-app-server.herokuapp.com/geocode/?address=474+bryant+st,san+francisco,CA
would query Google Maps with the given address, and return the response as JSON.

Your Google Maps API key should be set in the environment variable API_KEY before running the server.

See http://developer.dronedeploy.com for more information
