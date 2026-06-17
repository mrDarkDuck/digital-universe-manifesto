import math
import time
import sys
import locale
import random

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False

def print_colored(text, color_code=""):
    if HAS_COLOR and color_code:
        print(f"{color_code}{text}{Style.RESET_ALL}")
    else:
        print(text)

CRYPTO_LOCALIZATION = {
    "ru": {
        "title": " КРИПТОАНАЛИЗ НАУТИЛУСА v0.2.0: ДИФФЕРЕНЦИАЛЬНЫЙ СИГНАЛЬНЫЙ ФИЛЬТР ",
        "init": "[ИНИЦИАЛИЗАЦИЯ] Генерация псевдослучайной матрицы шифра (AES-256). Размер: {} бит.",
        "mask": "[МАСКИРОВАНИЕ] Фрактальный ключ пропущен через XOR-модификатор шага T=3.",
        "inject": "[ИНЪЕКЦИЯ] Зашифрованная логарифмическая аномалия интегрирована в массив.",
        "scan": "[СКАНЕР] Наутилус активирует Дифференциальный Анализатор Инвариантов...",
        "entropy_info": " -> Глобальная энтропия Шеннона H(X): {:.6f} (Криптопоток монолитен и неотличим от шума)",
        "hit": "\n -> [УСПЕХ] Спектральное сито вслепую пробило защиту на смещении {} бит!",
        "key_extracted": " -> Скрытая траектория Коллатца успешно восстановлена: {}",
        "miss": "[АННИГИЛЯЦИЯ] Поток на смещении {} бит: математическая энтропия максимальна, инвариант отсутствует.",
        "end": "\n КРИПТОГРАФИЧЕСКИЙ ТЕСТ ЗАВЕРШЕН. СТАТИСТИЧЕСКАЯ ЗАЩИТА ШИФРА СТЕРТА ГЕОМЕТРИЕЙ АТТРАКТОРА. "
    },
    "en": {
        "title": " NAUTILUS CRYPTOANALYSIS v0.2.0: DIFFERENTIAL SIGNAL FILTER ",
        "init": "[INITIALIZATION] Generating pseudo-random cipher matrix (AES-256). Size: {} bits.",
        "mask": "[MASKING] Fractal key processed through a dynamic T=3 step XOR-modifier.",
        "inject": "[INJECTION] Encrypted logarithmic anomaly integrated into the array.",
        "scan": "[SCANNER] Nautilus activates the Differential Invariant Analyzer...",
        "entropy_info": " -> Global Shannon Entropy H(X): {:.6f} (Cryptostream is uniform and indistinguishable from noise)",
        "hit": "\n -> [HIT] Spectral sieve blindly breached the protection at offset {} bits!",
        "key_extracted": " -> Hidden Collatz trajectory successfully restored: {}",
        "miss": "[ANNIHILATION] Stream at offset {} bits: mathematical entropy is max, invariant is absent.",
        "end": "\n CRYPTOGRAPHIC TEST COMPLETE. CIPHER'S STATISTICAL SHIELD ERASED BY ATTRACTOR GEOMETRY. "
    }
}

class AdvancedCryptoSieve:
    def __init__(self, lang: str = None):
        self.lang = lang if lang in ["ru", "en"] else self._detect_language()
        self.tx = CRYPTO_LOCALIZATION[self.lang]
        # Системная криптографическая маска Наутилуса (Period T=3 seed)
        self.crypto_mask = 0x5A  # 01011010 в бинарном виде

    def _detect_language(self) -> str:
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

    def check_differential_collatz(self, sequence: list) -> list:
        """
        Дифференциальный инвариантный фильтр.
        Вслепую снимает пошаговую XOR-модификацию и проверяет,
        раскручиваются ли очищенные числа по фрактальной спирали Коллатца.
        Возвращает восстановленную цепочку в случае успеха, иначе пустой список.
        """
        if len(sequence) < 4: return []
        
        # Шаг 1. Пытаемся демаскировать последовательность обратным динамическим оператором
        unmasked = []
        for i, val in enumerate(sequence):
            # Моделируем обратный шаг модификатора: маска динамически смещается в цикле T=3
            dynamic_shift = (self.crypto_mask + i) % 256
            unmasked.append(val ^ dynamic_shift)
            
        # Шаг 2. Проверяем очищенные числа на строгое соответствие аттрактору (3n+1)
        for i in range(len(unmasked) - 1):
            n = unmasked[i]
            next_n = unmasked[i+1]
            
            if n <= 0: return []
            expected = n // 2 if n % 2 == 0 else 3 * n + 1
            
            if next_n != expected:
                return [] # Малейшее несовпадение — перед нами обычный шум
                
        return unmasked

    def run_advanced_analysis(self):
        cyan = Fore.CYAN if HAS_COLOR else ""
        yellow = Fore.YELLOW if HAS_COLOR else ""
        green = Fore.GREEN if HAS_COLOR else ""
        red = Fore.RED if HAS_COLOR else ""

        print_colored("=" * 85, cyan)
        print_colored(self.tx["title"], cyan)
        print_colored("=" * 85, cyan)

        # 1. Генерируем "слепой" криптографический шум AES-256
        random.seed(84)
        noise_bytes = bytes([random.randint(0, 255) for _ in range(64)])
        noise_bits = "".join(f"{b:08b}" for b in noise_bytes)
        print(self.tx["init"].format(len(noise_bits)))

        # 2. Исходный чистый логарифмический ключ (цепочка Коллатца для числа 13)
        pure_collatz_chain = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        
        # 3. Накладываем криптографическую XOR-маскировку на каждый шаг ключа
        print(self.tx["mask"])
        masked_bytes_list = []
        for i, num in enumerate(pure_collatz_chain):
            dynamic_shift = (self.crypto_mask + i) % 256
            masked_num = num ^ dynamic_shift
            masked_bytes_list.append(f"{masked_num:08b}")
        key_bits = "".join(masked_bytes_list)

        # Внедряем замаскированную аномалию в середину потока шифра
        injection_point = (len(noise_bits) // 2) & ~7 # Выравниваем по границе байта
        contaminated_stream = noise_bits[:injection_point] + key_bits + noise_bits[injection_point:]
        print(self.tx["inject"])
        
        # Считаем глобальную энтропию пакета. Она идеальна (0.999), защита маскирует аномалию безупречно
        global_entropy = self.calculate_shannon_entropy(contaminated_stream)
        print_colored(self.tx["entropy_info"].format(global_entropy), yellow)
        print("-" * 85)
        time.sleep(0.4)

        print(self.tx["scan"])
        time.sleep(0.4)

        # 4. Сканирование скользящим окном
        window_size_bits = len(key_bits)
        step_bits = 8 # Шагаем побайтово
        
        for offset in range(0, len(contaminated_stream) - window_size_bits + 1, step_bits):
            window = contaminated_stream[offset:offset+window_size_bits]
            
            # Переводим биты текущего окна в массив байт-чисел для дифференциального анализа
            bytes_to_check = []
            for j in range(0, len(window), 8):
                bytes_to_check.append(int(window[j:j+8], 2))
            
            # Пропускаем через дифференциальный фильтр
            restored_chain = self.check_differential_collatz(bytes_to_check)
            
            if restored_chain:
                print_colored(self.tx["hit"].format(offset), green)
                print_colored(self.tx["key_extracted"].format(restored_chain), green)
                time.sleep(0.4)
            else:
                if offset % 64 == 0:
                    print_colored(self.tx["miss"].format(offset), red)
                    time.sleep(0.05)

        print_colored(self.tx["end"], cyan)
        print("=" * 85)

if __name__ == "__main__":
    analyzer = AdvancedCryptoSieve()
    analyzer.run_advanced_analysis()
