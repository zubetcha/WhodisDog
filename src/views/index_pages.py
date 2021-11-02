from flask import Blueprint, render_template, request, jsonify

index_pages = Blueprint('index_pages', __name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@index_pages.route("/")
def index():
    return render_template("index.html")

# # pet - POST
# @index_pages.route('/posting', method=['POST'])
# def pet_upload():
#     image = request.form['image']
#     pet_name = request.form['pet_name']
#     pet_age = request.form['pet_age']
#     pet_species = request.form['pet_species']
#     pet_intro = request.form['pet_intro']
#
#     doc = {
#         'image': image,
#         'pet_name': pet_name,
#         'pet_age': pet_age,
#         'pet_species': pet_species,
#         'pet_intro': pet_intro
#     }
#
#     db.collection.insert_one(doc)
#
#     return jsonify({'msg': '완료되었어요! 얼른 확인하러 가볼까요?'})
#
# # # pet - GET
# # @index_pages.route('/posting', method=['GET'])
# # def pet_print()
# #
# #
# like - POST
@index_pages.route('/like', methods=['POST'])
def like_click():
    user_name_receive = request.form['user_name_give']
    like_users_receive = request.form['like_users_give']

    target_user = db.pet_board.find_one({'user_name': user_name_receive})
    curren_like = target_user['like_count']
    new_like = curren_like + 1

    doc = {
        'user_name': user_name_receive,
        'like_count': new_like,
        'like_users': like_users_receive
    }

    db.pet_board.insert_one(doc)

    return jsonify({'msg': '업로드 완료! 얼른 확인하러 가볼까요?'})

@index_pages.route('/cancel', methods=['POST'])
def like_cancel():
    user_name_receive = request.form['user_name_give']
    like_users_receive = request.form['like_users_give']

    target_user = db.pet_board.find_one({'user_name': user_name_receive})
    curren_like = target_user['like_count']
    new_like = curren_like - 1

    doc = {
        'user_name': user_name_receive,
        'like_count': new_like,
        'like_users': like_users_receive
    }

    db.pet_board.insert_one(doc)

    return jsonify({'msg': '업로드 완료! 얼른 확인하러 가볼까요?'})
# #
# # # like_count - GET
# # @index_pages.route('/like', method=['GET'])
# # def like_print
# #
# # # sort_by - GET
# # @index_pages.route('/sort', method=['GET'])
# # def sort_by_like
# # def sort_by_upload
#
#
#
#
#
