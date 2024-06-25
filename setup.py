from setuptools import setup, find_packages

setup(
    name='one_llm',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "openai",
        "anthropic"
    ],
    include_package_data=True,
    description='A brief description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/enesgrahovac/one_llm',
    license='MIT',  # or any other license
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python versions you support
)
