from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Geospacial(http.Controller):

    @http.route('/get_delivery', type='json', auth='user')
    def get_delivery_partner(self):
        print("Yes here entered")
        deliveries = request.env['stock.picking'].search([('state', '=', 'assigned'),('picking_type_id.name', '=', 'Livraisons')])
        delivery = []
        for rec in deliveries:
            vals = {
                'id': rec.id,
                'partner_name': rec.partner_id.name,
                'latitude': rec.partner_id.partner_latitude,
                'longitude': rec.partner_id.partner_longitude,
            }
            delivery.append(vals)
        print("Patient List--->", delivery)
        data = {'status': 200, 'response': delivery, 'message': 'Done All Patients Returned'}
        return data

    # Sample Controller Created
    @http.route('/update_partner', type='json', auth='user')
    def update_patient(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                print("rec...", rec)
                delivery_man = request.env['res.partner'].sudo().search([('id', '=', rec['id'])])
                if delivery_man:
                    delivery_man.sudo().write(rec)
                    args = {'success': True, 'message': 'coordinates Updated'}
                else:
                    args = {'success': True, 'message': 'no recorde Updated'}
        return args
