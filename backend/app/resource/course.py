from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

import helper.validator as validator
from model.course import Course, User, Bulletin, Billing, Softskill, Grade
from helper.schema import CourseSchema, BulletinSchema, BillingSchema, SoftskillSchema, GradeSchema

class CourseListAPI(Resource):
    @jwt_required()
    def get(self):
        courses = Course.objects()
        serialized_payload = CourseSchema(many=True).dump(courses)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_course()
        course = Course(**serialized_payload)
        course.save()
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200

class CourseAPI(Resource):
    @jwt_required()
    def get(self, course_id):
        course = Course.objects.get(id=course_id)
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, course_id):
        course = Course.objects.get(id=course_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_course()
        for key, value in serialized_payload.items():
            setattr(course, key, value)
        course.save()
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, course_id):        
        course = Course.objects.get(id=course_id)
        course.delete()
        app.logger.info("Course with id %s deleted", course_id)
        msg={"message": "Course: {} deleted".format(course_id)}
        return msg, 200
    
class BulletinListAPI(Resource):
    @jwt_required()
    def get(self):
        bulletin = Bulletin.objects()
        serialized_payload = BulletinSchema(many=True).dump(bulletin)
        return serialized_payload, 200
    
    def post(self):
        serialized_payload = validator.bulletin_validator()
        bulletin = Bulletin(**serialized_payload)
        bulletin.save()
        serialized_payload = BulletinSchema().dump(bulletin)
        return serialized_payload, 200

class BulletinAPI(Resource):
    @jwt_required()
    def get(self, bulletin_id):
        app.logger.info("bulletin id: {}".format(bulletin_id))
        bulletin = Bulletin.objects.get(id=bulletin_id)
        serialized_payload = BulletinSchema().dump(bulletin)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, bulletin_id):
        bulletin = Bulletin.objects.get(id=bulletin_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.bulletin_validator()
        for key, value in serialized_payload.items():
            setattr(bulletin, key, value)
        bulletin.save()
        serialized_payload = BulletinSchema().dump(bulletin)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, bulletin_id):        
        bulletin = Bulletin.objects.get(id=bulletin_id)
        bulletin.delete()
        app.logger.info("Bulletin with id %s deleted", bulletin_id)
        msg={"message": "Bulletin: {} deleted".format(bulletin_id)}
        return msg, 200
    


class BillingListAPI(Resource):
    @jwt_required()
    def get(self):
        billing = Billing.objects()
        serialized_payload = BillingSchema(many=True).dump(billing)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_billing()
        billing = Billing(**serialized_payload)
        billing.save()
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200

class BillingAPI(Resource):
    @jwt_required()
    def get(self, billing_id):
        app.logger.info("billing id: {}".format(billing_id))
        billing = Billing.objects.get(id=billing_id)
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, billing_id):
        billing = Billing.objects.get(id=billing_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_billing()
        for key, value in serialized_payload.items():
            setattr(billing, key, value)
        billing.save()
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, billing_id):        
        billing = Billing.objects.get(id=billing_id)
        billing.delete()
        app.logger.info("Billing with id %s deleted", billing_id)
        msg={"message": "Billing: {} deleted".format(billing_id)}
        return msg, 200
    
    
class SoftskillListAPI(Resource):
    @jwt_required()
    def get(self):
        softskill = Softskill.objects()
        serialized_payload = SoftskillSchema(many=True).dump(softskill)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_softskill()
        softskill = Softskill(**serialized_payload)
        softskill.save()
        serialized_payload = SoftskillSchema().dump(softskill)
        return serialized_payload, 200

class SoftskillAPI(Resource):
    @jwt_required()
    def get(self, softskill_id):
        app.logger.info("softskill id: {}".format(softskill_id))
        softskill = Softskill.objects.get(id=softskill_id)
        serialized_payload = SoftskillSchema().dump(softskill)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, softskill_id):
        softskill = Softskill.objects.get(id=softskill_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_softskill()
        for key, value in serialized_payload.items():
            setattr(softskill, key, value)
        softskill.save()
        serialized_payload = SoftskillSchema().dump(softskill)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, softskill_id):        
        softskill = Softskill.objects.get(id=softskill_id)
        softskill.delete()
        app.logger.info("Softskill with id %s deleted", softskill_id)
        msg={"message": "Softskill: {} deleted".format(softskill_id)}
        return msg, 200


class GradeListAPI(Resource):
    @jwt_required()
    def get(self):
        grades = Grade.objects()
        serialized_payload = GradeSchema(many=True).dump(grades)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_grade()
        grade = Grade(**serialized_payload)
        grade.save()
        serialized_payload = GradeSchema().dump(grade)
        return serialized_payload, 200


class GradeAPI(Resource):
    @jwt_required()
    def get(self, grade_id):
        app.logger.info("grade id: {}".format(grade_id))
        grade = Grade.objects.get(id=grade_id)
        serialized_payload = GradeSchema().dump(grade)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, grade_id):
        grade = Grade.objects.get(id=grade_id)
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        serialized_payload = validator.add_grade()
        for key, value in serialized_payload.items():
            setattr(grade, key, value)
        grade.user = user  # Update the user reference
        grade.save()
        serialized_payload = GradeSchema().dump(grade)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, grade_id):        
        grade = Grade.objects.get(id=grade_id)
        grade.delete()
        app.logger.info("Grade with id %s deleted", grade_id)
        msg={"message": "Grade: {} deleted".format(grade_id)}
        return msg, 200




        

            