from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self')

    def __str__(self):
        # friends_string = ''
        # for friend in self.friends.all():
        #     friends_string += friend.name
        #     friends_string += ','
        # friends_string = friends_string[:-2]

        # list comprehension 사용
        friends_string = ','.join([friend.name for friend in self.friends.all()])

        # Manager의 values_list 를 사용
        # DB에서 모든 freinds의 name필드 값만 가져옴
        friends_string = ','.join(self.friends.values_list('name', flat=True))

        return '{name} (친구:{friends})'.format(
            name = self.name,
            friends = friends_string,
        )
