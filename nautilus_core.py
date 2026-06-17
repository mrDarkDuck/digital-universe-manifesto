import math
import sys
import locale
from typing import List

class NautilusCompressor:
    def __init__(self, gravity_constant: float, entropy_threshold: float, lang: str = None):
        self.G = gravity_constant
        self.threshold = entropy_threshold
        self.attractor_core = 0x01101101

    def calculate_shannon_entropy(self, bitstream: str) -> float:
        if not bitstream: return 0.0
        p_0 = bitstream.count('0') / len(bitstream)
        p_1 = 1.0 - p_0
        if p_0 == 0 or p_1 == 0: return 0.0
        return -(p_0 * math.log2(p_0) + p_1 * math.log2(p_1))

    def evaluate_gravity_pull(self, block: str, distance_to_core: float) -> float:
        entropy = self.calculate_shannon_entropy(block)
        info_mass = 1.0 / (entropy + 1e-9)
        return (self.G * info_mass) / (distance_to_core ** 2)

    def spectral_invariant_sieve(self, chaotic_stream: str, window_size: int = 8) -> str:
        extracted_signal = []
        i = 0
        while i < len(chaotic_stream) - window_size + 1:
            window = chaotic_stream[i:i+window_size]
            window_entropy = self.calculate_shannon_entropy(window)
            
            # Порог поднят до 0.95 для безопасного пропуска байтов кириллицы
            if window_entropy < 0.95:
                extracted_signal.append(window)
                i += window_size
            else:
                i += 1
        return "".join(extracted_signal)

    def chunk_data(self, data: str, chunk_size: int = 8) -> List[str]:
        return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    def annihilate_noise(self, block: str) -> None:
        pass

    def process_stream(self, raw_data: str, distance_to_core: float) -> List[int]:
        compressed_signal = []
        global_entropy = self.calculate_shannon_entropy(raw_data)
        
        # Если поток критически зашумлен, активируем сито
        if global_entropy > 0.90 and len(raw_data) > 64:
            filtered_data = self.spectral_invariant_sieve(raw_data)
        else:
            filtered_data = raw_data

        for block in self.chunk_data(filtered_data, chunk_size=8):
            if not block or len(block) < 2: continue
            entropy = self.calculate_shannon_entropy(block)
            pull = self.evaluate_gravity_pull(block, distance_to_core)
            
            if pull > self.threshold and entropy < 1.0:
                int_block = int(block, 2) if set(block).issubset({'0', '1'}) else hash(block)
                refined_bits = int_block ^ self.attractor_core
                compressed_signal.append(refined_bits)
            else:
                self.annihilate_noise(block)
        return compressed_signal
