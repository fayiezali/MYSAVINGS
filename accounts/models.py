from django.db import models
#
from typing import ClassVar
# 
from django.db import models
# 
from django.contrib.auth.models import User # إستيراد اسم المستخدم
# 
from django.urls import reverse  # To generate URLS by reversing URL patterns
#
from django.db.models.signals import post_save # كلاس فكرته: انه بمجرد تنفيذ عملية الحفظ يقوم مباشرة بتنفيذ عملية اخرى بعده
#
# 
# 
#   
# 
# 
# Association Data
# class AssociationData_MODEL(models.Model):
#     ASS_NameAssociation =   models.CharField(max_length=100                       , db_index=True , blank=False , null=False , verbose_name="إسم الجمعية"              ,help_text='هذا الحقل مخصص لإسم الجمعية')
#     ASS_Slug            =   models.SlugField(unique=True                          , db_index=True , blank=False , null=False , verbose_name="الإسم التعريفي")
#     ASS_AssociationLogo =   models.ImageField(upload_to='AssociationData_Image/'  , db_index=True , blank=False , null=False , verbose_name="شعار الجمعية"             ,default='Default_Image.png' )
#     ASS_Address         =   models.CharField(max_length=250                       , db_index=True , blank=False , null=False , verbose_name="العنوان")
#     ASS_Mobile          =   models.CharField(max_length=10                        , db_index=True , blank=False , null=False , verbose_name="الجوال")
#     ASS_Phone           =   models.CharField(max_length=250                       , db_index=True , blank=False , null=False , verbose_name="الهاتف"                   ,help_text='ضع مفتاح المدينة قبل الرقم مثال:012')
#     ASS_Email           =   models.EmailField(max_length=250                      , db_index=True , blank=False , null=False , verbose_name="البريد الألكتروني")
#     ASS_BankAccount     =   models.CharField(max_length=50                        , db_index=True , blank=False , null=False , verbose_name="الحساب البنكي - الآيبان"  ,help_text='مثال: SA000000')
#     # 
#     # 'admin'عرض إسم الحقل في صفحة
#     def __str__(self):
#         return self.ASS_NameAssociation
#     # 
#     class Meta: #'admin'عرض إسم المودل/الجدول في صفحة
#         verbose_name_plural = 'AssociationData_MODEL'
#     # 
#     # 'A-Z' ترتيب تصاعدي 
#     class Meta:
#         ordering = ['ASS_NameAssociation'] 
# 
# 
# 
# 
# 
# 
# Personal Data
class PersonalData_MODEL(models.Model):
    # متغير لحفظ رموز الجنسية
    SAUDI    = 'SA'
    BAHRAIN  = 'BA'
    OMAN     = 'OM'
    QATAR    = 'QA'
    KUWAIT   = 'KU'
    EMIRATES = 'EM'
    YEMEN    = 'YE'
    NATIONALITY_CHOICES = [
        (SAUDI,    'Saudi'),
        (BAHRAIN,  'Bahrain'),
        (OMAN,     'Oman'),
        (QATAR,    'Qatar'),
        (KUWAIT,   'Kuwait'),
        (EMIRATES, 'Emirates'),
        (YEMEN,    'Yemen'),
]
# 
# 
# 
    # PER_Association            = models.ForeignKey(AssociationData_MODEL           , on_delete=models.CASCADE                 , verbose_name="اسم الجمعية")
    PER_User                   = models.OneToOneField(User                         , on_delete=models.CASCADE                 , verbose_name="اسم المشترك")
    PER_Avialable              = models.BooleanField(default=True                  , db_index=True , blank=False , null=False , verbose_name="حالة المشترك_نشط")
    FER_Slug                   = models.SlugField(unique=False                     , db_index=True , blank=True  , null=False , verbose_name="الإسم التعريفي")
    PER_FirstName              = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="الإسم الأول")
    PER_FatherName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الاب")
    PER_GrandFatherName        = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الجد")
    PER_FamilyName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم العائلة")
    PER_ImgePersonal           = models.ImageField(upload_to='PersonalData_Image/' , db_index=True , blank=False , null=False , verbose_name="الصورة الشخصية"      ,default='Default_Image.png')
    PER_IdNumber               = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="رقم الهوية الشخصية")
    PER_Nationality            = models.CharField(max_length=2                     , db_index=True , blank=False , null=False , verbose_name="الجنسية"             , choices=NATIONALITY_CHOICES, default=SAUDI)
    PER_Mobile                 = models.CharField(max_length=10                    , db_index=True , blank=False , null=False , verbose_name="الجوال")
    PER_Date_joined            = models.DateTimeField(                               db_index=True , auto_now_add=True,verbose_name="تاريخ الإنضمام للجمعية")
    # PER_SocialStatusMarried    = models.BooleanField(default=True                  , db_index=True , blank=False , null=False , verbose_name="الحالة الإجتماعية - أعزب")
    # PER_SocialStatusUnmarried  = models.BooleanField(default=False                 , db_index=True , blank=False , null=False , verbose_name="الحالة الإجتماعية -متزوج")
# #
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.PER_User)
    # 
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['PER_User'] 
##
    # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها 
    # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها 
    # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # user:
    # ['instance']: هي البيانات التي تسم إستقبالها
    # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ 
    def create_personal_data(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            PersonalData_MODEL.objects.create(PER_Customer=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف 
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن 
    post_save.connect(create_personal_data , sender=User)
# 
# 
# 
# 
#
# Financial Data
class  FinancialData_MODEL(models.Model):
    # متغير لحفظ رموز طريقة الدقع'
    CASH     = 'CA'
    CHECK    = 'CH'
    TRANSFER = 'TR'
    # قائمة بطريقة الدفع/الاستلام 
    METHOD_PAYMENT_CHOICES = [
        (CASH,     'Cash'),
        (CHECK,    'Check'),
        (TRANSFER, 'Transfer'),
    ]
    # 
    # FIN_Association             = models.ForeignKey(AssociationData_MODEL , on_delete=models.CASCADE                                              , verbose_name="اسم الجمعية")
    FIN_User                    = models.OneToOneField(User               , on_delete=models.CASCADE                                              , verbose_name="اسم المشترك")
    FIN_ShareValue              = models.DecimalField(default=50 , max_digits=8 , decimal_places=2   , db_index=True , blank=False  , null=False  , verbose_name="قيمة السهم")
    FIN_NumberShares            = models.IntegerField(default=1                                      , db_index=True , blank=False  , null=False  , verbose_name="عدد الأسهم")
    FIN_BankName                = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم البنك")
    FIN_BankAccount             = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الحساب البنكي - الآيبان")
    FIN_MethodPayment           = models.CharField(max_length=2                                      , db_index=True , blank=False  , null=False  , verbose_name="طريقة سداد قيمة اﻷسهم"         , choices=METHOD_PAYMENT_CHOICES , default=CASH)    
    FIN_MethodReceive           = models.CharField(max_length=2                                      , db_index=True , blank=False  , null=False  , verbose_name="طريقة إستلام قيمة اﻷسهم"         , choices=METHOD_PAYMENT_CHOICES , default=CASH)    
    FIN_SalaryDisbursementDate  = models.DateField(                                                    db_index=True , blank=True   , null=True   , verbose_name="تاريخ صرف الراتب" , help_text='Required Field')
    FIN_DateShareReceived       = models.DateField(                                                    db_index=True , blank=True   , null=True   , verbose_name="تاريخ استلام اﻷسهم/المشاركات/المستحقات" , help_text='Required Field')
    # FIN_MethodPaymentCash       = models.BooleanField(default=True                                   , db_index=True , blank=False  , null=False  , verbose_name="طريقة سداد قيمة اﻷسهم _ نقدا")
    # FIN_MethodPaymentCheck      = models.BooleanField(default=False                                  , db_index=True , blank=False  , null=False  , verbose_name="طريقة سداد قيمة اﻷسهم _ شيك")
    # FIN_MethodPaymentTransfer   = models.BooleanField(default=False                                  , db_index=True , blank=False  , null=False  , verbose_name="طريقة سداد قيمة اﻷسهم _ حوالة")
    # 
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.FIN_User)
    # 
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['FIN_User'] 
# #
    # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها 
    # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها 
    # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # user:
    # ['instance']: هي البيانات التي تسم إستقبالها
    # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ 
    def create_financia_data(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            FinancialData_MODEL.objects.create(FIN_Customer=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف 
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن 
    post_save.connect(create_financia_data , sender=User)
#
# 
# 
# 
# 
#
# Housing Data
class  HousingData_MODEL(models.Model):
    # HOU_Association  = models.ForeignKey(AssociationData_MODEL  , on_delete=models.CASCADE                 ,verbose_name="اسم الجمعية")
    HOU_User         = models.OneToOneField(User                , on_delete=models.CASCADE                 ,verbose_name="اسم المشترك")
    HOU_Region       = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="المنطقة")
    HOU_City         = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="المدينة")
    HOU_District     = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="الحي")
    HOU_HomeAddress  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="عنوان المنزل")
    HOU_CurrentWork  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="العمل الحالي")
    HOU_WorkAddress  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="عنوان العمل")
    # 
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.HOU_User) 
    # 
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['HOU_User'] 
# #
# #
    # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها 
    # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها 
    # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # user:
    # ['instance']: هي البيانات التي تسم إستقبالها
    # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ 
    def create_housing_data(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            HousingData_MODEL.objects.create(HOU_Customer=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف 
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن 
    post_save.connect(create_housing_data , sender=User)
# 
# 
# 
    # #
    # #  في حالة عدم قيام المستخدم بذلك"slug" فاكشن تقوم بتعبئة حقل 
    # # هذه الفانكش ممكن نربطها إي مودل/جدول نريده
    # # self , *args , **kwargs):بارمترات تقوم بإستقبال البيانات المرسلة من سجل المستخدم
    # #  slugify(self.user.username:
    # def save(self , *args , **kwargs):
    #     if not self.slug: # نفذ الكود أدناه "slug"في حالة عدم إستقبال بيانات من قبل المستخدم لحقل 
    #         self.slug = slugify(self.user.username) # "slug" ضع إسم المستخدم في الحقل 
    #     super(Profile , self).save(*args , **kwargs)

    # class Meta:
    #     verbose_name = ("Profile")
    #     verbose_name_plural = ("Profile")
    # #
    # #  "admin" في صفحة "user"تقوم بإظهار  اسم  
    # def __str__(self): 
    #     return '%s' %(self.user.username) #  يمكن ان تضع اي حقل  من حقول  الجدول ترغب فيه ان اردت "admin"  الذي سوف يظهر في صفحة  "user"  هذا هو إسم المستخدم 

    # # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها 
    # # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها 
    # # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # # user:
    # # ['instance']: هي البيانات التي تسم إستقبالها
    # # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ 
    # def create_profile(sender, **kwargs):
    #      if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
    #          Profile.objects.create(user=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "profile" قم بإنشاء ملف 

    # # "" "user"والمستخدم  "post_save" الربط بين الفانكشن 
    # post_save.connect(create_profile , sender=User)
#
#
#
    # متغير لحفظ رموز طريقة الدقع'
    CASH     = 'CA'
    CHECK    = 'CH'
    TRANSFER = 'TR'
    # قائمة بطريقة الدفع/الاستلام 
    METHOD_PAYMENT_CHOICES = [
        (CASH,     'Cash'),
        (CHECK,    'Check'),
        (TRANSFER, 'Transfer'),
    ]

# Comprehensive Record
class  Association_Months_MODEL(models.Model):
    # Variable To Save The Number Of Months
    CHOOSE_MONTH_NUMBER = '00'
    JAN                 = '01'
    FEB                 = '02'
    MAR                 = '03'
    APR                 = '04'
    MAY                 = '05'
    JUN                 = '06'
    JUL                 = '07'
    AUG                 = '08'
    SEP                 = '09'
    OCT                 = '10'
    NOV                 = '11'
    DEC                 = '12'

    # The Number Of Months 
    MONTH_NUMBER = [
    (CHOOSE_MONTH_NUMBER ,  'Choose The Month Number'),
    (JAN                 ,                       '01'),
    (FEB                 ,                       '02'),
    (MAR                 ,                       '03'),
    (APR                 ,                       '04'),
    (MAY                 ,                       '05'),
    (JUN                 ,                       '06'),
    (JUL                 ,                       '07'),
    (AUG                 ,                       '08'),
    (SEP                 ,                       '09'),
    (OCT                 ,                       '10'),
    (NOV                 ,                       '11'),
    (DEC                 ,                       '12'),
    ]
    # 
    #
    # Variable To Save The Month Code
    # The Data Will be Saved in the Database 
    JANUARY             = '01-January__Jumada Al-Awwal-(05)'
    FEBRUARY            = '02-February_Jumada Al-Thani-(06)'
    MARCH               = '03-March______________Rajab-(07)'
    APRIL               = '04-April_____________Shaban-(08)'
    MAY                 = '05-May______________Ramadan-(09)'
    JUNE                = '06-June_____________Shawwal-(10)'
    JULY                = '07-July__________Dhul-Qadah-(11)'
    AUGUST              = '08-August_______Dhul-Hijjah-(12)'
    SEPTEMBER           = '09-September_______Muharram-(01)'
    OCTOBER             = '10-October____________Safar-(02)'
    NOVEMBER            = '11-November___Rabi Al-Awwal-(03)'
    DECEMBER            = '12-December___Rabi Al-Thani-(04)'
    All                 = '00-All_______________Al-Kol-(00)'


    # List Of The Names Of The Months
    # This Data Will Be shown In the Menu
    MONTH_NAME = [
    (JANUARY            ,  '01-January__Jumada Al-Awwal-(05)')  ,
    (FEBRUARY           ,  '02-February_Jumada Al-Thani-(06)')  ,
    (MARCH              ,  '03-March______________Rajab-(07)')  ,
    (APRIL              ,  '04-April_____________Shaban-(08)')  ,
    (MAY                ,  '05-May______________Ramadan-(09)')  ,
    (JUNE               ,  '06-June_____________Shawwal-(10)')  ,
    (JULY               ,  '07-July__________Dhul-Qadah-(11)')  ,
    (AUGUST             ,  '08-August_______Dhul-Hijjah-(12)')  ,
    (SEPTEMBER          ,  '09-September_______Muharram-(01)')  ,
    (OCTOBER            ,  '10-October____________Safar-(02)')  ,
    (NOVEMBER           ,  '11-November___Rabi Al-Awwal-(03)')  ,
    (DECEMBER           ,  '12-December___Rabi Al-Thani-(04)')  ,
    (All                ,  '00-All_______________Al-Kol-(00)')  ,
    ]
    # 
    # FIN_Association             = models.ForeignKey(AssociationData_MODEL , on_delete=models.CASCADE                                              , verbose_name="اسم الجمعية")
    # AM_MonthNumber          = models.CharField(max_length=2                                      , db_index=True , blank=False  , null=False  , verbose_name="رقم الشهر"         , choices=MONTH_NUMBER , default=CHOOSE_MONTH_NUMBER)    
    AM_MonthName            = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم الشهر"         , choices=MONTH_NAME   , default='Please Choose ')    
    AM_User                 = models.ForeignKey(User         , on_delete=models.CASCADE                                                       , verbose_name="اسم المشترك")
    AM_DateShareReceived    = models.DateField(                                                    db_index=True , blank=True   , null=True   , verbose_name="تاريخ استلام اﻷسهم/المشاركات/المستحقات"    , help_text='Required Field')
    AM_ShareValue           = models.DecimalField(default=50 , max_digits=8 , decimal_places=2   , db_index=True , blank=False  , null=False  , verbose_name="قيمة السهم")
    AM_NumberShares         = models.IntegerField(default=1                                      , db_index=True , blank=False  , null=False  , verbose_name="عدد الأسهم")
    AM_DeservedAmount       = models.DecimalField(default=50 , max_digits=8 , decimal_places=2   , db_index=True , blank=False  , null=False  , verbose_name=" المبلغ المستحق")
    AM_Notes                = models.CharField(max_length=50                                     , db_index=True , blank=True   , null=True   , verbose_name="الملاحظات")    

    # 
    # Display The Name Of This Field In The Admin Page
    def __str__(self):
        return str(self.AM_MonthName)
    # 
    # Arrange The Fields In Ascending Order 'Z-A'
    class Meta:
        ordering = ['AM_MonthName'] 
#
#
#
#
#
#
class Monthes_Menu_MODEL(models.Model):
    MM_MonthName = models.CharField(unique=True  , max_length=50)
    #
    # Display The Name Of This Field In The Admin Page
    def __str__(self):
            return self.MM_MonthName
    #
    # Arrange The Fields In Ascending Order 'Z-A'
    class Meta:
        ordering = ['MM_MonthName'] 



# Create your models here.
class main_menu(models.Model):
    m_menu_id = models.AutoField(primary_key=True)
    m_menu_name = models.CharField(max_length=50)
    m_menu_link = models.CharField(max_length=100)


class sub_menu(models.Model):
    s_menu_id = models.AutoField(primary_key=True)
    m_menu_id = models.IntegerField()
    s_menu_name = models.CharField(max_length=50)
    s_menu_link = models.CharField(max_length=100)