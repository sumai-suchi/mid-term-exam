class star_Cinema:
    hall_list=[]


    def entry_hall(cls,hall):
        cls.hall_list.append(hall)


class hall(star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        super().entry_hall(self)
        self.__seats={}
        self.__show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no


    def entry_show(self,id,movie_name,time):
        show_information=(id,movie_name,time)
        self.__show_list.append(show_information)
        self.__seats[id]=[[0 for _ in range(self.__cols)] 
                           for _ in range(self.__rows)]
                
                     

    def seat_books(self,id,seat_list):
        if id not in self.__seats:
            print('Error id')
            return
        for row,col in seat_list:
            if row >=self.__rows or col >=self.__cols or row < 0 or col < 0:
               print("Seat is out of range")
            if self.__seats[id][row][col]=='Booked':
                print("Sorry,this sit is booked")
            self.__seats[id][row][col]='Booked'

    def view_show_list(self):
        return self.__show_list



    def view_available_seats(self,Id):
        if Id not in self.__seats:
             print ("Invalid show ID.")
        return self.__seats[Id]






hall1 =hall(10, 12, 1)
hall1.entry_show("S1", "Welcome", "10:00 AM")
hall1.entry_show("S2", "12th fail", "01:00 PM")

hall2=hall(15,18,2)
hall2.entry_show("S3","DDLJ","11:30 AM")
hall2.entry_show("S4","DDLJ2","1:30 PM")





while True:
          print("WELCOME TO STAR_CINEMA")

          print("List of hall")
          print("1:Hall1")
          print("2:Hall2")

          choosehall=input("choose hall")

          if choosehall=="1":
              print("Optione")
              print("1:View all running show")
              print("2:View avaiable seats in show")
              print("3:Book tickets in  a show")
              print("4:Exit")
              option=input("choose a option:")

              if option=="1":
                  print("All running shows")
                  hall1.view_show_list()
              elif option=="2":
                  print("Available seats")


                  print(" Take show Id")
                  print("Options")
                  print("1:S1")
                  print("2:S2")
                  take_id=input("Show_id")
                  if take_id=="1":
                      print(hall1.view_available_seats("S1"))
                  elif take_id=="2":
                      print(hall1.view_available_seats("S2"))
                  else:
                      print("INVALID ID")


              elif option=="3":
                  print("Book ticket in a show")
                  list=[]
                  num=int(input())

                  for _ in range(num):
                       seat=input()
                       s=tuple(map(int, seat.split()))
                       list.append(s)

                  print("Show Id")
                  print("1:S1")
                  print("2:S2")

                  take_id=input()
                  if take_id=="1":
                      hall1.seat_books("S1",list)
                  elif take_id=='2':
                      hall1.seat_books("S2",list) 
                  else:
                      print("Invalid")

              elif option=="4":
                  print("Exit")
                  break
                  
              else:
                  print("Invalid option")              
                             
              
                  
                
            
                           
          elif choosehall=="2":
              print("Option")
              print("1:View all running show")
              print("2:View available seats in show")
              print("3:Book tickets in  a show")
              print("4:Exit")
              option=input("choose a option:")

              if option=="1":
                  print("All running shows")
                  print(hall1.view_show_list())
              elif option=="2":
                  print("Available seats")


                  print(" Take show Id")
                  print("Options")
                  print("1:S1")
                  print("2:S2")
                  take_id=input()
                  if take_id=="1":
                      print(hall2.view_available_seats("S3"))
                  elif take_id=="2":
                      print(hall2.view_available_seats("S4"))
                  else:
                      print("INVALID ID")    
                          

              elif option=="3":
                  print("Book ticket in a show")
                  list=[]
                  num=int(input())

                  for _ in range(num):
                       seat=input()
                       s=tuple(map(int, seat.split()))
                       list.append(s)


                  print("Show Id")
                  print("1:S3")
                  print("2:S4")

                  take_id=input()
                  if take_id=="1":
                      hall2.seat_books("S3",list)
                  elif take_id=="2":
                      hall2.seat_books("S4",list) 
                  else:
                      print("Invalid")

              elif option=="4":
                  print("Exit")
                  break 
              else:
                  print("Invalid option") 
                  break
                    
                                  
                             
          else:
              print("Invalid option") 
              break
                  
            



                  
                   




          
         

                 
          


            
            
            
            


  

