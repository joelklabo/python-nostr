from setuptools import setup, find_packages

setup(
    name='nostr',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'cffi>=1.15.0',
        'cryptography>=37.0.4',
        'pycparser>=2.21',
        'secp256k1>=0.14.0',
        'websocket-client>=1.3.3',
    ]
)
