# EXPLNATION:
### For every additional element, why you are adding it?
Adding a firewall for each server that takes a request to make sure I am fully protected from data I don't want to receive
, Firewalls act as a barrier between a trusted internal network and untrusted external networks, such as the internet.  
Adding an SSL Certificate to encrypte the data so it makes it even if it was leaked by hackers, they can't decrypte it. so it's 
another layer of protection.  
Monitoring clients are there to collect data from servers to watch over the preformance.  
  
### What are firewalls for?
Again Firewalls act as a barrier between a trusted internal network and untrusted external networks, such as the internet.
Firewalls also filter traffic and controll access and many more uses for the firewalls.  
  
### Why is the traffic served over HTTPS?
to encrypte the data so it makes it even if it was leaked by hackers, they can't decrypte it. so it's
another layer of protection.  
  
### What monitoring is used for?
They are used to collect data from servers to watch over the preformance.

### How the monitoring tool is collecting data?
They analyze the preformance and measure the overall health and send alerts if something went out of the ordinary or something is
not working as expected.  
  
### what to do if you want to monitor your web server QPS?
I should install a datacollector on my webserver so it keeps an eye on the queries.  
  
## Issues of the design
### Why terminating SSL at the load balancer level is an issue?
Because it will make the requests and responds between the load balancer and the servers not encrypted which
will make it easier to hackers to access.  
  
### Why having only one MySQL server capable of accepting writes is an issue?
Because that creates a single point of failure, if the MySQL server went down for any reason the whole website will go down
because there is no backup or a slave server in that case.  
  
### Why having servers with all the same components (database, web server and application server) might be a problem?
I might argue about the datacollecting would be confusing to read, if some error occured it would not be easy to locate, which will
eventually lead to poor preformance.
