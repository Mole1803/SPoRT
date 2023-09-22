def update_venv():
    import subprocess
    subprocess.run(['pip', 'freeze', '>', 'requirements.txt'])


def install_requirements():
    import subprocess
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])


if __name__ == '__main__':
    update_venv()
    install_requirements()
