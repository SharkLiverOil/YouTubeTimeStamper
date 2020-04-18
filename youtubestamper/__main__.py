from youtubestamper.YouTubeTimeStamperGUI import YouTubeTimeStamper
import tkinter as tk


def main():
    root = tk.Tk()
    root.wm_title('YouTube Time Stamper')
    YouTubeTimeStamper(root)
    root.mainloop()


if __name__ == '__main__':
    main()
