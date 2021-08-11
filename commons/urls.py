from django.urls import path 
from commons import views
#
#
#
urlpatterns = [
    path(''        , views.Index.as_view(), name='Index_URL'),
    path('about/'  , views.About.as_view(), name='About_URL'),
    
] 
