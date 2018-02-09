from django.db import models


# Create your models here.
class Piece(models.Model):
    pass


class Article(Piece):
    article_piece = models.OneToOneField(
        Piece,
        on_delete=models.CASCADE,
        # 상속받아서 자동으로 생기는 테이블을 명시적으로
        # 만들어주는 것을 의미한다.

        parent_link=True,
    )


class Book(Piece):
    book_piece = models.OneToOneField(
        Piece,
        on_delete=models.CASCADE,
        parent_link=True,
    )


class BookReview(Book, Article):
    pass
