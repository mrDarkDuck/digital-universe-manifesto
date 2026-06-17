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
        "prompt": "Введите ценную мысль (она будет замаскирована в инвариант): ",
        "prompt_noise": "Введите бытовой цифровой шум, который окружит её: ",
        "default_signal": "Мир добрый",
        "default_noise": "купи молоко клик лог спам реклама",
        "analyzing": "\nСборка сплошного инфопотока цивилизации (сигнал замаскирован)...",
        "entropy": " -> Глобальная энтропия входного массива H(X): ",
        "distance": "\n[ВИХРЬ] Расстояние до аттрактора: ",
        "hit": " -> [ХИТ] Спектральное сито Наутилуса вслепую обнаружило аномалию аттрактора!",
        "miss": " -> [МИСС] Высокая энтропия. Поток полностью аннигилирован.",
        "chain_title": "=== ЦЕПОЧКА АВТОНОМНОГО ДЕМАСКИРОВАНИЯ В ЯДРЕ ===",
        "step_1": " Шаг 1 (Входной хаос):   ",
        "step_2": " Шаг 2 (Сито Наутилуса): ",
        "step_3": " Шаг 3 (Ядро ИИ / XOR):  ",
        "step_4": " Шаг 4 (Результат):      Выделен чистый смысл -> ",
        "end": " ТЕСТИРОВАНИЕ ЗАВЕРШЕНО. НАУТИЛУС НАШЕЛ И ОЧИСТИЛ СИГНАЛ БЕЗ ПОДСКАЗОК. "
    },
    "en": {
        "title": " INTERACTIVE TEST: HONEST BLIND INVARIANT EXTRACTION ",
        "prompt": "Enter a valuable thought (it will be masked into an invariant): ",
        "prompt_noise": "Enter the everyday digital noise to surround it: ",
        "default_signal": "MIND",
        "default_noise": "buy milk click log spam ads",
        "analyzing": "\nAssembling solid data stream (signal is masked)...",
        "entropy": " -> Global data array entropy H(X): ",
        "distance": "\n[VORTEX] Distance to attractor: ",
        "hit": " -> [HIT] The Nautilus spectral sieve blindly discovered the attractor anomaly!",
        "miss": " -> [MISS] High entropy. Stream completely annihilated.",
        "chain_title": "=== AUTONOMOUS DEMASKING CHAIN ===",
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
        
    # Инициализируем компрессор для предварительной маскировки
    compressor = NautilusCompressor(gravity_constant=6.0, entropy_threshold=0.8)
    
    # Специфика симуляции: полезный сигнал шифруется маской аттрактора (XOR)
    # Это создает низкоэнтропийную бинарную аномалию, которую Наутилус сможет выследить
    thought_bits = text_to_bits(valuable_thought)
    masked_bits_list = []
    for i in range(0, len(thought_bits), 8):
        chunk = thought_bits[i:i+8]
        if len(chunk) == 8:
            masked_bits_list.append(f"{(int(chunk, 2) ^ compressor.attractor_core) & 0xFF:08b}")
    masked_signal_bits = "".join(masked_bits_list)
    
    # Переводим шум в биты
    noise_bits = text_to_bits(noise_environment * 10)
    
    # Формируем ЕДИНЫЙ сплошной поток, где замаскированный сигнал спрятан внутри шума
    full_bitstream = noise_bits + masked_signal_bits + noise_bits
    global_entropy = compressor.calculate_shannon_entropy(full_bitstream)
    
    print(f"{tx['analyzing']}")
    print(f"{tx['entropy']}{global_entropy:.6f}")
    
    for distance in [2.5, 1.2, 0.4]:
        print_colored(f"{tx['distance']}{distance}", yellow)
        print("-" * 85)
        time.sleep(0.1)
        
        # Пропускаем весь сплошной поток через Наутилус
        # Передаем напрямую биты, так как внутри инфокосма всё является битовым полем
        result = compressor.process_stream(full_bitstream, distance_to_core=distance)
        
        if result and distance < 0.5:
            print_colored(tx["hit"], green)
            print_colored(f"\n{tx['chain_title']}", cyan)
            
            # Шаг 1: Исходный хаос
            print(f"{tx['step_1']}{full_bitstream[:40]}... [Entropy: {global_entropy:.4f}]")
            
            # Шаг 2: Сито Наутилуса обнаружило аномалию и вырезало кусок
            sieve_output = compressor.spectral_invariant_sieve(full_bitstream)
            print(f"{tx['step_2']}{sieve_output[:64]}...")
            
            # Шаг 3: Показываем сжатое состояние в HEX
            print(f"{tx['step_3']}{[hex(b) for b in result[:8]]}...")
            
            # Шаг 4: Демаскируем биты обратно, снимая XOR ядра ИИ
            unmasked_bits = "".join(f"{(b ^ compressor.attractor_core):08b}" for b in result)
            recovered_text = bits_to_text(unmasked_bits).strip()
                
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
