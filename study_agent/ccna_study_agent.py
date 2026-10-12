#!/usr/bin/env python3
"""Simple CCNA study agent.

This agent provides quick topic-based guidance for common CCNA questions.
It is intentionally lightweight and does not require external dependencies.
"""

import sys

TOPICS = {
    "osi": "OSI model: 7 layers. Physical, Data Link, Network, Transport, Session, Presentation, Application.",
    "tcpip": "TCP/IP model: Application, Transport, Internet, Network Access.",
    "subnet": "Subnetting: divide a network into smaller networks to reduce broadcast and improve efficiency.",
    "vlan": "VLANs segment a LAN logically. They improve security and reduce broadcast domains.",
    "stp": "STP prevents loops in redundant Layer 2 topologies by blocking redundant paths.",
    "routing": "Routing forwards packets between different networks. Routers use routing tables and protocols.",
    "ospf": "OSPF is a link-state routing protocol that uses areas and shortest path calculations.",
    "acl": "ACLs allow or deny traffic based on source, destination, protocol, and port.",
    "nat": "NAT translates private IP addresses into public ones, often using PAT overload.",
    "dhcp": "DHCP dynamically assigns IP addresses, subnet masks, and default gateways.",
    "dns": "DNS resolves hostnames such as www.cisco.com into IP addresses.",
    "ping": "Use ping to test reachability between devices.",
    "troubleshoot": "Follow a method: check physical status, IP addressing, gateway, routes, ACLs, and logs.",
    "ccna1": "CCNA 1 focuses on network fundamentals, OSI/TCP-IP, Ethernet, IP addressing, and basic troubleshooting.",
    "ccna2": "CCNA 2 focuses on switching, VLANs, routing, ACLs, and network services.",
    "ccna3": "CCNA 3 focuses on advanced routing, WAN, QoS, security, and troubleshooting.",
    "commands": "Use show ip route, show interfaces, show vlan brief, show cdp neighbors, ping, and traceroute.",
}


def display_help():
    print("CCNA Study Agent")
    print("Available topics:")
    for key in sorted(TOPICS):
        print(f"- {key}")
    print("\nExamples:")
    print("  python3 ccna_study_agent.py ospf")
    print("  python3 ccna_study_agent.py subnet")
    print("  python3 ccna_study_agent.py troubleshoot")


def main():
    if len(sys.argv) < 2:
        print("Enter a topic to study. Use 'help' for list of topics.")
        print("Example: python3 ccna_study_agent.py ospf")
        return

    query = sys.argv[1].lower()

    if query in ("help", "-h", "--help"):
        display_help()
        return

    topic = TOPICS.get(query)
    if topic:
        print(f"Topic: {query}")
        print(topic)
        return

    print(f"No direct match found for '{query}'.")
    print("Try one of these topics: osi, tcpip, subnet, vlan, stp, routing, ospf, acl, nat, dhcp, dns, ping, troubleshoot, ccna1, ccna2, ccna3, commands")


if __name__ == "__main__":
    main()
