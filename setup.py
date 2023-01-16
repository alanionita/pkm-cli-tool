from setuptools import setup, find_namespace_packages
from setuptools import find_packages  # or find_namespace_packages

if __name__ == "__main__":
    # setup(
    #     name='pkm-cli',
    #     version='0.0.1',
    #     py_modules=['pkm-cli'],
    #     install_requires=[
    #         'click',
    #         'frontmatter',
    #         'pyyaml',
    #         'ulid-py'
    #     ],
    #     package_dir={"":"pkm-cli"},
    #     packages=find_packages(
    #         # All keyword arguments below are optional:
    #         where='pkm-cli',  # '.' by default
    #         include=['*'],  # ['*'] by default
    #         exclude=['my_notes'],  # empty by default
    #     ),
    #     include_package_data=True,
    #     entry_points='''
    #         [console_scripts]
    #         pkm-cli=main:cli
    #     '''
    # )
    setup()