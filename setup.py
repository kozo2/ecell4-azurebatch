from setuptools import setup, find_packages

requirements = ['azure-batch', 'azure-storage-blob']

setup(name='ecell4_azurebatch',
	install_requires=requirements,
	author="Kozo Nishida",
	author_email='knishida@riken.jp',
	version='0.1.0',
	description='A command line tool to run E-Cell4 in Azure Batch.',
	url='https://github.com/kozo2/ecell4-azurebatch',
	license='GNU General Public License v2',
	packages=['ecell4_azurebatch'],
zip_safe=False)
