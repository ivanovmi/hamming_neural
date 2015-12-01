 #!/usr/bin/env python
# -- coding: utf-8 --

import re
import sys
import os
from os.path import sep, expanduser, isdir, dirname
import platform
from PIL import Image

# Import in this case needed for setting config
# variables before others import. If we put
# this code below others import, we can't guarantee
# his work on 100%
from kivy import config
import gtk

screen_size = gtk.gdk.screen_get_default()

config.Config.set('graphics', 'resizable', 0)
config.Config.set('graphics', 'height', screen_size.get_height()/2)
config.Config.set('graphics', 'width', screen_size.get_width()/3)

# Модули для создания UI
import kivy.app as app
import kivy.uix.button as btn
import kivy.uix.floatlayout as fl
import kivy.uix.label as label
import kivy.uix.popup as pu
import kivy.uix.textinput as ti
import kivy.uix.togglebutton as tb
import kivy.core.window as wi
import kivy.uix.filechooser as fc
import kivy.uix.filebrowser as fb
import kivy.uix.modalview as mv
# Импортируем модуль, в котором создается сеть
import neural
import image

class FieldRules(ti.TextInput):

    pattern = re.compile(r'[ A-Za-z!?=*+\\,]')

    def insert_text(self, substring, from_undo=False):
        search = re.sub(self.pattern, '', substring)
        return super(FieldRules, self).insert_text(search, from_undo=from_undo)


class NeuralNetworkApp(app.App):

    platform = platform.system().lower()

    @staticmethod
    def autosize_font(perc):
        """
        Функция для автоматического ресайза шрифтов (на любой размер экрана)
        :param perc: Процент на который надо умножить
        :return: Размер шрифта
        """
        return perc * wi.Window.height

    def create_browser(self):
        if platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'
        browser = fb.FileBrowser(select_string='Select',
                                 favorites=[(user_path, 'Documents')])
        browser.bind(
                    on_success=self._fbrowser_success,
                    on_canceled=self._fbrowser_canceled)
        return browser

    def _fbrowser_canceled(self, instance):
        self.view.dismiss()

    def _fbrowser_success(self, instance):
        try:
            self.file = instance.selection[0]
        except IndexError:
            pass
        else:
            self.filename_label = label.Label(text=self.file,
                                              pos_hint={'x': .0, 'y': .2})
            self.grid.add_widget(self.filename_label)
            self.view.dismiss()

    def calculate(self):
        """
        Функция для рассчета результата сети
        :return:
        """
        # Открываем попап
        self.popup.open()
        try:
            # Пробуем удалить label.
            self.grid.remove_widget(self.label)
        except AttributeError:
            # Если его нет - ничего страшного, создадим потом, и
            # будем удалять каждый раз, как вызовем self.calculate()
            pass

        letters = []

        tmp_dir = image.slice_image(self.file)
        #cv2.imshow('norm', self.file)
        print self.file
        self.im = Image.open(self.file)
        print self.file
        self.im.show(title=self.file)
        
        for self.image in sorted(os.listdir(tmp_dir)):
            input_value = image.convert_letter_to_bitmap(tmp_dir+'/'+self.image, False)
            #print input_value
            output = neural.get_output(input=input_value, neuron=self.neuron)
            #print(output)
        #    # Считаем сколько элементов отлично от 0
            sum_value = sum(i > 0 for i in output)
            if sum_value == 1:
                index = None
                for i in range(0, len(output)):
                    if output[i] > 0:
                        index = i
                letters.append(neural.result_dict[index])

        self.label = \
                label.Label(text=''.join(i for i in letters))

        # Формируем вывод в label
        #if sum_value == 0:
        #    self.label = \
        #        label.Label(text="Cеть даже понять не может, что это!",
        #                    font_size=self.autosize_font(0.038))
        #elif sum_value == 1:
        #    index = 'none'
        #    for i in range(0, len(output)):
        #        if output[i] > 0:
        #            index = i
        #    self.label = label.Label(text="Cеть считает что это: {0}".
        #                             format(neural.result_dict[index]),
        #                             font_size=self.autosize_font(0.038))
        #else:
        #    index = ', '.join(str(i)
        #                      for i in range(0, len(output))
        #                      if output[i] > 0)
        #    self.label = label.Label(text="Cеть считает что это: {0}".
        #                             format(neural.result_dict[index]),
        #                             font_size=self.autosize_font(0.038))
        self.grid.add_widget(self.label)
        self.popup.dismiss()

    def start_browsing(self):
        self.view = mv.ModalView(size_hint=(None, None),
                                 size=(screen_size.get_width()/3-50, screen_size.get_height()/2-50),
                                 auto_dismiss=False)
        self.view.add_widget(self.create_browser())
        self.view.open()

    def build(self):

        self.neuron = neural.train(image.create_target())

        # Сетка для размещения элементов внутри окна.
        self.grid = fl.FloatLayout(size=(200, 200))

        self.browse_button = btn.Button(text='Обзор',
                                        size_hint=(.33, .25),
                                        font_size =self.autosize_font(0.038),
                                        pos_hint={'x': .68, 'y': .75},
                                        on_press=lambda f: self.start_browsing())

        # Пустой ярлык, куда впоследствии
        # будем писать результаты обработки от сети
        self.label = label.Label()

        # Кнопки "Рассчитать", "Очистить" и "Выход"
        self.calculate_button = btn.Button(text='Рассчитать',
                                           size_hint=(.33, .25),
                                           font_size=self.autosize_font(0.038),
                                           pos_hint={'x': .0, 'y': .0},
                                           on_press=lambda f: self.calculate())
        self.clear_button = btn.Button(text='Очистить все',
                                       font_size=self.autosize_font(0.038),
                                       size_hint=(.33, .25),
                                       pos_hint={'x': .34, 'y': .0},
                                       on_press=lambda f: self.clean_all())
        self.exit_button = btn.Button(text='Выход',
                                      size_hint=(.33, .25),
                                      font_size=self.autosize_font(0.038),
                                      pos_hint={'x': .68, 'y': .0},
                                      on_press=lambda f: sys.exit())

        # Всплывающее окно, взывающее пользователя проявить терпение.
        # Пока сеть маленькая, может и не особо надо. В дальнейшем,
        # я чувствую, точно пригодится
        self.popup = pu.Popup(title='Loading',
                              content=label.Label(text='Please, wait...'),
                              size_hint=(None, None), size=(200, 200),
                              auto_dismiss=False)

        # Добавляем кнопки на форму
        self.grid.add_widget(self.browse_button)
        self.grid.add_widget(self.calculate_button)
        self.grid.add_widget(self.clear_button)
        self.grid.add_widget(self.exit_button)
        return self.grid
