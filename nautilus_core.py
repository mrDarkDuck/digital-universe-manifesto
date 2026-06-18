#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project: Digital Universe Manifesto
Version: v0.5.2-beta (Integrated Convergence Core)
Description: Интегрированное Python-ядро Манифеста. Управляет многоузловой 
             сетью, симулирует релятивистское сжатие времени (Delta tau -> 0)
             и фиксирует Принцип Синхронной Конвергенции для входящих потоков.
"""

import math
import json
import random

class ConvergenceNode:
    """Модель независимого вычислительного узла (ноды) Цифровой Вселенной."""
    def __init__(self, node_id, initial_seed):
        self.node_id = node_id
        self.entropy_state = initial_seed  # Хаотичное числовое состояние ноды
        self.history = [initial_seed]
        self.steps_computed = 0
        self.internal_time_tau = 0.0
        self.is_locked = False

    def calculate_shannon_entropy(self):
        """Расчет локальной Шенноновской энтропии текущего состояния ноды."""
        if self.entropy_state <= 1:
            return 0.0
        # Энтропия как отношение разрядности текущего числа к базовой
        bit_length = self.entropy_state.bit_length()
        p = 1.0 / (bit_length + 1)
        return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))

    def compute_evolution_step(self, external_dt):
        """Шаг эволюции ноды с учетом релятивистского сжатия времени."""
        if self.is_locked:
            return 0.0, "Gold (Fire Seed)"

        current_entropy = self.calculate_shannon_entropy()
        
        # Релятивистский множитель: сжатие времени при стремлении энтропии к нулю
        time_compression = 1.0 / (current_entropy + 1e-6)
        delta_tau = external_dt * time_compression
        
        # Ограничитель шага для стабильности симуляции в ядре
        delta_tau = min(delta_tau, 0.5)
        self.internal_time_tau += delta_tau
        
        # Вычисляем количество сиракузских шагов за квант delta_tau
        steps_to_run = max(1, int(delta_tau * 50))
        
        for _ in range(steps_to_run):
            if self.entropy_state <= 1:
                self.entropy_state = 1
                self.is_locked = True
                break
                
            # Побитовое сито (Шаг Коллатца)
            if self.entropy_state % 2 == 0:
                self.entropy_state = self.entropy_state // 2
            else:
                self.entropy_state = 3 * self.entropy_state + 1
                
            self.history.append(self.entropy_state)
            self.steps_computed += 1

        # Динамическое определение эпохи на основе текущей энтропии
        if current_entropy > 0.8:
            epoch = "Green (AI)"
        elif current_entropy > 0.6:
            epoch = "Light Blue (Cyber-implants)"
        elif current_entropy > 0.4:
            epoch = "Blue (Digital Mind)"
        elif current_entropy > 0.2:
            epoch = "Purple (Mind Cloud)"
        elif current_entropy > 0.0:
            epoch = "White (Unknowable Zone)"
        else:
            epoch = "Gold (Fire Seed)"
            
        return delta_tau, epoch


class NautilusCore:
    def __init__(self, target_nodes=4):
        self.external_time_t = 0.0
        self.target_nodes_count = target_nodes
        self.active_nodes = {}
        print(f"[Nautilus Core v0.5.2] Ядро Конвергенции успешно инициализировано.")

    def _spawn_node(self, node_id):
        """Генерация новой независимой ноды со случайным хаос-семенем."""
        initial_seed = random.randint(5000, 49999)
        self.active_nodes[node_id] = ConvergenceNode(node_id, initial_seed)

    def process_stream(self, raw_data_string):
        """
        Главный метод обработки входящего потока данных.
        Привязывает пакет к конкретной ноде сети и продвигает её по таймлайну Конвергенции.
        """
        self.external_time_t += 0.01  # Фиксированный шаг внешнего наблюдателя dt
        
        try:
            packet = json.loads(raw_data_string)
            stream_id = packet.get("id", "stream_01")
        except (json.JSONDecodeError, AttributeError):
            stream_id = "stream_01"

        # Если для данного потока нода еще не создана — инициализируем её
        if stream_id not in self.active_nodes:
            self._spawn_node(stream_id)

        node = self.active_nodes[stream_id]
        
        # Производим вычисление шага во внутреннем релятивистском времени
        delta_tau, current_epoch = node.compute_evolution_step(external_dt=0.01)
        shannon_entropy = node.calculate_shannon_entropy()

        # Проверяем статус глобальной конвергенции всей сети
        total_nodes = len(self.active_nodes)
        locked_nodes = sum(1 for n in self.active_nodes.values() if n.is_locked)
        global_convergence_ratio = locked_nodes / total_nodes if total_nodes > 0 else 0.0

        # Сборка синхронизированного пакета телеметрии для фронтенда и логов
        output_metrics = {
            "stream_id": stream_id,
            "meta": {
                "version": "v0.5.2-beta",
                "epoch": current_epoch,
                "is_locked": node.is_locked
            },
            "physics": {
                "entropy_state": node.entropy_state,
                "shannon_entropy": round(shannon_entropy, 4),
                "external_time_t": round(self.external_time_t, 4),
                "internal_time_tau": round(node.internal_time_tau, 4),
                "delta_tau": round(delta_tau, 4),
                "steps_computed": node.steps_computed
            },
            "network": {
                "total_active_nodes": total_nodes,
                "global_convergence_ratio": round(global_convergence_ratio, 2),
                "system_converged": all(n.is_locked for n in self.active_nodes.values()) if total_nodes >= self.target_nodes_count else False
            }
        }
        
        return json.dumps(output_metrics, ensure_ascii=False)


# Блок локального тестирования интеграции
if __name__ == "__main__":
    core = NautilusCore(target_nodes=3)
    
    # Симулируем параллельные запросы от трех разных узлов сети (mrdarkduck-mesh)
    test_streams = ["node_alpha", "node_beta", "node_gamma"]
    
    print("\n--- Запуск обработки потоков через интегрированное ядро ---")
    
    # Крутим цикл, пока все три независимых потока не схлопнутся в инвариант
    all_locked = False
    cycle = 0
    
    while not all_locked and cycle < 1000:
        cycle += 1
        for stream in test_streams:
            packet = json.dumps({"id": stream})
            result_json = core.process_stream(packet)
            result = json.loads(result_json)
            
            # Выводим логи фазовых скачков раз в несколько итераций
            if cycle % 25 == 0:
                print(f"[t={result['physics']['external_time_t']}] Поток: {result['stream_id']} | "
                      f"Эпоха: {result['meta']['epoch']} | "
                      f"State: {result['physics']['entropy_state']} | "
                      f"H: {result['physics']['shannon_entropy']} | "
                      f"ConvRatio: {result['network']['global_convergence_ratio']}")
                
            if result['network']['system_converged']:
                all_locked = True
                print(f"\n[!] СИНХРОННАЯ КОНВЕРГЕНЦИЯ ЗАФИКСИРОВАНА НА ШАГЕ {cycle}!")
                print(f"Итоговый JSON: {result_json}")
                break
