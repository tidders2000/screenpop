from django.urls import path, include
from business.views import market, business_profile, edit_profile

urlpatterns = [
    path('market/', market, name='market'),
    path('business_profile/', business_profile, name='business_profile'),
    path('business_profile/<int:pk>', edit_profile, name='edit_profile')
]
