import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='BlaguesApi',
    packages=['BlaguesApi'],
    version='1.0',
    license='MIT',
    description='Python API wrapper for BlaguesAPI.fr',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='coco875',
    author_email='pereira.jannin@gmail.com',
    url='https://github.com/coco875/BlagueAPI',
    download_url='https://github.com/coco875/BlagueAPI/archive/refs/tags/v_08.tar.gz',
    keywords=['API', 'Joke', 'French'],
    install_requires=[
        'jaro-winkler',
        'requests',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    python_requires=">=3.6",
)
