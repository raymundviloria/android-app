from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from functools import partial
import pygame

pygame.init()
pygame.display.set_icon(pygame.Surface((500, 600)))

def get_json():
    return [
        { "type": "title",
          "title": "Test application" },

        { "type": "options",
          "title": "My first key",
          "desc": "Description of my first key",
          "section": "section1",
          "key": "key1",
          "options": ["value1", "value2", "another value"] },

        { "type": "numeric",
          "title": "My second key",
          "desc": "Description of my second key",
          "section": "section1",
          "key": "key2" }
    ]


class TestApp(App):

    def build_settings(self, settings):
        jsondata = get_json()
        settings.interface.menu.width = dp(100)
        settings.add_json_panel('Test application',
            self.config, data=jsondata)

    def on_config_change(self, config, section, key, value):
        if config is self.config:
            token = (section, key)
            if token == ('section1', 'key1'):
                print('Our key1 have been changed to', value)
            elif token == ('section1', 'key2'):
                print('Our key2 have been changed to', value)


if __name__ == '__main__':
    TestApp().run()
