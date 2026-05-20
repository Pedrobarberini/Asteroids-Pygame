# 🚀 Asteroids Pygame

Um clone do clássico arcade **Asteroids** desenvolvido em Python com Pygame, com menu animado, sistema de partículas, sons e música de fundo.

---

## 🎮 Como Jogar

| Tecla | Ação |
|-------|------|
| `←` `→` | Girar a nave |
| `↑` | Acelerar |
| `Espaço` | Atirar |
| `R` | Reiniciar após Game Over |
| `Enter` | Select |

**Objetivo:** destrua todos os asteroides sem ser atingido. Cada asteroide grande se divide em menores ao ser destruído. Sobreviva o máximo que conseguir!

---

## 🗂️ Estrutura do Projeto

```
Asteroids Pygame/
├── assets/
│   ├── fonts/
│   ├── Images/
│   ├── sounds/
│   │   ├── Death-sound.mp3
│   │   ├── Explosion-sound.mp3
│   │   ├── Menu-music.mp3
│   │   └── Shooting-sound.mp3
│   └── sprites/
├── src/
│   ├── asteroid.py     # Classe dos asteroides e lógica de divisão
│   ├── bullet.py       # Classe dos projéteis
│   ├── main.py         # Loop principal do jogo
│   ├── menu.py         # Tela de menu com asteroides animados
│   ├── particle.py     # Sistema de partículas para explosões
│   ├── player.py       # Classe da nave do jogador
│   ├── settings.py     # Configurações gerais
│   ├── sounds.py       # Gerenciador de áudio
│   └── utils.py        # Funções utilitárias
├── venv/
└── Readme.md
```

---

## ⚙️ Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/Pedrobarberini/Asteroids-Pygame.git
cd Asteroids-Pygame
```

**2. Crie e ative um ambiente virtual:**
```bash
# Criar
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (macOS / Linux)
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install pygame
```

**4. Execute o jogo:**
```bash
python src/menu.py
```

---

## 🔊 Sistema de Áudio

O jogo conta com sons para cada ação importante:

| Som | Arquivo | Quando toca |
|-----|---------|-------------|
| Música de menu | `Menu-music.mp3` | Na tela inicial (loop) |
| Tiro | `Shooting-sound.mp3` | Ao pressionar Espaço |
| Explosão | `Explosion-sound.mp3` | Ao destruir um asteroide |
| Morte | `Death-sound.mp3` | Ao colidir com um asteroide / Game Over |

---

## ✨ Funcionalidades

- Menu animado com asteroides em movimento e campo de estrelas
- Nave com física de inércia e rotação
- Asteroides que se dividem em pedaços menores ao ser destruídos
- Sistema de partículas nas explosões
- Spawn progressivo de asteroides ao longo do tempo
- Placar e sistema de vidas
- Tela de Game Over com opção de reiniciar

---

## 🛠️ Tecnologias

- **Python 3** — linguagem principal
- **Pygame 2** — renderização, input e áudio

---

## 📄 Licença

Este projeto foi desenvolvido para fins de aprendizado.