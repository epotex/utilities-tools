# Home IPsec VPN server running on top of Kubernetes 


Run IPsec vpn on top of Kubernetes!
Credits: 

- The Docker images in this deployment was created by: hwdsl2, check his github repo: https://github.com/hwdsl2/docker-ipsec-vpn-server
- The service is exposed thanks to MetalLb, read more about it here: https://metallb.universe.tf/

YOu can build the image and host it in your own docker registry

I'm using the Odroid N2's to form a K8S cluster (bare metal) for home usage and a lab, and the MetalLb is really cool solution for the LB.

##Deployment :

1. Edit k8s_config_files/create_vpn_secret.yaml with
 your secret username/password/preshared key
2. Deploy the secret: "bash  k8s_config_files/IPsec-VPN-Secret.sh"
3. Deploy the service: "kubectl apply -f k8s_config_files/IPsec-VPN-Deployment.yaml"
4. Deploy the MetalLb service: "kubectl -f k8s_config_files/IPsec-VPN-Service.yaml"

## Get the service information:
 1.  kubectl get service -o wide  
 2. check for the "EXTERNAL-IP" column, that's your vpn IP address, you can port forward 500 and 4500 UDP from your router to this IP to allow external access to the VPN service

 