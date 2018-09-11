class Assignment(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)

    assignment_number = models.CharField(max_length=15, default='')
    title = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    num_of_problems = models.SmallIntegerField(default=1)
    total_grade = models.IntegerField(default=100)
    due = models.DateTimeField(auto_now_add=True, null=True)
    is_released = models.BooleanField(default=False)

    created_time = models.DateTimeField(auto_now_add=True, null=True)
    modified_time = models.DateTimeField(auto_now=True)

    use_git = models.BooleanField(default=False)
    auto_run = models.BooleanField(default=False)
    ci_files_dir = models.CharField(max_length=200, null=True)
    scripts_dir = models.CharField(max_length=200, null=True)

    attachment_path = models.FilePathField(default='')

    class Meta:
        unique_together = (
            'course',
            'assignment_number'
        )

class MarkerAssignment(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    problem = models.SmallIntegerField(default=1)
    marker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    @property
    def marker_name(self):
        if self.marker:
            return '%s %s' % (self.marker.first_name, self.marker.last_name)
        return None

    class Meta:
        unique_together = (
            'assignment',
            'problem'
        )

class AssignmentAttachment(models.Model):
    assignment  = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    file_name   = models.CharField(max_length=50, default='')
    file_type   = models.CharField(max_length=50, default='no_avail')

    def save(self, *args, **kwargs):
        full_path = '%s/%s' % (self.assignment.attachment_path, self.file_name)
        f_type = magic.from_file(full_path)

        if 'text' in f_type:
            self.file_type = 'text'
        elif 'PDF' in f_type:
            self.file_type = 'pdf'
        else:
            self.file_type = 'no_avail'

        super(AssignmentAttachment, self).save()


@receiver(pre_delete, sender=AssignmentAttachment)
def delete_attachment_file(sender, instance, **kwargs):
    fs = FileSystemStorage(instance.assignment.attachment_path)
    if fs.exists(instance.file_name):
        fs.delete(instance.file_name)
