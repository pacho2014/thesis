class CourseView(AbstractLoginRequiredView):
    template = 'course_summary.html'

    def get(self, request):
        course = self.get_course(request)
        cont = {
            'course': course,
        }

        return render(request, self.template, cont)