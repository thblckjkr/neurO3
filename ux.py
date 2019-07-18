# Teo Gonzalez Calzada [@thblckjkr] 2019/04/07
# Class to act as an interface to the user

class ui:
   colors = {
      'header' : '\033[95m', 'info' : '\033[94m', 'success' : '\033[92m', 'warning' : '\033[93m',
      'error' : '\033[91m', 'ENDC' : '\033[0m', 'bold' : '\033[1m', 'underline' : '\033[4m'
   }

   def __init__(self):
      self.show("Inicializando interfaz...\n", 'info')
      
   def show(self, message, type = 'info'):
      color = self.colors.get(type, "Programing error")
      print (color + message + self.colors['ENDC'])

   def askYesNo(self, message):
      self.show(message, 'info')
      message = "(y)Si o (n)No: "
      while(True):
         temp = input(message)
         if temp != 'y' and temp != 'Y'  and temp != 'n' and temp != 'N':
            self.show("No has seleccionado un valor coherente", 'warning')
         else:
            if temp == 'y' or temp == 'Y':
               temp = 1
            else:
               temp = 0
               
            return int(temp)
   
   def askNumber(self, message, t ='int'):
      self.show(message, 'info')
      message = ""
      while(True):
         temp = input("")
         try:
            if t == 'float':
               xtemp = float(temp)
            else:
               xtemp = int(temp)
            
            return xtemp
         except ValueError:
            self.show("No has seleccionado un valor coherente", 'warning')

   def ask(self, message):
      self.show(message, 'info')
      message = ""
      temp = input("")
      return temp