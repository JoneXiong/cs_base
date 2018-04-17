# coding=utf-8

from odoo import models, fields, api

class CsCroup(models.Model):
    _name = 'cs.group'
    _description = u'客服组'

    name = fields.Char(string='名称', required=True)
    state = fields.Selection([
        ('normal', '正常'),
        ('disable', ' 停用'),
        ], string=' 状态', default='normal')
    agent_ids = fields.Many2many('cs.agent', string='成员')


class Agent(models.Model):
    _name = 'cs.agent'
    _description = u'客服坐席'

    no = fields.Char(string=u'坐席工号')
    user_id = fields.Many2one('res.users', string=u'坐席用户')
    group_id = fields.Many2one('cs.group', string=u'所属客服组')
    remark = fields.Text(string='备注')

