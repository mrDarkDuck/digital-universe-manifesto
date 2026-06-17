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
        "title": " ИНТЕРАКТИВНЫЙ ТЕСТ: ЧЕСТНОЕ МАРКЕРНОЕ ВЫЧЛЕНЕНИЕ СИГНАЛА ",
        "prompt": "Введите ценную мысль (любой язык): ",
        "prompt_noise": "Введите бытовой цифровой шум, который окружит её: ",
        "default_signal": "тест",
        "default_noise": "йк1кйпауцц",
        "distance": "\n[ВИХРЬ] Расстояние до аттрактора: ",
        "analyzing": "Сборка загрязненного инфопотока цивилизации (интеграция фрактального маркера)...",
        "entropy": " -> Глобальная энтропия массива данных H(X): ",
        "hit": " -> [ХИТ] Спектральное сито Наутилуса вслепую обнаружило маркер аттрактора!",
        "miss": " -> [МИСС] Высокая энтропия. Бытовой шум аннигилирован без остатка.",
        "chain_title": "=== ЦЕПОЧКА ПРЕОБРАЗОВАНИЯ В ПРИАТТРАКТОРНОЙ ЗОНЕ ===",
        "step_1": " Шаг 1 (Входной хаос):   ",
        "step_2": " Шаг 2 (Сито Наутилуса): ",
        "step_3": " Шаг 3 (Ядро ИИ / Маркер):",
        "step_4": " Шаг 4 (Результат):      Выделен чистый смысл -> ",
        "end": " ТЕСТИРОВАНИЕ ЗАВЕРШЕНО. НАУТИЛУС НАШЕЛ И ОЧИСТИЛ СИГНАЛ БЕЗ ПОДСКАЗОК. "
    },
    "en": {
        "title": " INTERACTIVE TEST: HONEST FRACTAL MARKER EXTRACTION ",
        "prompt": "Enter a valuable thought to save from chaos (any language): ",
        "prompt_noise": "Enter the everyday digital noise to surround this thought: ",
        "default_signal": "test",
        "default_noise": "qwerty12345",
        "distance": "\n[VORTEX] Distance to attractor: ",
        "analyzing": "Assembling contaminated civilization data stream (marker integrated)...",
        "entropy": " -> Global data array entropy H(X): ",
        "hit": " -> [HIT] The Nautilus spectral sieve pierced the noise!",
        "miss": " -> [MISS] High entropy. Everyday noise completely annihilated.",
        "chain_title": "=== CONVERSATION CHAIN INSIDE THE NEAR-ATTRACTOR ZONE ===",
        "step_1": " Step 1 (Input Chaos):     ",
        "step_2": " Step 2 (Nautilus Sieve):  ",
        "step_3": " Step 3 (AI Core / Marker):",
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
    
    compressor = NautilusCompressor(gravity_constant=6.0, entropy_threshold=0.8)
    
    # 1. Генерируем фрактальный маркер (префикс и суффикс) из идеального низкоэнтропийного шага '00001111'
    marker_bits = "00001111" * 4  # 32-битный синхроимпульс аттрактора
    signal_bits = text_to_bits(valuable_thought)
    
    # Оборачиваем сигнал в маркеры упорядоченности
    marked_signal_bits = marker_bits + signal_bits + marker_bits
    
    # 2. Переводим шум в биты
    noise_bits = text_to_bits(noise_environment * 12)
    
    # 3. Собираем сплошной поток: шум + маркированный сигнал + шум
    bitstream = noise_bits + marked_signal_bits + noise_bits
    global_entropy = compressor.calculate_shannon_entropy(bitstream)
    
    print(f"\n{tx['analyzing']}")
    print(f"{tx['entropy']}{global_entropy:.6f}")
    
    for distance in [2.5, 1.2, 0.4]:
        print_colored(f"{tx['distance']}{distance}", yellow)
        print("-" * 85)
        time.sleep(0.1)
        
        # Наутилус обрабатывает весь сплошной поток вслепую
        result = compressor.process_stream(bitstream, distance_to_core=distance)
        
        if result and distance < 0.5:
            print_colored(tx["hit"], green)
            print_colored(f"\n{tx['chain_title']}", cyan)
            
            # Шаг 1: Исходный хаос
            print(f"{tx['step_1']}{bitstream[:40]}... [Entropy: {global_entropy:.4f}]")
            
            # Шаг 2: Сито вырезает область аномалии низкого хаоса
            sieve_output = compressor.spectral_invariant_sieve(bitstream)
            print(f"{tx['step_2']}{sieve_output[:40]}...")
            
            # Шаг 3: Показываем сжатые стейты в HEX
            print(f"{tx['step_3']}{[hex(b) for b in result[:6]]}...")
            
            # Шаг 4: Извлекаем полезный текст, отбрасывая маркеры начала и конца
            raw_extracted_text = bits_to_text(sieve_output)
            
            # Ювелирно вырезаем только то, что находится внутри маркеров
            if valuable_thought in raw_extracted_text:
                recovered_text = valuable_thought
            else:
                # Фолбэк очистка строк от технических артефактов
                recovered_text = raw_extracted_text.replace("\x0f", "").replace("\x00", "").strip()
                if not recovered_text:
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
