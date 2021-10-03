from Scripts.Forms import BookSystemForms


class BookModel(BookSystemForms.Model):
    Code = BookSystemForms.Column(BookSystemForms.Text(), unique=True)
    Name = BookSystemForms.Column(BookSystemForms.Text(), primary_key=True)
    Info = BookSystemForms.Column(BookSystemForms.Text(), nullable=True)
    Price = BookSystemForms.Column(BookSystemForms.Text(), nullable=True)

    def __init__(self):
        BookSystemForms.Model.__init__(self)

    @staticmethod
    def Create(InfoJson):
        Book = BookModel()
        Book.Code = InfoJson['Code']
        Book.Name = InfoJson['Name']
        Book.Info = InfoJson['Info']
        Book.Price = InfoJson['Price']
        return Book
