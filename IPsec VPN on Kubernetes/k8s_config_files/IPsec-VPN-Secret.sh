#!/usr/bin/env bash
kubectl create secret generic vpnvar --from-literal=VPN_IPSEC_PSK='123' --from-literal=VPN_USER='abc'  --from-literal=VPN_PASSWORD='xyz'
