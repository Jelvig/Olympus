class Files:
    def file_list(self):
        """By choosing the working folder, it gathers the master files, and location of folder"""
        from tkinter import filedialog
        import glob
        while True:
            file_loc = filedialog.askdirectory(title="Choose Working Folder", initialdir=r'W:\Production\Probe Oligos\REMP Files\_Re-Rack Files')
            files = list(glob.glob(file_loc+"/*_opf.csv"))
            files.reverse()

            if files != None:
                return file_loc, files
            else:
                print("No master files were found, Exiting program")
                exit()
