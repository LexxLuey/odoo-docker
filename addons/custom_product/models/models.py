from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    slug = fields.Char(string="Slug", compute="_compute_slug", store=True)
    additional_barcode = fields.Char(
        string="Additional Barcode", required=True, copy=False
    )

    @api.depends("name")
    def _compute_slug(self):
        for record in self:
            record.slug = record.name and record.name.replace(" ", "-").lower() or ""

    @api.constrains("additional_barcode")
    def _check_unique_additional_barcode(self):
        for record in self:
            if record.additional_barcode:
                existing_product = self.search(
                    [
                        ("additional_barcode", "=", record.additional_barcode),
                        ("id", "!=", record.id),
                    ]
                )
                if existing_product:
                    raise ValidationError(_("Additional barcode must be unique."))
