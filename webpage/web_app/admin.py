from django.contrib import admin
from web_app.models import  Student_profile,Hobby_details,Course_page,Exam_detail,Branch_detail,Degree_detail
from web_app.models import subcoursepage
# Register your models here.
#admin.site.register(Student_profile)
#admin.site.register(Hobby_details)
admin.site.register(Course_page)
admin.site.register(Exam_detail)
admin.site.register(Branch_detail)
admin.site.register(Degree_detail)
admin.site.register(subcoursepage)
