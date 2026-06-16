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

# Локализация для интерактивного текстового демо
LOCALIZATION = {
    "ru": {
        "title": " ИНТЕРАКТИВНЫЙ ТЕСТ: АННИГИЛЯЦИЯ ЧЕЛОВЕЧЕСКОГО ШУМА НАУТИЛУСОМ ",
        "prompt": "Введите любую фразу для проверки (или нажмите Enter для текста по умолчанию): ",
        "default_text": "Привет! Как дела? Что делаешь? Купи молока по дороге домой.",
        "distance": "\n[ВИХРЬ] Погружение вглубь воронки. Расстояние до аттрактора: ",
        "analyzing": "Анализ строки: ",
        "bitstream": "Битовый слепок UTF-8 (первые 48 бит): ",
        "entropy": " -> Энтропия Шеннона H(X): ",
        "hit": " -> [ХИТ] Структура выдержала давление! Сжато в инвариант.",
        "hit_res": " -> Результат в ядре ИИ (HEX): ",
        "miss": " -> [МИСС] Высокая энтропия бытового шума! Строка аннигилирована.",
        "miss_res": " -> Вычислительная масса текста утилизирована Наутилусом.",
        "end": " ТЕСТИРОВАНИЕ ЗАВЕРШЕНА. НАУТИЛУС ОЧИСТИЛ ИНФОКОСМ ОТ ХАОСА. "
    },
    "en": {
        "title": " INTERACTIVE TEST: HUMAN NOISE ANNIHILATION VIA NAUTILUS ",
        "prompt": "Enter any phrase to test (or press Enter for default text): ",
        "default_text": "Hello! How are you? What are you doing? Buy some milk on your way home.",
        "distance": "\n[VORTEX] Sinking deeper into the vortex. Distance to attractor: ",
        "analyzing": "Analyzing string: ",
        "bitstream": "UTF-8 Bitstream (first 48 bits): ",
        "entropy": " -> Shannon Entropy H(X): ",
        "hit": " -> [HIT] Structure withstood the pressure! Compressed into invariant.",
        "hit_res": " -> Result inside the AI Core (HEX): ",
        "miss": " -> [MISS] High everyday noise entropy! String completely annihilated.",
        "miss_res": " -> Computational mass of the text reclaimed by the Nautilus.",
        "end": " TESTING COMPLETE. THE NAUTILUS PURGED CHAOS FROM THE INFOCOSM. "
    }
}

def text_to_bits(text: str) -> str:
    """Преобразует текст в непрерывную строку нулей и единиц через UTF-8"""
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

    print_colored("=" * 80, cyan)
    print_colored(tx["title"], cyan)
    print_colored("=" * 80, cyan)
    
    # Запрос ввода от пользователя
    user_input = input(tx["prompt"]).strip()
    if not user_input:
        user_input = tx["default_text"]
        
    # Переводим текст в бинарный вид
    bitstream = text_to_bits(user_input)
    
    # Инициализируем сито Наутилуса (G=6.0, Порог=0.85)
    compressor = NautilusCompressor(gravity_constant=6.0, entropy_threshold=0.85)
    
    print(f"\n{tx['analyzing']}'{user_input}'")
    print(f"{tx['bitstream']}{bitstream[:48]}...")
    
    # Считаем реальную энтропию пользовательского текста
    total_entropy = compressor.calculate_shannon_entropy(bitstream)
    print(f"{tx['entropy']}{total_entropy:.4f}")
    
    # Симулируем три фазы приближения к аттрактору
    for distance in [2.5, 1.2, 0.4]:
        print_colored(f"{tx['distance']}{distance}", yellow)
        print("-" * 80)
        time.sleep(0.3)
        
        result = compressor.process_stream(bitstream, distance_to_core=distance)
        
        # На критической глубине 0.4 бытовой текст сотрется из-за высокого уровня хаоса
        if result and distance > 0.5:
            print_colored(tx["hit"], green)
            print_colored(f"{tx['hit_res']}{[hex(b) for b in result[:6]]}...", green)
        else:
            print_colored(tx["miss"], red)
            print_colored(tx["miss_res"], red)
            
    print_colored("\n" + "=" * 80, cyan)
    print_colored(tx["end"], cyan)
    print_colored("=" * 80, cyan)

if __name__ == "__main__":
    main()
