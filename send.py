import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello', durable=True)
channel.queue_declare(queue='reply_hello2', durable=True)
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!',
		      properties=pika.BasicProperties(
		      	delivery_mode = 2, # make message persistent
                        reply_to = 'reply_hello2',
			))
print " [x] Sent 'Hello World!'"
connection.close()
