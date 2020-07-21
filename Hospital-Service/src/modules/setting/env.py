from pathlib import Path
import os
import subprocess

def get_root_path():
    try:
        mypath = os.path.dirname(os.path.abspath(__file__))
        root_path =  Path(mypath).parent.parent.parent.parent 

        return str(root_path)
    except Exception as e:
        print(str(e))                

def get_env():
    try:
        env = os.environ['ISM_HOME']
        print(env)
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    get_env()