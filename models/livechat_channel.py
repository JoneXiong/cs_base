# coding=utf-8

import logging
import random


from openerp import models, fields, api

_logger = logging.getLogger(__name__)


class LivechatChannel(models.Model):

    _inherit = 'im_livechat.channel'

    group_ids = fields.Many2many('cs.group', string=u'客服组')

    def get_users(self, livechat_channel_id):
        channel = self.sudo().browse(livechat_channel_id)
        if channel.group_ids:
            agents = channel.group_ids.get_available_agents()
            users = [agent.user_id for agent in agents]
        else:
            users = self.sudo().browse(livechat_channel_id).get_available_users()
        return users

    @api.model
    def get_mail_channel(self, livechat_channel_id, anonymous_name):
        users = self.get_users(livechat_channel_id)
        if len(users) == 0:
            return False
        # choose the res.users operator and get its partner id
        user = self.choose_cs(users)
        return self._create_mail_channel(user, livechat_channel_id, anonymous_name)

    def _create_mail_channel(self, user, livechat_channel_id, anonymous_name):
        """
        CS定制化(开启了导航时直接调用此函数)
        """
        operator_partner_id = user.partner_id.id
        # partner to add to the mail.channel
        channel_partner_to_add = [(4, operator_partner_id)]
        if self.env.uid:  # if the user if logged (portal user), he can be identify
            channel_partner_to_add.append((4, self.env.user.partner_id.id))
        # create the session, and add the link with the given channel
        mail_channel = self.env["mail.channel"].with_context(mail_create_nosubscribe=False).sudo().create({
            'channel_partner_ids': channel_partner_to_add,
            'livechat_channel_id': livechat_channel_id,
            'anonymous_name': anonymous_name,
            'channel_type': 'livechat',
            'name': ', '.join([anonymous_name, user.name]),
            'public': 'private',
            'email_send': False,
        })
        return mail_channel.sudo().with_context(im_livechat_operator_partner_id=operator_partner_id).channel_info()[0]

    def choose_cs(self, users):
        user = random.choice(users)
        return user

    def replace_uuid_cs(self, uuid, user):
        mail_channel = self.env["mail.channel"].sudo().search([('uuid', '=', uuid)], limit=1)
        mail_channel.write({'channel_partner_ids': [(6,0,[user.partner_id.id])]})
