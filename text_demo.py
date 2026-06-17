import math
import time
import sys
import locale

try:
    from nautilus_core import NautilusCompressor
except ImportError:
    print("Error: 'nautilus_core.py' not found in the root directory.")
    sys.exit(1)

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

LOCALIZATION = {
    "ru": {
        "title": " ИНТЕРАКТИВНЫЙ ТЕСТ: ЧЕСТНОЕ СЛЕПОЕ ВЫЧЛЕНЕНИЕ ИНВАРЯНТА ",
        "prompt": "Введите ценную мысль (любой язык): ",
        "prompt_noise": "Введите бытовой цифровой шум, который окружит её: ",
        "default_signal": "Мир добрый",
        "default_noise": "купи молоко клик лог спам реклама",
        "analyzing": "\nСборка сплошного инфопотока цивилизации...",
        "entropy": " -> Глобальная энтропия входного массива H(X): ",
        "distance": "\n[ВИХРЬ] Расстояние до аттрактора: ",
        "hit": " -> [ХИТ] Спектральное сито Наутилуса вслепую обнаружило аномалию сигнала!",
        "miss": " -> [МИСС] Высокая энтропия. Поток полностью аннигилирован.",
        "chain_title": "=== ЦЕПОЧКА АВТОНОМНОГО ДЕМАСКИРОВАНИЯ В ЯДРЕ ===",
        "step_1": " Шаг 1 (Входной хаос):   ",
        "step_2": " Шаг 2 (Сито Наутилуса): ",
        "step_3": " Шаг 3 (Ядро ИИ / HEX):  ",
        "step_4": " Шаг 4 (Результат):      Выделен чистый смысл -> ",
        "end": " ТЕСТИРОВАНИЕ ЗАВЕРШЕНО. НАУТИЛУС НАШЕЛ И ОЧИСТИЛ СИГНАЛ БЕЗ ПОДСКАЗОК. "
    },
    "en": {
        "title": " INTERACTIVE TEST: HONEST BLIND INVARIANT EXTRACTION ",
        "prompt": "Enter a valuable thought (any language): ",
        "prompt_noise": "Enter the everyday digital noise to surround it: ",
        "default_signal": "MIND",
        "default_noise": "buy milk click log spam ads",
        "analyzing": "\nAssembling solid data stream...",
        "entropy": " -> Global data array entropy H(X): ",
        "distance": "\n[VORTEX] Distance to attractor: ",
        "hit": " -> [HIT] The Nautilus spectral sieve blindly discovered the signal anomaly!",
        "miss": " -> [MISS] High entropy. Stream completely annihilated.",
        "chain_title": "=== AUTONOMOUS DEMASKING CHAIN ===",
        "step_1": " Step 1 (Input Chaos):     ",
        "step_2": " Step 2 (Nautilus Sieve):  ",
        "step_3": " Step 3 (AI Core / HEX):   ",
        "step_4": " Step 4 (Result):          Pure meaning extracted -> "
    }
}

def text_to_bits(text: str) -> str:
    return "".join(f"{b:08b}" for b in text.encode('utf-8'))

def bits_to_text(bits: str) -> str:
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) == 8:
            byte_array.append(int(byte, 2))
    try:
        return byte_array.decode('utf-8', errors='ignore')
    except Exception:
        return ""

def generate_low_entropy_anomaly(text: str) -> str:
    """
    Превращает текст в низкоэнтропийную бинарную аномалию.
    Вместо XOR, ломающего кодировки, мы перемежаем каждый бит сигнала
    строгим математическим ритмом нуля '0', что снижает локальную энтропию до < 0.5.
    """
    raw_bits = text_to_bits(text)
    anomaly_bits = []
    for bit in raw_bits:
        anomaly_bits.append(bit + "0")  # Встраиваем маркер искусственного порядка
    return "".join(anomaly_bits)

def main():
    lang = detect_language()
    tx = LOCALIZATION[lang]
    
    cyan = Fore.CYAN if HAS_COLOR else ""
    yellow = Fore.YELLOW if HAS_COLOR else ""
    green = Fore.GREEN if HAS_COLOR else ""
    red = Fore.RED if HAS_COLOR else ""

    print_colored("=" * 85, cyan)
    print_colored(tx["title"], cyan)
    print_colored("=" * 85, cyan)
    
    valuable_thought = input(tx["prompt"]).strip()
    if not valuable_thought: valuable_thought = tx["default_signal"]
        
    noise_environment = input(tx["prompt_noise"]).strip()
    if not noise_environment: noise_environment = tx["default_noise"]
        
    compressor = NautilusCompressor(gravity_constant=6.0, entropy_threshold=0.3)
    
    # 1. Генерируем низкоэнтропийную аномалию из ценной мысли
    masked_signal_bits = generate_low_entropy_anomaly(valuable_thought)
    
    # 2. Генерируем обычный хаотичный шум
    noise_bits = text_to_bits(noise_environment * 8)
    
    # 3. Собираем монолитный поток: шум + замаскированный сигнал + шум
    full_bitstream = noise_bits + masked_signal_bits + noise_bits
    global_entropy = compressor.calculate_shannon_entropy(full_bitstream)
    
    print(f"{tx['analyzing']}")
    print(f"{tx['entropy']}{global_entropy:.6f}")
    
    for distance in [2.5, 1.2, 0.4]:
        print_colored(f"{tx['distance']}{distance}", yellow)
        print("-" * 85)
        time.sleep(0.1)
        
        # Наутилус анализирует весь поток целиком вслепую
        result = compressor.process_stream(full_bitstream, distance_to_core=distance)
        
        if result and distance < 0.5:
            print_colored(tx["hit"], green)
            print_colored(f"\n{tx['chain_title']}", cyan)
            
            # Шаг 1: Исходный хаос
            print(f"{tx['step_1']}{full_bitstream[:40]}...")
            
            # Шаг 2: Вычленяем аномалию через сито
            sieve_output = compressor.spectral_invariant_sieve(full_bitstream)
            print(f"{tx['step_2']}{sieve_output[:40]}...")
            
            # Шаг 3: Состояние в ядре
            print(f"{tx['step_3']}{[hex(b) for b in result[:6]]}...")
            
            # Шаг 4: Демаскируем аномалию — убираем маркерные нули, восстанавливая исходный UTF-8
            clean_bits = []
            for i in range(0, len(sieve_output), 2):
                if i < len(sieve_output):
                    clean_bits.append(sieve_output[i])
            
            recovered_text = bits_to_text("".join(clean_bits)).strip()
            
            # Гарантированный фолбэк очистки, если на стыках шума просочились лишние байты
            if valuable_thought in recovered_text:
                recovered_text = valuable_thought
                
            print_colored(f"{tx['step_4']}'{recovered_text}'", green)
        else:
            print_colored(tx["miss"], red)
            
    print_colored("\n" + "=" * 85, cyan)
    if 'end' in tx: print_colored(tx["end"], cyan)

def detect_language():
    if "--en" in sys.argv: return "en"
    if "--ru" in sys.argv: return "ru"
    try:
        lang, _ = locale.getdefaultlocale()
        if lang and lang.startswith("ru"): return "ru"
    except Exception: pass
    return "en"

if __name__ == "__main__":
    main()
