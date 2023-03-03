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
        self.ui.sepete_ekle_button.clicked.connect(self.sepete_ekle)
        self.ui.klas_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.Mar_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.turk_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.ui.s_pizza_check.stateChanged.connect(self.checkBox_secim)
        self.siparis=[]

    def sepete_ekle(self):
        a=self.pizza_secim(self.pizza_tuple())
        return print(a)
    

    def pizza_tuple(self):
        s_pi= sade_pizza()
        t_pi= Turk_pizza()
        m_pi= margarita_pizza()
        kl_pi = klasik_pizza()        
        pizzalar_tuple = [
            (kl_pi.description, kl_pi.cost, self.ui.klas_pizza_check.isChecked()),
            (m_pi.description, m_pi.cost, self.ui.Mar_pizza_check.isChecked()),
            (t_pi.description, t_pi.cost, self.ui.turk_pizza_check.isChecked()),
            (s_pi.description, s_pi.cost, self.ui.s_pizza_check.isChecked())
        ]
        return pizzalar_tuple
    
    def malzeme_tuple(self):
        pass
         
    def soslar_tuple(self):
        pass

    def icecekler_tuple(self):
        pass
    

    def pizza_secim(self, pizza_listesi):
        for eleman in pizza_listesi:
            if eleman[2] == True:
                self.siparis.append(eleman[0:2])
        return self.siparis


    def malzeme_secimi(self, malzeme_listesi):
        for eleman in malzeme_listesi:
            if eleman[2] == True:
                self.siparis.append(eleman[0:2])
        return self.siparis
    
    def sos_secim(self, sos_listesi):
        pass

    def icecekler_secim(self, icecek_listesi):
        pass


    def sozluk_olustur(siparis_listesi):
        sepet_ekle = {"Pizza": "", "Malzemeler": "","Soslar":"", "İçecekler":"", "Fiyat": 0, "Notlar":""}
        for veri in siparis_listesi:
            if "Pizza" in veri[0]:
                sepet_ekle['pizza'] = veri[0]
            else:
                if sepet_ekle["malzeme"] != "":
                    sepet_ekle["malzeme"] += ", "
                sepet_ekle["malzeme"] += veri[0]
            sepet_ekle["fiyat"] += veri[1]
        return sepet_ekle


    def checkBox_secim(self):
        check_box =[
            [self.ui.klas_pizza_check ,self.ui.klas_pizza_check.isChecked()],
            [self.ui.Mar_pizza_check ,self.ui.Mar_pizza_check.isChecked()], 
            [self.ui.turk_pizza_check, self.ui.turk_pizza_check.isChecked()],
            [self.ui.s_pizza_check ,self.ui.s_pizza_check.isChecked()]
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
     

    def tabloya_veri_ekle(self, veriler):  
        table_widget = self.ui.sepet_table
        row_count = table_widget.rowCount()
        table_widget.setRowCount(row_count + 1)
        row = row_count

        # yeni bir QTableWidgetItem objesi oluştur
        pizza_item = QTableWidgetItem(veriler["Pizza"])
        malzeme_item = QTableWidgetItem(veriler["Malzemeler"])
        sos_item = QTableWidgetItem(veriler["Soslar"])
        icecekler_item = QTableWidgetItem(veriler["İçecekler"])
        tutar_item = QTableWidgetItem(str(veriler["Fiyat"]))
        notlar_item = QTableWidgetItem(veriler["Notlar"])

        # Tablonun dışarıdan erişilmesini engelleme
        pizza_item.setFlags(pizza_item.flags() ^ Qt.ItemIsEditable)
        malzeme_item.setFlags(malzeme_item.flags() ^ Qt.ItemIsEditable)
        sos_item.setFlags(sos_item.flags() ^ Qt.ItemIsEditable)
        icecekler_item.setFlags(icecekler_item.flags() ^ Qt.ItemIsEditable)
        tutar_item.setFlags(tutar_item.flags() ^ Qt.ItemIsEditable)
        notlar_item.setFlags(notlar_item.flags() ^ Qt.ItemIsEditable)


        # QTableWidgetItem objelerini tableWidget'a ekle
        table_widget.setItem(row, 0, pizza_item)
        table_widget.setItem(row, 1, malzeme_item)
        table_widget.setItem(row, 2, sos_item)
        table_widget.setItem(row, 3, icecekler_item)
        table_widget.setItem(row, 4, tutar_item)
        table_widget.setItem(row, 5, notlar_item)
        
        #  Sil Sütununa Checkbox eklenmesi
        checkbox_item = QTableWidgetItem()
        checkbox_item.setCheckState(Qt.Checked)
        table_widget.setItem(row, 6, checkbox_item)





uyg = QApplication(sys.argv)
pencere = MainPage()
pencere.show()
sys.exit(uyg.exec_())