

__author__ = "AZIZI Sajjad"
__author_email__ = "sajjaad.azizi@yahoo.com"
__copyright__ = "Copyright (c) 2021 SDACO, Inc."
__license__ = "LIBRE SERVICE"


'''
Prérequis  : à installer
pip install proxmoxer
pip install requests
pip install paramiko

Référence :
https://pypi.org/project/proxmoxer/
'''

from proxmoxer import ProxmoxAPI
# Importer le Module proxmoxer et sa

proxmoxServers = ['192.168.2.160', 'sdmox']
# Créer une liste d'IP ou des FQDN des serveurs ProxMox existant sur le réseau
# Les deux membres de la liste sont le même serveur
# /!\ En cas d'utilisation du nom du DNS, l'IP du serveur doit être atteignable avec son NOM /!\

for proxmoxSrv in proxmoxServers:
    proxmox = ProxmoxAPI(proxmoxSrv, user='root@pam', password='rootroot', verify_ssl=False)
    #print ("proxmox TYPE : ", type(proxmox))
    # Imprimer le type de la variable "proxmox", permettant d'établir la connexion aux serveurs PROXMOX
    # Il s'agit d'une CLASS, d'autre élément qui montre que le type est de la CLASS, c'est le fait d'avoir multiples paramètres entre parenthèses
    print('État des VM du serveur ProxMox : %s' %(proxmoxSrv))
    # Imprimer le nom
    for vm in proxmox.cluster.resources.get(type='vm'):
        print("VM-ID : {0} \nNOM : {1} \nStatus: {2}" .format(vm['vmid'], vm['name'], vm['status']))
        print("*" * 20)


'''
import proxmoxer

proxmoxServers = ['192.168.2.160', 'sdmox']
# Créer une liste d'IP ou des FQDN des serveurs ProxMox existant sur le réseau
# Les deux membres de la liste sont le même serveur
# /!\ En cas d'utilisation du nom du DNS, l'IP du serveur doit être atteignable avec son NOM /!\

for i in proxmoxServers:
    proxmox = proxmoxer.ProxmoxAPI('192.168.2.160', user='root@pam', password='rootroot', verify_ssl=False)
    for vm in proxmox.cluster.resources.get(type='vm'):
        print("{0}. {1} => {2}" .format(vm['vmid'], vm['name'], vm['status']))
        print("*" * 20)
'''



'''
# Obteinir l'état des VMs via la fonction
# Elle prend qu'un paramètre qui est une liste
# Les deux membres de la liste sont le même serveur

proxmoxServers = ['192.168.2.160', '192.168.2.160']
# Créer une liste d'IP ou des FQDN des serveurs ProxMox existant sur le réseau
# Les deux membres de la liste sont le même serveur
# /!\ En cas d'utilisation du nom du DNS, l'IP du serveur doit être atteignable avec son NOM /!\


def getProxMoxVMStatus(ProxMoxServeursliste):
    from proxmoxer import ProxmoxAPI
    # Importer le Module proxmoxer et sa
    for proxmoxSrv in ProxMoxServeursliste:
        proxmox = ProxmoxAPI(proxmoxSrv, user='root@pam', password='rootroot', verify_ssl=False)
        #print ("proxmox TYPE : ", type(proxmox))
        # Imprimer le type de la variable "proxmox", permettant d'établir la connexion aux serveurs PROXMOX
        print('État des VM du serveur ProxMox : %s' %(proxmoxSrv))
        for vm in proxmox.cluster.resources.get(type='vm'):
            print("VM-ID : {0} \nNOM : {1} \nStatus: {2}" .format(vm['vmid'], vm['name'], vm['status']))
            print("*" * 20)
getProxMoxVMStatus(proxmoxServers)
'''