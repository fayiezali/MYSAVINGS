# 
from django.contrib import admin
# 
from django.contrib.auth.models import User # إستيراد اسم المستخدم
# 
from accounts.models import * #  استيراد كل المودل/الجداول من التطبيق المطلوب
# 
#
# 
# 
# 
# 
"""Important Note:
(fields) & (fieldsets) This Properties Can Not Be Put Together
# Controlling Which fields are Displayed and Laid Out
# fields = [('ASS_NameAssociation', 'ASS_Slug' ), 'ASS_AssociationLogo' , 'ASS_Address' ,('ASS_Mobile' , 'ASS_Phone') , 'ASS_Email' , 'ASS_BankAccount']
"""
#
#
#
#
##########################################################################
# *** Add The Child Table Inside The Parent Table ***
# class FinancialDataInline(admin.TabularInline):
#     """Defines format of inline book insertion (used in AuthorAdmin)"""
#     model = FinancialData_MODEL
# #
# class HousingDataDataInline(admin.TabularInline):
#     """Defines format of inline book insertion (used in AuthorAdmin)"""
#     model = HousingData_MODEL
#
# class PersonalDataInline(admin.TabularInline):
#     """Defines format of inline book insertion (used in AuthorAdmin)"""
#     model = PersonalData_MODEL
##########################################################################
#
#
#
#
#
# # 'admin' ظهور الجداول المطلوبة في صفحة 
# # 
# # بينات الجمعية
# @admin.register(AssociationData_MODEL)
# class AssociationData_admin(admin.ModelAdmin): # تم وراثة الكلاس ادمن من اجل عمل عليه تعديل/كستمايز
#     prepopulated_fields = {'ASS_Slug':['ASS_NameAssociation'] , 'ASS_Slug':['ASS_NameAssociation']} # ملئ حقل السلاق تلقائياَمن بيانات حقل إسم الجمعية
# # 
# # 
# # 
# # البيانات الشخصية
# @admin.register(PersonalData_MODEL)
# class PersonalData_admin(admin.ModelAdmin): # تم وراثة الكلاس ادمن من اجل عمل عليه تعديل/كستمايز
#         FullName = {"FER_Slug": [
#                             'PER_FirstName' , 
#                             'PER_FatherName' ,
#                             'PER_GrandFatherName' ,
#                             'PER_FamilyName'
#                             ]} # ملئ حقل السلاق تلقائياَمن بيانات حقل اﻷسم الاول+الاب+الجد+العائلة
#         prepopulated_fields = FullName
# 
# 
# 

# 'admin' ظهور الجداول المطلوبة في صفحة 
# 
# بينات الجمعية
# @admin.register(AssociationData_MODEL)
# class AssociationData_admin(admin.ModelAdmin): # تم وراثة الكلاس ادمن من اجل عمل عليه تعديل/كستمايز
#     # Automatically Fill In Slug Field From 
#     prepopulated_fields = {'ASS_Slug':['ASS_NameAssociation']} 
#     #
#     #
#     # Add aFilter Box
#     list_filter = ('ASS_NameAssociation', 'ASS_Mobile' , 'ASS_BankAccount')
#     #
#     #
#     # Show Fields a List
#     list_display = ('ASS_NameAssociation', 'ASS_Slug' , 'ASS_AssociationLogo' , 'ASS_Address' ,  'ASS_Mobile' , 'ASS_Phone' , 'ASS_Email' , 'ASS_BankAccount')
#     #
#     #
#     # Controlling Which fields are Displayed and Laid Out
#     # fields       = [('ASS_NameAssociation', 'ASS_Slug' ), 'ASS_AssociationLogo' , 'ASS_Address' ,('ASS_Mobile' , 'ASS_Phone') , 'ASS_Email' , 'ASS_BankAccount']
#     #
#     #
#     # Add Data In Different Sections
#     fieldsets = (
#         (None, {
#             'fields': ('ASS_NameAssociation','ASS_Slug','ASS_AssociationLogo','ASS_Address','ASS_Mobile')
#         }),
#         ('Advanced', {
#             'classes': ('collapse',),
#             'fields': ('ASS_Phone','ASS_Email','ASS_BankAccount')
#         }),
#     )

#     # inlines = [PersonalDataInline]
# 
# 
# 
# البيانات الشخصية
@admin.register(PersonalData_MODEL)
class PersonalData_admin(admin.ModelAdmin): # The class has been inherited as an addict in order to make a modification / customization 
        # Automatically Fill In Slug Field From Variable (FullName)
        FullName = {
        "FER_Slug": # Slug Field
        [
        'PER_FirstName'       , 
        'PER_FatherName'      ,
        'PER_GrandFatherName' ,
        'PER_FamilyName'
        ]
        } # ملئ حقل السلاق تلقائياَمن بيانات حقل اﻷسم الاول+الاب+الجد+العائلة
        prepopulated_fields = FullName
        #
        #
        # Add a Filter Box
        list_filter = (
        'PER_User'     , 
        'PER_Mobile'   , 
        'PER_IdNumber'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'PER_User'                  , 
        'PER_Avialable'             , 
        'FER_Slug'                  ,
        'PER_FirstName'             ,
        'PER_FatherName'            ,
        'PER_GrandFatherName'       ,
        'PER_FamilyName'            ,
        'PER_ImgePersonal'          ,
        'PER_IdNumber'              ,
        'PER_Nationality'           ,
        'PER_Mobile'                ,
        'PER_Date_joined'
        # 'PER_SocialStatusUnmarried' ,
        )
        #
        #
        # Add Data In Different Sections
        fieldsets = (
        (None, 
        {
        'fields': (
        'PER_User'              ,
        'FER_Slug'              ,
        'PER_FirstName'         ,
        'PER_FatherName'        ,
        'PER_GrandFatherName'   ,
        'PER_FamilyName'        ,
        'PER_ImgePersonal'      ,
        'PER_IdNumber'          ,
        )
        }
        ),
        ('Advanced', {
        'classes': ('collapse',),
        'fields': (
        'PER_Avialable'    ,
        'PER_Nationality'  ,
        'PER_Mobile'
        # 'PER_SocialStatusMarried'   ,
        # 'PER_SocialStatusUnmarried'
        )
        }
        ),
        )
        # inlines = [PersonalDataInline]
# 
# 
# 
#
# البيانات المالبة
@admin.register(FinancialData_MODEL)
class FinanciaData_admin(admin.ModelAdmin): # The class has been inherited as an addict in order to make a modification / customization 
        #
        # Add aFilter Box
        list_filter = (
        'FIN_User'         , 
        'FIN_BankAccount'  , 
        'FIN_ShareValue'   ,
        'FIN_NumberShares'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'FIN_User'                   , 
        'FIN_ShareValue'             , 
        'FIN_NumberShares'           , 
        'FIN_BankName'               , 
        'FIN_BankAccount'            , 
        'FIN_MethodPayment',
        'FIN_MethodReceive',
        'FIN_SalaryDisbursementDate' ,
        'FIN_DateShareReceived'
        # 'FIN_MethodPaymentCash'      , 
        # 'FIN_MethodPaymentCheck'     , 
        # 'FIN_MethodPaymentTransfer'  ,

        )
        #
        #
        # Add Data In Different Sections
        fieldsets = (
        (None, {
        'fields': (
        'FIN_User'                      , 
        'FIN_ShareValue'                , 
        'FIN_NumberShares'              , 
        'FIN_BankName'                  ,  
        'FIN_BankAccount'               , 
        'FIN_SalaryDisbursementDate'    ,
        'FIN_DateShareReceived'
        )
        }
        ),
        ('Advanced', {
        'classes': ('collapse',)    ,
        'fields': (
        # 'FIN_MethodPaymentCash'     ,
        # 'FIN_MethodPaymentCheck'    ,
        # 'FIN_MethodPaymentTransfer' ,
        'FIN_MethodPayment'           ,
        'FIN_MethodReceive'
        )
        }
        ),
        )
        # inlines = [PersonalDataInline]
# 
# 
# 
# البيانات السكنة
@admin.register(HousingData_MODEL)
class HousingData_admin(admin.ModelAdmin):  # The class has been inherited as an addict in order to make a modification / customization 
        #
        # Add aFilter Box
        list_filter = (
        'HOU_User'      , 
        'HOU_City'          , 
        'HOU_HomeAddress'   ,
        'HOU_CurrentWork'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'HOU_User'     , 
        'HOU_Region'       , 
        'HOU_City'         , 
        'HOU_District'     , 
        'HOU_HomeAddress'  , 
        'HOU_CurrentWork'  , 
        'HOU_WorkAddress'
        )
        #
        #
        # Add Data In Different Sections
        fieldsets = (
        (None, {
        'fields': (
        'HOU_User'     , 
        'HOU_Region'       , 
        'HOU_City'         , 
        'HOU_District'     , 
        'HOU_CurrentWork'  
        )
        }
        ),
        ('Advanced', {
        'classes': ('collapse',) ,
        'fields': (
        'HOU_HomeAddress'        , 
        'HOU_WorkAddress'
        )
        }
        ),
        )
        # inlines = [PersonalDataInline]
# 
# 
# 
# 
#
# 
# 
# 
# Comprehensive Record
@admin.register(Association_Months_MODEL)
class Association_Months_admin(admin.ModelAdmin):  # The class has been inherited as an addict in order to make a modification / customization 
        #
        # Add aFilter Box
        list_filter = (
        # 'AM_MonthNumber'       , 
        'AM_MonthName'         , 
        'AM_User'              ,
        'AM_DateShareReceived' ,
        # 'AM_ShareValue'        ,
        'AM_NumberShares'      ,
        'AM_DeservedAmount'    ,
        # 'AM_Notes'
        )
        #
        #
        # Show Fields a List
        list_display = (
        # 'AM_MonthNumber'       , 
        'AM_MonthName'         , 
        'AM_User'              ,
        'AM_DateShareReceived' ,
        'AM_ShareValue'        ,
        'AM_NumberShares'      ,
        'AM_DeservedAmount'    ,
        'AM_Notes'
        )
        #
        # search list
        search_fields = ['AM_MonthName']
        #
        #
        # Add Data In Different Sections
        fieldsets = (
        (None, {
        'fields': (
        # 'AM_MonthNumber'       , 
        'AM_MonthName'         , 
        'AM_User'              ,
        'AM_DateShareReceived' ,
        'AM_ShareValue'        ,
        'AM_NumberShares'      ,
        'AM_DeservedAmount'    ,
        )
        }
        ),
        ('Advanced', {
        'classes': ('collapse',) ,
        'fields': (
        'AM_Notes',
        )
        }
        ),
        )
        # inlines = [PersonalDataInline]
# 
# 
# 
# Monthes_List
@admin.register(Monthes_Menu_MODEL)
class Monthes_Menu_MODEL_admin(admin.ModelAdmin):  # The class has been inherited as an addict in order to make a modification / customization 
        #
        # Add aFilter Box
        list_filter = (
        'MM_MonthName'      ,
        )
        #
        #
        # Show Fields a List
        list_display = (
        # 'AM_MonthNumber'       , 
        'MM_MonthName'      , 
        )
        #
        # search list
        search_fields = ['MM_MonthName']
        #
        #
#
#
#
# Monthes_List
# @admin.register(main_menu)
# class main_menu_admin(admin.ModelAdmin):  # The class has been inherited as an addict in order to make a modification / customization 
#         #
#         # Add aFilter Box
#         list_filter = (
#         'm_menu_id'      ,
#         'm_menu_name'    ,
#         )
#         #
#         #
#         # Show Fields a List
#         list_display = (
#         # 'AM_MonthNumber'       , 
#         'm_menu_id'      , 
#         'm_menu_name'      , 
#         'm_menu_link'      , 

#         )
#         #
#         # search list
#         search_fields = ['m_menu_name']
#         #
#         #
