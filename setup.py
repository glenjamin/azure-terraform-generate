from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError) as ex:
    print("Pandoc failed", ex)
    long_description = open('README.md').read()

setup(
    name='aztfgen',
    version='0.1.3',
    description='Generate terraform config from deployed azure resources.',
    long_description=long_description,
    url='http://github.com/glenjamin/azure-terraform-generate',
    author='Glen Mailer',
    author_email='glen@stainlessed.co.uk',
    license='MIT',
    packages=['aztfgen', 'aztfgen.resources'],
    python_requires='>=3.5',
    zip_safe=False,
    entry_points = {
        'console_scripts': ['aztfgen=aztfgen:main'],
    }
)
