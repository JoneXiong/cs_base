# coding=utf-8

{
    'name': 'CS Base',
    'version': '0.1',
    'category': 'Social Network',
    'summary': '客服系统基础模块',
    'description': """""",
    'author': 'Oejia',
    'website': 'http://www.oejia.cn/',
    'depends': ['web'],
    'data': [
        'views/base_views.xml',
        'views/res_partner_views.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
