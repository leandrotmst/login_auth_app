import os

from dotenv import load_dotenv

load_dotenv()

def run(msg='Hello world!') -> None:
    print(os.getenv('GREETINGS', 'Valor padrão'))
    print(msg)


if __name__ == '__main__':
    run('Executando diretamento pelo Python')
