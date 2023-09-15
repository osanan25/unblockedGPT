from setuptools import setup, find_packages

setup(
    name='unblockedGPT',
    version='0.3.6',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'requests',
        'openai',
        'pycryptodome',  # This provides the Crypto module
    ],
    entry_points={
        'console_scripts': [
            'chat = unblockedGPT.run_app:run',
        ],
    },
)
