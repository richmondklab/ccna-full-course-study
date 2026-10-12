# CCNA 2 - Switching, Routing, and Basic Network Security

This document covers the network operations and configuration topics commonly covered in CCNA 2.

## 1. Layer 2 switching

Switches operate mainly at Layer 2.

### Functions of a switch
- Learn MAC addresses
- Forward frames to correct port
- Reduce collisions
- Provide segmentation within the LAN

### MAC address table
A switch builds a MAC address table by learning source MAC addresses from incoming frames.

## 2. VLANs

A VLAN is a logical segmentation of a LAN.

### Why use VLANs?
- Improve security
- Reduce broadcast traffic
- Group devices logically by function

### VLAN examples
- VLAN 10: Faculty
- VLAN 20: Students
- VLAN 30: Servers

### Access ports vs trunk ports
- Access port: carries only one VLAN
- Trunk port: carries multiple VLANs

### Trunking protocol
802.1Q is the standard trunking protocol used on Cisco networks.

## 3. Inter-VLAN routing

Hosts on different VLANs cannot communicate without routing.

### Common methods
- Router on a stick
- Layer 3 switch SVI

### Example
```bash
interface vlan 10
 ip address 192.168.10.1 255.255.255.0
 no shutdown
```

## 4. Spanning Tree Protocol (STP)

STP prevents loops in redundant Layer 2 networks.

### Why loops are bad
- Broadcast storms
- MAC table instability
- Device instability

### STP port roles
- Root port
- Designated port
- Blocking port

### Common STP types
- PVST+
- Rapid PVST+
- MST

## 5. EtherChannel

EtherChannel bundles multiple physical links into one logical link.

### Benefits
- More bandwidth
- Redundancy
- Simplified configuration

### Common protocol examples
- LACP
- PAgP

## 6. Routing basics

Routers forward packets between networks.

### Routing table
The routing table contains destination networks and next hops.

Common route types:
- Connected routes
- Static routes
- Dynamic routes

## 7. Static routing

Static routes are manually configured.

### Example
```bash
ip route 10.10.20.0 255.255.255.0 192.168.1.2
```

### Use cases
- Small networks
- Backup routes
- Special networks

## 8. Dynamic routing

Dynamic protocols automatically learn routes.

### Common protocols
- RIP
- OSPF
- EIGRP
- BGP

### OSPF basics
OSPF is link-state and widely used in enterprise networks.

#### OSPF router ID
The router selects a unique router ID for OSPF operation.

#### OSPF area
OSPF organizes networks into areas, commonly Area 0 for the backbone.

## 9. ACLs

An access control list filters traffic based on criteria.

### Types
- Standard ACL
- Extended ACL

### Standard ACL example
```bash
access-list 10 permit 192.168.10.0 0.0.0.255
```

### Extended ACL example
```bash
access-list 101 permit tcp 192.168.10.0 0.0.0.255 any eq 80
```

## 10. NAT and PAT

NAT translates private addressing to public addresses.

### PAT example
```bash
ip nat inside source list 1 interface g0/0 overload
```

## 11. DHCP, DNS, and client connectivity

### DHCP scope
A DHCP server assigns addresses to clients.

### DNS resolution
Clients query DNS for name resolution.

## 12. LAN security basics

### Port security
Port security restricts MAC addresses on switch ports.

### Example commands
```bash
switchport port-security
switchport port-security maximum 2
switchport port-security mac-address sticky
```

## 13. Wireless concepts

### WLAN basics
Wireless access points broadcast SSIDs and allow wireless client access.

### Wireless key concepts
- SSID
- RF interference
- Channel selection
- Signal strength

## 14. Troubleshooting switching and routing

### Useful commands
```bash
show mac address-table
show interfaces trunk
show spanning-tree
show ip route
show ip protocols
show cdp neighbors
show vlan brief
```

## 15. Common CCNA 2 topics to remember

- VLAN segmentation
- Trunking with 802.1Q
- Spanning Tree and loop prevention
- Inter-VLAN routing
- Static and dynamic routing
- ACL security
- EtherChannel and redundancy

## Lab ideas

- Configure VLANs on a Cisco switch
- Create trunk links between switches
- Configure inter-VLAN routing with a router or SVI
- Verify STP root election
- Configure static route between two routers
- Test connectivity across VLANs

## Quick review checklist

- [ ] Explain how a switch learns MAC addresses
- [ ] Describe VLAN segmentation
- [ ] Configure inter-VLAN routing
- [ ] Understand STP loop prevention
- [ ] Differentiate static and dynamic routing
- [ ] Configure a basic ACL
- [ ] Explain the role of NAT
