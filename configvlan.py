from netmiko import ConnectHandler 
SW9 = { 
'device_type':'cisco_ios', 
'ip':'10.215.27.131', 
'username':'vnpro', 
'password':'vnpro#123', 
'secret':'vnpro#321', 
} 
net_connect = ConnectHandler(**SW9) 
net_connect.enable() 
for n in range (10,31): 
    taoVlan= ['vlan ' + str(n)] 
ipVlan=['int vlan '+str(n),'ip add 172.16.'+str(n)+'.1 255.255.255.0','no shutdown'] 
output = net_connect.send_config_set(taoVlan) 
output = net_connect.send_config_set(ipVlan) 
output = net_connect.send_command('show ip interface brief | i Vlan') 
print(output)