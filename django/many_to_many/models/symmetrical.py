from django.db import models

__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    name = models.CharField(max_length=50)
    following = models.ManyToManyField(
        'self',
        # 1번에서 2번 친구 2번에서 1번 친구는 자동이 아님 false
        symmetrical=False,
        # 역참조시 사용할 이름
        related_name= 'followers',
    )

    def __str__(self):
        return self.name

    def followers(self):
        # 자신을 following하고 있는 사람들을 출력
        return self.followers.all()

