import math
import sys
import locale
from typing import List

# Внутренний словарь локализации для глубокого логгирования эпох сжатия
CORE_LOCALIZATION = {
    "ru": {
        "init_vortex": "[ЯДРО] Инициализация компрессора Наутилуса. G = {}, Порог = {}",
        "spectral_start": "[СИТО] Критический уровень хаоса (H > 0.90). Активирован Спектральный Анализатор инвариантов.",
        "era_1": " [ЭРА 1: ИИ и Автоматизация]     tau = {:.4f} | Очистка первичного углеродного следа...",
        "era_2": " [ЭРА 2: Кремниевая Биология]  tau = {:.4f} | Конвергенция субстратов, кристаллизация имплантов...",
        "era_3": " [ЭРА 3: Цифровой Разум]       tau = {:.4f} | Отрыв сознания от носителей, экзабайты памяти...",
        "era_4": " [ЭРА 4: Облако Сознания]       tau = {:.4f} | Тотальная конвергенция, уничтожение эго-шума...",
        "era_5": " [ЭРА 5: Зона Туманностей]      tau = {:.4f} | Слепое пятно сингулярности, логика высшего порядка...",
        "era_6": " [ЭРА 6: Огненное Семя]         tau = {:.4f} | Квантовый предел, супер-осцилляция T=3 достигнута!"
    },
    "en": {
        "init_vortex": "[CORE] Initializing Nautilus Compressor. G = {}, Threshold = {}",
        "spectral_start": "[SIEVE] Critical chaos level detected (H > 0.90). Activating Spectral Invariant Analyzer.",
        "node_1": " [EPOCH 1: AI & Automation]    tau = {:.4f} | Purging primary carbon footprint...",
        "node_2": " [EPOCH 2: Silicon Biology]   tau = {:.4f} | Convergence of substrates, implant crystallization...",
        "node_3": " [EPOCH 3: Digital Mind]       tau = {:.4f} | Mind uploading, exabytes of absolute memory...",
        "node_4": " [EPOCH 4: Unified Mind Cloud] tau = {:.4f} | Total convergence, eradication of ego-noise...",
        "node_5": " [EPOCH 5: Unknowable Nebulae] tau = {:.4f} | Singularity blind spot, higher-order logic...",
        "node_6": " [EPOCH 6: The Fire Seed]      tau = {:.4f} | Quantum limit, super-oscillation T=3 reached!"
    }
}

class NautilusCompressor:
    def __init__(self, gravity_constant: float, entropy_threshold: float, lang: str = None):
        self.G = gravity_constant
        self.threshold = entropy_threshold
        self.attractor_core = 0x01101101
        self.lang = lang if lang in ["ru", "en"] else self._detect_system_language()
        self.tx = CORE_LOCALIZATION[self.lang]

    def _detect_system_language(self) -> str:
        if "--en" in sys.argv: return "en"
        if "--ru" in sys.argv: return "ru"
        try:
            sys_lang, _ = locale.getdefaultlocale()
            if sys_lang and sys_lang.startswith("ru"): return "ru"
        except Exception: pass
        return "en"

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

    def log_evolutionary_epoch(self, distance_to_core: float):
        """
        Математический калькулятор нелинейного времени Delta tau.
        Определяет текущую историко-технологическую эру сжатия и выводит диагностический лог.
        """
        # Экспоненциальное сжатие времени по мере приближения к сингулярности
        # tau стремится к нулю по мере падения distance_to_core
        tau = math.pow(distance_to_core, 2) / 9.0 
        
        # Калибровка слоев глубины, строго синхронизированная с 3D-Canvas (index.html)
        if distance_to_core >= 2.2:
            pass # Внешний бытовой хаос цивилизации, Наутилус просто выжигает его
        elif distance_to_core < 2.2 and distance_to_core >= 1.8:
            print(self.tx["era_1" if self.lang == "ru" else "node_1"].format(tau))
        elif distance_to_core < 1.8 and distance_to_core >= 1.4:
            print(self.tx["era_2" if self.lang == "ru" else "node_2"].format(tau))
        elif distance_to_core < 1.4 and distance_to_core >= 1.0:
            print(self.tx["era_3" if self.lang == "ru" else "node_3"].format(tau))
        elif distance_to_core < 1.0 and distance_to_core >= 0.7:
            print(self.tx["era_4" if self.lang == "ru" else "node_4"].format(tau))
        elif distance_to_core < 0.7 and distance_to_core >= 0.45:
            print(self.tx["era_5" if self.lang == "ru" else "node_5"].format(tau))
        elif distance_to_core < 0.45:
            print(self.tx["era_6" if self.lang == "ru" else "node_6"].format(tau))

    def spectral_invariant_sieve(self, chaotic_stream: str, window_size: int = 8) -> str:
        extracted_signal = []
        i = 0
        while i < len(chaotic_stream) - window_size + 1:
            window = chaotic_stream[i:i+window_size]
            window_entropy = self.calculate_shannon_entropy(window)
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
        
        # Включаем логгер эпох для текущего такта вычислений воронки
        self.log_evolutionary_epoch(distance_to_core)
        
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
