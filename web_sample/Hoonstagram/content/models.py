from django.db import models

# Create your models here.

class Feed(models.Model):
    content = models.TextField() # 글 내용 // DB를 만들때 해당 필드에 어떤 형식으로 넣을지 지정을 해주는 것 그게 텍스트 필드임!
    image = models.TextField()  # 피드 이미지
    profile_image = models.TextField() # 프로필 이미지
    user_id = models.TextField() # 글쓴이
    like_count = models.IntegerField() # 좋아요 수 
