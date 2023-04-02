from django.db import models



# Create your models here.
class Resume(models.Model):
    resume_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone_number= models.IntegerField(max_length=200)
    image=models.ImageField(upload_to='media/',max_length=200)
    linked_in=models.CharField(max_length=200)
    github=models.CharField(max_length=200)


    def __str__(self):
        return str(self.resume_id)

class Institution(models.Model):
    resume_id= models.ForeignKey(Resume, on_delete=models.CASCADE)
    inst_name= models.CharField(max_length=200)
    result= models.FloatField(max_length=200)

    def __str__(self):
        return str(self.resume_id)


class Skill(models.Model):
    resume_id= models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=200)
    skill_level= models.IntegerField(max_length=200)

    def __str__(self):
        return str(self.resume_id)

class Experience(models.Model):
    resume_id= models.ForeignKey(Resume, on_delete=models.CASCADE)
    company= models.CharField(max_length=200)
    position= models.CharField(max_length=200)
    years= models.IntegerField(max_length=200)

    def __str__(self):
        return str(self.resume_id)