# CCNA 1 - Introduction to Networks

This document covers the foundations of networking as taught in CCNA 1 / NetAcad fundamentals.

## 1. Networking basics

### What is a network?
A network is a group of connected devices that share data and resources.

Key reasons to build networks:
- Share files and data
- Access printers and shared resources
- Centralize services and applications
- Support communication between users and systems

### Network components
- End devices: PC, server, phone, printer
- Intermediate devices: switches, routers, wireless access points
- Media: copper cable, fiber, wireless
- Protocols: rules that enable communication

## 2. OSI model

The OSI model has 7 layers:

1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

### Purpose
The OSI model helps explain how data travels through a network and how protocols work together.

### Important mapping to TCP/IP
- Application = HTTP, DNS, SMTP
- Transport = TCP, UDP
- Internet = IP
- Network Access = Ethernet, WLAN

## 3. TCP/IP model

The TCP/IP model is practical and used in real networking.

Layers:
- Application
- Transport
- Internet
- Network Access

## 4. Ethernet and LANs

### Ethernet
Ethernet is the most common LAN technology. It uses MAC addresses and frame-based communication.

### MAC address
- 48-bit physical address
- Format: `00:1A:2B:3C:4D:5E`
- Unique per NIC

### Switches
Switches connect hosts in a LAN and forward frames based on MAC address tables.

### Hubs
Hubs are legacy and operate at Layer 1; they broadcast traffic to all ports.

## 5. IP addressing

### IPv4
IPv4 is the most common version used today.

Example:
- `192.168.10.10`
- Subnet mask: `255.255.255.0`

### Private IPv4 ranges
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

### IPv6
IPv6 was developed to solve IPv4 exhaustion.

Example:
- `2001:db8::1`

## 6. Subnetting fundamentals

Subnetting divides a network into smaller logical networks.

### Why subnet?
- Reduce broadcast domains
- Improve performance
- Better address planning

### Subnet mask
The subnet mask determines network and host portions.

Example:
- `255.255.255.0` = /24
- `255.255.0.0` = /16

### Quick formula
- Total addresses = 2^host-bits
- Usable host addresses = total - 2

## 7. Binary and decimal review

### Decimal to binary
- 192 = 11000000
- 168 = 10101000

### Binary to decimal
- 11000000 = 192
- 10101000 = 168

## 8. Network topologies

Common topologies:
- Star
- Bus
- Ring
- Mesh
- Hybrid

The star topology is the most common today.

## 9. Cabling and media

### Copper cabling
- UTP
- STP
- RJ-45

### Fiber optics
- Single-mode
- Multi-mode

### Wireless
- 2.4 GHz
- 5 GHz
- Wi-Fi standards such as 802.11ac / 802.11ax

## 10. Device configuration basics

### Cisco IOS CLI modes
- User EXEC: `>`
- Privileged EXEC: `#`
- Global config: `(config)#`

### Common commands
```bash
enable
configure terminal
hostname SW1
interface gigabitEthernet 0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
end
show ip interface brief
```

## 11. DHCP and DNS

### DHCP
A server automatically assigns IP addresses to hosts.

### DNS
DNS translates names like `www.cisco.com` into IP addresses.

## 12. NAT basics

NAT allows private addresses to communicate with public networks.

Examples:
- Static NAT
- Dynamic NAT
- PAT (Port Address Translation)

## 13. Troubleshooting basics

Troubleshooting steps:
1. Identify symptoms
2. Verify physical connectivity
3. Check logical configuration
4. Validate IP addressing and routing
5. Test connectivity using ping and traceroute
6. Check logs and device status

## 14. Common CCNA 1 questions

### Q: What does a switch do?
It forwards Ethernet frames based on MAC addresses within a LAN.

### Q: What is the purpose of a router?
It forwards packets between networks and makes path decisions based on routing information.

### Q: What is a broadcast domain?
A network segment where broadcast frames are propagated.

## 15. Key summary

CCNA 1 introduces the core concepts of:
- how networks work
- how data travels
- how devices connect
- how IP addresses and subnets are planned
- how to perform basic troubleshooting

## Lab ideas

- Build a simple star topology with 2 PCs and a switch
- Configure a Cisco switch hostname and VLAN
- Assign static IPs and test connectivity
- Troubleshoot missing ping using cable checks and CLI commands

## Quick review checklist

- [ ] Understand OSI and TCP/IP models
- [ ] Know common Ethernet terms
- [ ] Understand IPv4 and IPv6 basics
- [ ] Explain subnet masks and addressing
- [ ] Use ping, traceroute, show commands
- [ ] Troubleshoot basic connectivity issues
