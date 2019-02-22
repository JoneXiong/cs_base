# coding=utf-8

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    agent_ids = fields.One2many('cs.agent', 'user_id', '关联的坐席')

    def is_available(self):
        if self.agent_ids:
            agent = self.agent_ids[0]
            if agent.status=='off':
                return False
        return self.im_status=="online"
