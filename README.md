# Semestral de protocolos

## Initial Setup

### Router 1 Setup

```sh
enable
configure terminal
hostname R1
no ip domain lookup

enable secret class
line console 0
 password cisco
 login
 logging synchronous
exit

line vty 0 4
 password cisco
 login
 logging synchronous
exit
banner motd #Acceso no autorizado está prohibido#

interface g0/0
 ip address 192.168.110.1 255.255.255.0
 no shutdown
exit

interface g0/1
 ip address 192.168.100.2 255.255.255.0
 no shutdown
exit

router ospf 1
  router-id 1.1.1.1
  network 192.168.100.0 0.0.0.255 area 0
  network 192.168.110.0 0.0.0.255 area 0
end

copy running-config startup-config
```

### Router 2 Setup

```sh
enable
configure terminal
hostname R2
no ip domain lookup

enable secret class
line console 0
 password cisco
 login
 logging synchronous
exit

line vty 0 4
 password cisco
 login
 logging synchronous
exit
banner motd #Acceso no autorizado está prohibido#

interface g0/0
 ip address 192.168.110.2 255.255.255.0
 no shutdown
exit

interface g0/1
 ip address 192.168.120.2 255.255.255.0
 no shutdown
exit

router ospf 1
  router-id 2.2.2.2
  network 192.168.110.0 0.0.0.255 area 0
  network 192.168.120.0 0.0.0.255 area 0
end

copy running-config startup-config
```

### OSPFv2 Optimization

```sh
interface g0/0
ip ospf priority 50
```

### Setup SSH Connection in Router IOS XE

```sh
enable
configure terminal
hostname R3
no ip domain lookup

ip domain-name semestral.local
crypto key generate rsa modulus 2048
username admin privilege 15 secret password
ip ssh version 2
line vty 0 4
 login local
 transport input ssh
exit

line console 0
  logging synchronous
exit

interface GigabitEthernet 1
 ip address 192.168.150.1 255.255.255.0
 no shutdown
exit

netconf-yang

exit
copy running-config startup-config

ip ssh pubkey-chain
username admin
key-string
<ssh-key>
```

### Configure ubuntu server

```sh
sudo apt update
sudo apt install git python3-pip python3-venv

# Add the key to Github
ssh-keygen -t rsa
git clone git@github.com:jerry-whoami/protocolos.semestral.git Semestral

# When adding it to the router
fold -w72 .ssh/id_rsa.pub

sudo nmcli con mod "Wired connection 1" ipv4.addresses 192.168.150.10/24
sudo nmcli con mod "Wired connection 1" ipv4.gateway 192.168.150.1
sudo nmcli con mod "Wired connection 1" ipv4.dns 8.8.8.8
sudo nmcli con mod "Wired connection 1" ipv4.method manual

sudo nmcli con down "Wired connection 1"
sudo nmcli con up "Wired connection 1"

# Setup project
python3 -m venv .venv
source .venv/bin/activate
pip install ansible-playbook ansible-pylibssh ncclient
```
