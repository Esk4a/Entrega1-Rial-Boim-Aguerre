Instrucciones para ejecutar este proyecto:

Clonar el proyecto y cambiar de rama


git clone https://github.com/Esk4a/Entrega1-Rial-Boim-Aguerre.git

cd Entrega1-Rial-Boim-Aguerre

git checkout proyectocoder

Crear base de datos con los Modelos (hacer migraciones y migrar):


python manage.py makemigrations Appfinal
python manage.py migrate

Crear super-usuario


python manage.py createsuperuser

Ejecutar proyecto

python manage.py runserver

Visualizar Web en:
127.0.0.1/Appfinal/

