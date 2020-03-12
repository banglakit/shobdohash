from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='sobdohash',
    version='1.0.2',
    packages=['shobdohash'],
    url='https://github.com/banglakit/shobdohash',
    license='MIT',
    author='The BanglaKit Project and Contributors',
    author_email='contact@banglakit.org',
    description='Phonetically compare Bengali words',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Natural Language :: Bengali',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
