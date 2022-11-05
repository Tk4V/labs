import pika
import time
import random


def on_message_received(ch, method, properties, body):
    duration_time = random.uniform(1,2.5)
    print(f"received: {body},will take {duration_time} to process")
    time.sleep(duration_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished processing the messsage and acknowledged message")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='kursova')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='kursova',on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()