Provisioning a new site
========================
## Required packages:
* nginx
* Python 3.12
* virtualenv + pip
* Git

## Nginx Virtual Host config
* see nginx.template.conf
* replace SITENAME with, e.g. staging.my-domain.com

## Systemd service
* see gunicorn-systemd.template.service
* replace SITENAME with, e.g. staging.my-domain.com

## Folder structure
Assume we have a user account at /home/username

/home/username

    ├── sites
        ├── SITENAME
            ├── database
            ├── source
            ├── static
            └── virtualenv