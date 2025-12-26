<div align="center">

  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3RxeXF4anh4eXF4anh4eXF4anh4eXF4anh4eXF4anh4eXF4anh4eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKSjRrfIPjeiVyM/giphy.gif" alt="Logo" width="100" height="100">

  # 🔮 The Oracle: Ultimate Number Guessing Game

  **A sleek, colorful, and addictive CLI logic game written in Python.**

  <p>
    <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
    <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License">
    <img src="https://img.shields.io/badge/maintenance-active-violet?style=for-the-badge" alt="Maintenance">
    <img src="https://img.shields.io/badge/fun_level-100%25-orange?style=for-the-badge" alt="Fun Level">
  </p>

  <h4>
    <a href="#-installation">Install</a>
    <span> · </span>
    <a href="#-how-to-play">How to Play</a>
    <span> · </span>
    <a href="#-features">Features</a>
    <span> · </span>
    <a href="#-contributing">Contribute</a>
  </h4>
</div>

---

## 🚀 Introduction

**Bored of "Hello World"?**

Welcome to **The Oracle**. This isn't just a random number generator; it's a battle of wits against the machine. Featuring a persistent Hall of Fame, dynamic difficulty adjustments, and a vibrant color-coded interface, this project demonstrates professional Python concepts including file I/O, error handling, and JSON data management.

Can you beat the **Impossible** mode?

## ✨ Features

* **🎨 ANSI Color UI:** Visual feedback using terminal colors (Green for wins, Red for errors, Blue for hints).
* **🏆 Hall of Fame:** Your high scores are saved locally to `highscores.json`. Prove your worth!
* **🛡️ Bulletproof Inputs:** Try entering text, symbols, or spaces—the game handles it all gracefully.
* **🧠 Smart Sorting:** The leaderboard automatically sorts by the fewest attempts, not just the score.

## 🕹️ How to Play

The game generates a random number based on your chosen difficulty. Your goal is to guess it in the fewest attempts possible.

### Difficulty Levels

| Level | Range | Max Guesses | Description |
| :--- | :---: | :---: | :--- |
| **1. Easy** | 1 - 50 | ∞ | Perfect for a casual warm-up. Unlimited tries. |
| **2. Hard** | 1 - 100 | **10** | The standard challenge. Requires binary search strategy. |
| **3. Impossible** | 1 - 1000 | **15** | Only for the brave. One mistake and it's Game Over. |

## 📦 Installation

You don't need fancy package managers. This game runs on pure Python standard libraries.

1.  **Clone the Repo**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/number-guessing-game.git](https://github.com/YOUR_USERNAME/number-guessing-game.git)
    cd number-guessing-game
    ```

2.  **Run the Game**
    ```bash
    python main.py
    ```

## 🤝 Contributing
Got an idea? Found a bug? We love contributions!

Fork the Project

Create your Feature Branch (git checkout -b feature/CoolFeature)

Commit your Changes (git commit -m 'Add some CoolFeature')

Push to the Branch (git push origin feature/CoolFeature)

Open a Pull Request

## 📄 License
Distributed under the MIT License. See LICENSE for more information.

<div align="center"> <p>⭐️ Star this repo if you had fun! ⭐️</p> <sub>Made with ❤️ and too much ☕ </sub> </div>
