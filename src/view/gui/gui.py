from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

import sys
sys.path.append("src")

from model.logica_calculadora_impuestos import (
    VariablesImpuestos,
    ValidarVariables,
    CalcularImpuesto,
    ErrorIngresos,
    ErrorTopesDeducciones,
    ErrorDependientes,
    ErrorPension,
    ErrorInteresVivienda,
    ErrorSalud
)

class CalcuImpuestosApp(App):

    def build(self):
        self.root_layout = BoxLayout(orientation='vertical', padding=10, spacing=8)

        titulo = Label(text='Calculadora de Impuestos', font_size=24, size_hint_y=None, height=40)
        self.root_layout.add_widget(titulo)

        form = GridLayout(cols=2, spacing=6, size_hint_y=None, height=300)

        form.add_widget(Label(text='Ingresos anuales:'))
        self.inp_ingresos = TextInput(multiline=False)
        form.add_widget(self.inp_ingresos)

        form.add_widget(Label(text='Deducciones generales:'))
        self.inp_deducciones = TextInput(multiline=False)
        form.add_widget(self.inp_deducciones)

        form.add_widget(Label(text='Aportes a pensión:'))
        self.inp_pension = TextInput(multiline=False)
        form.add_widget(self.inp_pension)

        form.add_widget(Label(text='Aportes a salud:'))
        self.inp_salud = TextInput(multiline=False)
        form.add_widget(self.inp_salud)

        form.add_widget(Label(text='Número de dependientes:'))
        self.inp_dependientes = TextInput(multiline=False)
        form.add_widget(self.inp_dependientes)

        form.add_widget(Label(text='¿Tiene vivienda propia?'))
        self.spin_vivienda = Spinner(
            text='No',
            values=['Sí', 'No']
        )
        form.add_widget(self.spin_vivienda)

        form.add_widget(Label(text='Intereses de vivienda:'))
        self.inp_intereses = TextInput(multiline=False)
        form.add_widget(self.inp_intereses)

        self.root_layout.add_widget(form)

        btn = Button(text='Calcular', size_hint_y=None, height=44)
        btn.bind(on_press=self.calcular)
        self.root_layout.add_widget(btn)

        self.lbl_resultado = Label(text='', font_size=16)
        self.root_layout.add_widget(self.lbl_resultado)

        return self.root_layout

    def calcular(self, instance):
        try:
            ingresos = float(self.inp_ingresos.text)
        except ValueError:
            self.lbl_resultado.text = "Error: Ingresos debe ser un número."
            return

        try:
            deducciones = float(self.inp_deducciones.text)
        except ValueError:
            self.lbl_resultado.text = "Error: Deducciones debe ser un número."
            return

        try:
            pension = float(self.inp_pension.text)
        except ValueError:
            self.lbl_resultado.text = "Error: Pensión debe ser un número."
            return

        try:
            salud = float(self.inp_salud.text)
        except ValueError:
            self.lbl_resultado.text = "Error: Salud debe ser un número."
            return

        try:
            dependientes = int(self.inp_dependientes.text)
        except ValueError:
            self.lbl_resultado.text = "Error: Dependientes debe ser un entero."
            return

        tiene_vivienda = self.spin_vivienda.text == "Sí"

        if tiene_vivienda:
            try:
                intereses = float(self.inp_intereses.text)
            except ValueError:
                self.lbl_resultado.text = "Error: Intereses debe ser un número."
                return
        else:
            intereses = 0
        try:
            variables = VariablesImpuestos(
                ingresos,
                deducciones,
                pension,
                salud,
                dependientes,
                tiene_vivienda,
                intereses
            )

            ValidarVariables.validar_parametros_entrada(variables)
            impuesto = CalcularImpuesto.calcular_impuesto_renta(variables)

            self.lbl_resultado.text = f"Impuesto a pagar: ${impuesto:,.2f}"

        except (
            ErrorIngresos,
            ErrorTopesDeducciones,
            ErrorDependientes,
            ErrorPension,
            ErrorInteresVivienda,
            ErrorSalud
        ) as e:
            self.lbl_resultado.text = str(e)


if __name__ == '__main__':
    CalcuImpuestosApp().run()