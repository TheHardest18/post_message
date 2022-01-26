# -*- coding: utf-8 -*-
# from odoo import http


# class PostMessage(http.Controller):
#     @http.route('/post_message/post_message/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/post_message/post_message/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('post_message.listing', {
#             'root': '/post_message/post_message',
#             'objects': http.request.env['post_message.post_message'].search([]),
#         })

#     @http.route('/post_message/post_message/objects/<model("post_message.post_message"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('post_message.object', {
#             'object': obj
#         })
