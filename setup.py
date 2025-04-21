from setuptools import setup, find_packages

setup(
    name='edabox',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.3.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0',
    ],
    author='Kiw',
    description='A reusable and modular EDA toolkit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Kyu-IC/EDA-Box',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
