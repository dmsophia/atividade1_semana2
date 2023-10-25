from confluent_kafka import Producer
import time

def main():
    conf = {
        'bootstrap.servers': 'localhost:9092',
    }

    producer = Producer(conf)

    while True:
        message = input("Digite a mensagem para enviar ao Kafka (ou 'sair' para encerrar): ")
        
        if message == 'sair':
            break

        producer.produce('begin', value=message)
        producer.flush()
        time.sleep(1)  # Para garantir que a mensagem foi enviada antes de enviar outra

if __name__ == '__main__':
    main()
