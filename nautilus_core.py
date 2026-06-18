#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project: Digital Universe Manifesto
Version: v0.5.0-beta (Nautilus Attractor Core)
Description: 3D динамическая система сжатия данных, побитового сита и инвариантов Коллатца.
"""

import numpy as np
import math
import json
import random

class NautilusAttractor:
    def __init__(self, omega=2.5, b=0.3, k=0.5, sigma=1.2, alpha=3.0, gamma=1.5):
        """
        Физический движок трехмерного аттрактора Наутилуса.
        
        :param omega: Угловая скорость вращения графов вокруг сингулярности.
        :param b: Коэффициент гравитационного затягивания данных к центру.
        :param k: Скорость эволюционного смещения по оси Z.
        :param sigma: Базовая мощность хаоса (энтропии) на внешних границах.
        :param alpha: Степень побитового сита (фильтрация краевого шума).
        :param gamma: Коэффициент релятивистского экспоненциального сжатия времени.
        """
        self.omega = omega
        self.b = b
        self.k = k
        self.sigma = sigma
        self.alpha = alpha
        self.gamma = gamma
        
        # Константы фазового пространства
        self.R_MAX = 10.0
        self.Z_MAX = 5.0
        self.EPSILON = 1e-5

    def _deterministic_derivs(self, state):
        """Вычисление детерминированного поля скоростей (dx/dtau, dy/dtau, dz/dtau)."""
        x, y, z = state
        r = np.sqrt(x**2 + y**2) + self.EPSILON
        
        # Логарифмическое ускорение падения при приближении к сингулярности (r -> 0)
        ln_r = np.log(r / self.R_MAX)
        
        dx = -self.omega * y - self.b * x * ln_r
        dy = self.omega * x - self.b * y * ln_r
        
        # Побитовый фильтр: η(r) стремится к 1 по мере очистки графа от хаоса
        eta_r = 1.0 - (r / self.R_MAX)
        dz = -self.k * z * (1.0 - eta_r)
        
        return np.array([dx, dy, dz])

    def calculate_step(self, state, dt):
        """
        Расчет следующего фазового состояния точки с учетом сжатия времени и шума Шеннона.
        """
        x, y, z = state
        r = np.sqrt(x**2 + y**2) + self.EPSILON
        
        # 1. Релятивистское искажение времени: dt (внешнее) -> dtau (внутреннее)
        time_factor = 1.0 / (np.power(np.abs(self.Z_MAX - z), self.gamma) + self.EPSILON)
        dtau = dt * time_factor
        
        # Стабилизация шага во избежание численного взрыва в точке сингулярности
        dtau = min(dtau, 0.05)

        # 2. Интегрирование детерминированной траектории методом RK4
        k1 = self._deterministic_derivs(state)
        k2 = self._deterministic_derivs(state + 0.5 * dtau * k1)
        k3 = self._deterministic_derivs(state + 0.5 * dtau * k2)
        k4 = self._deterministic_derivs(state + dtau * k3)
        
        new_state = state + (dtau / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        
        # 3. Наложение стохастического Шенноновского шума (Побитовое сито)
        # Амплитуда шума затухает степенным образом (alpha) по мере уменьшения радиуса
        noise_amplitude = self.sigma * np.power(r / self.R_MAX, self.alpha)
        
        if r < 0.05:
            # Предельный переход: система коллапсирует в дискретный шаг Коллатца
            new_state[0] = 0.0
            new_state[1] = 0.0
            
            # Дискретная модуляция координаты Z (эмуляция цикла 4-2-1)
            z_int = int(np.abs(new_state[2] * 100))
            if z_int == 0:
                z_int = 4  # Защита от полного затухания
            
            if z_int % 2 == 0:
                new_state[2] = (z_int // 2) / 100.0
            else:
                new_state[2] = (3 * z_int + 1) / 100.0
        else:
            # Генерация гауссова шума для X и Y координат графа
            noise_x = random.gauss(0, np.sqrt(dtau)) * noise_amplitude
            noise_y = random.gauss(0, np.sqrt(dtau)) * noise_amplitude
            new_state[0] += noise_x
            new_state[1] += noise_y
            
        return new_state, dtau

    def get_current_epoch(self, state):
        """Динамическое определение футурологической эпохи по удалению от центра."""
        x, y, _ = state
        r = np.sqrt(x**2 + y**2)
        relative_r = r / self.R_MAX
        
        if relative_r > 0.8:
            return "Green (AI)"
        elif relative_r > 0.6:
            return "Light Blue (Cyber-implants)"
        elif relative_r > 0.4:
            return "Blue (Digital Mind)"
        elif relative_r > 0.2:
            return "Purple (Mind Cloud)"
        elif relative_r > 0.05:
            return "White (Unknowable Zone)"
        else:
            return "Gold (Fire Seed)"


class NautilusCore:
    def __init__(self):
        # Инициализация аттрактора с кубическим затуханием шума
        self.attractor = NautilusAttractor(omega=2.5, b=0.3, k=0.5, sigma=1.2, alpha=3.0, gamma=1.5)
        self.active_particles = {}

    def calculate_shannon_entropy(self, radius):
        """Расчет теоретической Шенноновской энтропии на данном витке."""
        relative_r = radius / self.attractor.R_MAX
        # Вероятностная неопределенность шума падает при приближении к центру
        p_noise = max(min(np.power(relative_r, self.attractor.alpha), 0.999), 0.001)
        p_order = 1.0 - p_noise
        entropy = -(p_noise * math.log2(p_noise) + p_order * math.log2(p_order))
        return entropy

    def process_stream(self, raw_data_string):
        """
        Главный метод обработки входящего потока данных.
        Превращает хаотичный JSON-сигнал во фрактальные координаты аттрактора Наутилуса.
        """
        try:
            packet = json.loads(raw_data_string)
            particle_id = packet.get("id", "default_stream")
        except (json.JSONDecodeError, AttributeError):
            packet = {}
            particle_id = "default_stream"

        # Если частица новая, выбрасываем её на внешний хаотичный контур (Зеленая эпоха)
        if particle_id not in self.active_particles:
            angle = random.uniform(0, 2 * math.pi)
            self.active_particles[particle_id] = np.array([
                self.attractor.R_MAX * math.cos(angle),
                self.attractor.R_MAX * math.sin(angle),
                self.attractor.Z_MAX
            ])

        current_state = self.active_particles[particle_id]
        
        # Шаг вычисления по дифференциальным уравнениям аттрактора (dt = 0.01)
        dt = 0.01
        new_state, dtau = self.attractor.calculate_step(current_state, dt)
        
        # Сохраняем обновленные координаты частицы в фазовом пространстве
        self.active_particles[particle_id] = new_state
        
        # Расчет радиуса и Шенноновской энтропии
        r = np.sqrt(new_state[0]**2 + new_state[1]**2)
        shannon_entropy = self.calculate_shannon_entropy(r)
        epoch = self.attractor.get_current_epoch(new_state)

        # Сборка финального синхронизированного пакета для фронтенда
        output_metrics = {
            "id": particle_id,
            "coordinates": {
                "x": round(float(new_state[0]), 4),
                "y": round(float(new_state[1]), 4),
                "z": round(float(new_state[2]), 4)
            },
            "physics": {
                "radius": round(float(r), 4),
                "shannon_entropy": round(float(shannon_entropy), 4),
                "delta_tau": round(float(dtau), 4)
            },
            "meta": {
                "epoch": epoch,
                "version": "v0.5.0-beta",
                "collatz_trigger": bool(r < 0.05)
            }
        }
        
        return json.dumps(output_metrics, ensure_ascii=False)

# Точка входа для локального тестирования ядра
if __name__ == "__main__":
    core = NautilusCore()
    print("[Nautilus Core] Движок 3D-аттрактора запущен.")
    
    # Симулируем 5 шагов эволюции одного графа данных
    test_packet = json.dumps({"id": "node_alpha_01", "value": 42})
    for step in range(1, 6):
        result = core.process_stream(test_packet)
        parsed = json.loads(result)
        print(f"Шаг {step} | Эпоха: {parsed['meta']['epoch']} | Entropy: {parsed['physics']['shannon_entropy']} | XYZ: {list(parsed['coordinates'].values())}")
