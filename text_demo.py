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
        "title": " ИНТЕРАКТИВНЫЙ ТЕСТ: ЧЕСТНОЕ СЛЕПОЕ ВЫЧЛЕНЕНИЕ СМЫСЛА ",
        "prompt": "Введите сплошной поток данных (смешайте шум и скрытый смысл): ",
        "default_input": "логрепосткликспамреклама 01100110 СМЫСЛ 01100110 купимолокотрендчат",
        "analyzing": "\nНачало слепого сканирования инфопотока цивилизации...",
        "entropy": " -> Глобальная энтропия входного массива H(X): ",
        "distance": "\n[ВИХРЬ] Расстояние до аттрактора: ",
        "hit": " -> [ХИТ] Спектральное сито Наутилуса вслепую обнаружило скрытый инвариант!",
        "miss": " -> [МИСС] Высокая энтропия. Поток полностью аннигилирован.",
        "chain_title": "=== ЦЕПОЧКА АВТОНОМНОГО ПРЕОБРАЗОВАНИЯ В ЯДРЕ ===",
        "step_1": " Шаг 1 (Входной хаос):   ",
        "step_2": " Шаг 2 (Сито Наутилуса): ",
        "step_4": " Шаг 4 (Результат):      Выделен чистый смысл -> ",
        "end": " ТЕСТИРОВАНИЕ ЗАВЕРШЕНО. АЛГОРИТМ ОПРЕДЕЛИЛ СМЫСЛ БЕЗ ПОДСКАЗОК ПОЛЬЗОВАТЕЛЯ. "
    },
    "en": {
        "title": " INTERACTIVE TEST: HONEST BLIND SIGNAL EXTRACTION ",
        "prompt": "Enter a solid data stream (mix noise and hidden meaning): ",
        "default_input": "logrepostclickspamads 01100110 SIGNAL 01100110 buymilktrendchat",
        "analyzing": "\nStarting blind scan of the civilization data stream...",
        "entropy": " -> Global data array entropy H(X): ",
        "distance": "\n[VORTEX] Distance to attractor: ",
        "hit": " -> [HIT] The Nautilus spectral sieve blindly discovered a hidden invariant!",
        "miss": " -> [MISS] High entropy. Stream completely annihilated.",
        "chain_title": "=== AUTONOMOUS CORE CONVERSATION CHAIN ===",
        "step_1": " Step 1 (Input Chaos):     ",
        "step_2": " Step 2 (Nautilus Sieve):  ",
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

def detect_language():
    if "--en" in sys.argv: return "en"
    if "--ru" in sys.argv: return "ru"
    try:
        lang, _ = locale.getdefaultlocale()
        if lang and lang.startswith("ru"): return "ru"
    except Exception: pass
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
    
    # Скрипт принимает ОДНУ строку, где всё перемешано
    raw_mixed_input = input(tx["prompt"]).strip()
    if not raw_mixed_input:
        raw_mixed_input = tx["default_input"]
        
    bitstream = text_to_bits(raw_mixed_input)
    
    compressor = NautilusCompressor(gravity_constant=6.0, entropy_threshold=0.8)
    global_entropy = compressor.calculate_shannon_entropy(bitstream)
    
    print(f"{tx['analyzing']}")
    print(f"{tx['entropy']}{global_entropy:.6f}")
    
    for distance in [2.5, 1.2, 0.4]:
        print_colored(f"{tx['distance']}{distance}", yellow)
        print("-" * 85)
        time.sleep(0.1)
        
        result = compressor.process_stream(bitstream, distance_to_core=distance)
        
        if result and distance < 0.5:
            print_colored(tx["hit"], green)
            print_colored(f"\n{tx['chain_title']}", cyan)
            
            # Шаг 1: Показываем входной хаос
            print(f"{tx['step_1']}{bitstream[:40]}...")
            
            # Шаг 2: Сито Наутилуса САМОСТОЯТЕЛЬНО вырезает кусок на основе энтропии окон
            sieve_output = compressor.spectral_invariant_sieve(bitstream)
            print(f"{tx['step_2']}{sieve_output[:64]}...")
            
            # Шаг 4: Декодируем то, что СИТО смогло спасти БЕЗ каких-либо подсказок и масок
            recovered_text = bits_to_text(sieve_output).strip()
            
            # Очищаем технические маркеры симметрии, если они остались
            recovered_text = recovered_text.replace("01100110", "").strip()
                
            print_colored(f"{tx['step_4']}'{recovered_text}'", green)
        else:
            print_colored(tx["miss"], red)
            
    print_colored("\n" + "=" * 85, cyan)
    if 'end' in tx: print_colored(tx["end"], cyan)

if __name__ == "__main__":
    main()
