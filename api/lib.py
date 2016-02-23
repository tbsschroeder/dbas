# Common library for API Component
#
# @author Christian Meter, Tobias Krauthoff
# @email {meter, krauthoff}@cs.uni-duesseldorf.de

import json
import logging

from webob import Response, exc


def logger():
	"""
	Create a logger
	:return:
	"""
	log = logging.getLogger()
	log.setLevel(logging.DEBUG)
	return log


class response401(exc.HTTPError):
	"""
	Return a 401 HTTP Error message if user is not authenticated
	:return:
	"""
	def __init__(self, msg='Unauthorized'):
		body = {'status': 401, 'message': msg}
		Response.__init__(self, json.dumps(body))
		self.status = 401
		self.content_type = 'application/json'