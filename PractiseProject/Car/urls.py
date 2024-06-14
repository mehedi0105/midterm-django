
from django.urls import path
from . import views
urlpatterns = [
    path('signUp/', views.signUp,name='signUp'),
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('edit_profile/', views.editProfile,name='edit_profile'),
    path('update_pass/', views.pass_change,name='update_pass'),
    path('add_post/', views.AddPostCreateView.as_view(),name='add_post'),
    path('details_post/<int:id>',views.DetailsPostView.as_view(),name='details_post'),
    # path('buy_now/<int:id>',views.buyNow,name='buy_now')
]