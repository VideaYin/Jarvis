import os
from backend import settings
import yaml

def init_app_data():
    data_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(data_file, 'r',encoding='utf-8') as f:
        apps = yaml.load(f)
        return apps

def get_menu(request):
    global_app_data = init_app_data()
    published_app_data = global_app_data.get('published')
