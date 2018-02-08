from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


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
        # 관계에서 무언가를 가져와야하기 때문에 ,through로
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+'
    )

    class Meta:
        verbose_name_plural = 'symmetrical_intermediate - TwitterUser'

    def __str__(self):
        return self.name

    @property
    def block_user(self):
        pk_list = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_BLOCK).values_list('to_user', flat=True)

        return TwitterUser.objects.filter(pk__in=pk_list)

    @property
    def following(self):
        # 내가 from_user이며, type이 팔로잉인 Relation의 쿼리셋
        following_relations = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        # 위에서 정제한 쿼리셋에서 'to_user' 값만 리스트로 가져옴(내가 팔로잉하는 유저의 pk 리스트)
        following_pk_list = following_relations.values_list('to_user', flat=True)
        # TwitterUser테이블에서 pk가
        # 바로 윗줄에서 만든 follwing_pk_list(내가 팔로잉하는 유저의 pk 리스트)
        # 에 포함하는 User목록을 following_users변수로 할당
        following_users = TwitterUser.objects.filter(pk__in=following_pk_list)
        return following_users

    def follow(self, to_user):
        self.relations_by_from_user.filter(to_user=to_user).delete()

        self.relations_by_from_user.create(
            type=Relation.RELATION_TYPE_BLOCK,
            to_user=to_user,
        )

        # Relation.objects.create(
        #     from_user = self,
        #     to_user = to_user,
        #     type =  RELATION_TYPE_FOLLOWING
        # )

    def block(self, to_user):
        self.relations_by_from_user.filter(to_user=to_user).delete()

        self.relations_by_from_user.create(
        type = Relation.RELATION_TYPE_BLOCK,
        to_user = to_user, )


    def is_followee(self,to_user):
        '''
        내가 to_user를 follow하고 있는지 여부를 true/false로 반환
        :param to_user:
        :return:
        '''
        return self.following.filter(pk=to_user.pk).exists()

    def is_follower(self,from_user):
        return self.followers.filter(pk=from_user.pk).exists()

    @property
    def followers(self):
        pk_list = self.relations_by_to_user.filter(
            type = Relation.RELATION_TYPE_FOLLOWING).values_list('from_user', flat = True)
        return TwitterUser.objects.filter(pk__in=pk_list)


class Relation(models.Model):
    # 변수를 선언해서 사용하는 것이 좀 더 편리함. 나중에 기억하기 좋아서
    RELATION_TYPE_FOLLOWING = 'f'
    RELATION_TYPE_BLOCK = 'b'
    CHOICES_TYPE = (
        (RELATION_TYPE_FOLLOWING, '팔로잉'),
        (RELATION_TYPE_BLOCK, '차단'),
    )
    # 역참조하는 경우, 이름이 같기 때문에 역참조 이름이 필요함
    # 내가
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        #  자신이 from_user인인경우 Relations목록을 가져오고 싶은 경우
        related_name='relations_by_from_user'
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user'
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)
    # auto_now 업데이트 될때마다, auto_now_add 처음 불러왔을 때의 시간
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'symmetrical_intermediate - Relation'

        unique_together = (
            # from_user와 to_user의 값이 이미 있을 경우
            # DB에 중복 데이터 저장을 막음
            # EX) from_user가 1, to_user가 3인 데이터가 이미 있다면 두 항목의 값이
            # 모두 같은 또 다른 데이터가 존재 할 수 없음.
            ('from_user', 'to_user'),
        )
