# coding=utf-8
import random

from odoo import models, fields, api

class CsCroup(models.Model):
    _name = 'cs.group'
    _description = u'客服组'
    _rec_name = 'name'

    name = fields.Char(string='名称', required=True)
    state = fields.Selection([
        ('normal', '正常'),
        ('disable', ' 停用'),
        ], string=' 状态', default='normal')
    agent_ids = fields.Many2many('cs.agent', relation='cs_agent_group_rel', string='坐席成员')

    @api.multi
    def get_available_agents(self):
        agents = []
        for group in self:
            agents += group.agent_ids
        agents = [agent for agent in agents if agent.status=='on']
        return agents

    @api.multi
    def choose_agent(self):
        available_agents = self.get_available_agents()
        if available_agents:
            return random.choice(available_agents)
        else:
            return None


class Agent(models.Model):
    _name = 'cs.agent'
    _description = u'客服坐席'
    _rec_name = 'no'

    no = fields.Char(string=u'坐席工号')
    user_id = fields.Many2one('res.users', string=u'坐席用户')
    group_ids = fields.Many2many('cs.group', relation='cs_agent_group_rel', string=u'所属客服组')
    remark = fields.Text(string='备注')
    status = fields.Selection([
        ('off', '离线'),
        ('on', '在线'),
        ], string=' 状态', default='off')

