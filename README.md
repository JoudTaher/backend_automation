# Installation  

1. Create a docker container based off Ubuntu  

> port=$RANDOM
> echo $port
> docker run -p $port:80 -it ubuntu bash  


2. Install Ansible  

> apt update  
> apt install -y ansible  

3. Install Git  
> apt install -y git  

4. Clone Lab Repo (this time you are inside the container)  
> git clone https://github.com/fullstackdatascientist/backend_automation.git  
> cd backend_automation  

3. Deploy database  

> ansible-playbook database.yml  

4. Deploy webserver  

> ansible-playbook webservers.yml  

5. Deploy control packages  

> ansible-playbook control.yml

6. Test connection and endpoints

> curl 127.0.0.1
> curl 127.0.0.1/db