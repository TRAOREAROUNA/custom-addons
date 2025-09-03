{
    "name":"Real Estate Ads",
    "version": "1.0",
    "website":"https://www.eroarta.com",
    "author": "Aroun",
     "description": """  
        Real Estate module to show available properties
     """,
    "category":"Sales",
    "depends":["base","mail"],
    "data": [
        "security/ir.model.access.csv",
        "security/res_groups.xml",
        "security/model_access.xml",
        "security/ir_rule.xml",

        "views/property_view.xml",
        "views/property_type_view.xml",
        "views/property_offer_view.xml",
        "views/property_tag_view.xml",
        "views/menuitems.xml",
        "views/property_web_template.xml",

        "data/estate.property.type.csv",
        "data/mail_template.xml",

        "report/report_template.xml",
        "report/property_report.xml",
    ],
    "demo":[
        "demo/property_tags.xml"
    ],
    "assets":{
        'web.assets_backend': [
            'real_estate_ads/static/src/js/my_custom_tag.js',
            'real_estate_ads/static/src/xml/my_custom_tag.xml',

        ]
    },
    "installable":True,
    "application": True,
    "license": "LGPL-3"
}