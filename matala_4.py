from sys import exit
import requests
import pprint

#     address=line
#     api_key="AIzaSyAK4CvVbEg_IU2dU2juIhKUdV8_ELkQfoE"
#     url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address,api_key)
#     try:
#         response = requests.get(url)
#         if not response.status_code == 200:
#             print("HTTP error",response.status_code)
#         else:
#             try:
#                 response_data = response.json()
#             except:
#                 print("Response not in valid JSON format")
#     except:
#         print("Something went wrong with requests.get")
        
#     data=()
#     data=("lat",'value' ,"lng","value_2")          
#     value=response_data ['results'][0]['geometry']['location']['lat']  
#     value_2=response_data['results'][0]['geometry']['location']['lng'] 
#     data=("lat:",value ,"lng:",value_2)          
#     return data  
def location(line):
    try:
        address=line 
        api_key='AIzaSyAK4CvVbEg_IU2dU2juIhKUdV8_ELkQfoE'
        url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address,api_key)
        try:
            response = requests.get(url)
            if not response.status_code == 200:
                print("HTTP error",response.status_code)
            else:
                try:
                    response_data = response.json()
                except:
                    print("Response not in valid JSON format")
        except:
            print("Something went wrong with requests.get")
        lat=response_data['results'][0]['geometry']['location']['lat']
        lng=response_data['results'][0]['geometry']['location']['lng']
        return lat,lng
    except:
        print("Something went wrong with the dactination value ")
        exit()
          
    

      
def time_dest (line):
    try:
        address=line
        url="https://maps.googleapis.com/maps/api/distancematrix/json?key=AIzaSyAK4CvVbEg_IU2dU2juIhKUdV8_ELkQfoE&origins=tel+aviv&destinations=%s" % (address)
        try:
            response = requests.get(url)
            if not response.status_code == 200:
                print("HTTP error",response.status_code)
            else:
                try:
                    response_data = response.json()
                except:
                    print("Response not in valid JSON format")
        except:
            print("Something went wrong with requests.get")
        
        dst=response_data['rows'][0]['elements'][0]['distance']['text']
        sc=response_data['rows'][0]['elements'][0]['duration']['value']
        Hours=int(sc/(3600))
        Minute=round((sc-3600*Hours)/60)
        
        
        return dst,Minute,Hours
    except:
        print("Something went wrong with the dactination value ")
        exit()

def Nmaxelements(dict1):
    max1=0
    listt=[0,0,0]
    for i in range(3):
        max1=0
        for key in dict1:
            lst=dict1[key][0].split()
            lstt=lst[1]
            lstt=lstt.replace(",","")
            lstt=float(lstt)   
            if lstt>max1 :
                max1=lstt
                listt[i]=key
        dict1.pop(listt[i])
    return listt



global citiys
citiys={}
all_number=[]            
#The rest of your code should go below this line
file=open('dests.txt', "r", encoding="utf8" )
for line in file:
     data_2=location(line)
     data_1=time_dest(line)
     line=line.rstrip()
     all_inpo=()
     all_inpo=("dst: " + str(data_1[0]) ,"Time: " + str(data_1[1]) +" Minutes " + str(data_1[2]) +" Hours" ,"lat: " + str(data_2[0]),"lng: " + str(data_2[1]))
     citiys[line]=all_inpo
     num=data_1[0].split()    
     # num=num[0].replace(",","")
     # num=int(num)
     # all_number.append(num)
     
     
     
dict_3=citiys.copy()         
pprint.pprint(citiys)
x=Nmaxelements(dict_3)
print(x)




# list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
# N = 2



              
# read_file(file_name)    
# print(citiys)        

# https://maps.googleapis.com/maps/api/distancematrix/json?key=AIzaSyAK4CvVbEg_IU2dU2juIhKUdV8_ELkQfoE&origins=tel+aviv&destinations=jerusalem|rishon+lezion|eilat


# ef revword(word:str) -> str:
#     answer=word[::-1]
#     return(answer.lower())
    
# def countword()->int:
#     matala=open('text.txt')
#     word=matala.readline()
#     word=word.rstrip()
#     word=word.lower()
#     cunter=1
#     for l in matala:
#         line=l.split()
#         for w in line:
#             if revword(w)==word:
#                 cunter+= 1
#     return(cunter)           
                
            
        
    
        
        
        
        # messages = get_messages(lines)
        # metadata = get_metadata(lines)
        # file.close()
        # return {"messages": messages, "metadata": metadata}



 # def main():
#     cities_in_string = convert_file_to_string(file_name)
#     distances_url = "https://aksdjflkjsadlkf/destion=tel+aviv?" + cities_in_string
#     json_distances = send_request_for_google(url)
#     lines_url = ""
#     json_lines = ""
#     dist_dict = convert_data_to_dict(json_distances, json_lines)

# file_name=('dests.txt')

# def read_file(file_name):
#     with open(file_name, "r", encoding="utf8") as file:
#         global citiys
#         citiys={}
#         line = file.readlines()
#         for line in line:
#             print(line)
            
#             url="https://maps.googleapis.com/maps/api/distancematrix/json?key=AIzaSyAK4CvVbEg_IU2dU2juIhKUdV8_ELkQfoE&origins=tel+aviv&destinations=line" 
#             response = requests.get(url).json() 
#             response = requests.get(url)
#             print(response.status_code)
#             #print(response.content.decode('utf-8'))
#             res = response.content.decode('utf-8')
#             if line not in citiys:
#               # citiys[line] = 1  צריכה פה להכניס את הטפלים של כל אחד.
        
 
 

# def read_file(file_name):
    
#     file_name=('dests.txt')    
#         with open(file_name, "r", encoding="utf8") as file:
#             global citiys
#             citiys={}
            
