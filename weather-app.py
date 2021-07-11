import tkinter as tk
from PIL import ImageTk, Image
import PIL
import requests
##display method is used to fetch the individual information like temperature,humidity etc.
def display(info):
    try:
        temp = info['main']['temp']# in celsius
        desc = info['weather'][0]['description']
        pressure = info['main']['pressure']
        humid = info['main']['humidity']
        wind_speed = info['wind']['speed']

        country_code = info['sys']['country']
        identity = info['id']
        #concating the details as one string
        final = 'ID :'+str(identity)+'\n'+'Country Code :'+str(country_code)+'\n'+'Temperature :'+str(temp)+'°C'+'\n'+'Description :'+str(desc).upper()+'\n'+'Pressure :'+str(pressure)+'hPa'+'\n'+'Humidity :'+str(humid)+'%'+'\n'+'Wind Speed :'+str(wind_speed)+'m/sec'+'\n'
    except:
        final = 'No results'
    return final
#getting the weather information through API
#we have used openweathermap API
def get_info(city):
        key = 'API_KEY'
        url = 'http://api.openweathermap.org/data/2.5/weather?'
        prms = {'appid': key,'q': city,'units':'metric'}
        response = requests.get(url,params=prms)
        info = response.json()
        print(info)
        label2['text'] = display(info)

#method to give on click event to the 'Get Weather' button on interface
def on_click(event):
    entry.configure(state='normal')
    entry.delete(0, 'end')
    entry.unbind('<Button-1>', on_click_id)

    
#desing section of the interface
root = tk.Tk()
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.title('Weather-Info')
root.configure(bg='#856ff8')

head=tk.Label(text='Weather Info',font=('Courier',16))
head.place(relx=0.43,rely=0.01)
frame = tk.Frame(root,bg='skyblue',bd=4)
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

img = ImageTk.PhotoImage(Image.open("weathers.jpg"))
head_img = tk.Label(frame,image=img)
head_img.place(x=0,y=0,relwidth=1,relheight=0.27,height=30,width=30)

entry=tk.Entry(frame,font=50)
entry.insert(0, "Enter City Name")
entry.configure(state='disabled')
on_click_id = entry.bind('<Button-1>', on_click)
entry.place(relx=0.01,rely=0.335,relwidth=0.98,relheight=0.05)


button = tk.Button(frame,text="Get Weather!",command = lambda:get_info(entry.get()))
button.place(relx=0.4,rely=0.4,relwidth=0.2,relheight=0.05)


frame2 = tk.Frame(root,bg='#00ffff',bd=6)
frame2.place(relx=0.1,rely=0.49,relwidth=0.8,relheight=0.43)


label2 = tk.Label(frame2,text='You will get your weather information here...',font=('Courier',14),justify='center',bd=4,bg='skyblue')
label2.place(relwidth=1,relheight=1)

root.mainloop()