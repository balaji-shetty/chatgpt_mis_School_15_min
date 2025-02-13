from django.contrib import admin
from .models import SchoolClass, Subject, Teacher, ExamPattern, Student, Enrollment, FeeType, Fee, Exam, Result

class BaseAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

class SchoolClassAdmin(BaseAdmin):
    list_display = ('name', 'division', 'created', 'updated', 'user')
    search_fields = ('name', 'division')
    ordering = ('name',)

class SubjectAdmin(BaseAdmin):
    list_display = ('name', 'school_class', 'created', 'updated', 'user')
    search_fields = ('name',)
    ordering = ('name',)

class TeacherAdmin(BaseAdmin):
    list_display = ('name', 'created', 'updated', 'user')
    search_fields = ('name',)
    ordering = ('name',)

class ExamPatternAdmin(BaseAdmin):
    list_display = ('name', 'total_marks', 'created', 'updated', 'user')
    search_fields = ('name',)
    ordering = ('name',)

class StudentAdmin(BaseAdmin):
    list_display = ('name', 'school_class', 'created', 'updated', 'user')
    search_fields = ('name',)
    ordering = ('name',)

class EnrollmentAdmin(BaseAdmin):
    list_display = ('student', 'school_class', 'created', 'updated', 'user')
    search_fields = ('student__name', 'school_class__name')
    ordering = ('student',)

class FeeTypeAdmin(BaseAdmin):
    list_display = ('name', 'created', 'updated', 'user')
    search_fields = ('name',)
    ordering = ('name',)

class FeeAdmin(BaseAdmin):
    list_display = ('student', 'fee_type', 'amount', 'created', 'updated', 'user')
    search_fields = ('student__name', 'fee_type__name')
    ordering = ('student',)

class ExamAdmin(BaseAdmin):
    list_display = ('school_class', 'subject', 'exam_pattern', 'created', 'updated', 'user')
    search_fields = ('subject__name', 'exam_pattern__name')
    ordering = ('school_class',)

class ResultAdmin(BaseAdmin):
    list_display = ('student', 'exam', 'marks_obtained', 'created', 'updated', 'user')
    search_fields = ('student__name', 'exam__subject__name')
    ordering = ('student',)

admin.site.register(SchoolClass, SchoolClassAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(ExamPattern, ExamPatternAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(FeeType, FeeTypeAdmin)
admin.site.register(Fee, FeeAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Result, ResultAdmin)
