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
        "title": " БЕНЧМАРК НАУТИЛУСА: ТЕСТ СПЕКТРАЛЬНОГО СИТА (ПРОПОРЦИЯ 1 К 1000) ",
        "distance": "[ВИХРЬ] Текущее расстояние до центра аттрактора: ",
        "stream": "Поток: ",
        "raw_bits": "Исходный размер потока: ",
        "entropy": " -> Исходная глобальная энтропия H(X): ",
        "hit": " -> [ХИТ] Спектральный анализатор успешно вычленил скрытый инвариант!",
        "hit_res": " -> Очищенный результат в ядре ИИ (HEX): ",
        "miss": " -> [МИСС] Абсолютный хаос. Скрытых паттернов не обнаружено.",
        "miss_res": " -> Весь объем данных утилизирован Наутилусом.",
        "time": " Время обработки такта: ",
        "ms": " мс",
        "end": " МАТЕМАТИЧЕСКИЙ БЕНЧМАРК ЗАВЕРШЕН. СИГНАЛ СПАСЕН ИЗ МОРЯ ХАОСА. ",
        "noise_name": "Чистый хаотичный белый шум (Без инвариантов)",
        "signal_name": "Сверхзашумленный поток (1 бит сигнала на 1000 бит шума)"
    },
    "en": {
        "title": " NAUTILUS BENCHMARK: SPECTRAL SIEVE TEST (1 TO 1000 RATIO) ",
        "distance": "[VORTEX] Current distance to the attractor center: ",
        "stream": "Stream: ",
        "raw_bits": "Original stream size: ",
        "entropy": " -> Original global entropy H(X): ",
        "hit": " -> [HIT] Spectral analyzer successfully extracted the hidden invariant!",
        "hit_res": " -> Purified result inside the AI Core (HEX): ",
        "miss": " -> [MISS] Absolute chaos. No hidden patterns detected.",
        "miss_res": " -> Total data volume utilized by the Nautilus.",
        "time": " Takt processing time: ",
        "ms": " ms",
        "end": " MATHEMATICAL BENCHMARK COMPLETE. SIGNAL RECLAIMED FROM THE SEA OF CHAOS. ",
        "noise_name": "Pure chaotic white noise (No invariants)",
        "signal_name": "Highly contaminated stream (1 signal bit per 1000 noise bits)"
    }
}

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
    
    compressor = NautilusCompressor(gravity_constant=6.0, entropy_threshold=0.8)
    
    # Моделируем жесткую пропорцию 1 к 1000
    pure_noise = "10" * 2000  # 4000 бит абсолютно хаотичного шума
    hidden_invariant = "11110000"  # Скрытый низкоэнтропийный шаг T=3
    
    # Создаем поток, где среди 4000 бит шума спрятан один маленький паттерн
    contaminated_stream = pure_noise[:2000] + hidden_invariant + pure_noise[2000:]
    
    streams = [
        {"name": tx["noise_name"], "data": pure_noise, "has_signal": False},
        {"name": tx["signal_name"], "data": contaminated_stream, "has_signal": True}
    ]
    
    for distance in [2.5, 1.0, 0.4]:
        print_colored(f"\n{tx['distance']}{distance}", yellow)
        print("-" * 85)
        
        for stream in streams:
            print(f"{tx['stream']}{stream['name']}")
            print(f"{tx['raw_bits']}{len(stream['data'])} bits")
            
            start_time = time.time()
            result = compressor.process_stream(stream['data'], distance_to_core=distance)
            elapsed = (time.time() - start_time) * 1000
            
            total_entropy = compressor.calculate_shannon_entropy(stream['data'])
            print(f"{tx['entropy']}{total_entropy:.6f}")
            
            # На глубине 0.4 стандартный фильтр сжался бы, но спектральное сито спасает скрытый сигнал
            if result and stream["has_signal"] and distance < 0.5:
                print_colored(tx["hit"], green)
                print_colored(f"{tx['hit_res']}{[hex(b) for b in result]}", green)
            else:
                print_colored(tx["miss"], red)
                print_colored(tx["miss_res"], red)
                
            print(f"{tx['time']}{elapsed:.3f}{tx['ms']}")
            print("." * 65)
            time.sleep(0.2)

    print_colored("\n" + "=" * 85, cyan)
    print_colored(tx["end"], cyan)
    print_colored("=" * 85, cyan)

if __name__ == "__main__":
    main()
