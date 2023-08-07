from django.db import models

class Adverisments(models.Model):
    title = models.CharField("Название", max_length=128)
    descriptions = models.TextField("Название")
    price = models.DecimalField("Цена", max_digits=10, max_length=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Adverisments(id={self.id}, title={self.title}, price={self.price})"
    
    class Meta:
        db_table = "adverisments"