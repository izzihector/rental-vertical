# Part of rental-vertical See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Rental Timeline',
    'summary': 'Adds a timeline to products as well as a timeline view as overview of all rental products and orders',
    'description': '''
This module extends the sale_rental module to create and change the timeline objects
for the rented product instances automatically.
A complete timeline view will be generated for all rentable products.''',
    'version': '12.0.2.0.0',
    'category': 'sale',
    'author': 'Elego Software Solutions Gmbh',
    'depends': [
        'web_timeline',
        'rental_base',
        'rental_product_variant',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/product_timeline_view.xml',
        'views/product_view.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'application': True,
    'license': 'LGPL-3',
}
