Instrucciones para ejecutar este proyecto: 

Clonar el proyecto y cambiar de rama:


git clone https://github.com/Esk4a/Entrega1-Rial-Boim-Aguerre.git

cd Entrega1-Rial-Boim-Aguerre

git checkout proyectocoder


No olvide agregar los directorios de Templates y Scripts en el "Settings" del propyecto 

Crear base de datos con los Modelos (hacer migraciones y migrar):


python3 manage.py makemigrations Appfinal
python3 manage.py migrate

Crear super-usuario:


python3 manage.py createsuperuser

Ejecutar proyecto:

python3 manage.py runserver

Visualizar Web en:
127.0.0.1/Appfinal/

Donde se encuentra una barra de navegacion superior con las entradas "Inicio" "Sucursales" "Contactos" "Peliculas"
  Esta ultima, con una opcion para buscar por titulo en la lista de agregados.

 Y una entradas inferiores con opcion para agregar contenido a estas pestañas previamente mencionadas.
