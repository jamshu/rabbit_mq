import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep(20)
    print " [x] Done"
    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     body=str("ookkk"),
                     properties=pika.BasicProperties(
                        delivery_mode = 2, # make me$
                        reply_to = 'reply_hello2',
                     )			
    )
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='hello')
print ' [*] Waiting for messages. To exit press CTRL+C'

channel.start_consuming()
