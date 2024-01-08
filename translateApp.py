import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from ttkthemes import ThemedStyle

class TranslateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lingua Translate")

        # Mendapatkan lebar dan tinggi layar
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Variabel String untuk teks input, output, dan pronunisasi
        self.text_to_translate = tk.StringVar()
        self.translated_text = tk.StringVar()
        self.pronunciation_text = tk.StringVar()

        # Atur warna latar belakang
        self.root.configure(bg="#3498db")

        # Label untuk judul aplikasi
        title_label = ttk.Label(root, text="Lingua Translate", font=("Helvetica", 20), background="#3498db", foreground="white")
        title_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W + tk.E)

        # Label dan Entry untuk memasukkan teks
        label_input = ttk.Label(root, text="Masukkan teks yang ingin di terjemahkan:", font=("Helvetica", 12), background="#3498db", foreground="white")
        label_input.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W + tk.E)

        entry_text = ttk.Entry(root, textvariable=self.text_to_translate, font=("Helvetica", 12), width=50)
        entry_text.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W + tk.E)
        entry_text.bind("<Return>", lambda event: self.on_enter_pressed())

        # Label dan Combobox untuk memilih bahasa
        label_language = ttk.Label(root, text="Pilih bahasa tujuan:", font=("Helvetica", 12), background="#3498db", foreground="white")
        label_language.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W + tk.E)

        # Mendefinisikan 82 bahasa
        self.languages = [
            "Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Azerbaijani", "Basque", "Belarusian",
            "Bengali", "Bosnian", "Bulgarian", "Catalan", "Cebuano", "Chichewa", "Chinese (Simplified)",
            "Chinese (Traditional)", "Corsican", "Croatian", "Czech", "Danish", "Dutch", "English", "Esperanto",
            "Estonian", "Filipino", "Finnish", "French", "Frisian", "Galician", "Georgian", "German", "Greek",
            "Gujarati", "Haitian Creole", "Hausa", "Hawaiian", "Hebrew", "Hindi", "Hmong", "Hungarian", "Icelandic",
            "Igbo", "Indonesian", "Irish", "Italian", "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Korean",
            "Kurdish (Kurmanji)", "Kyrgyz", "Lao", "Latin", "Latvian", "Lithuanian", "Luxembourgish", "Macedonian",
            "Malagasy", "Malay", "Malayalam", "Maltese", "Maori", "Marathi", "Mongolian", "Myanmar (Burmese)", "Nepali",
            "Norwegian", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Romanian", "Russian", "Samoan",
            "Scots Gaelic", "Serbian", "Sesotho", "Shona", "Sindhi", "Sinhala", "Slovak", "Slovenian", "Somali",
            "Spanish", "Sundanese", "Swahili", "Swedish", "Tajik", "Tamil", "Telugu", "Thai", "Turkish", "Ukrainian",
            "Urdu", "Uzbek", "Vietnamese", "Welsh", "Xhosa", "Yiddish", "Yoruba", "Zulu"
        ]

        self.language_combobox = ttk.Combobox(root, values=self.languages, state="readonly", font=("Helvetica", 12), name="language_combobox")
        self.language_combobox.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W + tk.E)
        self.language_combobox.set("Indonesian")

        # Tombol untuk melakukan terjemahan
        translate_button = ttk.Button(root, text="Terjemahkan", command=self.translate_text, style="TButton")
        translate_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W + tk.E)

        # Label untuk menampilkan hasil terjemahan
        label_result = ttk.Label(root, text="Hasil Terjemahan:", font=("Helvetica", 12), background="#3498db", foreground="white")
        label_result.grid(row=6, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W + tk.E)

        result_text = ttk.Label(root, textvariable=self.translated_text, wraplength=400, justify=tk.LEFT, font=("Helvetica", 12), background="#3498db", foreground="white")
        result_text.grid(row=7, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W + tk.E)

        # Label untuk menampilkan pronunisasi
        label_pronunciation = ttk.Label(root, text="Pronunisasi:", font=("Helvetica", 12), background="#3498db", foreground="white")
        label_pronunciation.grid(row=8, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W + tk.E)

        pronunciation_text = ttk.Label(root, textvariable=self.pronunciation_text, wraplength=400, justify=tk.LEFT, font=("Helvetica", 12), background="#3498db", foreground="white")
        pronunciation_text.grid(row=9, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W + tk.E)

        # Responsif: atur berat kolom agar dapat menyesuaikan ukuran jendela
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

        # Menempatkan jendela di tengah layar
        root.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}+{int(screen_width/4)}+{int(screen_height/4)}")

        # Tambahkan gaya untuk tombol dengan efek hover
        style = ThemedStyle(root)
        style.set_theme("plastik")
        style.configure("TButton", foreground="#1f3a93", background="#1f3a93", font=("Helvetica", 12))
        style.map("TButton",
                foreground=[("active", "#1f3a93"), ("disabled", "grey")],
                background=[("active", "#3498db"), ("disabled", "grey")])

    def get_language_code(self, index):
        # Daftar kode bahasa sesuai dengan urutan pada Combobox
        language_codes = [
            "af", "sq", "am", "ar", "hy", "az", "eu", "be",
            "bn", "bs", "bg", "ca", "ceb", "ny", "zh-CN",
            "zh-TW", "co", "hr", "cs", "da", "nl", "en", "eo",
            "et", "tl", "fi", "fr", "fy", "gl", "ka", "de", "el",
            "gu", "ht", "ha", "haw", "iw", "hi", "hmn", "hu",
            "is", "ig", "id", "ga", "it", "ja", "jw", "kn",
            "kk", "km", "ko", "ku", "ky", "lo", "la", "lv", "lt",
            "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr",
            "mn", "my", "ne", "no", "ps", "fa", "pl", "pt",
            "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn",
            "sd", "si", "sk", "sl", "so", "es", "su", "sw",
            "sv", "tg", "ta", "te", "th", "tr", "uk", "ur",
            "uz", "vi", "cy", "xh", "yi", "yo", "zu"
        ]
        return language_codes[index]

    def translate_text(self):
        text = self.text_to_translate.get()
        language_index = self.language_combobox.current()
        language_code = self.get_language_code(language_index)

        translator = Translator()

        try:
            result = translator.translate(text, dest=language_code)
            self.translated_text.set(result.text)
            self.pronunciation_text.set(result.pronunciation)
        except Exception as e:
            self.translated_text.set("Terjemahan Gagal")
            self.pronunciation_text.set("")

    def on_enter_pressed(self):
        # Pindahkan fokus ke elemen GUI berikutnya
        self.language_combobox.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslateApp(root)
    root.mainloop()
