# coding: latin-1
import sys
import datetime


# Get the Month Day Year into string_date. 
# This is printed at the very bottom of the output.
now = datetime.datetime.now()
string_date = now.strftime("%b %d %Y")
#print(string_date)  



#print spreadsheet header
print ("GROUP,DSORT,DAY,TIME,LOCATION,ADDRESS")


# the number of AFG groups found so far
num_groups = 0

# after finding an AFG group, i is line count 
# of the input data within that AFG group.
i = 0

# Globals
csvline=""
s=""
DAY=""
TIME=""
LOC=""
ADDR=""
women=""
Allcaps = ""
zoom=""
chair=""
new=""
room=""


#with open("mdatashort.txt", "r") as file:
with open("mdata.txt", "r") as file:
#with open("mdata50.txt", "r") as file:

    for line in file:

        # remove the trailing newline character from each line
        clean_line = line.rstrip("\n")
        clean_line = clean_line[:46]  
        if ( clean_line.endswith("AFG")  or clean_line.endswith("GFA") ):
             i = 0     
             women=""
             zoom=""
             chair=""
             new=""
             room=""
       
        i = i + 1
        # look at the lines after AfG was found up until WSO is found

       
        if ( clean_line != ""):
        
              Allcaps =  clean_line.upper()
             
            
              #print ( "     " + str(i) + "    " + clean_line)
              myflag=0  # myflag indicates Day of week 

              if ("ZOOM" in Allcaps and csvline != ""):
                      zoom="\n ZOOM available. See NOTE."            
            
              # set the sort ordinal s for the day to  0=sun, 1=mon, etc.
              # get DAY and TIME
              if (i==3):   # line 3 is Day time e.g. "Thursday 6:00 PM"
                  # Get day of week
                  first_three = clean_line[:2]
                  upper_three = first_three.upper()
                  if (upper_three == "SU"):
                     s="0"
                  if (upper_three == "DO"):  # Domingo
                     s="0"                     
                  if (upper_three == "MO"):
                     s="1"   
                  if (upper_three == "LU"):  #Lunes
                     s="1"                     
                  if (upper_three == "TU"):
                     s="2"
                  if (upper_three == "MA"):  # Martes
                     s="2"                     
                  if (upper_three == "WE"):
                     s="3"   
                  if (upper_three == "MI"):  # Miércoles
                     s="3"                      
                  if (upper_three == "TH"):
                     s="4"  
                  if (upper_three == "JU"):  # Jueves
                     s="4"  
                  if (upper_three == "FR"):
                     s="5"
                  if (upper_three == "VI"):  # Viernes
                     s="5"
                  if (upper_three == "SA"): 
                     s="6" 
                  if (upper_three == "SÁ"): # Sabado
                     s="6"                     
                     
                  # "Thursday 6:00 PM"  split into DAY and TIME 
                  splitstuff = clean_line.split()
                  DAY=splitstuff[0]
                  TIME=splitstuff[1] + " " + splitstuff[2]
                     
              
              if (i==5):  # get location
                  LOC = clean_line
                     
                     
              if (i==7):  # get address
                  ADDR = clean_line                     

              if (i > 7): 
                  
                  if ("WOMEN" in Allcaps and csvline != ""):
                      women="\n Women Only."
                      
                  if ((Allcaps == "MEN") and (csvline != "") ): 
                      women="\n Men Only."
                      
                  if ("LGBTQIA" in Allcaps and csvline != ""):
                      women="\n LGBTQIA+ welcoming."                    
                      
                  if ("CHAIR" in Allcaps and csvline != ""):
                      chair="\n We meet under the tree. Bring a chair."  
                      
                  if ("NEWCOM" in Allcaps and csvline != ""):
                       new="\n Newcomers welcome."  
                       
                  if ("ROOM 161" in Allcaps and csvline != ""):
                       room="\n Room 161."    
                  if ("ROOM A" in Allcaps and csvline != ""):
                       room="\n Room 161."                                                         
                                    
                 

        # Assemble all the fields collected and print the final line.                      
        if ( clean_line[:3] == "WSO" ):
            csvline = csvline + "," + s + "," + DAY + "," + TIME + ",\"" +  LOC + "\",\"" + ADDR + women + zoom +  chair + new + room + "\""
            print (csvline)
   
            
        # get the name of the AFG group 
        if ( clean_line.endswith("AFG")  or clean_line.endswith("GFA") ):
            #print (clean_line)
            csvline = clean_line
            num_groups = num_groups +1

            
print ("\nThe number of meetings = " + str(num_groups))
print ("\nMeeting list created,,,," + string_date )
print (",,,,Shows meetings 25 miles of central Austin 78705.")

print ("\n\n  NOTE:,,,,This is my personal list and is not an official")
print (",,,,publication of Al-Anon or any of its groups.")
print (",,,,Some details were omitted for brevity. For com-")
print (",,,,plete meeting information see Al-Anon website")
print (",,,,https://al-anon.org/al-anon-meetings")

print ("\n\n,,,,A printable file (pdf) of this list is available on")
print (",,,,https://myalanon.github.io") 



            
            

                     
                     