#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project: Digital Universe Manifesto
Version: v0.1.0-bridge (WebSocket Middleware Server)
Description: Серверная прослойка для сквозной real-time трансляции метрик
             между фронтендом v0.4.2-beta и ядром nautilus_core.py.
"""

import asyncio
import json
import websockets
# Импортируем синхронизированное ядро
from nautilus_core import NautilusCore

class NautilusWSServer:
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        # Инициализируем ядро с ожиданием конвергенции 4 независимых нод
        self.core = NautilusCore(target_nodes=4)
        print(f"[Nautilus Gateway] Движок моста готов к работе.")

    async def handler(self, websocket):
        """Обработчик активной WebSocket-сессии с фронтендом."""
        client_ip = websocket.remote_address[0]
        print(f"[Gateway] Соединение установлено с узлом: {client_ip}")
        
        try:
            async for message in websocket:
                # 1. Принимаем сырые параметры (например, id частицы, gravity, distance) из JS
                # 2. Прогоняем через математику 3D-конуса и сито дифференциальных инвариантов
                processed_json = self.core.process_stream(message)
                
                # 3. Мгновенно отправляем обратно на фронтенд для рендеринга на HUD панели
                await websocket.send(processed_json)
                
        except websockets.exceptions.ConnectionClosedOK:
            print(f"[Gateway] Соединение штатно закрыто узлом: {client_ip}")
        except websockets.exceptions.ConnectionClosedError:
            print(f"[Gateway] Соединение аварийно разорвано узлом: {client_ip}")
        except Exception as e:
            print(f"[Gateway] Критическая ошибка сессии: {str(e)}")

    async def start(self):
        """Запуск асинхронного сервера."""
        print(f"[Gateway] Запуск WebSocket-сервера на ws://{self.host}:{self.port}")
        async with websockets.serve(self.handler, self.host, self.port):
            await asyncio.Future()  # Сервер работает перманентно

if __name__ == "__main__":
    server = NautilusWSServer()
    try:
        asyncio.run(server.start())
    except KeyboardInterrupt:
        print("\n[Gateway] WebSocket-сервер остановлен пользователем.")
