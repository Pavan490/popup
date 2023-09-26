from django.db import models
from datetime import datetime
class Customer(models.Model):
    TicketNumber=models.IntegerField()
    Customer=models.CharField(max_length=100)
    CustomerAddress=models.CharField(max_length=200)
    CustomerContactNumber=models.IntegerField()
    DateOfService=models.DateTimeField(default=datetime.now)
    TechnicianName=models.CharField(max_length=100)
    JobDescription=models.TextField()
    
    def __int__(self):
        return self.TicketNumber
