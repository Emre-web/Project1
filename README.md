# Courseapp

Courseapp is a Django-based application where users can view, add and delete courses. Users can register, log in and list courses. Authorized users can add and delete courses via the admin panel.

## Technologies Used
- Django
- Django REST Framework
- SQLite

## Features
- User registration and login.
- Course listing.
- Course adding and deleting operations for authorized users.

## Installation
1. Clone the repo:
bash
git clone https://github.com/Emre-web/Project1.git
Go to the project directory:

bash
Copy the code
cd courseapp
Create and activate the virtual environment:

bash
Copy the code
python -m venv venv
source venv/bin/activate # For Windows: venv\Scripts\activate
Install dependencies:

bash
Copy the code
pip install -r requirements.txt
Create the database:

bash
Copy the code
python manage.py migrate
Create a superuser:

bash
Copy the code
python manage.py createsuperuser
Start the server:

bash
Copy the code
python manage.py runserver
Usage
After logging in to the project, you can view the courses and access the courses by logging in as a user.
You can add and delete courses by logging into the admin panel or via the application.

Contribution
You can submit a pull request to contribute to the project. Please explain your changes and add any necessary tests.



----------------------------------------------------------------------------------------------------------------------







# Courseapp

Courseapp, kullanıcıların kursları görüntüleyebileceği, kurs ekleyip silebileceği bir Django tabanlı uygulamadır. Kullanıcılar kayıt olabilir, giriş yapabilir ve kursları listeleyebilirler. Yetkili kullanıcılar admin paneli üzerinden kurs ekleyebilir ve silebilirler.

## Kullanılan Teknolojiler
- Django
- Django REST Framework
- SQLite

## Özellikler
- Kullanıcı kayıt olma ve giriş yapma.
- Kurs listeleme.
- Yetkili kullanıcılar için kurs ekleme ve silme işlemleri.

## Kurulum

1. Reposu klonlayın:
   ```bash
   git clone https://github.com/Emre-web/Project1.git
Proje dizinine gidin:

bash
Kodu kopyala
cd courseapp
Sanal ortam oluşturun ve aktifleştirin:

bash
Kodu kopyala
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
Bağımlılıkları yükleyin:

bash
Kodu kopyala
pip install -r requirements.txt
Veritabanını oluşturun:

bash
Kodu kopyala
python manage.py migrate
Superuser oluşturun:

bash
Kodu kopyala
python manage.py createsuperuser
Sunucuyu başlatın:

bash
Kodu kopyala
python manage.py runserver
Kullanım
Projeye giriş yaptıktan sonra kursları görüntüleyebilir, kullanıcı girişi yaparak kurslara erişebilirsiniz.
Admin paneline giriş yaparak veya uygulama ğzerinden kurs ekleyebilir ve silebilirsiniz.
Katkı
Projeye katkıda bulunmak için pull request gönderebilirsiniz. Lütfen değişikliklerinizi açıklayın ve gerekli testleri ekleyin.
