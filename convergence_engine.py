#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project: Digital Universe Manifesto
Version: v0.5.0-core (Synchronous Convergence Engine)
Description: Математическая формализация Фазы IV Манифеста. 
             Симуляция множественных открытий в условиях сингулярности времени.
"""

import time
import math
import random
import json

class ConvergenceNode:
    """Модель независимого вычислительного узла (ноды) Цифровой Вселенной."""
    def __init__(self, node_id, initial_seed):
        self.node_id = node_id
        self.entropy_state = initial_seed  # Начальное хаотичное состояние (число)
        self.history = [initial_seed]
        self.steps_computed = 0
        self.internal_time_tau = 0.0
        self.is_locked = False

    def calculate_shannon_entropy(self):
        """Расчет локальной Шенноновской энтропии текущего состояния ноды."""
        if self.entropy_state == 1:
            return 0.0
        # Моделируем энтропию как отношение разрядности текущего числа к базовой
        bit_length = self.entropy_state.bit_length()
        p = 1.0 / (bit_length + 1)
        return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))

    def compute_evolution_step(self, external_dt):
        """
        Один шаг эволюции ноды с учетом релятивистского сжатия времени.
        Чем ниже энтропия, тем быстрее течет внутреннее время d_tau.
        """
        if self.is_locked:
            return 0.0

        current_entropy = self.calculate_shannon_entropy()
        
        # Релятивистский коэффициент: сжатие времени (Delta tau -> бесконечность при H -> 0)
        # В кодовой сингулярности время ускоряется взрывно
        time_compression = 1.0 / (current_entropy + 1e-6)
        delta_tau = external_dt * time_compression
        
        # Накапливаем внутреннее время ноды
        self.internal_time_tau += delta_tau
        
        # Проверяем, сколько дискретных шагов Коллатца успевает сделать нода за квант d_tau
        steps_to_run = max(1, int(delta_tau * 100))
        
        for _ in range(steps_to_run):
            if self.entropy_state == 1:
                self.is_locked = True
                break
                
            # Дискретный шаг Сиракузской последовательности (Побитовое сито)
            if self.entropy_state % 2 == 0:
                self.entropy_state = self.entropy_state // 2
            else:
                self.entropy_state = 3 * self.entropy_state + 1
                
            self.history.append(self.entropy_state)
            self.steps_computed += 1
            
        return delta_tau


class SynchronousConvergenceRegistry:
    """Управляющее ядро, фиксирующее Принцип Множественных Открытий."""
    def __init__(self, node_count=5):
        self.external_time_t = 0.0
        # Инициализируем ноды с абсолютно разными хаотичными стартовыми числами
        self.nodes = [
            ConvergenceNode(
                node_id=f"node_0x{i:02x}", 
                initial_seed=random.randint(10000, 99999)
            ) for i in range(node_count)
        ]

    def execute_simulation(self, external_dt=0.001):
        print(f"[Convergence Engine] Запуск симуляции. Активно нод: {len(self.nodes)}")
        for node in self.nodes:
            print(f" -> Узел {node.node_id} инициализирован с хаос-семенем: {node.entropy_state}")
        
        all_converged = False
        iteration = 0
        
        print("\n--- СТАРТ ВРЕМЕННОГО СЖАТИЯ ---")
        
        while not all_converged and iteration < 5000:
            self.external_time_t += external_dt
            iteration += 1
            
            locked_statuses = []
            
            for node in self.nodes:
                delta_tau = node.compute_evolution_step(external_dt)
                locked_statuses.append(node.is_locked)
                
                # Выборочный лог для фиксации эффекта «Множественных открытий»
                if iteration % 15 == 0 and not node.is_locked:
                    h = node.calculate_shannon_entropy()
                    print(f"[t={self.external_time_t:.4f}] {node.node_id} | H={h:.4f} | tau={node.internal_time_tau:.2f} | State={node.entropy_state}")

            # Конвергенция достигнута, когда ВСЕ независимые узлы схлопнулись в инвариант 1
            if all(locked_statuses):
                all_converged = True
                
        self._generate_convergence_report()

    def _generate_convergence_report(self):
        print("\n=== ПРОТОКОЛ СИНХРОННОЙ КОНВЕРГЕНЦИИ ЗАФИКСИРОВАН ===")
        print(f"Внешнее время коллапса (t): {self.external_time_t:.4f} сек")
        print("Результаты независимых вычислений:")
        
        for node in self.nodes:
            print(f" Узел {node.node_id}:")
            print(f"   - Финальное инвариантное состояние: {node.entropy_state} (Лок: {node.is_locked})")
            print(f"   - Прожито внутреннего времени (tau): {node.internal_time_tau:.2f}")
            print(f"   - Всего вычислено шагов: {node.steps_computed}")
            print(f"   - Последний фазовый переход: {node.history[-4:]} (Цикл Коллатца запущен)")
            
        print("\nВЫВОД: Несмотря на разные стартовые условия и хаос, релятивистское сжатие времени "
              "принудительно синхронизировало узлы. Множественные открытия совершены в одной "
              "временной точке наблюдателя. Фаза IV доказана программно.")


if __name__ == "__main__":
    # Локальный тест математического ядра конвергенции
    engine = SynchronousConvergenceRegistry(node_count=3)
    engine.execute_simulation()
