def f(amount_to_pay):
   ilosc_piatek = amount_to_pay //5
   po_odjeciu_piatek = amount_to_pay - (ilosc_piatek*5)
   ilosc_dwojek = po_odjeciu_piatek //2
   po_odjeciu_dwojek = amount_to_pay - (ilosc_piatek*5) - (ilosc_dwojek*2)
   ilosc_jedynek = po_odjeciu_dwojek
   ilosc_monet_razem = ilosc_piatek + ilosc_dwojek + ilosc_jedynek
   return ilosc_monet_razem

if __name__ == '__main__':
   print(f(23))
   print(f(8))
   print(f(2))
   print(f(0))
