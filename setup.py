from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

#with open('LICENSE') as f:
#    license = f.read()

setup(
    name='k8sTranslator',
    version='0.1.0',
    description='package for translating TOSCA normative templates into kubernetes YAML files',
    long_description=readme,
    author='Borisova Alexandra',
    packages=find_packages(exclude=('k8stranslator')),
    entry_points={
        'console_scripts':['kube-parser = k8stranslator.shell:main']},
    classifiers= [
        'Environment :: ISP RAS'
        'Intended Audience :: Information Technology'
        'Intended Audience :: System Administrators'
        'Operating System :: POSIX :: Linux'
        'Programming Language :: Python'
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.6'],
)
