def validate_instructor(val):
    user = User.objects.get(pk=val)
    p = get_object_or_404(UserProfileModel, user=user)
    if p.role != PROFESSOR:
        raise ValidationError(
            'User %s is not a professor' % user
        )

class CourseModel(models.Model):
    department = models.CharField(max_length=10) 
    number = models.CharField(max_length=10) 
    section = models.CharField(max_length=10) 
    title = models.CharField(max_length=100)
    repo_name = models.CharField(max_length=100, null=True)

    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
        validators=[validate_instructor])
    students = models.ManyToManyField(User, blank=True, related_name='student')
    TAs = models.ManyToManyField(User, blank=True, related_name='ta')

    YEAR_CHOICES = []
    for r in range(datetime.now().year, datetime.now().year + 5):
        YEAR_CHOICES.append((r,r))

    year = models.IntegerField(choices=YEAR_CHOICES,
        default=datetime.now().year)
    
    SEMESTER_CHOICES = [
        ('FALL', 'FALL'),
        ('WINTER', 'WINTER'),
        ('INT', 'INT')
    ]
    semester = models.CharField(choices=SEMESTER_CHOICES,
         default=SEMESTER_CHOICES[0], max_length=50)

    start_time = models.DateField(default=timezone.now)
    end_time = models.DateField(default=timezone.now)

    visible_after_end = models.BooleanField(default=False)

    @property
    def markers(self):
        return self.TAs.all()


    class Meta:
        unique_together = \
            ('department', 'number', 'section', 'year', 'semester')

