# coding=utf-8

{
    'name': 'CS',
    'version': '0.1',
    'category': 'Social Network',
    'summary': '客服系统基础实现,客服组、坐席、Web聊天接入',
    'description': """""",
    'author': 'Oejia',
    'website': 'http://www.oejia.cn/',
    'depends': ['web', 'im_livechat', 'oejia_wx'],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',

        #'views/assets.xml',
        'views/parent_menus.xml',
        #'views/dashboard.xml',
        'views/res_partner_views.xml',
        'views/cs_group_views.xml',
        'views/cs_agent_views.xml',
        'views/im_livechat_channel_views.xml',
        #'views/im_livechat_report_channel_views.xml',
        #'views/im_livechat_report_operator_views.xml',
        #'views/mail_channel_views.xml',
        #'views/mail_shortcode_views.xml',
        #'views/rating_rating_views.xml',

        #'views/other_inherit.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
