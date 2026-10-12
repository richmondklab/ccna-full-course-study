# Cisco Command Reference

This guide contains the most practical Cisco IOS commands for CCNA study and lab work.

## 1. Access and privilege

```bash
enable
configure terminal
show running-config
show startup-config
copy running-config startup-config
```

## 2. Device naming and basic config

```bash
hostname SW1
hostname R1
service password-encryption
enable secret class
banner motd #Authorized access only#
```

## 3. Interface management

```bash
interface gigabitEthernet 0/0
description Connection to Core Switch
ip address 192.168.1.1 255.255.255.0
no shutdown
exit
show ip interface brief
show interfaces
```

## 4. VLAN configuration

```bash
vlan 10
 name STUDENTS
exit
interface fastethernet 0/1
 switchport mode access
 switchport access vlan 10
```

## 5. Trunking

```bash
interface gigabitEthernet 0/1
 switchport mode trunk
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 10,20,30
```

## 6. Inter-VLAN routing

```bash
interface vlan 10
 ip address 192.168.10.1 255.255.255.0
 no shutdown
```

## 7. Static routing

```bash
ip route 10.10.20.0 255.255.255.0 192.168.1.2
show ip route
```

## 8. OSPF

```bash
router ospf 1
 network 10.0.0.0 0.0.0.255 area 0
 network 192.168.1.0 0.0.0.255 area 0
end
show ip ospf neighbor
show ip route ospf
```

## 9. EIGRP

```bash
router eigrp 10
 network 10.0.0.0 0.0.0.255
 network 192.168.1.0 0.0.0.255
```

## 10. DHCP

```bash
ip dhcp pool LAN-POOL
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 8.8.8.8
```

## 11. NAT and PAT

```bash
ip nat inside source list 1 interface g0/0 overload
interface g0/0
 ip nat outside
interface g0/1
 ip nat inside
access-list 1 permit 192.168.10.0 0.0.0.255
```

## 12. ACLs

```bash
access-list 10 permit 192.168.10.0 0.0.0.255
access-list 101 permit tcp 192.168.10.0 0.0.0.255 any eq 80
```

## 13. Port security

```bash
interface fastethernet 0/2
 switchport mode access
 switchport port-security
 switchport port-security maximum 2
 switchport port-security mac-address sticky
```

## 14. Troubleshooting commands

```bash
show mac address-table
show interfaces status
show vlan brief
show ip interface brief
show ip route
ping 192.168.1.2
traceroute 8.8.8.8
show logging
```

## 15. Useful show commands

```bash
show version
show running-config
show ip arp
show cdp neighbors
show spanning-tree
show interfaces trunk
show ip protocols
```

## 16. Windows host commands

```bash
ipconfig
ipconfig /all
ping 192.168.1.1
tracert 8.8.8.8
```

## 17. Linux host commands

```bash
ip addr
ip route
ping 192.168.1.1
traceroute 8.8.8.8
```

## 18. Quick memory reminders

- `show ip route` = routing table
- `show mac address-table` = switched host mapping
- `ping` = reachability test
- `traceroute` = path analysis
- `show interfaces` = physical status and errors
- `show vlan brief` = VLAN overview
