from pkg_resources import parse_version
from configparser import ConfigParser
import setuptools
assert parse_version(setuptools.__version__)>=parse_version('36.2')

# note: all settings are in settings.ini; edit there, not here
config = ConfigParser(delimiters=['='])
config.read('settings.ini')
config = config['DEFAULT']

config_keys = 'version description keywords author author_email'.split()
expected = config_keys + "lib_name user branch license status min_python audience language".split()

for setting in expected: 
    assert setting in config, f"missing expected setting: {setting}"

setup_config = {setting:config[setting] for setting in config_keys}

licenses = {
    'apache2': ('Apache Software License 2.0','OSI Approved :: Apache Software License'),
}
statuses = [ '1 - Planning', '2 - Pre-Alpha', '3 - Alpha',
    '4 - Beta', '5 - Production/Stable', '6 - Mature', '7 - Inactive' ]
py_versions = '2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9'.split()

requirements = config.get('requirements','').split()
lic = licenses[config['license']]
min_python = config['min_python']

setuptools.setup(
    name = config['lib_name'],
    license = lic[0],
    classifiers = [
        'Development Status :: ' + statuses[int(config['status'])],
        'Intended Audience :: ' + config['audience'].title(),
        'License :: ' + lic[1],
        'Natural Language :: ' + config['language'].title(),
    ] + [f'Programming Language :: Python :: {version}' for version in py_versions[py_versions.index(min_python):]],
    url = config['git_url'],
    packages = setuptools.find_packages(),
    include_package_data = True,
    install_requires = requirements,
    dependency_links = config.get('dep_links','').split(),
    python_requires  = '>=' + config['min_python'],
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    zip_safe = False,
    entry_points = { 'console_scripts': config.get('console_scripts','').split() },
    **setup_config)

