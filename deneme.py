pizzalar_tuple=[("sade Pizza",36,False),("margarita Pizza",50,True),("klasik Pizza",40,False),("türk Pizza",45,False)]
malzemeler_Tuple=[("zeytin",10 ,True), ("mısır",14, False), ("et",20, True), ("sosis", 16, False),("mantar", 7, True)]
siparis=[]


def pizza_secim(pizza_listesi):
  global siparis
  for eleman in pizza_listesi:
    if eleman[2] == True:
      siparis.append(eleman[0:2])
  return siparis

def malzeme_secimi(malzeme_listesi):
  global siparis
  for eleman in malzeme_listesi:
    if eleman[2] == True:
      siparis.append(eleman[0:2])
  return siparis

def sozluk_olustur(siparis_listesi):
  sepet_ekle = {"pizza": "", "malzeme": "", "fiyat": 0}
  for veri in siparis_listesi:
    if "Pizza" in veri[0]:
        sepet_ekle['pizza'] = veri[0]
    else:
        if sepet_ekle["malzeme"] != "":
            sepet_ekle["malzeme"] += ", "
        sepet_ekle["malzeme"] += veri[0]
    sepet_ekle["fiyat"] += veri[1]
  return sepet_ekle

pizza_secim(pizzalar_tuple)
print(siparis)
malzeme_secimi(malzemeler_Tuple)
print(siparis)

print(sozluk_olustur(siparis))

a= klasik_pizza()

description= a.de

        if self.ui.klas_pizza_check.isChecked():
            kl_pi = klasik_pizza()
            pi_tuple.append(kl_pi)
        elif self.ui.Mar_pizza_check.isChecked():
            m_pi= margarita_pizza()
            pi_tuple.append(m_pi)
        elif self.ui.turk_pizza_check.isChecked():
            t_pi= Turk_pizza()
            pi_tuple.append(t_pi)
        else:
            s_pi= sade_pizza()
            pi_tuple.append(s_pi)