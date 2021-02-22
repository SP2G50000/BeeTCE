import sys, os, subprocess
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow
from PySide6.QtCore import QFile, QIODevice
from ui_form import Ui_MainWindow
compile_radial_option = 0
vrad_option = "-fast"
#Sets up the configuration file.
import configparser
config = configparser.ConfigParser()
try:
    config.read('config.ini')
    p2_config = config["SETTINGS"]["Portal2FilePath"]
    p2ce_config = config["SETTINGS"]["P2CEFilePath"]
    vmf_config = config["SETTINGS"]["VMFFilePath"]
    print("Config file detected. Settings Applied.")
except:
    if not config.has_section("SETTINGS"):
        config.add_section("SETTINGS")
        config.set("SETTINGS", "Portal2FilePath", "")
        config.set("SETTINGS", "P2CEFilePath", "")
        config.set("SETTINGS", "VMFFilePath", "")
        with open("config.ini", 'w') as configfile:
            config.write(configfile)
        print("Created new config file.")
        p2_config = config["SETTINGS"]["Portal2FilePath"]
        p2ce_config = config["SETTINGS"]["P2CEFilePath"]
        vmf_config = config["SETTINGS"]["VMFFilePath"]

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.speedrun_toggle.setToolTip("This feature is not ready.")
        self.ui.p2ce_lineEdit.setReadOnly(True)
        self.ui.vmf_lineEdit.setReadOnly(True)
        self.ui.p2_lineEdit.setReadOnly(True)
        self.ui.compile_button.setDisabled(True)
        self.ui.p2_browse.clicked.connect(self.p2_browse_function)
        self.ui.p2ce_browse.clicked.connect(self.p2ce_browse_function)
        self.ui.vmf_browse.clicked.connect(self.vmf_browse_function)
        self.ui.setting_fast.clicked.connect(self.radial_button_function_fast)
        self.ui.setting_full.clicked.connect(self.radial_button_function_full)
        self.ui.setting_fast_fullbright.clicked.connect(self.radial_button_function_fullbright)
        self.ui.compile_button.clicked.connect(self.compile_function)
        self.p2_picked = 0
        self.p2ce_picked = 0
        self.vmf_picked = 0
        self.radial_button_picked = 0
        global p2_config
        global p2ce_config
        global vmf_config
        self.ui.p2_lineEdit.setText(p2_config)
        self.ui.p2ce_lineEdit.setText(p2ce_config)
        self.ui.vmf_lineEdit.setText(vmf_config)
    
    @QtCore.Slot() #This is where most of the UI functions go.
    def p2_browse_function(self): #This function is currently unused.
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            p2_fileNames = dialog.selectedFiles()
            p2_fileNames = "".join(str(x) for x in p2_fileNames)
            global config
            config.set("SETTINGS", "Portal2FilePath", p2_fileNames)
            with open("config.ini", 'w') as configfile:
                config.write(configfile)
            print("You picked",p2_fileNames)
            self.ui.p2_lineEdit.setText(p2_fileNames)
        self.p2_picked = 1
        self.compile_enable_function()
    def p2ce_browse_function(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.p2ce_fileNames = dialog.selectedFiles()
            self.p2ce_fileNames = "".join(str(x) for x in self.p2ce_fileNames)
            global config
            config.set("SETTINGS", "P2CEFilePath", self.p2ce_fileNames)
            with open("config.ini", 'w') as configfile:
                config.write(configfile)
            print("You picked",self.p2ce_fileNames)
            self.ui.p2ce_lineEdit.setText(self.p2ce_fileNames)
            self.p2ce_picked = 1
            self.compile_enable_function()
    def vmf_browse_function(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilter("Valve Map File (*.vmf)")
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.vmf_fileNames = dialog.selectedFiles()
            self.vmf_fileNames = "".join(str(x) for x in self.vmf_fileNames)
            global config
            config.set("SETTINGS", "VMFFilePath", self.vmf_fileNames)
            with open("config.ini", 'w') as configfile:
                config.write(configfile)
            print("You picked",self.vmf_fileNames)
            self.ui.vmf_lineEdit.setText(self.vmf_fileNames)
            self.vmf_picked = 1
            self.compile_enable_function()
    def radial_button_function_fast(self):
        global compile_radial_option
        compile_radial_option = 0
        self.radial_button_function()
    def radial_button_function_full(self):
        global compile_radial_option
        compile_radial_option = 1
        self.radial_button_function()
    def radial_button_function_fullbright(self):
        global compile_radial_option
        compile_radial_option = 2
        self.radial_button_function()
    def radial_button_function(self):
        self.radial_button_picked = 1
        self.compile_enable_function()
    def compile_enable_function(self):
        if self.p2_picked == 1:
            if self.p2ce_picked == 1:
                if self.vmf_picked == 1:
                    if self.radial_button_picked == 1:
                        self.ui.compile_button.setDisabled(False)
#This is where the program calls the P2:CE Compiler. As P2:CE is not out yet, it currently calls the Portal 2 Compiler.
    def compile_function(self):
        home_dir = os.getcwd()
        os.chdir(self.p2ce_fileNames) #This needs to be replaced with self.p2ce_fileNames later.
        vbsp_path = os.getcwd(),"\\bin\\vbsp.exe"
        vbsp_path = "".join(str(x) for x in vbsp_path)
        vbsp_args = os.getcwd(),"\\portal2"
        vbsp_args = "".join(str(x) for x in vbsp_args)
        vbsp_map = self.ui.vmf_lineEdit.text() #This is where the compiler finds the VMF.
        vproject_map = os.getcwd,"\\sdk_content\\maps"
        vproject_map = "".join(str(x) for x in vproject_map)
        vbsp_args = "".join(str(x) for x in vbsp_args)
        compiler_path = home_dir,"\\compiler.py" #This is unused.
        compiler_path = "".join(str(x) for x in compiler_path)
        self.ui.compile_button.setDisabled(True)
        subprocess.call([vbsp_path, "-game", vbsp_args, vbsp_map], shell=True, cwd=None)
        print("***\nVBSP has finished! Loading VVIS...\n***")
        vvis_path = os.getcwd(),"\\bin\\vvis.exe"
        vvis_path = "".join(str(x) for x in vvis_path)
        bsp_map = vbsp_map[:-4]
        subprocess.call([vvis_path, "-game", vbsp_args, bsp_map], shell=True, cwd=None)
        vrad_path = os.getcwd(),"\\bin\\vrad.exe"
        vrad_path = "".join(str(x) for x in vrad_path)
        global compile_radial_option
        global vrad_option
        if not compile_radial_option == 2:
            if compile_radial_option == 0:
                vrad_option = "-fast"
                print("\n***\nVVIS has finished!\nLoading VRAD (Fast Compile)...\n***")
                subprocess.call([vrad_path, "-fast", "-game", vbsp_args, bsp_map], shell=True, cwd=None)
            elif compile_radial_option == 1:
                vrad_option = "-textureshadows","-hdr","-StaticPropLighting","-StaticPropPolys"
                vrad_option = " ".join(str(x) for x in vrad_option)
                print("\n***\nVVIS has finished!\nLoading VRAD (Full Compile)...\n***")
                subprocess.call([vrad_path, "-textureshadows", "-hdr", "-StaticPropLighting", "-StaticPropPolys", "-game", vbsp_args, bsp_map], shell=True, cwd=None)
            print("***\nVRAD has finished!\n***")
        else:
            print("***\nVVIS has finished!\nThe fullbright option was selected. Skipping VRAD...\n***")
        print("Map has been compiled!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())