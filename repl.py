import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep(10)
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='reply_hello2')
print ' [*] Waiting for messages. To exit press CTRL+C'

channel.start_consuming()

print ">>>>>>>>>>>>>>>>>>>>>>"
