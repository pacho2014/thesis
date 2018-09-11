class AutoRunConfig(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    problem = models.SmallIntegerField(default=1)

    enable = models.BooleanField(default=False)

    build_stage = models.BooleanField(default=False)
    run_stage = models.BooleanField(default=False)

    compile_command = models.TextField(default='')

    class Meta:
        unique_together = (
            'assignment',
            'problem'
        )

class AutoRunTestCase(models.Model):
    config = models.ForeignKey(AutoRunConfig, on_delete=models.CASCADE)

    prog_name = models.CharField(max_length=256, default='')
    argv = models.CharField(max_length=256, default='')

    empty_input = models.BooleanField(default=False)
    display_input = models.BooleanField(default=False)
    sample_input = models.TextField(default='')

    strict_comparison = models.BooleanField(default=False)
    display_output = models.BooleanField(default=False)
    empty_output = models.BooleanField(default=False)
    sample_output = models.TextField(default='')

    time_limit = models.SmallIntegerField(default=1)
    prog_return = models.SmallIntegerField(default=0,
        choices=(
            (-1, 'no_check'),
            (0,  'success'),
            (1,  'failure')
        )
    )
