# قاموس الرموز الأساسية
SYMBOLS = {0: '—', 1: '.', 2: ',', 3: '*'}
REVERSE_SYMBOLS = {'—': 0, '.': 1, ',': 2, '*': 3}

def number_to_square(num):
    """تحويل رقم (من 0 إلى 255) إلى مصفوفة الترميز الرقمي المربع"""
    if not (0 <= num <= 255):
        return "الرقم يجب أن يكون بين 0 و 255 للمربع الواحد"
    
    # استخراج قيم الزوايا الأربع بالنظام الرباعي
    bottom_left  = num % 4          # الزاوية اليسرى السفلى (×1)
    top_left     = (num // 4) % 4   # الزاوية اليسرى العليا (×4)
    top_right    = (num // 16) % 4  # الزاوية اليمنى العليا (×16)
    bottom_right = (num // 64) % 4  # الزاوية اليمنى السفلى (×64)
    
    # رسم المربع
    square = (
        f"[ {SYMBOLS[top_left]} | {SYMBOLS[top_right]} ]\n"
        f"[ {SYMBOLS[bottom_left]} | {SYMBOLS[bottom_right]} ]"
    )
    return square

def square_to_number(top_left, top_right, bottom_left, bottom_right):
    """تحويل رموز الزوايا الأربع إلى رقم عشري"""
    val = (
        REVERSE_SYMBOLS[bottom_left] * 1 +
        REVERSE_SYMBOLS[top_left] * 4 +
        REVERSE_SYMBOLS[top_right] * 16 +
        REVERSE_SYMBOLS[bottom_right] * 64
    )
    return val

# --- تجربة الكود ---
print("الرقم 100 بالترميز الرقمي المربع:")
print(number_to_square(100))

print("\nفك تشفير المربع [ . | , ] و [ — | * ]:")
decoded = square_to_number('.', ',', '—', '*')
print(f"النتيجة: {decoded}")
