from django.db import models

# Create your models here.
class Building(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name



Choice_Field = [
    ('Single','single'),
    ('Double','double'),
]  

class Room_Type(models.Model):
    Room_Name = models.CharField(max_length=200, default='')
    Type = models.CharField(max_length=10, choices=Choice_Field, null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    
class Room(models.Model):
    Number = models.SmallIntegerField()
    room_type = models.ForeignKey(Room_Type, on_delete=models.CASCADE)
    price = models.FloatField(max_length=100)

   
# class Block_Day(models.Model):
#     start_date = models.DateField()
#     end_date = models.DateField()
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, default='')

#     def __str__(self):
#         return f"{self.start_date} - {self.end_date}"
    