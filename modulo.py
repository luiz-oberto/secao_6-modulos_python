def soma(x: float, y: float) -> float:
    return x + y

def main() -> None:
    print(soma(10, 20))
    print(soma(20, 20))

if __name__ == '__main__':
    # a partir do momento que em que nome do módulo for igual a '__main__' ele exibirá o nome desse módulo
    # Ou seja, toda vez que o arquivo atual (modulo.py) for executado, ele executará o main
    main()