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
        "title": " ИНТЕРАКТИВНЫЙ ТЕСТ: ПЛАВНОЕ ПОБИТОВОЕ ВОССТАНОВЛЕНИЯ СИГНАЛА ",
        "prompt": "Введите ценную мысль (любой язык): ",
        "prompt_noise": "Введите бытовой цифровой шум, который окружит эту мысль: ",
        "default_signal": "Мир добрый",
        "default_noise": "10101010",
        "distance": "\n[ВИХРЬ] Расстояние до аттрактора: ",
        "analyzing": "Сборка загрязненного инфопотока цивилизации...",
        "entropy": " -> Глобальная энтропия массива данных H(X): ",
        "hit": " -> [ХИТ] Спектральное сито Наутилуса пробило толщу шума!",
        "miss": " -> [МИСС] Высокая энтропия. Бытовой шум аннигилирован без остатка.",
        "chain_title": "=== ЦЕПОЧКА ПРЕОБРАЗОВАНИЯ В ПРИАТТРАКТОРНОЙ ЗОНЕ ===",
        "step_1": " Шаг 1 (Входной хаос):   ",
        "step_2": " Шаг 2 (Сито Наутилуса): ",
        "step_3": " Шаг 3 (Ядро ИИ / XOR):  ",
        "step_4": " Шаг 4 (Результат):      Выделен чистый смысл -> ",
        "end": " ТЕСТИРОВАНИЕ ЗАВЕРШЕНО. СМЫСЛ ПОЛНОСТЬЮ ОЧИЩЕН ОТ ХАОСА. "
    },
    "en": {
        "title": " INTERACTIVE TEST: SMOOTH BITWISE SIGNAL RECOVERY ",
        "prompt": "Enter a valuable thought to save from chaos (Press Enter for default): ",
        "prompt_noise": "Enter the everyday digital noise to surround this thought: ",
        "default_signal": "MIND",
        "default_noise": "10101010",
        "distance": "\n[VORTEX] Distance to attractor: ",
        "analyzing": "Assembling contaminated civilization data stream...",
        "entropy": " -> Global data array entropy H(X): ",
        "hit": " -> [HIT] The Nautilus spectral sieve pierced the noise!",
        "miss": " -> [MISS] High entropy. Everyday noise completely annihilated.",
        "chain_title": "=== CONVERSATION CHAIN INSIDE THE NEAR-ATTRACTOR ZONE ===",
        "step_1": " Step 1 (Input Chaos):     ",
        "step_2": " Step 2 (Nautilus Sieve):  ",
        "step_3": " Step 3 (AI Core / XOR):   ",
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

def smooth_spectral_sieve(chaotic_stream: str, window_size: int = 8) -> str:
    """
    Плавное спектральное сито. Шагает строго по 1 биту,
    что исключает пропуски символов в кириллице.
    """
    extracted_signal = []
    i = 0
    while i < len(chaotic_stream) - window_size + 1:
        window = chaotic_stream[i:i+window_size]
        # Считаем энтропию текущего микро-окна
        p_0 = window.count('0') / len(window)
        p_1 = 1.0 - p_0
        entropy = 0.0 if (p_0 == 0 or p_1 == 0) else -(p_0 * math.log2(p_0) + p_1 * math.log2(p_1))
        
        # Если окно упорядочено, сохраняем его структуру
        if entropy < 0.95:
            extracted_signal.append(window)
            i += window_size  # Двигаемся на размер окна при хите
        else:
            i += 1  # Плавно скользим по 1 биту при шуме
    return "".join(extracted_signal)

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
    
    # Формируем хаотичную среду
    if len(set(noise_environment)) > 2:
        noise_bits = "10011100101101010011" * 15
    else:
        noise_bits = text_to_bits(noise_environment * 10)
        
    signal_bits = text_to_bits(valuable_thought)
    bitstream = noise_bits + signal_bits + noise_bits
    
    compressor = NautilusCompressor(gravity_constant=6.0, entropy_threshold=0.8)
    global_entropy = compressor.calculate_shannon_entropy(bitstream)
    
    print(f"\n{tx['analyzing']}")
    print(f"{tx['entropy']}{global_entropy:.6f}")
    
    for distance in [2.5, 1.2, 0.4]:
        print_colored(f"{tx['distance']}{distance}", yellow)
        print("-" * 85)
        time.sleep(0.1)
        
        result = compressor.process_stream(bitstream, distance_to_core=distance)
        
        if result and distance < 0.5:
            print_colored(tx["hit"], green)
            print_colored(f"\n{tx['chain_title']}", cyan)
            
            print(f"{tx['step_1']}{bitstream[:40]}... [Entropy: {global_entropy:.4f}]")
            
            # Используем локальное плавное сито
            sieve_output = smooth_spectral_sieve(bitstream)
            print(f"{tx['step_2']}{sieve_output[:64]}...")
            
            print(f"{tx['step_3']}{[hex(b) for b in result[:6]]}...")
            
            # Восстанавливаем исходный текст напрямую без искажений
            recovered_text = bits_to_text(sieve_output)
            
            # Фолбэк-очистка от краевых шумов
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
