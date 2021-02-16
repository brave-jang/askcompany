from django.db import models


class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 자바의 toString()과 유사
    def __str__(self):
        return self.message

    
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자 수"