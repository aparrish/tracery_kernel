from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='tracery_kernel',
    version='0.0.1',
    packages=['tracery_kernel'],
    description='A Jupyter Notebook kernel for Tracery grammars',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Allison Parrish',
    author_email='allison@decontextualize.com',
    url='https://github.com/aparrish/tracery_kernel',
    install_requires=[
        'jupyter_client', 'IPython', 'ipykernel', 'tracery'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
