
import tkinter as tk

# إنشاء نافذة
window = tk.Tk()
window.title("آلة حاسبة بسيطة")
window.configure(bg='blue')  # خلفية زرقاء
window.geometry("300x400")  # حجم متوسط

# إدخال المستخدم
entry = tk.Entry(window, font=("Arial", 20), borderwidth=2, relief="solid")
entry.pack(pady=10, padx=10, fill="both")

# دالة لإضافة النص
def add_to_entry(symbol):
    entry.insert(tk.END, symbol)

# دالة للحساب
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "خطأ")

# دالة للمسح
def clear():
    entry.delete(0, tk.END)

# إنشاء الأزرار
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    frame = tk.Frame(window, bg='blue')
    frame.pack(expand=True, fill='both')
    for btn in row:
        action = lambda x=btn: calculate() if x == '=' else add_to_entry(x)
        if btn == '=':
            b = tk.Button(frame, text=btn, font=("Arial", 18), fg='white', bg='red',
                          command=calculate)
        else:
            b = tk.Button(frame, text=btn, font=("Arial", 18), fg='white', bg='red',
                          command=action)
        b.pack(side="left", expand=True, fill="both")

# زر مسح
clear_btn = tk.Button(window, text="مسح", font=("Arial", 18), fg='white', bg='red', command=clear)
clear_btn.pack(expand=True, fill="both", padx=10, pady=5)

# بدء التشغيل
window.mainloop()
