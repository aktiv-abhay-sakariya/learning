# -*- coding: utf-8 -*-
# Part of Aktiv software. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class BookCategory(models.Model):
    _name = 'book.category'
    _description = "Categories"

    category_name = fields.Char(string = 'Category Name', required = True)
    parent_categ_id = fields.Many2one(comodel_name = "book.category", string = "Parent Category")
