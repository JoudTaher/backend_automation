# Installation  

1. Create a docker container based off Ubuntu  

> docker run -it ubuntu bash  


2. Install Ansible  

> apt update  
> apt install ansible  

3. Deploy database  

> ansible-playbook database.yml  

4. Deploy webserver  

> ansible-playbook webservers.yml  

5. Deploy control packages  

> ansible-playbook control.yml

6. Test connection and endpoints

> curl 127.0.0.1
> curl 127.0.0.1/db