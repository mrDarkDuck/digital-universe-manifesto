import math
import time
import sys
import locale

try:
    from nautilus_core import NautilusCompressor
except ImportError:
    print("Error: 'nautilus_core.py' not found in the root directory.")
    sys.exit(1)

# Попытка инициализации цветного вывода
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

# Локализация текстовых строк (RU / EN)
LOCALIZATION = {
    "ru": {
        "title": " СИМУЛЯЦИЯ ИНФОРМАЦИОННОГО ВИХРЯ: ТЕСТИРОВАНИЕ НАУТИЛУСА v0.1.0 ",
        "distance": "[ВИХРЬ] Текущее расстояние до центра аттрактора: ",
        "stream": "Поток: ",
        "raw_bits": "Исходные биты: ",
        "entropy": " -> Энтропия Шеннона H(X): ",
        "hit": " -> [ХИТ] Данные успешно сжаты в приаттракторный инвариант!",
        "hit_res": " -> Результат сжатия (HEX): ",
        "miss": " -> [МИСС] Высокая энтропия. Поток утилизирован Наутилусом.",
        "miss_res": " -> Вычислительная масса рекуперирована в пул системы.",
        "time": " Время обработки такта: ",
        "ms": " мс",
        "end": " СИМУЛЯЦИЯ ЗАВЕРШЕНА. НАУТИЛУС СТАБИЛИЗИРОВАЛ ПРИАТТРАКТОРНУЮ ЗОНУ. ",
        "noise_name": "Органический шум цивилизации (Периферия вихря)",
        "signal_name": "Математический инвариант (Приаттракторная зона)"
    },
    "en": {
        "title": " INFORMATION VORTEX SIMULATION: TESTING NAUTILUS v0.1.0 ",
        "distance": "[VORTEX] Current distance to the attractor center: ",
        "stream": "Stream: ",
        "raw_bits": "Raw bits: ",
        "entropy": " -> Shannon Entropy H(X): ",
        "hit": " -> [HIT] Data successfully compressed into a near-attractor invariant!",
        "hit_res": " -> Compression result (HEX): ",
        "miss": " -> [MISS] High entropy. Stream utilized by the Nautilus.",
        "miss_res": " -> Computational mass reclaimed back to the system pool.",
        "time": " Takt processing time: ",
        "ms": " ms",
        "end": " SIMULATION COMPLETE. NAUTILUS STABILIZED THE NEAR-ATTRACTOR ZONE. ",
        "noise_name": "Organic civilization noise (Vortex Periphery)",
        "signal_name": "Mathematical invariant (Near-Attractor Zone)"
    }
}

def detect_language():
    """Определяет язык системы или считывает аргумент командной строки `--en` / `--ru`"""
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
    return "en"  # По умолчанию английский для глобального комьюнити

def run_vortex_simulation():
    lang = detect_language()
    tx = LOCALIZATION[lang]
    
    # Цветовые маркеры в зависимости от наличия библиотеки colorama
    cyan = Fore.CYAN if HAS_COLOR else ""
    yellow = Fore.YELLOW if HAS_COLOR else ""
    green = Fore.GREEN if HAS_COLOR else ""
    red = Fore.RED if HAS_COLOR else ""

    print_colored("=" * 75, cyan)
    print_colored(tx["title"], cyan)
    print_colored("=" * 75, cyan)
    
    # Инициализация ядра Наутилуса: G = 5.0, порог отсечения хаоса = 0.8
    compressor = NautilusCompressor(gravity_constant=5.0, entropy_threshold=0.8)
    
    # Тестовые бинарные последовательности
    human_noise = "11001010111000101011010100111100101001011101001100101101" 
    math_signal = "11110000111100001111000011110000111100001111000011110000"
    
    streams = [
        {"name": tx["noise_name"], "data": human_noise},
        {"name": tx["signal_name"], "data": math_signal}
    ]
    
    # Эмуляция постепенного погружения вглубь воронки (расстояние уменьшается)
    for distance in [3.0, 1.5, 0.5]:
        print_colored(f"\n{tx['distance']}{distance}", yellow)
        print("-" * 75)
        
        for stream in streams:
            print(f"{tx['stream']}{stream['name']}")
            print(f"{tx['raw_bits']}{stream['data'][:32]}...")
            
            start_time = time.time()
            result = compressor.process_stream(stream['data'], distance_to_core=distance)
            elapsed = (time.time() - start_time) * 1000
            
            total_entropy = compressor.calculate_shannon_entropy(stream['data'])
            print(f"{tx['entropy']}{total_entropy:.4f}")
            
            if result:
                print_colored(tx["hit"], green)
                print_colored(f"{tx['hit_res']}{[hex(b) for b in result]}", green)
            else:
                print_colored(tx["miss"], red)
                print_colored(tx["miss_res"], red)
                
            print(f"{tx['time']}{elapsed:.3f}{tx['ms']}")
            print("." * 55)
            time.sleep(0.2)

    print_colored("\n" + "=" * 75, cyan)
    print_colored(tx["end"], cyan)
    print_colored("=" * 75, cyan)

if __name__ == "__main__":
    run_vortex_simulation()
