import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Anaekran_UI import *
from PyQt5.QtCore import Qt
class pizza:
    def __init__(self, desciption, cost):
            self.description = desciption
            self.cost = cost

    def get_description(self):
            return self.description
    def get_cost(self):
            return self.cost

class klasik_pizza(pizza):
    def __init__(self):
             super().__init__("Klasik Pizza", 30)

class margarita_pizza(pizza):
    def __init__(self) :
            super().__init__("Margarita Pizza", 60)

class Turk_pizza(pizza):
    def __init__(self):
            super().__init__("Türk Pizza", 90)
class sade_pizza(pizza):
    def __init__(self):
            super().__init__("Sade Pizza", 8)


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.pizza_ad_cheB()
        #self.veri_ekle({'pizza': 'margarita Pizza', 'malzeme': 'zeytin, et, mantar', 'fiyat': 87})
        self.ui.sepete_ekle.clicked.connect(self.pizza_tuple)
        

    #def sepete_ekle(self):

    def pizza_tuple(self):
        s_pi= sade_pizza()
        t_pi= Turk_pizza()
        m_pi= margarita_pizza()
        kl_pi = klasik_pizza()
        check_box =[[self.ui.klas_pizza_check ,self.ui.klas_pizza_check.isChecked()],
                    [self.ui.Mar_pizza_check ,self.ui.Mar_pizza_check.isChecked()], 
                    [self.ui.turk_pizza_check, self.ui.turk_pizza_check.isChecked()],
                    [self.ui.s_pizza_check ,self.ui.s_pizza_check.isChecked()]]
        pizzalar_tuple = [
            (kl_pi.description, kl_pi.cost, self.ui.klas_pizza_check.isChecked()),
            (m_pi.description, m_pi.cost, self.ui.Mar_pizza_check.isChecked()),
            (t_pi.description, t_pi.cost, self.ui.turk_pizza_check.isChecked()),
            (s_pi.description, s_pi.cost, self.ui.s_pizza_check.isChecked())
        ]
        for checkbox in check_box:
            if checkbox[1]:
                for other_checkbox in check_box:
                    if other_checkbox[0] != checkbox[0]:
                        other_checkbox[0].setEnabled(False)
                checkbox[1] = False
                break
            else:
                for other_checkbox in check_box:
                    if other_checkbox[0] != checkbox[0]:
                        other_checkbox[0].setEnabled(True)

    
                     
        return print(pizzalar_tuple)
        





    def pizza_ad_cheB(self):
        check_box= [self.ui.checkBox_1, self.ui.checkBox_2, self.ui.checkBox_3, self.ui.checkBox_4,]
        liste= ["KlasikPizza", "MargaritaPizza",  "TürkPizza", "SadePizza"]
        for index, eleman in enumerate(check_box):
            eleman.setText(liste[index])


    def veri_ekle(self, veriler):  
        table_widget = self.ui.sepet_table
        row_count = table_widget.rowCount()
        table_widget.setRowCount(row_count + 1)
        row = row_count
        # yeni bir QTableWidgetItem objesi oluştur
        pizza_item = QTableWidgetItem(veriler["pizza"])
        malzeme_item = QTableWidgetItem(veriler["malzeme"])
        fiyat_item = QTableWidgetItem(str(veriler["fiyat"]))

        # QTableWidgetItem objelerinin ulaşılmaz yapılması
        pizza_item.setFlags(pizza_item.flags() ^ Qt.ItemIsEditable)
        malzeme_item.setFlags(malzeme_item.flags() ^ Qt.ItemIsEditable)
        fiyat_item.setFlags(fiyat_item.flags() ^ Qt.ItemIsEditable)

        # QTableWidgetItem objelerini tableWidget'a ekle
        table_widget.setItem(row, 0, pizza_item)
        table_widget.setItem(row, 1, malzeme_item)
        table_widget.setItem(row, 2, fiyat_item)

        # Checkbox ekle
        checkbox_item = QTableWidgetItem()
        checkbox_item.setCheckState(Qt.Checked)
        table_widget.setItem(row, 3, checkbox_item)





uyg = QApplication(sys.argv)
pencere = MainPage()
pencere.show()
sys.exit(uyg.exec_())