# Tarefa_Git
 Tarefa do módulo GIT

O material publicado é relacionado a tarefa do módulo de Git do curso de análise de dados, nele possui um projeto no qual trata-se de uma calculadora que está programada para realizar 4 operações, sendo elas, soma, subtração, multiplicação e divisão. 

Este repositório inclui alguns arquivos essenciais, como calculadora.sh e calculadora.py. A seguir, explicaremos o motivo da sua presença e como utilizá-los.

- calculadora.sh 
Este arquivo é um script que automatiza a execução da calculadora.py.
Como utilizar: 
Salve o arquivo em uma pasta/diratório que consiga localizar através do teriminal Linux. Ao localizar a pasta/diratório onde o arquivo está armazenado, realize os seguites passos. 

1 - Altere as permissões do arquivo para torná-lo executável. Utilize o seguinte comando em seu terminal: 
chmod +x calculadora.sh
2 - Após dar a permissão, execute o script. Para isso, utilize o comando:
./calculadora.sh

Feito isso, o script se tornará executável e podera rodá-lo no terminal.

- calculadora.py
Este arquivo é onde possibilita a utilização da calculadora. 
Como utilizar:
É necessario certificar que há Python instalado, localizar a pasta/diratório onde o arquivo calculadora.py está armazenado e rodar o comando abaixo nessa mesma pasta/diratório:
python3 calculadora.py 

Funcionamento da calculadora. 

Primeiro era irá solicitar o primeiro número (a). Em seguida o segundo número (b). Após informar os dois números, ela irá questionar qual tipo de operação deseja realizar, dispondo de 4 operações.

adicionar(a, b): soma dois números.
subtrair(a, b): subtrai dois números.
multiplicar(a, b): multiplica dois números.
dividir(a, b): divide dois números.

Após informar os número e o tipo de operação, ela irá executar e em seguida exibir o resultado.
