from django.urls import path

from .views import delete_question, savollar, savol_detail, check_answer, create_question, groups_view, users_view, create_choice

app_name = 'poll'
urlpatterns = [
    path('users/', users_view, name="users"),
    path('groups/', groups_view, name="groups"),
    path('savollar/', savollar, name="savollar"),
    path('savol/<int:id>/', savol_detail, name="savol"),
    path('check/<int:variant_id>/', check_answer, name="check_answer"),
    path('create-question/', create_question, name="create"),
    path('delete-question/<int:id>/', delete_question, name="delete_question"),
    path('tanlov-yaratish/', create_choice, name="create_choice"),
    
    # path('delete-group/<int:id>/', delete_group, name="delete_group"),
    # path('create-choice/', create_choice, name="create_choice"),
    # path('create-group/', create_group, name="create_group")
]