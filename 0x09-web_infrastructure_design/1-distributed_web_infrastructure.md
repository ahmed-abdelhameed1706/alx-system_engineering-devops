# EXPLNATION
### Why I added a Load Balancer?
To be able to handle more requests using multiple server, now this design can handle more traffic.  
  
### What distribution algorithm your load balancer is configured with and how it works?
HAProxy uses Round Robin distribution algorithm by default, how that works? it sends requests in turns to each server connected to the 
load balancer.  
  
### Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both?
it's enabling an active-active setup, it sends requests to both servers in order. the difference between active-active and 
active-passive is that active-active is the default setup of a load balancer, it balances the loads between all active servers,
while active-passive only works with one server and if it went down it switches to the next in line and so on.

### How a database Primary-Replica (Master-Slave) cluster works?
If the primary database (Master database) server went down, it switches to the Replica (Slave database) one, the replica database
is a copy of the updated master database.

### What is the difference between the Primary node and the Replica node in regard to the application?
The primary node is the one that works by default while the replica node is there to make sure that there would not be a single point
of failure ragarding nodes. so if the primary went down the replica starts to work.

## Issues of the design
### Where are SPOF?
I would say it's in the load balancer, if it went down we wouldn't be able to handle the traffic.  
  
### Security issues (no firewall, no HTTPS)
the design has no firewall or HTTPS makes the requests and responds not encrypted, which makes it easier for the data to be leaked.  
  
### No Monitoring
We are not using any monitoring software so we have no idea what the current data/services state is.
