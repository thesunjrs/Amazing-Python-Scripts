import subprocess
import os
mypath = os.getcwd()
infofile = f'{mypath}/.git/config'


def takeInfo():
    print('No Existing repo info found\n')
    url = str(input('Enter the Github Repo URL: '))
    branch = str(input('Enter the branch: '))
    return ['n', url, branch]


def checkinfoInDir():
    if not (os.path.exists(infofile)):
        return takeInfo()
    url = subprocess.Popen(
        'git config --get remote.origin.url',
        stdout=subprocess.PIPE).stdout.read().decode('utf-8')

    branch = subprocess.Popen(
        'git rev-parse --symbolic-full-name HEAD',
        stdout=subprocess.PIPE).stdout.read().decode('utf-8')

    url, branch = url.split('\n')[0], branch.split('\n')[0].split('/')[2]
    return [url, branch]
