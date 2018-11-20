{
    'name': 'Copia MRP Validation',
    'version': '1.1',
    'author': 'Peter Mudoko',
    'website': 'http://www.mobilepower.com',
    'category': 'Manufacturing',
    'author': 'Peter Mudoko',
    'sequence': 20,
    'summary': 'Validation of Manufacturing Orders, Bill of BARMaterials',
    'depends': ['mrp'],
    'description': """
Validate Manufacturing
======================

Validate Manufacturing forcing Bill of Materials from accepting partial consumption, as follows:\n
* Force the use of whole number ratios on Bill of Materials (mrp.bom)\n
* Force the consumption and product of whole number quantities enforcing whole number ratios mentioned above, on Manufacturing Order (mrp.production)\n
    """,
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}