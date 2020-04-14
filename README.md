# OOP Application
## Index
[Brief](#brief)
   * [Solution](#solution)
   
[Construction](#construction)
   * [Risk Assessment](#risk_assessment)	
   * [Risk Assessment Table](#risk_table)

[Pie chart of Risks](#piechart) 
   * [Pie chart risk percentage](#piechart) 
	* [User Stories](#userstories)

[Sprints & Planning](#spr1)
   * [Trello Board Sprint 1.0](#spr1) 
   * [Trello Board Completion Stage](#sprcompletion)

[Sprints explained](#sprintsexplained)
 
	
[Testing](#testing)
   * [Report](#report)

[Architecture](#Projectarchitecture)
   * [Project Architecture](#Projectarchitecture)

[Deployment](#depl)
   * [Technologies Used](#tech)

[Retrospective](#retro)
  
[Improvements for the Future](#improve)

[References](#references)

[Authors](#auth)

[Acknowledgements](#ack)

<a name="brief"></a>
# The Brief
The aim is to create an OOP based application using CRUD method. Here the incorporation of tools methods and technologies was implemented. 
The application must made up of a total of 4 applications each with their own required elements. Each must be Flask based be able to control and alter data 
via at least one table with on fuctionality for the user to input data. This application will be using the framework jenkins, where jenkins should 
go into another server that can run the application. the should be handed the ssh key to activate the instance. This application ran jenkins with a before and after installation to assign a pipeline dedicated server.  

<a name="solution"></a>
# Solution
For my second project I created an application that require Docker. It was a Flask OOP orientated project via Jenkins framework. I create 4 separate services that 
would communicate with each other to form one application. The over aim was to create a website that would allow a user to generate their baby’s first 
name and middle name, and well as obtaining data from them, to store in a database. Service1 managed the frontend, and send data into the database, as well as 
to receive information. Service2 held the list of random baby names (first names).Service3 held the random list of baby middle names. Service4 would then 
preform the task, which was to pull and creating the first names and middle names from Service2 and Service3, and then output the combination by sending it to Service1.  
This project allowed me to understand how Docker works, with Docker, building images, how they ran as containers, and many other important properties such as Ansible and Nginx. 

<a name="risk_assessment"></a>
# Risk Assessment
## Requirements / Product Backlog
Here, is where all the requirments of the project are listed, the different colours show, the importance of each of them. Red means must, yellow mean it would 
add get value but the application will still run without it; and blue means that no needed but add descretive futures to the application. 

![Requirements4Light](/images/requirementsProductBacklog.PNG)

<a name="risk_table"></a>
Here, the risk assessment is analysing potential actions that can have a negative impact towards individuals, or the surrounding.

## Risk Assessment Table
![Risk Assessment Table1](/images/risktable1.PNG)
![Risk Assessment Table2](/images/risktable2.PNG)

<a name="piechart"></a>
## Pie chart risk 
Here shows the chances of each risk as a percentage.

![Pie chart risk](/images/piechartchances.PNG)

<a name="userstories"></a>
# User Stories (Users and Developers)
To create the user stories, Trello was used, there was listed all the use-cases for the product in the terms of a ‘user’ and ‘developer’.

![UserStories](/images/userdev.PNG)
![UserStories](/images/userdev2.PNG)

<a name="spr1"></a>
# Trello Board (Sprint)
Each entry represents a sprint. Most sprint was roughly 4 days, so took a lot longer due to server issues which required created new instances, 
however each needed to be met. 
![Sprint](/images/sprint.PNG)

![Sprints](/images/sprints.PNG)


<a name="sprcompletion"></a>
## Trello to completion
The project is now in the completion stage, where all are moved to the 'Done' as all tasks was complete.

![Completed..](/images/Done.PNG)

![Complete..](/images/Done2.PNG)


<a name="sprintsexplained"></a>
## Sprints explained 

### kanban board: SERVICES
here was to create simply database for customer input, then create the code for each of the 4 services.
In addition, to creating the the elements for each for each service; .dockerignore, Dockerfile, app.py, and
requirements folder. the templete folder was create (but only unquie to service1.)

### kanban board: NGINX
Create Dockerfile which will be the latest nginx which will as a host for all 
the services. Next was to create the reverse_proxy.conf file, which will allow nginx
to listen if the port is in use, and it will run on its port if available.(port 80).
When running an application without NGINX the application has to be run on localhost, 
with port ':5000' as an extension to the servers external ipaddress. Hosting your website
on NGINX allows one to ditch the extension, and runs the website on port 80 where NGINX runs on.  

Running on MANAGER 

![manager](/images/Managernodecircle.PNG)


Running on WORKER

![worker](/images/Workernodecircle.PNG)

### kanban board: ROLES
This folder would would hold 3 yaml files named 'docker add swarm', 'docker init'
and 'docker install'.
'docker swarm' yaml file, contained the the script to create manager node and produce a token.
the 'docker init' yaml file preformed the status, checks and gets the manager token and add the 
worker node to the swarm. Lastly, the 'docker install' installed docker onto the worker node.


### kanban board: JENKINS
Create jenkinsfile for jenkins framework. this included all instructions for jenkins,
in regards to all the elements made for jenkins, and how jenkins should run them and when.


### kanban board: CREATE IMAGE & CREATE CONTAINERS
Create images for each service
Create containers for each service


### kanban board: DOCKERHUB
Create a builds to push up to dockerhub, so docker-compose knows where to look.
 

### kanban bored: DOCKER-COMPOSE
Create instruction for execution, rather than executing each service one by one.


### kanban board: DOCKER SWARM 
Once everything was up and working it was ready to be part of a swarm. All that had to be done
was to run the playbook and with the inventory file. However this was option and could be done more of a 
test to see if everything was working, since it will be run via jenkin, the manager node would be 
created and a worker would be created to become part of the swarm then. 


### kanban board: FIREWALL (add to things to improve)
the basic firewall had been create which allowed HTTP traffic,
disrupted the instances, 2 instances was created before had which went wrong,
so a 3rd and final one had to be created without HTTP traffic and it would without problem.


### kanban board: ANSIBLE
Ansible had to was installed to made the configuation of each serivce the same and to better way to manage your service
It Orchestrates the services to come and work together in harmony. 


<a name="testing"></a>
# Testing 
Here pytest was implemeted in hand with coverage. these tools help me to see if my URLs worked and
if my database was functioning. It showed me which passed and which did, and the over percentage of success.
On VScode as seen, all tests passed, however on jenkins testing url and database- that section was 78%. Without source,
the coverage was 46% but with source the over all was 100%

## URL Testing
Here was the creation of testing in order to test. Code to test was being created in python for each area of the application. 
Firstly, the code to test the application’s URL was created. Once it was made it was then pushed up to GitHub, to invoke Jenkins (without automated build), 
once Jenkins was triggered the results could be seen on Jenkins console to see whether it was a success or not. 

Here as shown the url testing with pytest and without jenkins passed at 100%.

![url pytest](/images/pytestURL.PNG)

Here shows the testing  on jenkins which passed at 78%

![jenkins test](/images/jenkinsURLandDatabase.PNG)

<a name="report"></a>
## Report
### Database Testing and full coverage report
Test coverage for the coverage report passed at 100%. 

![overall coverage](/images/coverageReport.PNG)



Jenkins comfirmation of success 

![success](/images/successjenkinsbuild.PNG)

<a name="Projectarchitecture"></a>
# Project Architecture
Here shows docker-compose being run, where it can pull from the containerised services and run them as one application. 
In addition, making them into a stack to later to be run via jenkins. 

![process](/images/process.PNG)


Here shows what each Services do. Service_1 is the frontend and output Service_4 to the screen. Service_2 hold the first part of the data,
and Service_3 holds the second part of the data. Service_4 grab both data from Service_2 and Service_3, combines they accordingly.

![process2](/images/process2.PNG)


<a name="depl"></a>
# Deployment
The automated build was included in this project, but the test and deployment process was still done by Jenkins, via GitHub which was 
triggered with every push event. This website can be deployed both locally as well as externally by a virtual machine. 

## JENKINS & GIT
(2020, Steffi) "Another tool in our continuous deployment process will be Jenkins, originally called Hudson. We will use a Jenkins integration server as a trigger.
A push in our repository will trigger the Jenkins server so that we are able to get a Docker environment. This can be achieved by the Docker Plugin for Jenkins. 
To be able to trigger a Jenkins build with a Git push you need to install a Git Plugin as well."

![deployment](/images/deployment.PNG)

### Technologies Used
* GCP Database Engine - Database
* Python - Logic
* Dockerhub
* Jenkins - CI Server
* [Git](https://github.com/Shana12345/LatestDocker.git) - VCS
* [Trello](https://trello.com/b/rR5y1QHA/projects) - Project Tracking

<a name="retro"></a>
# Retrospective

## Achievements
- What was good was that everything was delieved within the timeframe even though there was issue involved.
- Understanding the tools used in depth, understanding each had their own unique part and knowing the side effects  without them.
- All complusory tasks were met.

## Problems faced
- Not understand the tasks and tools at hand at the beginning of the project. This made it harder to start and plan on what I need to do.
- VM failed twice which cause a quite a bit of a setback for me, as I could move fowards with the next task.
- When trying to run the VM with 'allowing HTTP traffic' on the firewall rules, it keep make an error, which caused me to keep create new instances. 
- One the VM was fixed I had to catch up rather quickly, which cause me to do all nighters, this cause physical strain on my back and eyes. 


<a name="improve"></a>
# Improvements for the Future
- The improvement that needed to be made would be adding the firewall. Due to the fact that the ipaddress kept altering made it more difficult to implement.
  In addition, add HTTP traffic to the firewall rules without the VMs producing an error. 
- Adding CRUD functionality
- Learning more in depth testing 

![future](/images/future.PNG)


<a name="references"></a>
# References 
(2020), Steffi, 'Learning Continuous Deployment', https://learning-continuous-deployment.github.io/docker/jenkins/git/2015/04/21/getting-started/,
Data Accessed: 14/04/2020

<a name="auth"></a>
# Authors

Shana Charlery

<a name="ack"></a>
# Acknowledgements

* QA consulting and our fantastic instructors
* The rest of our wonderful cohort on the programme


