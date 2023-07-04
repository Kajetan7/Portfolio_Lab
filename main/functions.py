from .models import *
from datetime import date, time


def filling_db_with_categories():
    Category.objects.create(name='Ubrania')
    Category.objects.create(name='Ksiazki')
    Category.objects.create(name='Gotowka')
    Category.objects.create(name='Srodki czystosci')
    Category.objects.create(name='Artykuly spozywcze')
    Category.objects.create(name='Zabawki')
    Category.objects.create(name='Artykuly dla niemowlat')


def filling_db_with_institutions():
    Institution.objects.create(name='Fundacja Pomoc Dzieciom',
                               description='Wsparcie dla dzieci z rodzin w trudnej sytuacji życiowej', type=1)
    Institution.objects.create(name='Fundacja Pomoc Bezdomnym',
                               description='Pomoc dla osób bezdomnych w zdobywaniu schronienia i jedzenia', type=2)
    Institution.objects.create(name='Fundacja Nadzieja dla Wszystkich',
                               description='Wsparcie społeczności poprzez edukację', type=3)
    Institution.objects.create(name='Fundacja Ratowania Zwierząt',
                               description='Ratownictwo i rehabilitacja zwierząt w potrzebie', type=1)
    Institution.objects.create(name='Fundacja Ochrony Zdrowia', description='Poprawa dostępu do usług medycznych',
                               type=2)
    Institution.objects.create(name='Fundacja Ochrony Środowiska',
                               description='Ochrona i zachowanie środowiska naturalnego', type=3)
    Institution.objects.create(name='Fundacja Opieki nad Osobami Starszymi', description='Troska o dobrostan seniorów',
                               type=1)
    Institution.objects.create(name='Organizacja Pomocy przy Katastrofach',
                               description='Pomoc w czasie klęsk żywiołowych', type=2)
    Institution.objects.create(name='Inicjatywa Edukacji dla Wszystkich',
                               description='Zapewnienie jakościowej edukacji dla każdego dziecka', type=3)
    Institution.objects.create(name='Sieć Wsparcia Kobiet', description='Promocja równouprawnienia i wsparcie kobiet',
                               type=1)


def filling_db_with_institution_category_relation():
    InstitutionCategory.objects.create(institution_id=1, category_id=1)
    InstitutionCategory.objects.create(institution_id=2, category_id=2)
    InstitutionCategory.objects.create(institution_id=3, category_id=3)
    InstitutionCategory.objects.create(institution_id=4, category_id=4)
    InstitutionCategory.objects.create(institution_id=5, category_id=5)
    InstitutionCategory.objects.create(institution_id=6, category_id=6)
    InstitutionCategory.objects.create(institution_id=7, category_id=7)
    InstitutionCategory.objects.create(institution_id=8, category_id=1)
    InstitutionCategory.objects.create(institution_id=9, category_id=2)
    InstitutionCategory.objects.create(institution_id=10, category_id=3)


def filling_db_with_donations():
    Donation.objects.create(quantity=5, institution_id=1,
                            address='ul. Kwiatowa 1', phone_number='123456789',
                            city='Warszawa', zip_code='00-001',
                            pick_up_date=date(2023, 7, 4), pick_up_time=time(14, 30, 0),
                            pick_up_comment='Pierwsza donacja')

    Donation.objects.create(quantity=3, institution_id=2,
                            address='ul. Słoneczna 2', phone_number='987654321',
                            city='Kraków', zip_code='12-345',
                            pick_up_date=date(2022, 7, 4), pick_up_time=time(15, 30, 0),
                            pick_up_comment='Druga donacja')

    Donation.objects.create(quantity=2, institution_id=3,
                            address='ul. Polna 3', phone_number='555555555',
                            city='Gdańsk', zip_code='80-001',
                            pick_up_date=date(2021, 7, 4), pick_up_time=time(16, 30, 0),
                            pick_up_comment='Trzecia donacja')

    Donation.objects.create(quantity=4, institution_id=4,
                            address='ul. Leśna 4', phone_number='111222333',
                            city='Poznań', zip_code='60-123',
                            pick_up_date=date(2020, 7, 4), pick_up_time=time(17, 30, 0),
                            pick_up_comment='Czwarta donacja')

    Donation.objects.create(quantity=7, institution_id=5,
                            address='ul. Ogrodowa 5', phone_number='999888777',
                            city='Wrocław', zip_code='50-999',
                            pick_up_date=date(2019, 7, 4), pick_up_time=time(18, 30, 0),
                            pick_up_comment='Piąta donacja')

    Donation.objects.create(quantity=1, institution_id=6,
                            address='ul. Główna 6', phone_number='444555666',
                            city='Lublin', zip_code='20-111',
                            pick_up_date=date(2018, 7, 4), pick_up_time=time(19, 30, 0),
                            pick_up_comment='Szósta donacja')

    Donation.objects.create(quantity=8, institution_id=7,
                            address='ul. Nowa 7', phone_number='777888999',
                            city='Szczecin', zip_code='70-777',
                            pick_up_date=date(2017, 7, 4), pick_up_time=time(20, 30, 0),
                            pick_up_comment='Siódma donacja')


def filling_db_with_donation_category_relation():
    DonationCategory.objects.create(donation_id=1, category_id=1)
    DonationCategory.objects.create(donation_id=2, category_id=2)
    DonationCategory.objects.create(donation_id=3, category_id=3)
    DonationCategory.objects.create(donation_id=4, category_id=4)
    DonationCategory.objects.create(donation_id=5, category_id=5)
    DonationCategory.objects.create(donation_id=6, category_id=6)
    DonationCategory.objects.create(donation_id=7, category_id=7)
