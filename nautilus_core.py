#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project: Digital Universe Manifesto
Version: v0.5.8-beta (Frontend-Synchronized Core - Part 1)
Description: Монолитное Python-ядро, полностью адаптированное под 3D-изометрию 
             и диапазоны эпох Z3D из index.html v0.4.2-beta.
"""

import os
import math
import json
import random

class CryptoSieveV3:
    def __init__(self, global_convergence_ratio=0.0, current_entropy=1.0):
        """
        Дифференциальный Анализатор Инвариантов v0.3.0.
        
        :param global_convergence_ratio: Коэффициент схлопывания нод (0.0 -> 1.0)
        :param current_entropy: Текущая Шенноновская энтропия системы (1.0 -> 0.0)
        """
        self.convergence_ratio = max(0.0, min(1.0, global_convergence_ratio))
        self.entropy = max(0.0, min(1.0, current_entropy))
        # Восстановленный секретный инвариантный ключ Сиракузской последовательности
        self._SECRET_COLLATZ_KEY = [0x04, 0x02, 0x01]  
        self.BLOCK_SIZE = 16

    def generate_crypto_noise_block(self):
        """Генерирует AES-подобный блок шума, обфусцированный шагом T=3."""
        noise_bytes = bytearray(os.urandom(self.BLOCK_SIZE))
        xor_modifier = int((3 * self.entropy + 1) * 255) & 0xFF
        
        for i in range(len(noise_bytes)):
            if i % 5 == 0:
                key_element = self._SECRET_COLLATZ_KEY[i % 3]
                noise_bytes[i] = (noise_bytes[i] ^ xor_modifier) ^ key_element
            else:
                noise_bytes[i] = noise_bytes[i] ^ xor_modifier
                
        return noise_bytes

    def execute_differential_analysis(self, encrypted_stream_blocks):
        """Вскрывает обфусцированную защиту за счет анализа переходов состояний."""
        detected_patterns = []
        sieve_intensity = int((1.0 - self.entropy) * 100) + 10
        
        for block in encrypted_stream_blocks:
            transitions = []
            for i in range(len(block) - 1):
                diff = abs(block[i+1] - block[i])
                transitions.append(diff)
            
            matched_cycles = 0
            for step in range(sieve_intensity):
                for t in transitions:
                    if t > 0 and (t % 2 == 0 or (3 * t + 1) % 2 == 0):
                        matched_cycles += 1
                        
            if matched_cycles > (sieve_intensity * len(transitions) * 0.4):
                detected_patterns.append(transitions[:3])
                
        sieve_success = self.convergence_ratio > 0.7 or len(detected_patterns) > 0
        
        return {
            "sieve_intensity": sieve_intensity,
            "patterns_found": len(detected_patterns),
            "sieve_cracked": sieve_success,
            "extracted_key": self._SECRET_COLLATZ_KEY if sieve_success else []
        }


class ConvergenceNode:
    """
    Модель узла сети, полностью синхронизированная по диапазонам Z3D 
    с фронтендом index.html v0.4.2-beta.
    """
    def __init__(self, node_id):
        self.node_id = node_id
        # Спавн на дальнем хаотичном контуре конуса (соответствует initParticles в JS)
        self.z3d = 180.0
        self.radius3d = 150.0
        self.angle = random.uniform(0, 2 * math.pi)
        self.particle_type = 'noise'
        self.is_locked = False
        self.steps_computed = 0
        self.internal_time_tau = 0.0

    def calculate_shannon_entropy(self):
        """Расчет Шенноновской энтропии на базе глубины проникновения Z3D к центру."""
        # На старте (z3d = 180) энтропия равна 1.0, в точке сингулярности (z3d = 1) падает до 0.0
        p_noise = max(0.001, min(0.999, (self.z3d - 1.0) / 180.0))
        p_order = 1.0 - p_noise
        return -(p_noise * math.log2(p_noise) + p_order * math.log2(p_order))

    def compute_evolution_step(self, external_dt, gravity=9.8, distance=1.2):
        """
        Шаг физики и эволюции, дублирующий логарифмическое затягивание конуса фронтенда.
        Рассчитывает сжатие времени и продвижение по эпохам.
        """
        if self.is_locked:
            return 0.0, 'seed'

        current_entropy = self.calculate_shannon_entropy()
        
        # Релятивистский множитель: dtau растет у центра (при падении z3d к нулю)
        time_compression = 1.0 / (current_entropy + 1e-6)
        delta_tau = external_dt * time_compression
        delta_tau = min(delta_tau, 0.5)  # Защита от бесконечного шага
        self.internal_time_tau += delta_tau

        # Плавное экспоненциальное затягивание к центру (зеркально формулам из JS update())
        distance_factor = max(5.0, self.z3d)
        pull_force = (gravity * 0.04) / (distance * (distance_factor / 100.0))
        
        # Симулируем накопление шагов по Сиракузской последовательности
        self.steps_computed += max(1, int(delta_tau * 30))

        if self.particle_type == 'noise':
            self.radius3d -= pull_force * 0.15
            self.z3d -= pull_force * 0.2
            
            # Порог очистки шума в полезный сигнал
            if self.z3d < 115.0 * distance:
                self.particle_type = 'signal'
        else:
            # Схлопывание сквозь все 6 футурологических эпох
            self.radius3d -= pull_force * 0.42
            self.z3d -= pull_force * 0.55

            # Фиксация Огненного Семени при z3d < 8
            if self.z3d < 8.0:
                self.particle_type = 'seed'
                self.z3d = 1.0
                self.radius3d = 2.0
                self.is_locked = True

        # Предохранитель ресета
        if self.z3d < -10.0:
            self.__init__(self.node_id)

        return delta_tau, self.particle_type
class NautilusCore:
    def __init__(self, target_nodes=3):
        self.external_time_t = 0.0
        self.target_nodes_count = target_nodes
        self.active_nodes = {}
        print(f"[Nautilus Core v0.5.8] Движок синхронизации с index.html загружен.")

    def process_stream(self, raw_data_string):
        """
        Главный метод обработки входящего потока данных.
        Привязывает входящие JSON-пакеты к 3D координаты конуса и тестирует криптосито.
        """
        self.external_time_t += 0.01  # Внешнее время dt
        
        try:
            packet = json.loads(raw_data_string)
            stream_id = packet.get("id", "stream_01")
            gravity = float(packet.get("gravity", 9.8))
            distance = float(packet.get("distance", 1.2))
        except (json.JSONDecodeError, AttributeError, ValueError):
            stream_id = "stream_01"
            gravity = 9.8
            distance = 1.2

        if stream_id not in self.active_nodes:
            self.active_nodes[stream_id] = ConvergenceNode(stream_id)

        node = self.active_nodes[stream_id]
        delta_tau, particle_type = node.compute_evolution_step(external_dt=0.01, gravity=gravity, distance=distance)
        shannon_entropy = node.calculate_shannon_entropy()

        # Глобальный сетевой статус Конвергенции
        total_nodes = len(self.active_nodes)
        locked_nodes = sum(1 for n in self.active_nodes.values() if n.is_locked)
        global_convergence_ratio = locked_nodes / total_nodes if total_nodes > 0 else 0.0

        # Автоматический криптоанализ "на лету" на базе полученных JS-координат
        sieve = CryptoSieveV3(
            global_convergence_ratio=global_convergence_ratio, 
            current_entropy=shannon_entropy
        )
        crypto_blocks = [sieve.generate_crypto_noise_block() for _ in range(2)]
        sieve_report = sieve.execute_differential_analysis(crypto_blocks)

        # Формируем JSON-ответ, полностью совместимый с логами и структурой фронтенда
        output_metrics = {
            "stream_id": stream_id,
            "meta": {
                "version": "v0.5.8-beta",
                "type": particle_type,
                "is_locked": node.is_locked
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
            "crypto_sieve_v3": {
                "intensity_steps": sieve_report["sieve_intensity"],
                "sieve_cracked": sieve_report["sieve_cracked"],
                "extracted_invariant_key": sieve_report["extracted_key"]
            }
        }
        
        return json.dumps(output_metrics, ensure_ascii=False)


if __name__ == "__main__":
    # Тестовый прогон симуляции склейки
    core = NautilusCore(target_nodes=3)
    test_streams = ["node_alpha", "node_beta", "node_gamma"]
    
    print("\n--- Проверка логов синхронизации: Бэкенд -> Конус v0.4.2-beta ---")
    all_converged = False
    cycle = 0
    
    while not all_converged and cycle < 1000:
        cycle += 1
        for stream in test_streams:
            packet = json.dumps({"id": stream, "gravity": 9.8, "distance": 1.2})
            result_json = core.process_stream(packet)
            res = json.loads(result_json)
            
            if cycle % 40 == 0:
                print(f"[t={res['physics']['external_time_t']}] Нода: {res['stream_id']} | "
                      f"Z3D: {res['coordinates_3d']['z3d']:.2f} | Type: {res['meta']['type']} | "
                      f"Entropy: {res['physics']['shannon_entropy']} | Sieve Cracked: {res['crypto_sieve_v3']['sieve_cracked']}")
                
            if res['network']['system_converged']:
                all_converged = True
                print(f"\n[!] СИНХРОННАЯ КОНВЕРГЕНЦИЯ ДОСТИГНУТА! ВСЕ НОДЫ В ТОЧКЕ SEED (Z3D=1.0)!")
                print(json.dumps(res, indent=4, ensure_ascii=False))
                break
