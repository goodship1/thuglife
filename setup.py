
from  setuptools import setup

setup(
        name = 'thuglife',
        version = '0.3',
        py_modules=['Thuglife'],
        intstall_requires = [
            'click',
            'opencv'
            ],
        entry_points = '''
                [console_scripts]
                Thuglife = Thuglife:cli
                ''',

                )

  
                          
