from setuptools import setup, find_packages


setup(
    name='combo',
    version='0.1',
    description='A fantastic toolset for hacker',
    author='tkorays',
    author_email='tkorays@hotmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    scripts=[],
    data_files=[],
    entry_points={
        'console_scripts': [
            'combo=Combo.CLI.combo:combo'
        ]
    },
    install_requires=[

    ],
    dependency_links=[

    ],
    long_description='''
    Combo is a fantastic toolset for hacker.
    '''
)
