from confluent_kafka import Consumer

def main():
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'meu_grupo_consumidor',
        'auto.offset.reset': 'earliest',
    }

    consumer = Consumer(conf)
    consumer.subscribe(['begin'])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Erro ao consumir mensagem: {msg.error()}")
            else:
                print(f"Mensagem recebida: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    main()
