cisco vs juniper commands 
cisco 									juniper 
show ip interfaces brief 						show interfaces terse 
									help topic ?
									help topic interfaces 

create vlan 
vlan 10 								set vlans hello vlan-id 10 
name hello

interface config mode and then configure switchport and vlan 
interface ge 0/0/1 							edit interfaces ge-0/0/1 
switchport mode access 							set unit 0 family ethernet-switching port-mode access 
switchport access vlan 10 						set unit 0 family ethernet-switching vlan members hello 

switchport mode trunk 							set unit 0 family ethernet-switching port-mode trunk
switchport trunk vlan 10, 20, 30 					set unit 0 family ethernet-switching vlan members hello 

set password (must be done for juniper device or else it won't work) 
configure terminal 							edit system 
enable secret cisco 							set root-authentication plain-text-password 
									juniper123	
									show 
											
									set root-authentication encrypted-password 
									juniper123 
											
									top
									edit chasis 
									show 
									delete (whats in the show thing)
											
configure a user 
config t 								edit system
username admin privilige 15 password bob1				set user admin class super-user authentication plain-text-password
									(enter the new password) 
											
configure ssh 
hostname router1							set system host-name router1 
ip domain-name local.local						set system domain-name local.local 
transport input ssh 							set system ssh 
line vty 0 4 	
transport input ssh 
login local 
											

configure interfaces 
interface ge 0/0/1.0 							edit interface ge-0/0/0
ip address 192.168.0.2 							edit unit 0 
									edit interfaces ge-0/0/0.0 (same but in one line) 
									edit unit 0 family inet 
									set address 192.168.0.1/24 
											
vlan 10 								set vlans hello vlan-id 10 
exit 									set interfaces vlan.10 family inet address 192.168.0.1 
interface vlan 10 							set vlans hello l3-interface vlan.10 
ip address 192.168.0.1 

