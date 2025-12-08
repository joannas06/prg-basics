# tv_show.py file
# main program
import tv

def main():
   # object creation
   telewizor = tv.TV()

   # object usage
   telewizor.show_status()
   telewizor.turn_on()
   telewizor.show_status()
   telewizor.set_channels(['TVP1','TVP2','Polsat','TVN','Filmbox','Discovery'])
   telewizor.show_status()
   telewizor.turn_off()
   telewizor.show_status()
   

if __name__ == "__main__":
   main() 