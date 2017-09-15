from flask import Flask, jsonify, abort, make_response
# from getTerm import getTerm


api = Flask(__name__)


@api.route('/getTerm/<string:keyword>', methods=['GET'])
def get_term(keyword):
    try:
        questions, answers = getTerm(keyword)
    except Exception as e:
        print(e)
        abort(404)

    return make_response(jsonify([questions, answers]))


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


if __name__ == '__main__':
    api.run(host='127.0.0.1', port=8083)
