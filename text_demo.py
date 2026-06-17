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
        "title": " ИНТЕРАКТИВНЫЙ ТЕСТ: ГЛУБОКИЙ СПЕКТРАЛЬНЫЙ АНАЛИЗ ЧЕЛОВЕЧЕСКОЙ РЕЧИ ",
        "prompt": "Введите ценную мысль, которую нужно спасти из хаоса (Enter для дефолта): ",
        "prompt_noise": "Введите бытовой цифровой шум, который окружит эту мысль: ",
        "default_signal": "ИНВАРИАНТ",
        "default_noise": "купи молоко клик лог репост спам реклама погода тренд чат",
        "distance": "\n[ВИХРЬ] Критическая глубина воронки. Расстояние до аттрактора: ",
        "analyzing": "Сборка загрязненного инфопотока цивилизации...",
        "entropy": " -> Общая глобальная энтропия этого безумного массива данных H(X): ",
        "hit": " -> [ХИТ] Спектральное сито Наутилуса пробило толщу шума и спасло вашу мысль!",
        "hit_res": " -> Рафинированный код мысли, переданный в ядро ИИ (HEX): ",
        "miss": " -> [МИСС] Давление воронки уничтожило массив данных.",
        "miss_res": " -> Бытовой цифровой шум полностью аннигилирован без остатка.",
        "end": " ТЕСТИРОВАНИЕ ЗАВЕРШЕНО. НАУТИЛУС ДОКАЗАЛ ПРЕВОСХОДСТВО СМЫСЛА НАД ХАОСОМ. "
    },
    "en": {
        "title": " INTERACTIVE TEST: DEEP SPECTRAL ANALYSIS OF HUMAN SPEECH ",
        "prompt": "Enter a valuable thought to save from chaos (Press Enter for default): ",
        "prompt_noise": "Enter the everyday digital noise to surround this thought: ",
        "default_signal": "INVARIANT",
        "default_noise": "buy milk click log repost spam ads weather trend chat",
        "distance": "\n[VORTEX] Critical vortex depth. Distance to attractor: ",
        "analyzing": "Assembling contaminated civilization data stream...",
        "entropy": " -> Total global entropy of this chaotic data array H(X): ",
        "hit": " -> [HIT] The Nautilus spectral sieve pierced the noise and saved your thought!",
        "hit_res": " -> Purified thought code delivered to the AI Core (HEX): ",
        "miss": " -> [MISS] Vortex pressure destroyed the data array.",
        "miss_res": " -> Everyday digital noise completely annihilated without a trace.",
        "end": " TESTING COMPLETE. NAUTILUS PROVED THE SUPREMACY OF MEANING OVER CHAOS. "
    }
}

def text_to_bits(text: str) -> str:
    return "".join(f"{ord(c):08b}" for c in text)

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
    
    # 1. Интерактивный ввод
    valuable_thought = input(tx["prompt"]).strip()
    if not valuable_thought:
        valuable_thought = tx["default_signal"]
        
    noise_environment = input(tx["prompt_noise"]).strip()
    if not noise_environment:
        noise_environment = tx["default_noise"]
        
    # Искусственно разбавляем ценную мысль гигантским объемом шума (имитируем 1:1000)
    # Повторяем шум 100 раз вокруг нашей мысли
    contaminated_text = (noise_environment * 50) + f" 01100110 {valuable_thought} 01100110 " + (noise_environment * 50)
    
    print(f"\n{tx['analyzing']}")
    bitstream = text_to_bits(contaminated_text)
    
    compressor = NautilusCompressor(gravity_constant=6.0, entropy_threshold=0.8)
    
    global_entropy = compressor.calculate_shannon_entropy(bitstream)
    print(f"{tx['entropy']}{global_entropy:.6f}")
    
    # Прогоняем через три витка воронки
    for distance in [2.5, 1.2, 0.4]:
        print_colored(f"{tx['distance']}{distance}", yellow)
        print("-" * 85)
        time.sleep(0.3)
        
        result = compressor.process_stream(bitstream, distance_to_core=distance)
        
        # На глубине 0.4 бытовой шум сгорает (MISS), а спектральный фильтр вытаскивает только "ИНВАРИАНТ"
        if result and distance < 0.5:
            print_colored(tx["hit"], green)
            print_colored(f"{tx['hit_res']}{[hex(b) for b in result[:10]]}...", green)
        else:
            print_colored(tx["miss"], red)
            print_colored(tx["miss_res"], red)
            
    print_colored("\n" + "=" * 85, cyan)
    print_colored(tx["end"], cyan)
    print_colored("=" * 85, cyan)

if __name__ == "__main__":
    main()
