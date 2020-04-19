from fabric.api import local

def deploy():
    local('docker build -t garciadiazjaime/website-acarrillo .')
    local('docker push garciadiazjaime/website-acarrillo')
    local('echo "docker pull garciadiazjaime/website-acarrillo"')
