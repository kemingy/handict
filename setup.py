from setuptools import setup, find_packages
from os import path
from io import open
from Cython.Build import cythonize


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = [req.strip() for req in f if req]


setup(
    name='handict',
    version='0.0.1',
    author='Keming Yang',
    author_email='kemingy94@gmail.com',
    description=('Yet another word segmentation tool.'),
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/kemingy/handict',
    packages=find_packages(exclude=['examples*', 'tests*']),
    package_data={},
    ext_modules=cythonize(
        [],
        compiler_directives={
            'language_level': 3,  # Python3
        }
    ),
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    install_requires=requires,
    extras_require={},
    zip_safe=False,
    entry_points={
        'console_scripts': [],
    },
)