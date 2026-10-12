# CCNA 3 - Scaling Networks and Advanced Connectivity

This document covers advanced network services, routing, security, and troubleshooting techniques typically included in CCNA 3.

## 1. Advanced routing protocols

### OSPF
Open Shortest Path First (OSPF) is a widely used IGP.

Key concepts:
- Link-state routing
- Areas and Area 0
- Router ID
- Hello packets
- SPF algorithm

### Example OSPF config
```bash
router ospf 1
 network 10.0.0.0 0.0.0.255 area 0
 network 192.168.1.0 0.0.0.255 area 0
```

### EIGRP
Enhanced Interior Gateway Routing Protocol is Cisco-proprietary and efficient in Cisco networks.

Key concepts:
- Composite metric
- Successor/feasible successor
- Neighbor discovery

## 2. WAN concepts

WANs connect geographically separated networks.

### Common WAN technologies
- Leased lines
- MPLS
- Frame Relay (legacy)
- VPNs
- Broadband links

### Typical WAN concerns
- latency
- QoS
- circuit availability
- security

## 3. QoS fundamentals

QoS prioritizes traffic based on business needs.

### Common QoS tools
- Classification
- Marking
- Policing
- Shaping
- Queues

### Example marking values
- DSCP values
- CoS values

## 4. Network security deeper concepts

### AAA
Authentication, Authorization, and Accounting are critical for secure network access.

### Common protocols
- RADIUS
- TACACS+

### Device hardening
- Disable unused services
- Use secure passwords
- Restrict management access
- Apply ACLs

## 5. Wireless and mobility

Wireless networks require understanding of:
- SSID
- RF environment
- AP and client association
- roaming
- security protocols (WPA2/WPA3)

## 6. Network automation and programmability

The modern CCNA includes developing concepts around automation.

## Key topics
- APIs
- JSON
- Python scripting basics
- Controller-based networks
- Network management platforms

## 7. High availability and redundancy

Redundancy improves continuity of network access.

### Techniques
- HSRP
- VRRP
- GLBP

### Example HSRP
```bash
interface vlan 10
 standby 1 ip 192.168.10.1
 standby 1 priority 110
```

## 8. Network design and scaling

Designing networks requires balancing:
- scalability
- redundancy
- performance
- manageability

## 9. Troubleshooting methodology

### Systematic approach
1. Define the problem
2. Gather symptoms
3. Hypothesize likely cause
4. Isolate the layer
5. Test and validate
6. Document the fix

### Layer-by-layer troubleshooting
- Physical: cabling, LEDs, power
- Data link: VLANs, STP, MAC issues
- Network: routing, subnets, ACLs
- Transport: ports, TCP/UDP checks
- Application: DNS, services, permissions

## 10. Useful troubleshooting commands

```bash
show ip route
show ip ospf neighbor
show interfaces
show cdp neighbors
show running-config
show vlan brief
show logging
ping
traceroute
```

## 11. Security in routing and switching

- Control management plane access
- Filter suspicious traffic with ACLs
- Segment networks with VLANs and firewalling
- Monitor logs for anomalies

## 12. Exam-style concepts to review

- OSPF vs EIGRP
- VLAN and trunk design
- NAT and PAT operation
- WAN connectivity types
- AAA and device security
- QoS traffic handling
- Troubleshooting layered network issues

## 13. Lab ideas

- Configure OSPF between routers
- Build a multi-VLAN switched network
- Implement HSRP for redundancy
- Verify path selection using routing tables
- Configure ACLs to restrict traffic
- Test connectivity using ping and traceroute

## Quick review checklist

- [ ] Explain OSPF operation
- [ ] Understand WAN technologies
- [ ] Know QoS principles
- [ ] Explain AAA and secure management
- [ ] Troubleshoot Layer 2 and Layer 3 issues
- [ ] Use network logs and show commands to diagnose problems
