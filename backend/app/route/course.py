from flask import Blueprint
from flask_restful import Api
from resource.course import CourseAPI, CourseListAPI,BulletinAPI, BulletinListAPI, BillingAPI, BillingListAPI, SoftskillAPI, SoftskillListAPI, GradeAPI, GradeListAPI


course_blueprint = Blueprint("course_api", __name__)
course_blueprint_api = Api(course_blueprint)

course_blueprint_api.add_resource(
    CourseAPI, "/courses/<string:course_id>"
)
course_blueprint_api.add_resource(
    CourseListAPI, "/courses"
)

course_blueprint_api.add_resource(
    BulletinAPI, "/bulletin/<string:bulletin_id>"
)
course_blueprint_api.add_resource(
    BulletinListAPI, "/bulletin"
)


course_blueprint_api.add_resource(
    BillingListAPI, "/billing"
)

course_blueprint_api.add_resource(
    BillingAPI, "/billing/<string:billing_id>"
)


course_blueprint_api.add_resource(
    SoftskillAPI, "/softskill/<string:softskill_id>"
)
course_blueprint_api.add_resource(
    SoftskillListAPI, "/softskill"
)


course_blueprint_api.add_resource(
    GradeAPI, "/grades/<string:grade_id>"
)
course_blueprint_api.add_resource(
    GradeListAPI, "/grades"
)

