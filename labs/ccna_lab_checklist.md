# CCNA Lab Checklist and Troubleshooting Practice

This file is a practical lab pack for CCNA study, based on real networking tasks.

## Lab 1: Basic device connectivity

Goal: Verify that a PC can ping a switch and another PC.

### Tasks
- Cable hosts to switch
- Configure IP addresses
- Verify VLANs
- Run `ping`
- Check `show ip interface brief`

## Lab 2: VLAN segmentation

Goal: Create multiple VLANs and verify isolation.

### Tasks
- Create VLAN 10 and VLAN 20
- Assign access ports
- Configure trunk link
- Verify using `show vlan brief`

## Lab 3: Inter-VLAN routing

Goal: Allow communication between VLANs.

### Tasks
- Configure SVI interfaces
- Add IP addresses
- Verify ping between hosts in different VLANs

## Lab 4: Static routing

Goal: Connect two routers and route between networks.

### Tasks
- Configure IP addresses on router interfaces
- Add static routes
- Validate through ping and `show ip route`

## Lab 5: OSPF routing

Goal: Learn dynamic routing.

### Tasks
- Configure OSPF on two or more routers
- Verify neighbors with `show ip ospf neighbor`
- Confirm route learning

## Lab 6: ACL practice

Goal: Restrict traffic according to policy.

### Tasks
- Permit selected subnet
- Deny unauthorized traffic
- Verify using ping or telnet

## Lab 7: NAT/PAT practice

Goal: Enable internal hosts to access the Internet using one public IP.

### Tasks
- Configure inside/outside interfaces
- Create access list
- Configure NAT overload
- Verify translation using `show ip nat translations`

## Lab 8: Port security

Goal: Protect switch ports from unauthorized MAC addresses.

### Tasks
- Enable port security
- Add maximum MAC count
- Shut down unexpected devices
- Verify `show port-security`

## Lab 9: Troubleshooting connectivity

Goal: Diagnose a broken network.

### Troubleshooting sequence
1. Check cable and LEDs
2. Verify VLAN and port mode
3. Confirm IP addressing
4. Check default gateway
5. Verify routing table
6. Run `ping` and `traceroute`
7. Review logs and interfaces

## Lab 10: Wireless and access review

Goal: Learn wireless fundamentals.

### Topics
- SSID
- Channel overlap
- Authentication
- Signal strength
- Security modes

## Critical troubleshooting questions

- Can the device ping its gateway?
- Does the interface show status `up/up`?
- Is the default gateway correct?
- Is the route present in the routing table?
- Is the firewall or ACL blocking traffic?
- Are the VLANs and trunking configured correctly?

## Lab final checklist

- [ ] switch is reachable
- [ ] VLAN and trunk configured
- [ ] interface has IP address
- [ ] gateway is reachable
- [ ] route exists
- [ ] ACL does not block traffic
- [ ] NAT/PAT works where required
- [ ] logs and outputs are reviewed
