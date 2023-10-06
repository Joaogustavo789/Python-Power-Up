# Python-Power-Up

Olá, sejam bem vindos ao repositório! `Python-Power-Up` é um projeto de automação de cadastro de produtos, desenvolvido em `Python` em conjunto com as bibliotecas `pandas` para dados e `pyautogui` que faz de fato a automação.

## Stack utilizada

<table width="320px" align="center">
  <tbody>
    <tr valign="top">
      <td width="80px" align="center">
        <span><strong>Python</strong></span><br>
        <img height="45" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
      </td>
      <td width="80px" align="center">
        <span><strong>Pandas</strong></span><br>
        <img height="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" />
      </td>
    </tr>
  </tbody>
</table>

## Rodando localmente
<details>
    <summary>Clique para expandir</summary>
<br>

- Clone o projeto

```bash
  git clone git@github.com:Joaogustavo789/Python-Power-Up.git
```

- Entre no diretório do projeto

```bash
  cd Python-Power-Up
```

- Criar um ambiente virtual:

```bash
  python3 -m venv .venv
```

- Acessar o ambiente virtual:

```bash
  source .venv/bin/activate
```

- Instalar as dependências dentro do ambiente virtual:

```bash
  pip install pyautogui pandas
```

- Executar código python dentro do ambiente virtual:

```bash
  python3 nome_do_arquivo.py
```

#### OBS: Caso queira sair do ambiente virtual, basta rodar o seguinte comando:

```bash
  deactivate
```

</details>

## Demonstração

<details>
    <summary>Clique para expandir</summary>
<br>

  ![Gif da aplicação](https://github.com/Joaogustavo789/Python-Power-Up/assets/99046967/cb0e85f3-09a1-4ce0-84d6-9957396b6cf1)
</details>

## Funcionamento

<details>
    <summary>Clique para expandir</summary>
<br>

- Para aplicação funcionar corretamente, basta rodar o seguinte comando dentro do ambiente virtual:

```bash
  python3 codigo.py
```

Após rodar o comando ele irá abrir área de trabalho, procurar pelo navegador, abrir o navegador, digitar a url fornecida, fazer o login, cadastrar todos os produtos.

#### OBS: Dependendo da máquina que estiver rodando, poderá haver a necessidade de alteração no código.
##### - Exemplos:

- Caso tenha problemas com posicionamentos, o arquivo `posicao.py` irá fornecer a posição exata do mouse após 5 segundos. Para executa-lo, basta rodar o seguinte comando:

```bash
  python3 posicao.py
```

![posicao-click](https://github.com/Joaogustavo789/Python-Power-Up/assets/99046967/14b9ea59-7a1d-4170-a7d6-25d8a5406e3c)

- Caso tenha problemas com tempo de espera, a solução é adaptando os tempos de acordo com sua máquina.

  ![tempo-espera](https://github.com/Joaogustavo789/Python-Power-Up/assets/99046967/62ee6758-b5ff-465c-b6b1-4ca493b54bba)

- Caso o navegador padrão seja diferente, basta trocar o nome pelo o navegador que utiliza.

  ![navegador](https://github.com/Joaogustavo789/Python-Power-Up/assets/99046967/52aebfa1-846e-44d7-8986-ede1c284294b)


- Se estiver utilizando o Macbook, troque o nome da tecla `win` pela `command`

  ![print-teclas2](https://github.com/Joaogustavo789/Python-Power-Up/assets/99046967/287464eb-bce3-483a-b602-66ec1d17f28d)



</details>

## Documentação

- [Python](https://www.python.org/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Pandas](https://pandas.pydata.org/)

## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de jgustavomendonca@gmail.com
