# Configuration WSGI pour PythonAnywhere
# Remplacez le contenu de votre fichier wsgi.py par ceci

import os
import sys

# Chemin vers votre projet Django
path = '/home/willaz/Frameworks-master'
if path not in sys.path:
    sys.path.append(path)

# Configuration de l'environnement Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'dcwf.settings'

# Import de l'application WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
