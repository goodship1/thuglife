from setuptools import setup

setup(
        name = "thuglife",
        version = '0.1',
        py_modules = ['thuglife'],
        install_requires= ["click",'opencv'],
        entry_points = ''' [console_scripts]
                          thuglife = thuglife:cli'''
                          ,
                          )

                          
                          
