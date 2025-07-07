from odoo import models, fields


class Report(models.Model):
    _name = "monthly_report.report"
    _description = "Report Table"

    name = fields.Char(string="Name", required=True)

    def action_open_monthly_report_preview(self):
        self.ensure_one()
        report_url = "/report/pdf/monthly_report.report_monthly_report_custom_document/%s" % (self.id)
        return {
            "type": "ir.actions.act_url",
            "url": report_url,
            "target": "new",
        }