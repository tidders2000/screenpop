from django.urls import path, include
from business.views import market, business_profile, edit_profile, bp_view, new_business, edit_profile_b

urlpatterns = [
    path('market/', market, name='market'),
    path('business_profile/', business_profile, name='business_profile'),
    path('business_profile/<int:pk>', edit_profile, name='edit_profile'),
    path('view_profile/<int:pk>', bp_view, name='bp_view'),
    path('new_business/', new_business, name='new_business'),
    path('editb/<int:pk>', edit_profile_b, name='edit_profile_b'),
]
