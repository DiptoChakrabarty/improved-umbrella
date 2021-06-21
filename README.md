# improved-umbrella

## Instructions

```
- Activate virtualenv or do without it your choice
   virtualenv venv --python=python3 

 - Install dependencies
   pip3 install -r requirements.txt
   
 - Run a rabbitmq server using docker using following command
   sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   ** If you want your raabitmq container to not terminate after usage remove --rm
 
 - Go to locahost:15672 to view your rabbitmq server , default login are guest and guest

```