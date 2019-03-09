{
    'name': 'TDS Report',
    'summary': 'TDS Report',
    'category': 'account',
    'version': '1.0',
    'description': """Print and Send your Sales Order by Post""",
    'depends': ['base', 'tds_calculation','account'],
    'website': 'http://www.prixgen.com',
    'data': ['report/report_template.xml', 'wizard/tds_date.xml', 'views/addcin.xml'],
    'auto_install': False,
    'application': True,
}