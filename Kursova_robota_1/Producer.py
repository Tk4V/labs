import pika
import time
import random


connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='kursova')

messageId =1

while(True):

    channel.basic_publish(exchange='', routing_key='kursova', body=message)

    print(f"sent message: {message}")

    time.sleep(random.uniform(1, 2))
    
    messageId+=1

    message = (f"Sending Message Id:{messageId}")
