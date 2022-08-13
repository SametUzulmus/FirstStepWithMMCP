from django.db import models

# Create your models here.

class Book(models.Model):

    name=models.CharField(max_length=100,verbose_name="Konu Başlığı") # verbose_name, databese içerisine tanımlanmış isim yerine 
    description=models.TextField(verbose_name="Açıklama") # bizim belirlediğimiz daha kullanışlı ismin görünmesine yarıyor.
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Eklenme Tarihi")
    isPublished=models.BooleanField(default=True)
    
    
    # database içerisinde kayıtlı olan bilgilerin, admin paneli içerisinde kendi adıyla görünmesi için,
    # str fonksiyonunu tanımlayıp, return self.name dedik
    def __str__(self):
        return self.name
