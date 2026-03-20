
import telebot
from telebot import types

TOKEN = "8786811766:AAFgfWxYYvnstR-d8KcdhEUJ_BYZFfpciIU"
bot = telebot.TeleBot(TOKEN)
ADMEN_ID = 5923258583
WORK_ACCOUNT = "@BellaBoxX"

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn_info = types.KeyboardButton("ما هي BellaBox؟ 🎀")
    btn_support = types.KeyboardButton("خدمة العملاء 💬")
    btn_choose = types.KeyboardButton("إختاري باقتك 💖")

    keyboard.row(btn_info, btn_support)
    keyboard.add(btn_choose)

    bot.send_message(
        message.chat.id,
        "أهلاً فيكي بعالم BellaBox\nحيث تبدأ لحظاتك الجميلة ✨",
        reply_markup=keyboard
    )
   

# ================================
#   واجهة اختيار الباقات
# ================================

@bot.message_handler(func=lambda m: m.text and m.text.strip() == "ما هي BellaBox؟ 🎀")
def what_is_bellabox(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_home = types.KeyboardButton("رجوع للصفحة الرئيسية ⬅️")
    keyboard.add(back_home)

    bot.send_message(
        message.chat.id,
        "BellaBox هو بوكس مفاجآت جاهز، منسّق بإيدين مختصين، وبيوصلك فيه منتجات مختارة بعناية لتعيشي تجربة فريدة وممتعة كل مرة ❤️✨",
        reply_markup=keyboard
    )
#==================
@bot.message_handler(func=lambda m: m.text and m.text.strip() == "خدمة العملاء 💬")
def customer_service(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_home = types.KeyboardButton("رجوع للصفحة الرئيسية ⬅️")
    keyboard.add(back_home)

    bot.send_message(
        message.chat.id,
        "إذا واجهتك أي مشكلة في الحجز أو التوصيل، يسعدنا استقبال شكواك على الحساب وسنقوم بالرد عليك في أقرب وقت 🤍✨\n\n@BellaBoxX",
        reply_markup=keyboard
    )
#==================
#==================

@bot.message_handler(func=lambda m: m.text == "إختاري باقتك 💖")
def choose_package(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    basic = types.KeyboardButton("Basic Box 📦")
    glow = types.KeyboardButton("Glowry Box 🎗️")
    lux = types.KeyboardButton("Luxury Box 💎")
    back = types.KeyboardButton("رجوع 🔄")

    keyboard.row(basic)
    keyboard.row(glow, lux)
    keyboard.add(back)

    bot.send_message(
        message.chat.id,
        "يلا نعيش تجربة الخيال مع BellaBox.....🎀\nإختاري باقتك..!",
        reply_markup=keyboard
    )

# ================================
#   Glowry غير متوفر
# ================================
@bot.message_handler(func=lambda m: m.text == "Glowry Box 🎗️")
def glowry_unavailable(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_packages = types.KeyboardButton("رجوع للباقات 🔄")
    keyboard.add(back_packages)

    bot.send_message(
        message.chat.id,
        "للأسف Glowry Box غير متوفرة حالياً 💔✨\nسوف نخبركم فور توفر الباقة 🤍",
        reply_markup=keyboard
    )

# ================================
#   Luxury غير متوفر
# ================================
@bot.message_handler(func=lambda m: m.text == "Luxury Box 💎")
def luxury_unavailable(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_packages = types.KeyboardButton("رجوع للباقات 🔄")
    keyboard.add(back_packages)

    bot.send_message(
        message.chat.id,
        "للأسف Luxury Box غير متوفرة حالياً 💔✨\nسوف نخبركم فور توفر الباقة 🤍",
        reply_markup=keyboard
    )

# ================================
#   Basic Box (جاهز للتعديل)
# ================================
@bot.message_handler(func=lambda m: m.text == "Basic Box 📦")
def basic_box(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    content = types.KeyboardButton("محتوى البوكس 🧸✨")
    back_packages = types.KeyboardButton("رجوع للباقات 🔄")

    keyboard.add(content)
    keyboard.add(back_packages)

    bot.send_message(
        message.chat.id,
        "اختيار موفق… Basic Box دايمًا لمسة جمال 🎀✨",
        reply_markup=keyboard
    )
#====================
#====================
@bot.message_handler(func=lambda m: m.text == "محتوى البوكس 🧸✨")
def box_content(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    book = types.KeyboardButton("للحجز و الطلب 🧸💗")
    back_basic = types.KeyboardButton("رجوع لـ Basic Box ↩️")

    keyboard.add(book)
    keyboard.add(back_basic)

    bot.send_message(
        message.chat.id,
        "✨🧸 يلا نشوف محتوى الـ Basic Box\n\n"
        "محتوى البوكس:\n"
        "Mini lip gloss 💄\n"
        "Skin care 🌸\n"
        "Mini manicure 💐\n"
        "Mini perfume 🌷\n"
        "Surprise 🎁",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda m: m.text == "رجوع لـ Basic Box ↩️")
def back_to_basic(message):
    basic_box(message)


#==============
@bot.message_handler(func=lambda m: m.text == "للحجز و الطلب 🧸💗")
def booking(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    confirm = types.KeyboardButton("تثبيت الحجز 🧸✨")
    back_content = types.KeyboardButton("رجوع لـ محتوى البوكس ↩️")

    keyboard.add(confirm)
    keyboard.add(back_content)

    bot.send_message(
        message.chat.id,
        "سعر الـ Basic Box هو:\n"
        "45,000 / 450 ل.س 🧸💗\n"
        "متضمنة التوصيل داخل دمشق 🚚✨",
        reply_markup=keyboard
    )
#===============================
# ================================
#   تثبيت الحجز – الخطوة الأولى
# ================================
@bot.message_handler(func=lambda m: m.text == "تثبيت الحجز 🧸✨")
def confirm_booking(message):
    msg = bot.send_message(
        message.chat.id,
        "تمام… خلّينا نكمّل 🧸✨\n\n"
        "اكتبي اسمك:"
    )
    bot.register_next_step_handler(msg, get_name)


# ================================
#   الخطوة الثانية – الاسم
# ================================
def get_name(message):
    name = message.text
    msg = bot.send_message(
        message.chat.id,
        "حلو… هلا اكتبي رقم الموبايل للتواصل 🌸"
    )
    bot.register_next_step_handler(msg, get_phone, name)


# ================================
#   الخطوة الثالثة – رقم الهاتف
# ================================
def get_phone(message, name):
    phone = message.text
    msg = bot.send_message(
        message.chat.id,
        "تمام… هلا اكتبي عنوان التوصيل 🚚✨"
    )
    bot.register_next_step_handler(msg, get_address, name, phone)


# ================================
#   الخطوة الرابعة – العنوان + إرسال الطلب
# ================================
def get_address(message, name, phone):
    address = message.text

    # رسالة للزبونة
    bot.send_message(
        message.chat.id,
        f"تم استلام طلبك بنجاح 🧸💗\n\n"
        f"الاسم: {name}\n"
        f"الرقم: {phone}\n"
        f"العنوان: {address}\n\n"
        "رح يتم التواصل معك لتأكيد الطلب خلال وقت قصير 🎀✨"
    )

    # إرسال الطلب للإدمن
    ADMIN_ID = 5923258583
    bot.send_message(
        ADMIN_ID,
        f"طلب جديد من BellaBox 🧸✨\n\n"
        f"الاسم: {name}\n"
        f"الرقم: {phone}\n"
        f"العنوان: {address}\n"
        f"نوع البوكس: Basic Box 🛍"
    )

    # زر الرجوع للصفحة الرئيسية
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_home = types.KeyboardButton("رجوع للصفحة الرئيسية ⬅️")
    keyboard.add(back_home)

    bot.send_message(
        message.chat.id,
        "اضغطي رجوع للعودة للقائمة الرئيسية 🌸",
        reply_markup=keyboard
    )
# ================================
@bot.message_handler(func=lambda m: m.text == "رجوع لـ محتوى البوكس ↩️")
def back_to_content(message):
    box_content(message)
#   زر الرجوع
# ================================
@bot.message_handler(func=lambda m: m.text == "رجوع للصفحة الرئيسية ⬅️")
def back_home(message):
    start(message)

@bot.message_handler(func=lambda m: m.text == "رجوع للباقات 🔄")
def back_to_packages(message):
    choose_package(message)

# ================================
bot.polling(none_stop=True)


