# coding=utf-8

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    agent_ids = fields.One2many('cs.agent', 'user_id', '关联的坐席')
