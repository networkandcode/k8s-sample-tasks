import os

namespaces = {'staging': '30100', 'production': '30200'}
directories = ['deploy', 'svc']

for namespace, nodeport in namespaces.items():
    for directory in directories:
        os.system("sed -i 's/NamespaceName/{}/g' {}/*".format(namespace, directory))
        files = os.popen('ls {}'.format(directory)).read().split()
        for file in files:
            if 'frontend' in file:
                os.system("sed -i 's/NodePortNumber/{}/g' {}/{}".format(nodeport, directory, file))
            os.system('kubectl create -f {}/{}'.format(directory, file))
            if 'frontend' in file:
                os.system("sed -i 's/{}/NodePortNumber/g' {}/{}".format(nodeport, directory, file))
        os.system("sed -i 's/{}/NamespaceName/g' {}/*".format(namespace, directory))

