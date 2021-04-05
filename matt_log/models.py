from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField()             # UserのID（社員番号など）
    name = models.CharField(max_length = 50)    # Userの氏名
    mail = models.EmailField()                  # Userの電子メールアドレス

    def __str__(self):
        return "{}: {}".format(self.pk, self.name)

class Matt(models.Model):
    matt_id = models.IntegerField()                  # S_mattの識別ID
    name = models.CharField(max_length = 100)   # S_mattの識別名称（任意）

    def __str__(self):
        return self.name

class Log_data(models.Model):
    s_matt_id = models.ForeignKey(Matt, related_name='log_datas', on_delete=models.SET_NULL, null=True)  # データ送信元S_mattの識別ID
    created_at = models.DateTimeField(auto_now_add=True)    # 測定日時（測定値を受信した日時）
    weight = models.FloatField()                # 測定した重量
    quantity = models.IntegerField()            # S_matt側で算出した数量（個数、容量など）

    def __str__(self):
        created_date = self.created_at.isoformat(" ",timespec='seconds')
        return "{}: {}  {:.2f}g  {}個".format(self.s_matt_id, created_date, self.weight, self.quantity)
