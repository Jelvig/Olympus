  class files:
    def file_list():
        from tkinter import filedialog
        import glob

        file_loc = filedialog.askdirectory(title="Choose Working Folder", initialdir=r'W:\Production\Probe Oligos\REMP Files\_Re-Rack Files')
        files = glob.glob(file_loc+"/*_opf.csv")

        return file_loc, files
