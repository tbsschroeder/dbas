"""
Introducing websockets.

.. codeauthor:: Tobias Krauthoff <krauthoff@cs.uni-duesseldorf.de
"""

import json
import dbas.helper.issue_helper as IssueHelper

from cornice import Service

from dbas.logger import logger
from graph.lib import get_sigma_data, get_d3_data

# =============================================================================
# SERVICES - Define services for several actions of DBAS
# =============================================================================

sigma_graph = Service(name='sigma',
                      path='/sigma',
                      description="Sigma Dump")

# =============================================================================
# WEBSOCKET REQUESTS
# =============================================================================


@sigma_graph.get()
def get_sigma_dump(request):
    logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
    logger('Graph', 'sigma', 'main')
    issue = IssueHelper.get_issue_id(request)

    return_dict = get_sigma_data(issue)
    return json.dumps(return_dict, True)