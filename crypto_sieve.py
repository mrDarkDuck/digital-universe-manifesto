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
        "title": " КРИПТОАНАЛИЗ НАУТИЛУСА: ПОИСК ИНВАРЯНТОВ В КРИПТОШУМЕ (AES) ",
        "init": "[ИНИЦИАЛИЗАЦИЯ] Генерация псевдослучайного шума AES. Объем: {} бит.",
        "inject": "[ИНЪЕКЦИЯ] Скрытый логарифмический ключ Коллатца интегрирован в поток.",
        "scan": "[СКАНЕР] Наутилус активирует Анализатор Логарифмических Инвариантов...",
        "entropy_info": " -> Глобальная энтропия Шеннона H(X): {:.6f} (Шифр неотличим от шума)",
        "hit": "\n -> [УСПЕХ] Обнаружена фрактальная аномалия Коллатца на смещении {}!",
        "key_extracted": " -> Скрытый инвариант успешно извлечен: {}",
        "miss": "[АННИГИЛЯЦИЯ] Блок на смещении {} признан чистым хаосом. Смысл равен нулю.",
        "end": "\n КРИПТОГРАФИЧЕСКИЙ ТЕСТ ЗАВЕРШЕН. НАУТИЛУС ВИДИТ ЗАКОН СКВОЗЬ СЛЕПОЙ ХАОС. "
    },
    "en": {
        "title": " NAUTILUS CRYPTOANALYSIS: LOOKING FOR INVARIANTS IN AES NOISE ",
        "init": "[INITIALIZATION] Generating pseudo-random AES-like noise. Size: {} bits.",
        "inject": "[INJECTION] Hidden Collatz logarithmic key integrated into the stream.",
        "scan": "[SCANNER] Nautilus activates the Logarithmic Invariant Analyzer...",
        "entropy_info": " -> Global Shannon Entropy H(X): {:.6f} (Cipher is indistinguishable from noise)",
        "hit": "\n -> [HIT] Collatz fractal anomaly discovered at offset {}!",
        "key_extracted": " -> Hidden invariant successfully extracted: {}",
        "miss": "[ANNIHILATION] Block at offset {} identified as pure chaos. Meaning is zero.",
        "end": "\n CRYPTOGRAPHIC TEST COMPLETE. NAUTILUS SEES THE LAW THROUGH BLIND CHAOS. "
    }
}

class CryptoNautilusSieve:
    def __init__(self, lang: str = None):
        self.lang = lang if lang in ["ru", "en"] else self._detect_language()
        self.tx = CRYPTO_LOCALIZATION[self.lang]

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

    def is_collatz_congruent(self, sequence: list) -> bool:
        """
        Проверяет, подчиняется ли последовательность чисел закону Коллатца (3n+1).
        Это математический фильтр Наутилуса, заменяющий слепой расчет энтропии Шеннона.
        """
        if len(sequence) < 4: return False
        
        # Проверяем шаги переходов между числами цепочки
        for i in range(len(sequence) - 1):
            n = sequence[i]
            next_n = sequence[i+1]
            
            if n % 2 == 0:
                expected = n // 2
            else:
                expected = 3 * n + 1
                
            if next_n != expected:
                return False
        return True

    def run_crypto_analysis(self):
        cyan = Fore.CYAN if HAS_COLOR else ""
        yellow = Fore.YELLOW if HAS_COLOR else ""
        green = Fore.GREEN if HAS_COLOR else ""
        red = Fore.RED if HAS_COLOR else ""

        print_colored("=" * 80, cyan)
        print_colored(self.tx["title"], cyan)
        print_colored("=" * 80, cyan)

        # 1. Генерируем "слепой" криптографический шум (AES-подобный)
        # Набор случайных байт, переведенных в биты
        random.seed(42)
        noise_bytes = bytes([random.randint(0, 255) for _ in range(64)])
        noise_bits = "".join(f"{b:08b}" for b in noise_bytes)
        print(self.tx["init"].format(len(noise_bits)))

        # 2. Создаем скрытый логарифмический ключ (цепочка Коллатца)
        # Траектория для числа 13: [13, 40, 20, 10, 5, 16]
        collatz_chain = [13, 40, 20, 10, 5, 16]
        # Кодируем каждое число в 8-битный блок
        key_bits = "".join(f"{num:08b}" for num in collatz_chain)
        
        # Внедряем скрытый инвариант ровно в середину криптошума
        injection_point = len(noise_bits) // 2
        contaminated_stream = noise_bits[:injection_point] + key_bits + noise_bits[injection_point:]
        print(self.tx["inject"])
        
        # Считаем общую энтропию — она будет ~1.0, шифр идеально маскируется под хаос
        global_entropy = self.calculate_shannon_entropy(contaminated_stream)
        print_colored(self.tx["entropy_info"].format(global_entropy), yellow)
        print("-" * 80)
        time.sleep(0.5)

        print(self.tx["scan"])
        time.sleep(0.5)

        # 4. Анализатор логарифмических инвариантов запускает скользящее окно
        # Размер окна = 6 байт (48 бит), шаг = 8 бит (1 байт)
        window_size_bits = len(key_bits)
        step_bits = 8
        
        for offset in range(0, len(contaminated_stream) - window_size_bits + 1, step_bits):
            window = contaminated_stream[offset:offset+window_size_bits]
            
            # Переводим биты текущего окна обратно в массив чисел для проверки геометрии
            numbers_to_check = []
            for j in range(0, len(window), 8):
                byte_str = window[j:j+8]
                numbers_to_check.append(int(byte_str, 2))
            
            # Проверяем блок на соответствие аттрактору Коллатца
            if self.is_collatz_congruent(numbers_to_check):
                print_colored(self.tx["hit"].format(offset), green)
                print_colored(self.tx["key_extracted"].format(numbers_to_check), green)
                time.sleep(0.5)
            else:
                # Все блоки криптошума, не имеющие фрактальной структуры, утилизируются
                # Выводим логи выборочно, чтобы не перегружать консоль
                if offset % 64 == 0:
                    print_colored(self.tx["miss"].format(offset), red)
                    time.sleep(0.1)

        print_colored(self.tx["end"], cyan)
        print("=" * 80)

if __name__ == "__main__":
    sieve = CryptoNautilusSieve()
    sieve.run_crypto_analysis()
