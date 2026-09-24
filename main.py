import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

# Global Ses Deyiseni
current_sound = None

def play_audio(file_name):
    global current_sound
    try:
        if current_sound:
            current_sound.stop()
        if os.path.exists(file_name):
            current_sound = SoundLoader.load(file_name)
            if current_sound:
                current_sound.play()
    except Exception as e:
        print(f"Səs oxunarkən xəta oldu: {e}")

# ==========================================
# VIZUAL INTERFEYS DIZAYNI (KV LANGUAGE)
# ==========================================
KV_DESIGN = '''
ScreenManager:
    GirisEkrani:
    SecimEkrani:
    TesdiqEkrani:
    NeticeEkrani:

<GirisEkrani>:
    name: 'giris_ekrani'
    BoxLayout:
        orientation: 'vertical'
        padding: 30
        spacing: 20

        Label:
            text: "Kişilik Testi 2026 (by ayxanfr)"
            font_size: '22sp'
            bold: True
            color: 0.2, 0.6, 1, 1

        TextInput:
            id: ad_daxil_et
            hint_text: "Adıvı yaz bləd"
            multiline: False
            size_hint_y: None
            height: '50dp'
            font_size: '18sp'

        Button:
            text: "Başla"
            size_hint_y: None
            height: '55dp'
            background_color: 0.1, 0.8, 0.3, 1
            on_press: root.sonraki_sehife()

<SecimEkrani>:
    name: 'secim_ekrani'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 12

        Label:
            id: secim_bashliq
            text: "Seçim et!"
            font_size: '20sp'
            bold: True

        Button:
            text: "1) Elmanam"
            size_hint_y: None
            height: '50dp'
            on_press: root.secim_et("Elmanam")

        Button:
            text: "2) Ismayılam"
            size_hint_y: None
            height: '50dp'
            on_press: root.secim_et("Ismayilam")

        Button:
            text: "3) Raufam"
            size_hint_y: None
            height: '50dp'
            on_press: root.secim_et("Raufam")

        Button:
            text: "4) Ceyhunam"
            size_hint_y: None
            height: '50dp'
            on_press: root.secim_et("Ceyhunam")

        Button:
            text: "5) Men özüməm blədd!"
            size_hint_y: None
            height: '50dp'
            background_color: 0.9, 0.2, 0.2, 1
            on_press: root.secim_et("Ozumem")

<TesdiqEkrani>:
    name: 'tesdiq_ekrani'
    BoxLayout:
        orientation: 'vertical'
        padding: 30
        spacing: 25

        Label:
            text: "Əminsən? diqqətli ol."
            font_size: '22sp'
            bold: True
            color: 1, 0.3, 0.3, 1

        BoxLayout:
            orientation: 'horizontal'
            spacing: 20
            size_hint_y: None
            height: '60dp'

            Button:
                text: "BƏLI"
                background_color: 0.2, 0.8, 0.2, 1
                on_press: root.beli_basildi()

            Button:
                text: "XEYR"
                background_color: 0.8, 0.2, 0.2, 1
                on_press: root.xeyr_basildi()

<NeticeEkrani>:
    name: 'netice_ekrani'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        Image:
            id: netice_shekili
            source: ''
            allow_stretch: True
            keep_ratio: True
            size_hint_y: 0.5

        Label:
            id: netice_yazisi
            text: ""
            font_size: '18sp'
            text_size: self.width, None
            height: self.texture_size[1]
            halign: 'center'
            size_hint_y: 0.3

        Button:
            text: "Yenidən Başla"
            size_hint_y: None
            height: '50dp'
            on_press: app.yeniden_basla()
'''

# ==========================================
# MENTIQ VE FUNKSIYALAR (PYTHON KODU)
# ==========================================

istifadeci_adi = ""
secilen_variant = ""

class GirisEkrani(Screen):
    def sonraki_sehife(self):
        global istifadeci_adi
        ad = self.ids.ad_daxil_et.text.strip()
        if ad:
            istifadeci_adi = ad
            secim_screen = self.manager.get_screen('secim_ekrani')
            secim_screen.ids.secim_bashliq.text = f"Seçim et, {istifadeci_adi}!"
            self.manager.current = 'secim_ekrani'

class SecimEkrani(Screen):
    def secim_et(self, variant):
        global secilen_variant
        secilen_variant = variant
        self.manager.current = 'tesdiq_ekrani'

class TesdiqEkrani(Screen):
    def beli_basildi(self):
        netice_screen = self.manager.get_screen('netice_ekrani')
        
        if secilen_variant == "Elmanam":
            netice_screen.ids.netice_yazisi.text = f"Ən ağırlardan birisən.Yəqin səhvən seçmisən.Aşağdan bas yenidən seç."
            if os.path.exists('elman.jpg'):
                netice_screen.ids.netice_shekili.source = 'elman.jpg'
            play_audio('elman.mp3')
            
        elif secilen_variant == "Ismayilam":
            netice_screen.ids.netice_yazisi.text = f"Saçaqlı pendiri sox götüvə.110 kiloluq elmanın qardaşı."
            if os.path.exists('ismayıl.jpg'):
                netice_screen.ids.netice_shekili.source = 'ismayıl.jpg'
            play_audio('ismayıl.mp3')
            
        elif secilen_variant == "Raufam":
            netice_screen.ids.netice_yazisi.text = f"...""
            if os.path.exists('rauf.png'):
                netice_screen.ids.netice_shekili.source = 'rauf.png'
            play_audio('rauf.mp3')
            
        elif secilen_variant == "Ceyhunam":
            netice_screen.ids.netice_yazisi.text = f"Ceyhun çıx evdən!!!"
            if os.path.exists('ceyhun.png'):
                netice_screen.ids.netice_shekili.source = 'ceyhun.png'
            play_audio('ceyhun.mp3')
            
        elif secilen_variant == "Ozumem":
            netice_screen.ids.netice_yazisi.text = f"Bu günlük rahat yata bilərsən.Belə belə işlər."
            if os.path.exists('ozumem.png'):
                netice_screen.ids.netice_shekili.source = 'ozumem.png'
            play_audio('ozumem.mp3')

        self.manager.current = 'netice_ekrani'

    def xeyr_basildi(self):
        self.manager.current = 'secim_ekrani'
        
        popup_metni = "Ağıllı ol, az qala səhv yol verirdin!"
        
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=popup_metni, font_size='16sp'))
        
        close_btn = Button(text="X", size_hint=(None, None), size=('40dp', '40dp'), pos_hint={'right': 1})
        content.add_widget(close_btn)

        popup = Popup(title='Diqqet!', content=content, size_hint=(0.8, 0.4), auto_dismiss=False)
        close_btn.bind(on_release=popup.dismiss)
        popup.open()

class NeticeEkrani(Screen):
    pass

class KisilikTestiApp(App):
    def build(self):
        return Builder.load_string(KV_DESIGN)

    def yeniden_basla(self):
        global current_sound
        if current_sound:
            current_sound.stop()
        self.root.current = 'giris_ekrani'

if __name__ == '__main__':
    KisilikTestiApp().run()

