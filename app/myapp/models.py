from django.db import models


# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # blank true의 경우, 글자색이 연하게 바뀜 (페이지에서)
    instrument = models.CharField(max_length=100, blank=True)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # blank-true의 경우, 에러가 뜬다. 데이터베이스에서 이를 허용안함
    # 빈값이 들어갈 수 있는 필드는 제약이 있음 - 텍스트
    # blank만 true로 하고, null - False가 뜬다.
    # blank는 from 상에서만, null 은 데이터베이스
    release_date = models.DateField(
        blank=True,
        null=True,
    )
    num_stars = models.IntegerField()


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1,
                                  choices=SHIRT_SIZES)

    def __str__(self):
        return '{name} (PK: {pk}, 셔츠 사이즈: {shirt_size}'.format(
            name=self.name,
            pk=self.pk,
            shirt_size=self.get_shirt_size_display(),
        )
