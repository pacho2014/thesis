class Commit(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    problem = models.SmallIntegerField(default=1)
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=200, null=True)
    commit_time = models.DateTimeField(null=True)
    commit_id = models.CharField(max_length=200, null=True)
    auto_run_status = models.CharField(max_length=100, default='pending')

    grade = models.IntegerField(null=True)
    marked_by = models.ForeignKey(User, null=True,
        on_delete=models.SET_NULL, related_name='marker')
    marked_time = models.DateTimeField(null=True)
    marker_comments = models.TextField(null=True)

    class Meta:
        unique_together = (
            'assignment',
            'problem',
            'by'
        )

class CommitFile(models.Model):
    commit      = models.ForeignKey(Commit, on_delete=models.CASCADE)
    file_name   = models.CharField(max_length=50, default='')
    file_type   = models.CharField(max_length=50, default='no_avail')
