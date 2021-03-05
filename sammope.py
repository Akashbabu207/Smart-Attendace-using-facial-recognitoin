import tkinter as tk
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from PIL import ImageTk, Image
 
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.ard_stat = read_json(JSON_PATH)
        self.switch_frame(StartPage)
 
    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
 
 
class StartPage(tk.Frame):
    def loopCap(self):
        with open(JSON_PATH) as json_file1:
            self.data = json.load(json_file1)
            #print(self.data)
        if self.data['status'] == 'ACTIVE': #and (self.data['RH_img']!= 'null' or self.data['LH_img']!= 'null')
            a = self.text.set(self.data['status'])
            b = self.text1.set(self.data['RH_cnt'])
            c = self.text2.set(self.data['LH_cnt'])
            d = self.text3.set(self.data['barcode'])
            return self.text, self.text1, self.text2, self.text3, self.data
 
    def next_save(self):
        new_string = self.data['barcode']
        new_folder = os.path.join(DATA_PATH,new_string)
        if os.path.exists(new_folder):
            #print("Folder Already Exists If Condition")
            tk.messagebox.showinfo("Info", "Folder Already Exists")
        else:
            #os.isfile(new_string)
            #print("Folder Already Exists")
            #tkMessageBox.showinfo("Info", "Folder Already Exists")
            #print("Make Directory Else Condition")
            json_dict = read_json(JSON_PATH)
            json_dict.update({"frontend_status": "True"})
            dump_to_json(json_dict, JSON_PATH)
            os.mkdir(new_folder)
            for i in range(0,len(data)):
                folder_name = os.path.join(DATA_PATH, new_string, data[i])
                os.mkdir(folder_name)
                files = [('All Files', '*.*'),
                         ('Python Files', '*.py'),
                         ('Text Document', '*.txt')]
                file = asksaveasfile(initialdir=folder_name, filetypes=files, defaultextension=files)
            json_dict = read_json(JSON_PATH)
            json_dict.update({"frontend_status": "False"})
            dump_to_json(json_dict, JSON_PATH)
 
            self.master.after(500, self.loopCap)
 
    def __init__(self, master):
        super().__init__(master)
        self.master.geometry("1000x700+%d+%d" % (((self.master.winfo_screenwidth() / 2.) - (1280 / 2.)), ((self.master.winfo_screenheight() / 2.) - (720 / 2.))))
        #self.master.state('zoomed')
        self.master.config(bg='powder blue')
        #myvar = self.master
        Frame1 = tk.Frame(self.master)
        Frame1.pack(side="bottom", fill="x", pady=10, anchor='w')
        Frame2 = tk.Frame(self.master)
        Frame2.pack(side="left", fill="both", pady=10, anchor='w', expand=True )
        photo = tk.PhotoImage(file="images/BG.jpg")
        label = tk.Label(Frame2, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        tk.Label(Frame2, text='  Decal Check  ', font=('arial', 25, 'bold'), bg='powder blue',
                 fg='black', anchor='w').grid(column=0,pady=2)
 
        b = tk.Button(Frame2, text="Add New Files", command= self.next_save)
        b.grid(row=11, column=1, pady=5, sticky='w')
 
        self.master.after(500, self.loopCap)
 
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
