from datetime import datetime, timedelta

from odoo import fields, http
from odoo.exceptions import AccessError
from odoo.http import request
from odoo import release

class WebSettingsDashboard(http.Controller):

    @http.route('/cs_base_dashboard/data', type='json', auth='user')
    def cs_base_dashboard_data(self, **kw):
        ret = {}
        if request.env.user.agent_ids:
            agent = request.env.user.agent_ids[0]
            ret['agent'] = {
                'no': agent.no,
                'mobile': request.env.user.mobile,
                'groups': ','.join([g.name for g in agent.group_ids]),
            }
        return ret
