import time
import random
import keyboard
import config as conf
from state import state

cfg = conf.config

last_spam_time = 0

messages = [
    "Тренируешь PvP? Я сделал бота для прокачки — t.me/retroLabPvP",
    "Хочешь апнуть PvP скилл? Вот мой бот — t.me/retroLabPvP",
    "Учусь PvP с помощью своего бота, глянь — t.me/retroLabPvP",
    "Сделал бота для тренировки PvP, может зайдёт — t.me/retroLabPvP",
    "Если качаешь PvP — вот мой бот для тренировок — t.me/retroLabPvP",
    "Пишу бота, который помогает учить PvP — t.me/retroLabPvP",
    "Треню PvP через своего бота, делюсь — t.me/retroLabPvP",
    "Бот для практики PvP, кому интересно — t.me/retroLabPvP",
    "Делаю бота для PvP тренировок, можно посмотреть — t.me/retroLabPvP",
    "Хочешь лучше драться в PvP? Я сделал бота — t.me/retroLabPvP",

    "Прокачиваю PvP с ботом, который сам написал — t.me/retroLabPvP",
    "Бот для улучшения PvP, тестирую — t.me/retroLabPvP",
    "Тренировки PvP с ботом, заходи — t.me/retroLabPvP",
    "Сделал удобного бота для PvP тренинга — t.me/retroLabPvP",
    "Если играешь PvP — может пригодится — t.me/retroLabPvP",
    "Разрабатываю PvP бота, показываю прогресс — t.me/retroLabPvP",
    "Бот, который помогает учиться PvP быстрее — t.me/retroLabPvP",
    "Тестирую своего PvP бота, вот канал — t.me/retroLabPvP",
    "Учусь PvP и сделал под это бота — t.me/retroLabPvP",
    "Пилил бота под PvP тренировки — t.me/retroLabPvP",

    "Кто хочет апнуть PvP — зацените бота — t.me/retroLabPvP",
    "Бот для PvP практики, делюсь — t.me/retroLabPvP",
    "Разрабатываю бота под PvP, можно чекнуть — t.me/retroLabPvP",
    "Хочу улучшить PvP, сделал для этого бота — t.me/retroLabPvP",
    "PvP тренировки через бота, вот ссылка — t.me/retroLabPvP",
    "Если интересен PvP — вот мой проект — t.me/retroLabPvP",
    "Создаю бота для PvP обучения — t.me/retroLabPvP",
    "Бот помогает тренить PvP, сам пользуюсь — t.me/retroLabPvP",
    "Начал делать бота под PvP — t.me/retroLabPvP",
    "Бот для PvP тренировок в процессе — t.me/retroLabPvP",

    "Качаю PvP через своего бота — t.me/retroLabPvP",
    "Сделал инструмент для PvP практики — t.me/retroLabPvP",
    "Делюсь ботом для PvP тренировок — t.me/retroLabPvP",
    "Работаю над PvP ботом, заходи — t.me/retroLabPvP",
    "PvP бот для тренировки реакции — t.me/retroLabPvP",
    "Тренирую PvP эффективнее с ботом — t.me/retroLabPvP",
    "Хочешь стабильнее PvP? Я сделал бота — t.me/retroLabPvP",
    "Бот для PvP, который реально помогает — t.me/retroLabPvP",
    "Пишу полезного бота для PvP — t.me/retroLabPvP",
    "Разрабатываю PvP тренажёр в виде бота — t.me/retroLabPvP"
]

def run_spam():
    global last_spam_time

    if not cfg.SPAM:
        return
    
    if not state.is_active_window_minecraft:
        return

    now = time.time()

    delay = 60 * 17 + 37

    if now - last_spam_time >= delay:
        message = random.choice(messages)

        keyboard.press_and_release('t')
        time.sleep(0.05)

        keyboard.write(message)
        time.sleep(0.05)

        keyboard.press_and_release('enter')

        last_spam_time = now