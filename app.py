from flask import Flask
from flask_restful import Api, Resource
from KahootClass import Kahoot

app = Flask(__name__)
api = Api(app)

def check_kahoot_validity(dat):
    if not dat.data: return False
    return True

class GetData(Resource):
    def get(self, uuid):
        try:
            if check_kahoot_validity(Kahoot(uuid)): return Kahoot(uuid).data
            else: return {"kahoot_api": "Enter a valid uuid."}
        except Exception as err:
            return {"kahoot_api": "Error " + err}

class GetQuizDetails(Resource):
    def get(self, uuid):
        try:
            if check_kahoot_validity(Kahoot(uuid)): return Kahoot(uuid).get_quiz_details()
            else: return {"kahoot_api": "Enter a valid uuid."}
        except Exception as err:
            return {"kahoot_api": "Error " + err}

class GetQuestions(Resource):
    def get(self, uuid):
        try:
            if check_kahoot_validity(Kahoot(uuid)): return Kahoot(uuid).get_questions()
            else: return {"kahoot_api": "Enter a valid uuid."}
        except Exception as err:
            return {"kahoot_api": "Error " + err}

class GetQuestionNames(Resource):
    def get(self, uuid):
        try:
            if check_kahoot_validity(Kahoot(uuid)): return Kahoot(uuid).get_question_names()
            else: return {"kahoot_api": "Enter a valid uuid."}
        except Exception as err:
            return {"kahoot_api": "Error " + err}

class GetQuizLength(Resource):
    def get(self, uuid):
        try:
            if check_kahoot_validity(Kahoot(uuid)): return Kahoot(uuid).get_quiz_length()
            else: return {"kahoot_api": "Enter a valid uuid."}
        except Exception as err:
            return {"kahoot_api": "Error " + err}

class GetQuestionDetails(Resource):
    def get(self, uuid, question):
        try:
            if check_kahoot_validity(Kahoot(uuid)): return Kahoot(uuid).get_question_details(question)
            else: return {"kahoot_api": "Enter a valid uuid."}
        except Exception as err:
            return {"kahoot_api": "Error " + err}

class GetAnswer(Resource):
    def get(self, uuid, question):
        try:
            if check_kahoot_validity(Kahoot(uuid)): return Kahoot(uuid).get_answer(question)
            else: return {"kahoot_api": "Enter a valid uuid."}
        except Exception as err:
            return {"kahoot_api": "Error " + err}


api.add_resource(GetData, "/<string:uuid>/get-data")
api.add_resource(GetQuizDetails, "/<string:uuid>/get-question-details")
api.add_resource(GetQuestions, "/<string:uuid>/get-questions")
api.add_resource(GetQuestionNames, "/<string:uuid>/get-question-names")
api.add_resource(GetQuizLength, "/<string:uuid>/get-quiz-length")
api.add_resource(GetQuestionDetails, "/<string:uuid>/get-question-details/<int:question>")
api.add_resource(GetAnswer, "/<string:uuid>/get-answer/<int:question>")

if __name__ == "__main__":
    app.run(debug=False)