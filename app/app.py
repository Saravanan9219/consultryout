from pymemcache.client.base import Client
from flask import Flask, Response, request


app = Flask(__name__)
cache = Client(('memcached.service.consul', 11211))


@app.route('/get')
def get_value():
    key = request.args.get('key')
    return Response(cache.get(key), mimetype='text/plain')


@app.route('/set')
def set_value():
    key = request.args.get('key')
    value = request.args.get('value')
    cache.set(key, value)
    return Response('OK', mimetype='text/plain')
