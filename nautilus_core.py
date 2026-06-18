#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project: Digital Universe Manifesto
Version: v0.2.0-bridge (WebSocket Multiverse Server - Part 1)
Description: Серверная прослойка для сквозной real-time трансляции метрик
             Мультивселенной Фазы V между фронтендом и ядром.
"""

import asyncio
import json
import websockets
# Импортируем многомерное ядро из nautilus_core.py
from nautilus_core import NautilusCore

class NautilusWSServer:
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        # ИСПРАВЛЕНИЕ ПОД ФАЗУ V: Ожидаем конвергенцию 4 параллельных нод Мультивселенной
        self.core = NautilusCore(target_nodes=4)
        print(f"[Nautilus Multiverse Gateway] Движок моста Фазы V готов к работе.")
    async def handler(self, websocket):
        """Обработчик активной WebSocket-сессии с фронтендом."""
        client_ip = websocket.remote_address
        print(f"[Gateway V5] Соединение установлено с пространством: {client_ip}")
        
        try:
            async for message in websocket:
                # 1. Принимаем параметры изометрии конуса из JavaScript
                # 2. Прогоняем через многомерный анализатор альтернативных инвариантов T-фактора
                processed_json = self.core.process_stream(message)
                
                # 3. Возвращаем обогащенную структуру метаданных Мультивселенной обратно на UI
                await websocket.send(processed_json)
                
        except websockets.exceptions.ConnectionClosedOK:
            print(f"[Gateway V5] Сессия штатно закрыта узлом: {client_ip}")
        except websockets.exceptions.ConnectionClosedError:
            print(f"[Gateway V5] Сессия аварийно разорвана узлом: {client_ip}")
        except Exception as e:
            print(f"[Gateway V5] Критическая ошибка многомерного потока: {str(e)}")

    async def start(self):
        """Запуск асинхронного сервера."""
        print(f"[Gateway V5] Сервер Мультивселенной запущен на ws://{self.host}:{self.port}")
        async with websockets.serve(self.handler, self.host, self.port):
            await asyncio.Future()  # Сервер работает перманентно

if __name__ == "__main__":
    server = NautilusWSServer()
    try:
        asyncio.run(server.start())
    except KeyboardInterrupt:
        print("\n[Gateway V5] WebSocket-сервер Мультивселенной остановлен.")
