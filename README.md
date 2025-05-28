<h1>Pasos para ejecutar app</h1>
<li>cd /home/labs/GestionPacientes/</li>
<li>sudo apt install python3-pip</li>
<li>sudo pip install Django==2.1.5 psycopg2-binary==2.8.6 requests</li>
<li>cd gestionPacientes</li>
<li>sudo python3 manage.py makemigrations</li>
<li>sudo python3 manage.py migrate</li>
<li>sudo python3 manage.py runserver 0.0.0.0:8080</li>
