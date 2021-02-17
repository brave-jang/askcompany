from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 자바의 toString()과 유사
    def __str__(self):
        return self.message

    
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자 수"


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=CASCADE) # post_id 필드 생성
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)