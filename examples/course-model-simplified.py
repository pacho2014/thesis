class CourseModel(models.Model):
    department = models.CharField(max_length=10) 
    number = models.CharField(max_length=10) 
    section = models.CharField(max_length=10) 
    title = models.CharField(max_length=100)