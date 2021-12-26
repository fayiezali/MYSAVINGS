from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views # This Views Built-in Django
from accounts import views # This Views I Created It
#
#
# # روابط الصفحات
# urlpatterns = [
#     # Home/Index Page URLs:
#     path('index_home/'                                         , index_home_FUNCTION                             , name='index_home_URL'),
#     # Association Data URLs:
#     path('association_data_show_all/'                          , association_data_show_all_FUNCTION              , name='association_data_show_all_URL'), 
#     path('association_data_show_details_id/<int:id>/'          , association_data_show_details_id_FUNCTION       , name='association_data_show_details_id_URL'), 
#     path('association_data_show_details_slug/<slug:slug>/'     , association_data_show_details_slug_FUNCTION     , name='association_data_show_details_slug_URL'), 
#     path('association_data_new/'                               , association_data_new_FUNCTION                   , name='association_data_new_URL'),  
#     path('association_data_update/<int:id>'                    , association_data_update_FUNCTION                , name='association_data_update_URL'),  
#     path('association_data_delete/<int:id>'                    , association_data_delete_FUNCTION                , name='association_data_delete_URL'),  
#     ]
#
#
# AUTHENTICATION:--------------------------------------------------------------------
urlpatterns = [
# Login - Logout - Logout Confirm - Logout Done (1) Login (1)
        # Login In System   
        path('login/'                                   , auth_views.LoginView.as_view(),
        name='login'),
        #
        # Exit From System
        path('logout/'                                  , auth_views.LogoutView.as_view(), 
        name='logout'),
        #
        # Logout Confirme 
        path('my_logout_confirm/'                        , views.My_LogoutConfirm.as_view(),
        name='My_LogoutConfirm_URL'), 
        #
        # Checkout Confirmed Successfull
        path('my_logout_done/'                          , views.My_LogoutDone.as_view(),
        name='My_LogoutDone_URL'), 
# Change Password - Password Change Done (2)
        # Change Password
        path('change-password/'                         , auth_views.PasswordChangeView.as_view(
        template_name='registration/change-password.html', # The Name Of a Template To Display For The View Use
        success_url= reverse_lazy('password_change_done')), # Redirect To URL Address
        name='password_change'), # Name URL pattern
        #
        # Password Change completed Succesfull
        path('password_change_done/'                   , auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password-change-done.html'), # The Name Of a Template To Display For The View Use
        name='password_change_done'), # Name URL pattern
# Password Reset - Password Reset Done - Password Reset Confirm - Password Reset Comlete (3)
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        #The Full Name Of a Template To Use For GEnerating The Email With The Reset Password Link
        # The URL To Redirect To After a Successful Password Reset Request
        path('password-reset/'                         , auth_views.PasswordResetView.as_view(
        template_name='registration/my_password_reset.html', # The Name Of a Template To Display For The View Use 
        subject_template_name='registration/my_password_reset_subject.txt',
        success_url= reverse_lazy('password_reset_done')), # Redirect To URL Address
        name='password_reset'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        path('password-reset/done/'                    , auth_views.PasswordResetDoneView.as_view(
        template_name='registration/my_password_reset_done.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_done'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/my_password_reset_confirm.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_confirm'), # Name URL pattern
        #
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        path('password-reset-complete/'               , auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/my_password_reset_complete.html'), # The Name Of a Template To Display For The View Use
        name='password_reset_complete'), # Name URL pattern
]
#
#
# PROFILE DATA:----------------------------------------------------------------------------------------
urlpatterns +=[
        ##
# Signup - Activate Account - Contact Us (1):
        # Signup And Confirm Registration With Email
        path('my_signup/'                            , views.My_Signup.as_view()                        , name='My_Signup_URL'), 
        # Active Registration Withe Email.
        path('activate/<uidb64>/<token>/'            , views.Activate.as_view()                         , name='activate'),  
        # Contact Us
        # path('my_profile_contact_us/'              , views.My_ProfileContactUs                        , name='My_Profile_Contact_Us'),
        #
# Profile Detail ID-Slug - Update -  (2):
        # View Profile Details By (ID)
        path('my_Profile_Detail_ID/<int:pk>/'        , views.My_Profile_Detail_ID.as_view()             , name='My_Profile_Detail_ID_URL'),
        # View Profile Details By (slug)
        path('my_profile_detail_sluIDg/<slug:slug>/' , views.My_Profile_Detail_Slug.as_view()           , name='My_Profile_Detail_Slug_URL'), 
        # Update Profile
        path('my_profile_update/<int:pk>/'           , views.My_Profile_Update.as_view()                , name='my_profile_update_URL'),
        # Checkout Confirmed Successfull
        path('my_profile_update_done/'               , views.My_Profile_Update_Done.as_view()           , name='My_Profile_Update_Done_URL'), 
        # Delete Profile
        path('my_Profile_delete/<int:pk>/delete/'    , views.My_Profile_Delete.as_view()                , name='My_Profile_delete_URL'),
        # Checkout Confirmed Successfull
        path('my_profile_delete_done/'               , views.My_Profile_Delete_Done.as_view()           , name='My_Profile_Delete_Done_URL'), 
        # Delete Multiple Select
        path('my_Profile_delete/<int:pk>/delete/'    , views.My_Profile_Delete_Multiple_Select.as_view(), name='My_Profile_Delete_Multiple_Select_URL'),
        # View a List Of The Profiles 
        path('my_profile_list/'                      , views.My_Profile_ListView_Search.as_view()       , name='My_Profile_ListView_Search_URL'),
        #*********************************************************************************
        # Show Details In The Profile - But The code Is Written In The Model
        # path('associationdetailid/<int:pk>/'       , AssociationDetailViewID.as_view()   , name='AssociationData_MODEL-detail'),
        # <td><a href="{{ object_list_item.get_absolute_url }}">{{ object_list_item.ASS_NameAssociation }}</a> ({{object_list_item.ASS_Phone}})</td> <!-- This Link Is From The Database and usls.py File-->
        #*********************************************************************************
]
#
#
# PERSONAL DATA:--------------------------------------------------------------------
urlpatterns += [
        # View Profile Details By (ID)
        path('my_personal_data_Detail_ID/<int:pk>/'  , views.My_Personal_Data_Detail_ID.as_view()      , name='My_Personal_Data_Detail_ID_URL'),
        # Update
        path('my_personal_update/<int:pk>/'          , views.My_Personal_Data_Update.as_view()         , name='My_Personal_Data_Update_URL'),
        # Checkout Confirmed Successfull
        path('my_personal_data_update_done/'         , views.My_Personal_Data_Update_Done.as_view()   , name='My_Personal_Data_Update_Done_URL'), 
        # # Checkout Confirmed Successfull
        # path('my_personal_delete_done/'              , views.My_Profile_Delete_Done.as_view()          , name='My_Profile_Delete_Done_URL'), 
]
#
#
# FINANCIAL DATA:----------------------------------------------------------------------------------------
urlpatterns += [
        # View Profile Details By (ID)
        path('my_financial_data_Detail_ID/<int:pk>/' , views.My_Financial_Data_Detail_ID.as_view()     , name='My_Financial_Data_Detail_ID_URL'),
        # Update
        path('my_financial_data_update/<int:pk>/'    , views.My_Financial_Data_Update.as_view()        , name='My_Financial_Data_Update_URL'),
        # Checkout Confirmed Successfull
        path('my_financial_data_update_done/'        , views.My_Financial_Data_Update_Done.as_view()   , name='My_Financial_Data_Update_Done_URL'), 
]
#
#
# HOUSING DATA:----------------------------------------------------------------------------------------
urlpatterns += [
        # View Housing Details By (ID)
        path('my_housing_data_Detail_ID/<int:pk>/'  , views.My_Housing_Data_Detail_ID.as_view()       , name='My_Housing_Data_Detail_ID_URL'),
        # Update
        path('my_housing_update/<int:pk>/'          , views.My_Housing_Data_Update.as_view()          , name='My_Housing_Data_Update_URL'),
        # Checkout Confirmed Successfull
        path('my_housing_data_update_done/'         , views.My_Housing_Data_Update_Done.as_view()     , name='My_Housing_Data_Update_Done_URL'), 
]
#
#
# DUES RECORD:----------------------------------------------------------------------------------------
urlpatterns +=[
        # View a List Of The Dues Record 
        path('my_dues_record_list/'                      , views.My_Dues_Record_ListView_Search.as_view()       , name='My_Dues_Record_ListView_Search_URL'),
        path('accounts/'                          , views.My_Monthes_Menu.as_view()                      , name='My_Monthes_Menu_URL'),
        #*********************************************************************************

]



urlpatterns += [
    path('', views.countown, name='countdown'),
    path('main',views.maninmenu,name='mainmenu'),
    path('mainsave',views.mainsave,name='msave'),
    path('submenusave',views.subsave,name='submenusave'),
    path('dmenu',views.dynamic_menu,name='dmenu')
]