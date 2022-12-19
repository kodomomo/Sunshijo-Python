

def run_macro():
    import os
    import subprocess

    file_path = os.getcwd() + '/macro_structure.py'

    subprocess.run(['python3', file_path])

    exit()