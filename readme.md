# Xbox Controller Overlay 

Este projeto é um overlay visual para controle de Xbox, desenvolvido em **Python** com **Pygame**, para exibição em transmissões ao vivo ou gravações no **OBS Studio**.

## 🕹️ Sobre o Projeto

O objetivo deste projeto é fornecer uma interface visual que represente a entrada de um controle de Xbox em tempo real. Isso permite que espectadores visualizem os comandos que estão sendo executados durante uma gameplay.

O overlay captura entradas de botões, gatilhos e analógicos do controle e os exibe na tela.

## 📦 Bibliotecas Necessárias

Antes de executar o projeto, é necessário instalar as bibliotecas utilizadas. Você pode instalá-las com o seguinte comando:

```bash
pip install pygame
```

## 🚀 Como Executar

1. Conecte o controle de Xbox ao computador.
2. Execute o script principal:

```bash
python main.py
```

## 🎮 Funcionalidades

- Exibição de botões pressionados (A, B, X, Y, L1, R1, Start, Select, D-Pad)
- Representação dos gatilhos analógicos (L2, R2)
- Indicação da posição dos analógicos esquerdo e direito
- Fundo transparente para uso como overlay no OBS Studio

## 🏗️ Estrutura do Código

- **Inicialização**: Configurações de tela, transparência e joystick.
- **Captura de Entrada**: Monitoramento de botões e analógicos.
- **Renderização Gráfica**: Desenho dinâmico do controle baseado nas entradas capturadas.
- **Loop Principal**: Atualização da interface a cada frame.

## 🛠️ Possíveis Melhorias

- Adicionar suporte a múltiplos controles
- Personalização de cores e layout
- Configuração de transparência ajustável pelo usuário

## 📜 Licença

Este projeto é de código aberto e pode ser utilizado livremente.

