# Setting up your dev environment
Examples given for Ubuntu 16.04 LTS on the WSL.

## Install Python 3.8

Default Python 3 on Ubuntu 16 is 3.6, we want 3.8

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
```

## Python Virtual env

It is *STRONGLY* (looking at you Squiddy) recommended you use a python virtual env to install python
modules for this repo.

Install Python3.8 virtual env using in-built venv tool (python 3.8 must be
installed before this).
If you want to make the venv with a different name but still store it in the
repo locally, make sure you add to the .gitignore

#### Installation
```bash
sudo apt update
sudo install python3.8-venv
python3.8 -m venv /path/to/repo/.chess_venv
```

#### Activation
Assuming you are in the repo root dir
```bash
source .chess_venv/bin/activate
```

#### Make sure its working
Should return paths ending `.../[venv name]/bin/[pip/python]`  
e.g `/mnt/c/Users/domin.D35K70P/Documents/git/chess/.chess_venv/bin/python`
```bash
which python ; which pip
```

#### Install packages from file
```bash
pip install -r requirements.txt
```

#### Add packages to file
First install them to the venv using pip, then run (with the venv activated):
```bash
pip freeze > requirements.txt
```

#### Deactivation
```bash
deactivate
```
