from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

QUESTIONS = {
    '1': {'question': 'How do we do XY?', 'answers': {'1': 'We do it like that...', '2': 'lalala ...'}},
    '2': {'question': 'Where to find XY?', 'answers': {'3': 'It is found here and there'}},
    '3': {'question': 'On which time is XY?', 'answers': {'4': 'Abount XY'}},
}


def abort_if_question_doesnt_exist(question_id):
    if question_id not in QUESTIONS:
        abort(404, message="Question {} doesn't exist".format(question_id))

parser = reqparse.RequestParser()
parser.add_argument('question', type=str)

# TODO move to resources as own file
# Question
#   show a single question item and lets you delete them
class Question(Resource):
    def get(self, question_id):
        abort_if_question_doesnt_exist(question_id)
        return QUESTIONS[question_id]

    def delete(self, question_id):
        abort_if_question_doesnt_exist(question_id)
        del QUESTIONS[question_id]
        return '', 204

    def put(self, question_id):
        args = parser.parse_args()
        task = {'question': args['question']}
        QUESTIONS[question_id] = question
        return task, 201


# TODO move to resources as own file
# QuestionList
#   shows a list of all questions, and lets you POST to add new questions
class QuestionList(Resource):
    def get(self):
        return QUESTIONS

    def post(self):
        args = parser.parse_args()
        question_id = 'question%d' % (len(QUESTIONS) + 1)
        QUESTIONS[question_id] = {'question': args['question']}
        return QUESTIONS[question_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(QuestionList, '/questions')
api.add_resource(Question, '/questions/<string:question_id>')


if __name__ == '__main__':
    app.run(debug=True)