# EXPLANATION:
### What is a server?
Server the way I see it is like a super PC that runs a special type of operating system and it's usually placed in a datacenter
it doesn't have to have a screen because it's accessed remotely and it has tools to help run different type of application services
including but not limited to web services.  
  
### What is the role of the domain name?
It makes it easier for humans to access website, becaues basically to access a website you need to either remember the website's IP 
or to have some kind of service/system that translates the "Domain name" you remember into that IP, because it's always easier for humans
to remember relative words over random numbers.  
  
### What type of DNS record www is in www.foobar.com?
It's an A record, it's a very common subdomain prefix you can find it's an A record by using dig www.foobar.com.  
  
### What is the role of the web server?
Webservers are responsible of handling HTTP requests and sending back HTTP respnds.  
  
### What is the role of the application server?
The way I see it, application servers are responsible for connecting to codebases to generate dynamic web content to send back with the
HTTP respond.  
  
### What is the role of the database?
Databases are there to store all the content that will be recalled and filled into the templates from the codebase.

### What is the server using to communicate with the computer of the user requesting the website?
It uses the internet, HTTP request and HTTP respond.  

## Issues of the Design
### SPOF
There are multiple Singe Points of Failures in this design, if the application server went down, website goes down, if SQL server goes down, website goes down
if webserver goes down, website goes down.  
  
### Downtime when maintenance needed
There would be a downtime everytime we try to update/maintain the server.  
  
### Cannot scale if too much incoming traffic
Because we don't have a load balancer we cannot scale this to multiple servers if got too much incoming traffic.
