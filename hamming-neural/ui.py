#!/usr/bin/env python
# -- coding: utf-8 --

import os
import re
import sys

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

import kivy.app as app
import kivy.uix.button as btn
import kivy.uix.floatlayout as fl
import kivy.uix.label as label
import kivy.uix.popup as pu
import kivy.uix.tabbedpanel as tp
import kivy.uix.tabbedpanel as tph
import kivy.uix.textinput as ti
import kivy.uix.checkbox as cb
import kivy.uix.togglebutton as tb
import kivy.core.window as wi

import neural


class FieldRules(ti.TextInput):

    pattern = re.compile(r'[ A-Za-z!?=*+\\,]')

    def insert_text(self, substring, from_undo=False):
        search = re.sub(self.pattern, '', substring)
        return super(FieldRules, self).insert_text(search, from_undo=from_undo)


class NeuralNetworkApp(app.App):

    @staticmethod
    def autosize_font(perc):
        return perc * wi.Window.height

    def create_table(self):
        x = 0
        y = 0
        self.toogle_button = []
        for i in range(0, 40):
            if i%5 == 0:
                x = 0
                y -= .05
            else:
                x += .05
            self.check = tb.ToggleButton(size_hint=(.05, .05), pos_hint={'x': .36+x, 'y': .95+y})
            self.toogle_button.append(self.check)
            self.grid.add_widget(self.check)

    def clean_all(self):
        for button in self.toogle_button:
            self.grid.remove_widget(button)
        self.create_table()

    def calculate(self):
        self.popup.open()
        try:
            self.grid.remove_widget(self.label)
        except AttributeError:
            pass

        input_value = []
        for button in self.toogle_button:
            if button.state == 'down':
                input_value.append(1)
            else:
                input_value.append(0)

        output = neural.get_output(target=neural.target, input=input_value)[0]
        sum_value = sum(i > 0 for i in output)

        if sum_value == 0:
            self.label = label.Label(text="Cеть даже понять не может, что это!",
                                     font_size=self.autosize_font(0.038))
        elif sum_value == 1:
            index = 'none'
            for i in range(0, len(output)):
                if output[i] > 0:
                    index = i
            self.label = label.Label(text="Cеть считает что это: {0}".format(index),
                                     font_size=self.autosize_font(0.038))
        else:
            index = ', '.join(str(i) for i in range(0, len(output)) if output[i]>0)
            self.label = label.Label(text="Cеть считает что это: {0}".format(index),
                                     font_size=self.autosize_font(0.038))
        self.grid.add_widget(self.label)
        self.popup.dismiss()


    def build(self):
        self.grid = fl.FloatLayout(size=(200, 200))

        self.create_table()
        self.label = label.Label()
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
        self.popup = pu.Popup(title='Loading',
                              content=label.Label(text='Please, wait...'),
                              size_hint=(None, None), size=(200, 200),
                              auto_dismiss=False)

        self.grid.add_widget(self.calculate_button)
        self.grid.add_widget(self.clear_button)
        self.grid.add_widget(self.exit_button)
        return self.grid

if __name__ == '__main__':
    NeuralNetworkApp().run()
