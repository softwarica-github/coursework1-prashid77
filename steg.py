from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from io import BytesIO
import os

class ImageSteganographyApp:

    MATRIX_FONT = 'Matrix Code NFI'

    def __init__(self, root):
        self.root = root
        root.title('Image Steganography')
        root.geometry('{0}x{1}'.format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Set to full-screen
        root.resizable(width=False, height=False)
        root.config(bg='#000000')  # Set background color to black
        self.output_image_size = 0
        self.create_main_frame()

    # Method to create the main frame of the application
    def create_main_frame(self):
        f = Frame(self.root, bg='#000000')

        title = Label(f, text='Image Steganography', bg='#000000', fg='#00FF00')
        title.config(font=(self.MATRIX_FONT, 20))
        title.grid(pady=10)

        encode_button = Button(f, text="Encode", command=self.frame1_encode, padx=14, bg='#000000', fg='#00FF00')
        encode_button.config(font=(self.MATRIX_FONT, 14))
        decode_button = Button(f, text="Decode", padx=14, command=self.frame1_decode, bg='#000000', fg='#00FF00')
        decode_button.config(font=(self.MATRIX_FONT, 14))
        decode_button.grid(pady=12)

        ascii_art_label = Label(f, text=self.get_ascii_art(), bg='#000000', fg='#00FF00')
        ascii_art_label.config(font=(self.MATRIX_FONT, 12))

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1, pady=5)
        encode_button.grid(row=2)
        decode_button.grid(row=3)
        ascii_art_label.grid(row=4, pady=10)

    # ASCII art for the title
    def get_ascii_art(self):
        return r'''
         _______ _                 _     _             
        |__   __| |               | |   | |            
           | |  | |__   __ _ _ __ | |__ | |_   _  ___ 
           | |  | '_ \ / _` | '_ \| '  \| | | | |/ _ \
        '''

    # Method to go back to the main frame
    def home(self):
        self.destroy_current_frame()
        self.create_main_frame()

    # Frame for decoding
    def frame1_decode(self):
        self.destroy_current_frame()
        d_frame = Frame(self.root, bg='#2C3E50')

        label_art = Label(d_frame, text='٩(^‿^)۶', bg='#2C3E50', fg='#E74C3C')
        label_art.config(font=('Matrix Code NFI', 30))  # Use Matrix-style font
        label_art.grid(row=1, pady=20)

        l1 = Label(d_frame, text='Select Image with Hidden text:', bg='#2C3E50', fg='#ECF0F1')
        l1.config(font=('Matrix Code NFI', 12))  # Use Matrix-style font
        l1.grid()

        browse_button = Button(d_frame, text='Select', command=self.frame2_decode, bg='#3498DB', fg='white')
        browse_button.config(font=('Matrix Code NFI', 12))  # Use Matrix-style font
        browse_button.grid()

        back_button = Button(d_frame, text='Cancel', command=self.home, bg='#3498DB', fg='white')
        back_button.config(font=('Matrix Code NFI', 12))  # Use Matrix-style font
        back_button.grid(pady=10)

        d_frame.grid()

    # Frame for selecting image to decode
    def frame2_decode(self):
        d_frame = Frame(self.root, bg='#2C3E50')
        myfile = tkinter.filedialog.askopenfilename(filetypes=[('Image Files', '*.png; *.jpeg; *.jpg; *.gif; *.bmp')])
        
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((400, 300))  # Adjusted the image size
            img = ImageTk.PhotoImage(myimage)

            l4 = Label(d_frame, text='Selected Image :', bg='#2C3E50', fg='#ECF0F1')
            l4.config(font=('Matrix Code NFI', 12))  # Use Matrix-style font
            l4.grid()

            panel = Label(d_frame, image=img)
            panel.image = img
            panel.grid()

            hidden_data = self.decode(myimg)

            l2 = Label(d_frame, text='Hidden data is :', bg='#2C3E50', fg='#ECF0F1')
            l2.config(font=('Matrix Code NFI', 12))  # Use Matrix-style font
            l2.grid(pady=5)

            text_scroll = Scrollbar(d_frame, orient=VERTICAL)
            text_area = Text(d_frame, width=40, height=8, bg='#ECF0F1', yscrollcommand=text_scroll.set)
            text_area.insert(INSERT, hidden_data)
            text_area.configure(state='disabled')
            text_scroll.config(command=text_area.yview)

            text_scroll.grid(row=5, column=1, sticky='ns')
            text_area.grid(row=5, column=0)

            back_button = Button(d_frame, text='Cancel', command=self.home, bg='#3498DB', fg='white')
            back_button.config(font=('Matrix Code NFI', 11))  # Use Matrix-style font
            back_button.grid(pady=10)

            show_info = Button(d_frame, text='More Info', command=self.info, bg='#3498DB', fg='white')
            show_info.config(font=('Matrix Code NFI', 11))  # Use Matrix-style font
            show_info.grid(pady=5)

            d_frame.grid(row=1)

    # Frame for encoding
    def frame1_encode(self):
        self.destroy_current_frame()
        e_frame = Frame(self.root, bg='#2C3E50')

        label_art = Label(e_frame, text='\'\(°Ω°)/\'', bg='#2C3E50', fg='#E74C3C')
        label_art.config(font=('Matrix Code NFI', 30))  # Use Matrix-style font
        label_art.grid(row=1, pady=20)

        l1 = Label(e_frame, text='Select the Image in which \nyou want to hide text :', bg='#2C3E50', fg='#ECF0F1')
        l1.config(font=('Matrix Code NFI', 12))  # Use Matrix-style font
        l1.grid()

        browse_button = Button(e_frame, text='Select', command=self.frame2_encode, bg='#3498DB', fg='white')
        browse_button.config(font=('Matrix Code NFI', 12))  # Use Matrix-style font
        browse_button.grid()

        back_button = Button(e_frame, text='Cancel', command=self.home, bg='#3498DB', fg='white')
        back_button.config(font=('Matrix Code NFI', 12))  # Use Matrix-style font
        back_button.grid(pady=10)

        e_frame.grid()

    # Frame for selecting image to encode
    def frame2_encode(self):
        e_frame = Frame(self.root, bg='#2C3E50')
        myfile = tkinter.filedialog.askopenfilename(filetypes=[('Image Files', '*.png; *.jpeg; *.jpg; *.gif; *.bmp')])

        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((400, 300))  # Adjusted the image size
            img = ImageTk.PhotoImage(myimage)

            l3 = Label(e_frame, text='Selected Image', bg='#2C3E50', fg='#ECF0F1')
            l3.config(font=('Matrix Code NFI', 12))  # Use Matrix-style font
            l3.grid()

            panel = Label(e_frame, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()

            l2 = Label(e_frame, text='Enter the message', bg='#2C3E50', fg='#ECF0F1')
            l2.config(font=('Matrix Code NFI', 12))  # Use Matrix-style font
            l2.grid(pady=5)

            text_scroll = Scrollbar(e_frame, orient=VERTICAL)
            text_area = Text(e_frame, width=40, height=8, bg='#ECF0F1', yscrollcommand=text_scroll.set)
            text_scroll.config(command=text_area.yview)

            encode_button = Button(e_frame, text='Cancel', command=self.home, bg='#3498DB', fg='white')
            encode_button.config(font=('Matrix Code NFI', 11))  # Use Matrix-style font
            data = text_area.get("1.0", "end-1c")
            back_button = Button(e_frame, text='Encode', command=lambda: [self.enc_fun(text_area, myimg), self.home()],
                                 bg='#3498DB', fg='white')
            back_button.config(font=('Matrix Code NFI', 11))  # Use Matrix-style font

            text_scroll.grid(row=5, column=1, sticky='ns')
            text_area.grid(row=5, column=0)
            encode_button.grid(pady=10)
            back_button.grid(pady=10)

            e_frame.grid(row=1)

    # Method to show information about images
    def info(self):
        try:
            str_info = 'Original Image:\nSize: {} MB\nWidth: {}\nHeight: {}\n\n' \
                       'Decoded Image:\nSize: {} MB\nWidth: {}\nHeight: {}'.format(
                           self.output_image_size.st_size / (1024 * 1024),
                           self.o_image_w, self.o_image_h,
                           self.d_image_size / (1024 * 1024),
                           self.d_image_w, self.d_image_h)
            messagebox.showinfo('Info', str_info)
        except Exception as e:
            messagebox.showinfo('Info', 'Unable to get the information')

    # Method to generate binary data from text
    def gen_data(self, data):
        new_data = [format(ord(i), '08b') for i in data]
        return new_data

    # Method to modify pixels for encoding
    def mod_pix(self, pix, data):
        data_list = self.gen_data(data)
        len_data = len(data_list)
        im_data = iter(pix)

        for i in range(len_data):
            pix = [value for value in im_data.__next__()[:3] +
                   im_data.__next__()[:3] +
                   im_data.__next__()[:3]]

            for j in range(8):
                if (data_list[i][j] == '0') and (pix[j] % 2 != 0):
                    pix[j] -= 1
                elif (data_list[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1

            if i == len_data - 1:
                if pix[-1] % 2 == 0:
                    pix[-1] -= 1
            else:
                if pix[-1] % 2 != 0:
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    # Method to encode data into image
    def encode_enc(self, new_img, data):
        w = new_img.size[0]
        (x, y) = (0, 0)

        for pixel in self.mod_pix(new_img.getdata(), data):
            new_img.putpixel((x, y), pixel)
            if x == w - 1:
                x = 0
                y += 1
            else:
                x += 1

    # Method for encoding
    def enc_fun(self, text_area, my_img):
        data = text_area.get("1.0", "end-1c")
        if len(data) == 0:
            messagebox.showinfo("Alert", "Kindly enter text in TextBox")
        else:
            new_img = my_img.copy()
            self.encode_enc(new_img, data)
            my_file = BytesIO()
            temp = os.path.splitext(os.path.basename(my_img.filename))[0]
            new_img.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=[('PNG Files', '*.png')],
                                                               defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w, self.d_image_h = new_img.size
            messagebox.showinfo("Success", "Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")

    # Method for decoding hidden text from image
    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())

        while True:
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data

    # Method to destroy the current frame
    def destroy_current_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        

# Main program
root = Tk()
app = ImageSteganographyApp(root)
root.mainloop()
