# -*- coding: utf-8 -*-

from odoo import models, fields, api


class post_message(models.Model):
    _inherit = 'sale.order'
    activate_message = fields.Boolean()

    def post_message(self):
        message="ESTA LISTO"
        self.activate_message = False
        if self.activate_message == False:
            self.message_post(body=message)
            self.activate_message =True
