from django.db import models
from django.template.defaultfilters import slugify
from django.utils.timezone import now
from uuid import uuid4
from .department import DEPARTMENTS

# Create your models here.
class UtilFields(models.Model):

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = now()
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]

        self.last_updated = now()

        super(UtilFields, self).save(*args, **kwargs)
    

class FaClerkInformation(UtilFields):
    
    DEPT_CHOICES =[
    ['000', "NA - Not Available"],
 ['100', "Executive President's Office"],
 ['101', 'CBC Proportionate Giving'],
 ['110', 'Nkwen Baptist Centre'],
 ['138', 'Rest House - Bamenda'],
 ['140', 'Evangelism & Missions Admin.'],
 ['144', 'Bassossia Mission Station'],
 ['145', 'National Missionaries'],
 ['150', 'Foreign Missions'],
 ['170', 'Theological & Christian Education'],
 ['180', '"Cameroon Baptist Theological Seminary, Ndu"'],
 ['181', 'Rest House - CBTS - Ndu'],
 ['185', '"CBTS, Kumba Campus"'],
 ['200', 'Education Department Administration'],
 ['202', 'Baptist Book Depot & Supplies'],
 ['203', 'ED Chaplain Coordinator Office'],
 ['206', 'ED Rest Houses'],
 ['250', 'Buea Managerial Area'],
 ['252', 'Bamenda Managerial Area'],
 ['255', 'Ndu Managerial Area'],
 ['256', 'West Region Primary Schools'],
 ['260', "CBC Classical Sch Centenary L'be"],
 ['262', 'CBC Classical School Musang'],
 ['265', '"CBC Early Childhood Education, Soppo"'],
 ['300', '"Saker Baptist College, Limbe"'],
 ['301', '"Baptist High School, Buea"'],
 ['307', '"Baptist High School, Yaounde"'],
 ['310', '"Baptist Comprehensive High School, Nkwen"'],
 ['311', '"Baptist Comprehensive College, Soppo"'],
 ['320', '"Baptist Teacher Training College, Ndop"'],
 ['400', 'Health Services Admininstration'],
 ['405', 'Mbingo Baptist Hospital'],
 ['406', "Mbingo Hansen's disease Department"],
 ['407', 'Mbingo Eye Department'],
 ['409', 'Mbingo ENT'],
 ['413', 'Mbingo Metal Workshop'],
 ['414', 'Mbingo Cattle Ranch'],
 ['415', 'Mbingo Provision Shop'],
 ['417', 'Mbingo Carpentry Workshop'],
 ['418', '"CBC Inclusive PS & Sign Language Ctr, Mbingo"'],
 ['419', 'Mbingo Vocational Rehabilitation'],
 ['425', 'Baptist Institute of Health Sciences'],
 ['430', 'Banso Baptist Hospital'],
 ['431', '"PAACS, Banso"'],
 ['432', 'Banso Eye Department'],
 ['435', 'Baptist Training School for Health Personnel'],
 ['436', 'Banso Bookshop'],
 ['438', 'BBH Canteen'],
 ['439', '"CBC Inclusive PS & Braille Ctr, Kumbo"'],
 ['445', '"Meskine Baptist Hospital, Maroua"'],
 ['450', 'Baptist Hospital Mutengene'],
 ['451', 'BHM Orthopedics'],
 ['452', 'BHM Eye Department'],
 ['455', 'Ekounou Baptist Health Centre'],
 ['456', 'Ekounou Eye Department'],
 ['460', '"Mboppi Baptist Hospital, Douala"'],
 ['461', 'Mboppi Eye Department'],
 ['466', 'Mboppi Provision Shop'],
 ['467', 'Mboppi Canteen'],
 ['470', 'Baptist Hospital Banyo'],
 ['475', '"Etoug-Ebe Baptist Hospital, Yaounde"'],
 ['476', 'Etoug-Ebe Eye Department'],
 ['480', 'Nkwen Baptist Health Centre'],
 ['481', 'Nkwen Eye Department'],
 ['485', 'Bafoussam Baptist Health Centre'],
 ['486', 'Bafoussam Eye Department'],
 ['490', 'Ngounso Baptist Health Centre'],
 ['491', 'Ngounso Provision Shop'],
 ['495', 'Kumba Baptist Health Centre'],
 ['499', '"Dunger Baptist Hospital, Mbem"'],
 ['500', 'Belo Baptist Health Centre'],
 ['501', 'Ashong Baptist Health Centre'],
 ['502', 'Kwighe Baptist Health Centre'],
 ['503', 'Sabga Baptist Health Centre'],
 ['504', 'Finkwi Baptist Health Centre'],
 ['505', 'Bayangam Baptist Health Centre'],
 ['506', 'Ndebaya Baptist Health Centre'],
 ['507', 'Mamfe Baptist Health Centre'],
 ['508', 'Akeh Baptist Health Centre'],
 ['520', 'Koussam Baptist Health Centre'],
 ['521', 'Nwat Baptist Health Centre'],
 ['522', 'Jikijem Baptist Health Centre'],
 ['523', 'Bangolan Baptist Health Centre'],
 ['524', 'Ndu Baptist Health Centre'],
 ['525', 'Kouahouat Baptist Health Centre'],
 ['526', 'Ngeptang Baptist Health Centre'],
 ['527', 'Lassin Baptist Health Centre'],
 ['528', 'Romkong Baptist Health Centre'],
 ['540', 'Bafia-Muyuka Baptist Health Centre'],
 ['541', 'Ekondo Titi Baptist Health Centre'],
 ['560', 'Nyamboya Baptist Health Centre'],
 ['561', 'Allat Baptist Health Centre'],
 ['562', 'Sarki Barka Baptist Health Centre'],
 ['563', 'Tibati Baptist Health Centre'],
 ['571', 'Voundou Baptist Health Centre'],
 ['572', 'Nkoabang Baptist Health Centre'],
 ['580', 'Kribi Baptist Health Centre'],
 ['581', 'Baptist Health Centre Bonaberi'],
 ['601', 'Life Abundant Program'],
 ['602', 'LAP/BFTW Project'],
 ['609', 'Mental Health Services'],
 ['612', 'SEEPD'],
 ['615', 'Chosen Children Program'],
 ['616', "Women's Health Program"],
 ['618', 'Empowerment & Disability Inclusive Development'],
 ['619', 'Cameroon Clubfoot Care Project'],
 ['620', 'CBCHS Community Based Rehabilitation (CBR)'],
 ['621', 'CBCHS- Hope & Healing International Partnership'],
 ['622', 'CBCHS- Inclusive Eye Care Project'],
 ['630', 'Central Pharmacy-Distribution'],
 ['631', 'CP Sterile Production'],
 ['632', 'CP  Non-Sterile Production'],
 ['633', 'CP Chemical Production'],
 ['634', 'CP Quality Assurance'],
 ['636', 'HESCO Water Bottling'],
 ['637', 'Mutengene Health Serv. Complex'],
 ['638', 'Regional Training School Mutengene'],
 ['650', 'HS Technical Services Dept.'],
 ['660', 'HS Rest House - Bamenda'],
 ['661', 'HS Rest House - Etoug-Ebe'],
 ['662', 'HS Rest House - Banso'],
 ['663', 'HS Rest House - Mbingo'],
 ['665', 'HS Rest House - Mutengene'],
 ['667', 'HS Hostel - Mbingo'],
 ['668', 'HS Hostel - Banso'],
 ['669', 'LAP Canteen/Rest House'],
 ['670', 'Mbingo Eating House'],
 ['671', 'Nkwen HC Eating House'],
 ['690', 'Cameroon Health & Education Fund'],
 ['691', 'Strategy 9 Project'],
 ['700', 'Finance sub-Department'],
 ['701', 'Development sub-Department'],
 ['702', 'Self Precautionary Scheme'],
 ['703', 'CBC Development Fund'],
 ['721', 'Printing Press'],
 ['722', 'Communication - Bamenda'],
 ['723', 'Communications - Buea'],
 ['740', "Women's Department"],
 ['760', "Men's Department"],
 ['780', "Youth & Students' Department"],
 ['900', 'Director of Cooperating Missions'],
 ['901', 'Cooperating Missions Administration'],
 ['903', 'CMF Hostel'],
 ['904', 'Hostel Studio Apt.'],
 ['905', 'Converge (BGC)'],
 ['906', 'World Team Ministries'],
 ['907', 'NAB Administration'],
 ['908', 'NAB Fulfulde Ministries'],
 ['911', 'Christian Supply Center']]
    
    name = models.CharField(null=True, blank=True, max_length=100)
    dept_number = models.CharField(null=True, blank=True, max_length=3, choices=DEPT_CHOICES)
    dept_name = models.CharField(null=True, blank=True, max_length=100)
    phone_number = models.CharField(null=True, blank=True, max_length=100)
    email = models.CharField(null=True, blank=True, max_length=100)
    
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    
    def __str__(self):
        return '{} {} {}'.format(self.name, self.dept_number, self.dept_name)
    
    
    def get_absolute_url(self):
        return reverse('fa-clerk', kwargs={'slug': self.slug})
    
    
    def save(self, *args, **kwargs):
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            
        self.dept_name = DEPARTMENTS.get(self.dept_number, 'None')
        
        self.slug = slugify('{} {} {}'.format(self.name, self.dept_number, self.uniqueId))
        
        super(FaClerkInformation, self).save(*args, **kwargs)