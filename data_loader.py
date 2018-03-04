import json, os, sys

#find current directory path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#find project path
project_path = os.path.join(BASE_DIR)

#find all project related stuff
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mineral_Catalogue.settings")

#append project path to Django system
sys.path.append(project_path)

#emsure project models get loaded
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#reference models
from minerals.models import Mineral


def get_mineral_data(mineral):
    """Creates the dictionary with all possible fields for a mineral."""
    full_mineral_dict = {
        'name': None,
        'image filename': None,
        'image caption': None,
        'category': None,
        'formula': None,
        'strunz classification': None,
        'crystal system': None,
        'unit cell': None,
        'color': None,
        'crystal symmetry': None,
        'cleavage': None,
        'mohs scale hardness': None,
        'luster': None,
        'streak': None,
        'diaphaneity': None,
        'optical properties': None,
        'refractive index': None,
        'crystal habit': None,
        'specific gravity': None
    }
    for key, value in mineral.items():
        full_mineral_dict[key] = value
    return full_mineral_dict


with open('fixtures.json', 'w') as fixture:
    minerals = json.load(open('minerals.json'))
    for mineral in minerals:
        data = get_mineral_data(mineral=mineral)
        Mineral(
            name=data['name'],
            image_filename=data['image filename'],
            image_caption=data['image caption'],
            category=data['category'],
            formula=data['formula'],
            strunz_classification=data['strunz classification'],
            crystal_system=data['crystal system'],
            unit_cell=data['unit cell'],
            color=data['color'],
            crystal_symmetry=data['crystal symmetry'],
            cleavage=data['cleavage'],
            mohs_scale_hardness=data['mohs scale hardness'],
            luster=data['luster'],
            streak=data['streak'],
            diaphaneity=data['diaphaneity'],
            optical_properties=data['optical properties'],
            group=data['group'],
            refractive_index=data['refractive index'],
            crystal_habit=data['crystal habit'],
            specific_gravity=data['specific gravity']
        ).save()
