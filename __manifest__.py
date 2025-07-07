{
    "name": "Monthly Report",
    "version": "1.1",
    "sequence": 10,
    "depends": [
        "web",
    ],
    "data": [
        "views/monthly_report_views.xml",
        "views/monthly_report_custom_report.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "application": True,
    "assets": {
        "web.report_assets_common": [
            "monthly_report/static/src/css/styles.css",
        ],
    },
    "license": "LGPL-3",
}
