# Lab: Backend Automation with Ansible

## Demo 1  

This demo sets up a simple Flask web application on an Apache Web Server, backed by a MySQL database, using Ansible.

### Installation  

1. Create a docker container based off Ubuntu  

> port=$((10000 + RANDOM % 55535))
> echo $port # Make sure the random number is between 10000 and 65535
> docker run -p $port:80 -it ubuntu bash  

2. Install Ansible  

> apt update  
> apt install -y ansible  

3. Install Git  
> apt install -y git  

4. Install text editors  

> apt install -y nano vim  

5. Clone Lab Repo (this time you are inside the container)  
> git clone https://github.com/fullstackdatascientist/backend_automation.git  
> cd backend_automation  

6. Deploy database  

> ansible-playbook database.yml  

7. Deploy webserver  

> ansible-playbook webservers.yml  

8. Deploy control packages  

> ansible-playbook control.yml

9. Test connection and endpoints

> curl 127.0.0.1
> curl 127.0.0.1/db  


## Demo 2  

This demo setup a Flask Web Form on an Apache Web Server. Submitting the form calls an Azure Function of your choice.  

### Installation

1. Assuming you are still inside the ubuntu container, run the required ansible playbook:  

> ansible-playbook webservers2.yml  

Pay heed to configuration file changes in directory demo2.  

2. Test the form submission from your web browser and ensure the Azure Function is called. When provided with the correct URL, the Azure Function will return a JSON response. You must copy the Invoke URL for your Azure Function, including the access key, from the Azure Portal.  

