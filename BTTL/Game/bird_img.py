try:                        # In order to be able to import tkinter for
    import tkinter as tk    # either in python 2 or in python 3
except ImportError:
    import tkinter as tk


def download_images():
    # In order to fetch the image online
    try:
        import urllib.request as url
    except ImportError:
        import urllib as url
    url.urlretrieve("https://i.stack.imgur.com/57uJJ.gif", "13.gif")
    url.urlretrieve("https://i.stack.imgur.com/8LThi.gif", "8.gif")


def animate_and_move(i):
    i = (i + 1) % 2
    canvas.itemconfig(moving_image, image=canvas.images[i])
    canvas.move(moving_image, 1, 1)
    canvas.after(100, animate_and_move, i)


if __name__ == '__main__':
    download_images() # comment out after initial run
    root = tk.Tk()
    canvas = tk.Canvas(root, height=644, width=644, bg='#ffffff')
    canvas.images = list()
    canvas.images.append(tk.PhotoImage(file="bird1.png"))
    canvas.images.append(tk.PhotoImage(file="bird2.png"))
    moving_image = canvas.create_image((50, 50), image=canvas.images[0])
    animate_and_move(0)
    canvas.pack()
    root.mainloop()