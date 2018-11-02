from setuptools import setup

setup(name='baybars',
      version='0.0.5',
      description='Python Common Packages',
      copyright='Copyright 2018 Jet.com',
      url='http://pypi.org/project/baybars/',
      author='Bugra Akyildiz',
      author_email='bugra.akyildiz@jet.com',
      license='Apache 2.0',
      packages=['baybars'],
      install_requires=[
        'python-consul==0.7.2',
        'azure-storage-blob==0.37.0',
        'azure-storage-queue==0.37.0',
        'confluent-kafka==0.11.0',
        'azure-cosmos==3.0.1 ',
        'pysftp==0.2.9',
        'requests==2.17.3',
        'numpy==1.14.1',
        'pandas==0.20.3',
        'python-consul==0.7.2',
        'PyHive==0.5.0'
      ],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
      ],
      keywords='azure kafka blob documentdb cosmosdb queue tar',
      python_requires='>=3.5',
      zip_safe=False)
