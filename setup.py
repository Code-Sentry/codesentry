from setuptools import setup, find_packages

setup(
    name='codesentry',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Adicione dependências aqui
    ],
    entry_points={
        'console_scripts': [
            'codesentry=codesentry.main:main',
        ],
    },
)