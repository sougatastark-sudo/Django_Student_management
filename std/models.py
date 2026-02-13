from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Students(models.Model):
    roll = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^[0-9]{10}$', 'Phone must be 10 digits')]
    )

    def __str__(self):
        return f"{self.name} ({self.roll})"


class Fees(models.Model):
    student = models.OneToOneField(
        Students,
        on_delete=models.CASCADE,
        related_name="fees"
    )
    total_fees = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.paid_amount > self.total_fees:
            raise ValidationError("Paid amount cannot exceed total fees")

    @property
    def due_amount(self):
        return self.total_fees - self.paid_amount

    def __str__(self):
        return f"{self.student.name} Fees"