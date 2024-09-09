from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run

REPO_URL = 'https://github.com/troshchiy/flashnote.git'


def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder, env.host)
    _get_latest_source(source_folder)
    _update_virtualenv(source_folder)
    _update_settings(source_folder, env.host)
    _update_static_files(source_folder, env.host)
    _update_database(source_folder)


def _create_directory_structure_if_necessary(site_folder, site_name):
    for subfolder in ('static', 'virtualenv', 'source'):
        run(f'mkdir -p {site_folder}/{subfolder}')
    run(f'sudo mkdir -p /var/www/{site_name}')


def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run(f'cd {source_folder} && git fetch')
    else:
        run(f'git clone {REPO_URL} {source_folder}')
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run(f'cd {source_folder} && git reset --hard {current_commit}')


def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run(f'python3 -m venv {virtualenv_folder}')
    run(f'{virtualenv_folder}/bin/pip install -r {source_folder}/requirements.txt')


def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/flashnote/flashnote/settings.py'
    sed(settings_path, 'DEBUG = True', 'DEBUG = False')
    sed(settings_path, 'ALLOWED_HOSTS = .+$', f'ALLOWED_HOSTS = ["{site_name}"]')
    sed(settings_path, 'STATIC_ROOT = .+$', f'STATIC_ROOT = "/var/www/{site_name}/static"')
    secret_key_file = source_folder + '/flashnote/flashnote/secret_key.py'
    if not exists(secret_key_file):
        key = run(f'{source_folder}/../virtualenv/bin/python -c '
                  '"from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"')
        append(secret_key_file, f'SECRET_KEY = "{key}"')
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')


def _update_static_files(source_folder, site_name):
    run(f'cd {source_folder}/flashnote && ../../virtualenv/bin/python manage.py collectstatic --noinput')


def _update_database(source_folder):
    if exists(source_folder + '/.env'):
        run(f'cd {source_folder}/flashnote && ../../virtualenv/bin/python manage.py migrate --noinput')
