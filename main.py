from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class TrialApp(MDApp):
    def build(self):
        label = MDLabel(text="Hey Everyone", halign="center", theme_text_color="Custom", text_color=(245/255, 100/255, 85/255), font_style="Caption")
        icon_label = MDIcon(icon='language-python', halign="center")
        return label  # Trả về label

TrialApp().run()
