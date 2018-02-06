from django.db import models


class TwitterUser(models.Model):
    '''
     내가 a를 follow 함
     나는 a의 follower
     a는 나의 followee

    a와 내가 서로 follow함
        나와 a는 friend

     Block기능이 있어야 함
    '''

    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        # 관계에서 무언가를 가져와야하기 때문에 ,throuch로
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+'
    )

class Relation(models.Model):
    RELATION_TYPE_FOLLOWING = 'f'
    RELATION_TYPE_BLOCK = 'b'
    CHOICES_TYPE = (
        (RELATION_TYPE_FOLLOWING, '팔로잉'),
        (RELATION_TYPE_BLOCK, '차단'),
    )

    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)
