STUDENT = 1
PROFESSOR = 2

class UserProfileModel(models.Model):

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (PROFESSOR, 'Professor'),
    ]

    role = models.SmallIntegerField(choices=ROLE_CHOICES,
        default=STUDENT)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s, %s)' % (self.user.username, self.user.last_name, \
            self.user.first_name)

    def get_role(self):
        return self.user.role
