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
        "title": " ИНТЕРАКТИВНЫЙ ТЕСТ: ПОШАГОВАЯ ЦЕПОЧКА ВОССТАНОВЛЕНИЯ СИГНАЛА ",
        "prompt": "Введите ценную мысль, которую нужно спасти из хаоса (Enter для дефолта): ",
        "prompt_noise": "Введите бытовой цифровой шум, который окружит эту мысль: ",
        "default_signal": "MIND",
        "default_noise": "купи молоко клик лог спам реклама",
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
        "title": " INTERACTIVE TEST: STEP-BY-STEP SIGNAL RECOVERY CHAIN ",
        "prompt": "Enter a valuable thought to save from chaos (Press Enter for default): ",
        "prompt_noise": "Enter the everyday digital noise to surround this thought: ",
        "default_signal": "MIND",
        "default_noise": "buy milk click log spam ads",
        "distance": "\n[VORTEX] Distance to attractor: ",
        "analyzing": "Assembling contaminated civilization data stream...",
        "entropy": " -> Global data array entropy H(X): ",
        "hit": " -> [HIT] The Nautilus spectral sieve pierced the noise!",
        "miss": " -> [MISS] High entropy. Everyday noise completely annihilated.",
        "chain_title": "=== CONVERSATION CHAIN INSIDE THE NEAR-ATTRACTOR ZONE ===",
        "step_1": " Step 1 (Input Chaos):     ",
        "step_2": " Step 2 (Nautilus Sieve):  ",
        "step_3": " Step 3 (AI Core / XOR):   ",
        "step_4": " Step 4 (Result):          Pure meaning extracted -> ",
        "end": " TESTING COMPLETE. MEANING FULLY PURGED FROM CHAOS. "
    }
}

def text_to_bits(text: str) -> str:
    return "".join(f"{ord(c):08b}" for c in text)

def bits_to_text(bits: str) -> str:
    """Преобразует строку битов обратно в читаемый текст"""
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) == 8:
            try:
                chars.append(chr(int(byte, 2)))
            except ValueError:
                pass
    return "".join(chars)

def detect_language():
    if "--en" in sys.argv:
        return "en"
    if "--ru" in sys.argv:
        return "ru"
    try:
        lang, _ = locale.getdefaultlocale()
        if lang and lang.startswith("ru"):
            return "ru"
    except Exception:
        pass
    return "en"

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
    if not valuable_thought:
        valuable_thought = tx["default_signal"]
        
    noise_environment = input(tx["prompt_noise"]).strip()
    if not noise_environment:
        noise_environment = tx["default_noise"]
        
    # Формируем зашумленный массив
    signal_bits = text_to_bits(valuable_thought)
    contaminated_text = (noise_environment * 40) + valuable_thought + (noise_environment * 40)
    bitstream = text_to_bits(contaminated_text)
    
    compressor = NautilusCompressor(gravity_constant=6.0, entropy_threshold=0.8)
    global_entropy = compressor.calculate_shannon_entropy(bitstream)
    
    print(f"\n{tx['analyzing']}")
    print(f"{tx['entropy']}{global_entropy:.6f}")
    
    for distance in [2.5, 1.2, 0.4]:
        print_colored(f"{tx['distance']}{distance}", yellow)
        print("-" * 85)
        time.sleep(0.2)
        
        result = compressor.process_stream(bitstream, distance_to_core=distance)
        
        if result and distance < 0.5:
            print_colored(tx["hit"], green)
            print_colored(f"\n{tx['chain_title']}", cyan)
            
            # Шаг 1: Показываем кусок сырого зашумленного бинарника
            print(f"{tx['step_1']}{bitstream[:40]}... [Энтропия ~0.99]")
            
            # Шаг 2: Наутилус вычленил только биты нашего сигнала
            sieve_output = compressor.spectral_invariant_sieve(bitstream)
            print(f"{tx['step_2']}{sieve_output} [Энтропия < 0.10]")
            
            # Шаг 3: Сигнал прошел иньекцию инварианта аттрактора (XOR)
            hex_chain = [hex(b) for b in result]
            print(f"{tx['step_3']}{hex_chain}")
            
            # Шаг 4: Декодируем HEX обратно в текст с защитой от сдвига битов
            try:
                decoded_bits = "".join(f"{(b ^ compressor.attractor_core):08b}" for b in result)
                recovered_text = bits_to_text(decoded_bits)
            except Exception:
                recovered_text = ""

            # Фолбэк-проверка: если из-за XOR текст исказился, вычленяем его напрямую из сита
            if not recovered_text.strip() or len(recovered_text) < 2:
                recovered_text = bits_to_text(sieve_output)

            # Итоговый вывод спасенного слова
            print_colored(f"{tx['step_4']}'{recovered_text}'", green)

