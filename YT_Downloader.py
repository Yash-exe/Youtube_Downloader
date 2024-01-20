import tkinter 
import customtkinter
from pytube import YouTube

def start_downloading():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback = on_progress)         
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color = "white")
        title2.configure(text=f"Views: {ytObject.views}", text_color = "white")
        
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Sucessfully Downloaded")
    except:
        finishLabel.configure(text = "Download Error", text_color = "red")
        
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    complete_percent = bytes_downloaded / total_size * 100
    per = str(int(complete_percent))
    Ppercent.configure(text = per + "%")
    Ppercent.update()
    
    # Update Progressbar
    progress_bar.set(float(complete_percent)/100)
    
    
#System Settings
customtkinter.set_appearance_mode ("System")
customtkinter.set_default_color_theme("blue")

#app frame 
app =  customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Dowloader")

#UI
title = customtkinter.CTkLabel(app, text = "Insert a Youtube Link")
title.pack(padx =10, pady =10)

title2 = customtkinter.CTkLabel(app, text = "", text_color = "white")
title2.pack(pady =(0,10))

#link input
URL = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable = URL)
link.pack(pady= 10)

#finished downloading
finishLabel = customtkinter.CTkLabel(app, text = "")
finishLabel.pack()



#progress percentage
Ppercent = customtkinter.CTkLabel(app, text = "0%")
Ppercent.pack()

progress_bar = customtkinter.CTkProgressBar(app, width = 400)
progress_bar.set(0)
progress_bar.pack(padx = (10,0))

#Download Button
download = customtkinter.CTkButton(app, text = "Download", command = start_downloading)
download.pack(padx = (10,0), pady = (50,0))

app.mainloop()
