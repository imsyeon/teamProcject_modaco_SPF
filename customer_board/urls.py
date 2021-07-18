from django.urls import path

from .views import base_views, question_views, answer_views, comment_views
from . import views

app_name = 'customer_board'
urlpatterns = [

    path('', base_views.board, name='board'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    path('comment/create/<int:question_id>/' ,comment_views.comment_create_question, name='comment_create_question'), #질문에댓글
    path('comment/modify/<int:comment_id>/' ,comment_views.comment_modify_question, name='comment_modify_question'), #댓글 수정
    path('comment/delete/<int:comment_id>/' ,comment_views.comment_delete_question, name='comment_delete_question'), # 댓글삭제

    path('comment/create/answer/<int:answer_id>/' ,comment_views.comment_create_answer, name='comment_create_answer'), #댓글에댓글
    path('comment/modify/answer/<int:comment_id>/' ,comment_views.comment_modify_answer, name='comment_modify_answer'), #댓글 수정
    path('comment/delete/answer/<int:comment_id>/' ,comment_views.comment_delete_answer, name='comment_delete_answer'), # 댓글삭제


]