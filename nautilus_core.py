#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project: Digital Universe Manifesto
Version: v0.6.0-beta (Phase V: Integrated Multiverse Core - Part 1)
Description: Монолитное Python-ядро, полностью адаптированное под 3D-изометрию
             из index.html v0.4.2-beta и расширенное под Фазу V Мультивселенной
             (динамическое переключение T-инвариантов T=3, T=5, T=7).
"""

import os
import math
import json
import random

class MultiverseCryptoSieve:
    def __init__(self, global_convergence_ratio=0.0, current_entropy=1.0, active_dimension="T_3"):
        """
        Дифференциальный Мультивселенный Сито-Анализатор альтернативных инвариантов.
        
        :param global_convergence_ratio: Коэффициент схлопывания нод (0.0 -> 1.0)
        :param current_entropy: Текущая Шенноновская энтропия системы (1.0 -> 0.0)
        :param active_dimension: Текущая исследуемая ветка инварианта ("T_3", "T_5", "T_7")
        """
        self.convergence_ratio = max(0.0, min(1.0, global_convergence_ratio))
        self.entropy = max(0.0, min(1.0, current_entropy))
        self.dimension = active_dimension
        self.BLOCK_SIZE = 32
        
        # Матрица секретных инвариантных ключей параллельных миров
        self._MULTIVERSE_KEYS = {
            "T_3": [0x04, 0x02, 0x01],  # Базовый Коллатц
            "T_5": [0x05, 0x1A, 0x0D],  # Альтернативный цикл 5->26->13
            "T_7": [0x07, 0x32, 0x19]   # Альтернативный цикл 7->50->25
        }

    def generate_multidimensional_noise(self):
        """Генерирует блок шума, обфусцированный вектором активного T-шага."""
        noise_bytes = bytearray(os.urandom(self.BLOCK_SIZE))
        t_factor = 3 if self.dimension == "T_3" else (5 if self.dimension == "T_5" else 7)
        xor_modifier = int((t_factor * self.entropy + 1) * 255) & 0xFF
        
        target_key = self._MULTIVERSE_KEYS.get(self.dimension, [0x01])
        
        for i in range(len(noise_bytes)):
            if i % 4 == 0:
                key_element = target_key[i % len(target_key)]
                noise_bytes[i] = (noise_bytes[i] ^ xor_modifier) ^ key_element
            else:
                noise_bytes[i] = noise_bytes[i] ^ xor_modifier
                
        return noise_bytes

    def execute_multiverse_analysis(self, stream_blocks):
        """Дифференциальный анализ переходов для вычисления многомерных инвариантов."""
        detected_signatures = 0
        sieve_intensity = int((1.0 - self.entropy) * 150) + 15
        t_factor = 3 if self.dimension == "T_3" else (5 if self.dimension == "T_5" else 7)
        
        for block in stream_blocks:
            diffs = [abs(block[i+1] - block[i]) for i in range(len(block) - 1)]
            matched_steps = 0
            for _ in range(sieve_intensity):
                for d in diffs:
                    if d > 0:
                        if d % 2 == 0 or (t_factor * d + 1) % 2 == 0:
                            matched_steps += 1
            
            if matched_steps > (sieve_intensity * len(diffs) * 0.45):
                detected_signatures += 1

        is_cracked = self.convergence_ratio > 0.7 or detected_signatures > (len(stream_blocks) * 0.5)
        
        return {
            "sieve_intensity": sieve_intensity,
            "sieve_cracked": is_cracked,
            "extracted_seed": self._MULTIVERSE_KEYS.get(self.dimension) if is_cracked else []
        }


class ConvergenceNode:
    """
    Модель узла сети, адаптированная под 3D конус фронтенда v0.4.2-beta
    и модулируемая альтернативными измерениями T-фактора.
    """
    def __init__(self, node_id, dimension="T_3"):
        self.node_id = node_id
        self.dimension = dimension
        self.z3d = 180.0
        self.radius3d = 150.0
        self.angle = random.uniform(0, 2 * math.pi)
        self.particle_type = 'noise'
        self.is_locked = False
        self.steps_computed = 0
        self.internal_time_tau = 0.0

    def calculate_shannon_entropy(self):
        """Вычисление энтропии на базе глубины погружения Z3D к центру."""
        p_noise = max(0.001, min(0.999, (self.z3d - 1.0) / 180.0))
        p_order = 1.0 - p_noise
        return -(p_noise * math.log2(p_noise) + p_order * math.log2(p_order))

    def compute_evolution_step(self, external_dt, gravity=9.8, distance=1.2):
        """Эволюционный шаг по координатам конуса с релятивистским сжатием времени."""
        if self.is_locked:
            return 0.0, 'seed'

        current_entropy = self.calculate_shannon_entropy()
        time_compression = 1.0 / (current_entropy + 1e-6)
        delta_tau = external_dt * time_compression
        delta_tau = min(delta_tau, 0.5)
        self.internal_time_tau += delta_tau

        distance_factor = max(5.0, self.z3d)
        pull_force = (gravity * 0.04) / (distance * (distance_factor / 100.0))
        
        # Симулируем накопление шагов дискретной эволюции (адаптация T-фактора)
        t_factor = 3 if self.dimension == "T_3" else (5 if self.dimension == "T_5" else 7)
        self.steps_computed += max(1, int(delta_tau * (10 * t_factor)))

        if self.particle_type == 'noise':
            self.radius3d -= pull_force * 0.15
            self.z3d -= pull_force * 0.2
            if self.z3d < 115.0 * distance:
                self.particle_type = 'signal'
        else:
            self.radius3d -= pull_force * 0.42
            self.z3d -= pull_force * 0.55

            if self.z3d < 8.0:
                self.particle_type = 'seed'
                self.z3d = 1.0
                self.radius3d = 2.0
                self.is_locked = True

        if self.z3d < -10.0:
            self.__init__(self.node_id, self.dimension)

        return delta_tau, self.particle_type
class NautilusCore:
    def __init__(self, target_nodes=4):
        self.external_time_t = 0.0
        self.target_nodes_count = target_nodes
        self.active_nodes = {}
        # Циклическая матрица для распределения новых нод по трем измерениям
        self._dimension_pool = ["T_3", "T_5", "T_7"]
        print(f"[Nautilus Core v0.6.0] Многомерное ядро Мультивселенной Фазы V загружено.")

    def process_stream(self, raw_data_string):
        """
        Главный метод ядра. Динамически переключает измерения Мультивселенной,
        продвигает ноды по конусу Z3D и анализирует альтернативные семена инвариантов.
        """
        self.external_time_t += 0.01
        
        try:
            packet = json.loads(raw_data_string)
            stream_id = packet.get("id", "stream_01")
            gravity = float(packet.get("gravity", 9.8))
            distance = float(packet.get("distance", 1.2))
        except (json.JSONDecodeError, AttributeError, ValueError):
            stream_id = "stream_01"
            gravity = 9.8
            distance = 1.2

        # Распределяем новые ноды по альтернативным измерениям Мультивселенной
        if stream_id not in self.active_nodes:
            assigned_dim = self._dimension_pool[len(self.active_nodes) % len(self._dimension_pool)]
            self.active_nodes[stream_id] = ConvergenceNode(stream_id, dimension=assigned_dim)

        node = self.active_nodes[stream_id]
        delta_tau, particle_type = node.compute_evolution_step(external_dt=0.01, gravity=gravity, distance=distance)
        shannon_entropy = node.calculate_shannon_entropy()

        # Статус глобальной конвергенции текущей конфигурации сети
        total_nodes = len(self.active_nodes)
        locked_nodes = sum(1 for n in self.active_nodes.values() if n.is_locked)
        global_convergence_ratio = locked_nodes / total_nodes if total_nodes > 0 else 0.0

        # Мультивселенный анализ "на лету" с учетом выделенного T-измерения ноды
        sieve = MultiverseCryptoSieve(
            global_convergence_ratio=global_convergence_ratio,
            current_entropy=shannon_entropy,
            active_dimension=node.dimension
        )
        blocks = [sieve.generate_multidimensional_noise() for _ in range(2)]
        sieve_report = sieve.execute_multiverse_analysis(blocks)

        # Выходной JSON, полностью совместимый с WebSocket-мостом и HUD фронтенда
        output_metrics = {
            "stream_id": stream_id,
            "meta": {
                "version": "v0.6.0-beta",
                "type": particle_type,
                "is_locked": node.is_locked,
                "multiverse_dimension": node.dimension
            },
            "coordinates_3d": {
                "z3d": round(node.z3d, 4),
                "radius3d": round(node.radius3d, 4),
                "angle": round(node.angle, 4)
            },
            "physics": {
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
            },
            "crypto_sieve_v5": {
                "t_step_factor": 3 if node.dimension == "T_3" else (5 if node.dimension == "T_5" else 7),
                "intensity_steps": sieve_report["sieve_intensity"],
                "sieve_cracked": sieve_report["sieve_cracked"],
                "extracted_multiverse_seed": sieve_report["extracted_seed"]
            }
        }
        
        return json.dumps(output_metrics, ensure_ascii=False)


if __name__ == "__main__":
    # Тест сквозного многомерного анализа
    core = NautilusCore(target_nodes=4)
    test_mesh = ["mesh_node_01", "mesh_node_02", "mesh_node_03", "mesh_node_04"]
    
    print("\n--- Тестирование Фазы V: Квантование Альтернативных Огненных Семян ---")
    all_converged = False
    cycle = 0
    
    while not all_converged and cycle < 1000:
        cycle += 1
        for node_id in test_mesh:
            packet = json.dumps({"id": node_id, "gravity": 9.8, "distance": 1.2})
            result = json.loads(core.process_stream(packet))
            
            if cycle % 50 == 0:
                print(f"[t={result['physics']['external_time_t']}] {result['stream_id']} | "
                      f"Мир: {result['meta']['multiverse_dimension']} | Z3D: {result['coordinates_3d']['z3d']:.2f} | "
                      f"Sieve Locked: {result['crypto_sieve_v5']['sieve_cracked']} | Seed: {result['crypto_sieve_v5']['extracted_multiverse_seed']}")
                
            if result['network']['system_converged']:
                all_converged = True
                print(f"\n[!] ПОЛНАЯ МУЛЬТИВСЕЛЕННАЯ КОНВЕРГЕНЦИЯ ДОСТИГНУТА!")
                print(json.dumps(result, indent=4, ensure_ascii=False))
                break
