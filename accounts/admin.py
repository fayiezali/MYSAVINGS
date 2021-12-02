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
        'PER_FirstName'      , 
        'PER_FatherName'     ,
        'PER_GrandFatherName',
        'PER_FamilyName'
        ]
        } # ملئ حقل السلاق تلقائياَمن بيانات حقل اﻷسم الاول+الاب+الجد+العائلة
        prepopulated_fields = FullName
        #
        #
        # Add a Filter Box
        list_filter = (
        'PER_Customer', 
        'PER_Mobile'  , 
        'PER_IdNumber'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'PER_Customer'              , 
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
        'PER_Mobile'                ,
        'PER_SocialStatusUnmarried' ,
        'PER_Date_joined'
        )
        #
        #
        # Add Data In Different Sections
        fieldsets = (
        (None, 
        {
        'fields': (
        'PER_Customer'          ,
        'FER_Slug',
        'PER_FirstName'         ,
        'PER_FatherName'        ,
        'PER_GrandFatherName'   ,
        'PER_FamilyName',
        'PER_ImgePersonal'      ,
        'PER_IdNumber'          ,
        'PER_Nationality'       ,
        'PER_Mobile'
        )
        }
        ),
        ('Advanced', {
        'classes': ('collapse',),
        'fields': (
        'PER_Avialable'             ,
        'PER_SocialStatusMarried'   ,
        'PER_SocialStatusUnmarried'
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
        'FIN_Customer'     , 
        'FIN_BankAccount'  , 
        'FIN_ShareValue'   ,
        'FIN_NumberShares'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'FIN_Customer'               , 
        'FIN_ShareValue'             , 
        'FIN_NumberShares'           , 
        'FIN_BankName'               , 
        'FIN_BankAccount'            , 
        'FIN_MethodPaymentCash'      , 
        'FIN_MethodPaymentCheck'     , 
        'FIN_MethodPaymentTransfer'  ,
        'FIN_MethodPayment'          ,
        'FIN_SalaryDisbursementDate' ,
        'FIN_DateShareReceived'
        )
        #
        #
        # Add Data In Different Sections
        fieldsets = (
        (None, {
        'fields': (
        'FIN_Customer'                  , 
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
        'FIN_MethodPaymentCash'     ,
        'FIN_MethodPaymentCheck'    ,
        'FIN_MethodPaymentTransfer' ,
        'FIN_MethodPayment'
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
        'HOU_Customer'      , 
        'HOU_City'          , 
        'HOU_HomeAddress'   ,
        'HOU_CurrentWork'
        )
        #
        #
        # Show Fields a List
        list_display = (
        'HOU_Customer'     , 
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
        'HOU_Customer'     , 
        'HOU_Region'       , 
        'HOU_City'         , 
        'HOU_District'     , 
        'HOU_CurrentWork'  , 
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
