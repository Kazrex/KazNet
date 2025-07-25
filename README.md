# KAZNET - Тегін хабарландыру боты

Бұл Қазақстан бойынша тегін хабарландыру беруге арналған Telegram бот.

## 🚀 Іске қосу

1.  **Репозиторийді көшіріп алыңыз:**
    ```bash
    git clone <сіздің_репозиторий_сілтемеңіз>
    cd kaznet_bot
    ```

2.  **Виртуалды ортаны құрып, активтендіріңіз:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows үшін: venv\Scripts\activate
    ```

3.  **Тәуелділіктерді орнатыңыз:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Токенді конфигурациялаңыз:**
    *   `.env.example` файлының көшірмесін жасап, атын `.env` деп өзгертіңіз.
    *   `.env` файлының ішіне `@BotFather`-дан алған өз токеніңізді қойыңыз.

5.  **Базаны инициализациялаңыз:**
    Бот бірінші рет іске қосылғанда, `ads.db` файлы мен кестелер автоматты түрде құрылады.

6.  **Ботты іске қосыңыз:**
    ```bash
    python main.py
    ```

## 📂 Жоба структурасы

Жоба модульдік принциппен құрастырылған, бұл оны болашақта кеңейтуді жеңілдетеді.
*   `main.py`: Ботты іске қосатын негізгі файл.
*   `bot/`: Боттың негізгі логикасы.
    *   `handlers/`: Пайдаланушы командалары мен әрекеттерін өңдейтін хендлерлер.
    *   `keyboards/`: Telegram батырмалары.
    *   `states/`: FSM (Finite State Machine) күйлері.
    *   `utils/`: Көмекші модульдер (базамен жұмыс, логгинг).
*   `data/`: Қалалар мен категориялар сияқты статикалық деректер (JSON).
*   `database/`: Дерекқорға қатысты файлдар.