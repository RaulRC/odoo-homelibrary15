from odoo import fields, models


class Homelibrary(models.Model):
    _name = 'homelibrary.homelibrary'
    _description = "Biblioteca"
    owner = fields.Many2one('res.users', string='Propietario')
    name = fields.Char(required=True, string='Nombre')


class Book(models.Model):
    _name = 'homelibrary.book'
    _description = "Libros para la biblioteca"
    name = fields.Char(required=True, string='Título')
    description = fields.Text(string='Descripción adicional')
    rack_id = fields.Many2one('homelibrary.rack', string='Estantería')
    author_id = fields.Many2one('homelibrary.author', string='Autor')


class Rack(models.Model):
    _name = 'homelibrary.rack'
    _description = "Estantería"

    def count_books(self):
        self.number_books = len(self.book_ids)
        return True

    name = fields.Char(required=True, string='Nombre de la estantería')
    book_ids = fields.One2many('homelibrary.book', 'rack_id', string='Libros en estantería')
    number_books = fields.Integer(compute='count_books', string='Total libros en estantería')


class Author(models.Model):
    _name = 'homelibrary.author'
    _description = "Autor"

    def count_books(self):
        self.number_books = len(self.book_ids)
        return True

    name = fields.Char(required=True, string='Nombre')
    book_ids = fields.One2many('homelibrary.book', 'author_id', string='Libros del autor')
    number_books = fields.Integer(compute='count_books', string='Total libros autor')


class Video(models.Model):
    _name = 'homelibrary.video'
    _description = "Vídeos para la biblioteca"
    name = fields.Char(required=True, string='Título')
    description = fields.Text(string='Descripción adicional')
    rack_id = fields.Many2one('homelibrary.rack', string='Estantería')
