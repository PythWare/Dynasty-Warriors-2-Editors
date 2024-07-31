import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
import shutil
file2 = "DW2.bin"
itemsoffset = 0x160D7E10
unit_data = [0x160A27E8, 0x160A2A8B]
unit_names = [
    "0: Zhao Yun",
    "1: Guan Yu",
    "2: Zhang Fei",
    "3: Xiahou Dun",
    "4: Dian Wei",
    "5: Xu Zhu",
    "6: Zhou Yu",
    "7: Lu Xun",
    "8: Taishi Ci",
    "9: Diao Chan",
    "10: Zhuge Liang",
    "11: Cao Cao",
    "12: Lu Bu",
    "13: Sun Shang Xiang",
    "14: Liu Bei",
    "15: Sun Jian",
    "16: Sun Quan",
    "17: Dong Zhuo",
    "18: Yuan Shao",
    "19: Ma Chao",
    "20: Huang Zhong",
    "21: Xiahou Yuan",
    "22: Zhang Liao",
    "23: Sima Yi",
    "24: Lu Meng",
    "25: Gan Ning",
    "26: Jiang Wei",
    "27: Zhang Jiao",
    "28: Cao Ren",
    "29: Cheng Pu",
    "30: Huang Gai",
    "31: Han Dang",
    "32: Zhang Bao",
    "33: Zhang Liang",
    "34: Zhang Man Cheng",
    "35: Bo Zhang",
    "36: Cao Hong",
    "37: Yan Liang",
    "38: Wen Chou",
    "39: Zhang He",
    "40: Gongsun Zan",
    "41: Hua Xiong",
    "42: Xu Rong",
    "43: Gao Shun",
    "44: Li Ru",
    "45: Li Jue",
    "46: Jia Xu",
    "47: Guo Si",
    "48: Hu Zhen",
    "49: Xu Huang",
    "50: Yu Jin",
    "51: Chun Yuqiong",
    "52: Yue Jin",
    "53: Li Dian",
    "54: Xiahou En",
    "55: Cheng Yu",
    "56: Xun You",
    "57: Zhou Tai",
    "58: Ling Tong",
    "59: Xu Sheng",
    "60: Ding Feng",
    "61: Pang De",
    "62: Huang Quan",
    "63: Guan Xing",
    "64: Zhang Bao",
    "65: Shamoke",
    "66: Deng Ai",
    "67: Zhong Hui",
    "68: Wei Yan",
    "69: Ma Dai",
    "70: Guan Suo",
    "71: Yuan Tan",
    "72: Yuan Xi",
    "73: Yuan Shang",
    "74: Ju Shou",
    "75: Gao Lan",
    "76: Zhao Cen",
    "77: Niou Fu",
    "78: Fan Chou",
    "79: Wang Fang",
    "80: Li Meng",
    "81: He Jin",
    "82: Zhu Yun",
    "83: Lu Zhi",
    "84: Huangfu Song",
    "85: Zhang Chao",
    "86: Liu Yan",
    "87: Zou Ying",
    "88: Cheng Yuanzhi",
    "89: Deng Mao",
    "90: Guan Hai",
    "91: Pei Yuan Shao",
    "92: He Yi",
    "93: Yan Zheng",
    "94: Gao Sheng",
    "95: Liu Yan",
    "96: Song Xian",
    "97: Wei Xu",
    "98: Dong Xi",
    "99: Lu Wei Kuang",
    "100: Xun Chen",
    "101: Han Meng",
    "102: Han Xun",
    "103: Zhou Cang",
    "104: Guan Ping",
    "105: Sun Qian",
    "106: Mi Zhu",
    "107: Mi Fang",
    "108: Liu Feng",
    "109: Chen Dao",
    "110: Liao Hua",
    "111: Liu Qi",
    "112: Cao Pi",
    "113: Cao Zhang",
    "114: Zhu Huan",
    "115: Zhu Ran",
    "116: Jiang Qin",
    "117: Dong Xi",
    "118: Pan Zhang",
    "119: Yan Yan",
    "120: Wu Lan",
    "121: Lei Tong",
    "122: Zhang Ji",
    "123: Zhu Ran",
    "124: Jiang Qin",
    "125: Dong Xi",
    "126: Pan Zhang",
    "127: Yan Yan",
    "128: Private (Wei - sword)",
    "129: Corporal(Sergeant) (Wei - sword)",
    "130: Sergeant(Major) (Wei - sword)",
    "131: Private (Wei - spear)",
    "132: Sergeant (Wei - spear)",
    "133: Major (Wei - spear)",
    "134: Corporal(Private) (Wei - pike)",
    "135: Sergeant (Wei - pike)",
    "136: Major (Wei - pike)",
    "137: Guard (Wei - sword)",
    "138: Guard Captain (Wei - sword)",
    "139: Guard (Wei - spear)",
    "140: Guard Captain (Wei - spear)",
    "141: Guard (Wei - pike)",
    "142: Guard Captain (Wei - pike)",
    "143: Bowman (Wei)",
    "144: First bow (Wei)",
    "145: Crossbow (Wei)",
    "146: First Crossbow (Wei)",
    "147: Gate Guard (Wei)",
    "148: Gate Captain (Wei)",
    "149: Private (Wu - sword)",
    "150: Sergeant (Wu - sword)",
    "151: Major (Wu - sword)",
    "152: Private (Wu - spear)",
    "153: Sergeant (Wu - spear)",
    "154: Major (Wu - spear)",
    "155: Private (Wu - pike)",
    "156: Sergeant (Wu - pike)",
    "157: Major (Wu - pike)",
    "158: Guard (Wu - sword)",
    "159: Guard Captain (Wu - sword)",
    "160: Guard (Wu - spear)",
    "161: Guard Captain (Wu - spear)",
    "162: Guard (Wu - pike)",
    "163: Guard Captain (Wu - pike)",
    "164: Bowman (Wu)",
    "165: First Bow (Wu)",
    "166: Crossbow (Wu)",
    "167: F.Crossbow (Wu)",
    "168: Gate guard (Wu)",
    "169: Gate Captain (Wu)",
    "170: Private (Shu - sword)",
    "171: Sergeant (Shu - sword)",
    "172: Major (Shu - sword)",
    "173: Private (Shu - spear)",
    "174: Sergeant (Shu - spear)",
    "175: Major (Shu - spear)",
    "176: Private (Shu - pike)",
    "177: Sergeant (Shu - pike)",
    "178: Major (Shu - pike)",
    "179: Guard (Shu - sword)",
    "180: Guard Captain (Shu - sword)",
    "181: Guard (Shu - spear)",
    "182: G.Captain (Shu - spear)",
    "183: Guard (Shu - pike)",
    "184: G.Captain (Shu - pike)",
    "185: Bowman (Shu)",
    "186: First Bow (Shu)",
    "187: Crossbow (Shu)",
    "188: First Crossbow (Shu)",
    "189: G.guard (Shu)",
    "190: Gate Captain (Shu)",
    "191: Private (YS - sword)",
    "192: Sergeant (YS - sword)",
    "193: Major (YS - sword)",
    "194: Private (YS - spear)",
    "195: Sergeant (YS - spear)",
    "196: Major (YS - spear)?",
    "197: Private (YS - pike)?",
    "198: Sergeant (YS - pike)?",
    "199: Major (YS - pike)?",
    "200: Guard (YS - sword)",
    "201: G.Captain (YS - sword)",
    "202: Guard (YS - spear)",
    "203: G.Captain (YS - spear)",
    "204: Guard (YS - pike)",
    "205: G.Captain (YS - pike)",
    "206: Bowman (YS)",
    "207: First Bow (YS)",
    "208: Crossbow (YS)",
    "209: Catapult Chief (YS)",
    "210: Gate Guard (YS)",
    "211: G.Captain (YS)",
    "212: Private (Purple - sword)",
    "213: Sergeant (Purple - sword)?",
    "214: Major (Purple - sword)?",
    "215: Private (Purple - spear)?",
    "216: Sergeant (Purple - spear)?",
    "217: Major (Purple - spear)?",
    "218: Private (Purple - pike)?",
    "219: Sergeant (Purple - pike)?",
    "220: Major (Purple - pike)",
    "221: Guard (Purple - sword)",
    "222: G.captain (Purple - sword)",
    "223: Guard (Purple - spear)?",
    "224: G.Captain (Purple - spear)?",
    "225: Guard (Purple - pike)?",
    "226: G.Captain (Purple - pike)",
    "227: Bowman (Purple)",
    "228: First Bow (Purple)?",
    "229: Crossbow (Purple)?",
    "230: First Crossbow (Purple)",
    "231: Gate Guard (Purple)",
    "232: G.Captain (Purple)",
    "233: Trooper (YT - sword)",
    "234: Trooper (YT - spear)",
    "235: Trooper (YT - pike)",
    "236: Captain (YT - sword)",
    "237: Captain (YT - spear)",
    "238: Captain (YT - pike)",
    "239: General (YT - sword)",
    "240: General (YT - spear)",
    "241: General (YT - pike)",
    "242: Bowman (YT)",
    "243: First bow (YT)",
    "244: Bowman (YT)",
    "245: First Bow (YT)",
    "246: Gate guard (YT)",
    "247: Gate Captain (YT)",
    "248: Lady Guard",
    "249: Lady Guard",
    "250: Lady Guard",
    "251: Lady Captain",
    "252: Lady Bowman",
    "253: First Lady Bow",
    "254: Bodyguard",
]
# offsets to obtain stage data
stage_data = [
    [0x24DD6DD8, 0x24DD7708, 0x24DD8038, 0x24DD8968, 0x24DD9298, 0x24DD9BC8, 0x24DDA4F8, 0x24DDAE28],
    [0x24DDF7A8, 0x24DE00D8, 0x24DE0A08, 0x24DE1338, 0x24DE1C68, 0x24DE2598, 0x24DE2EC8, 0x24DE37F8],
    [0x24DE8178, 0x24DE8AA8, 0x24DE93D8, 0x24DE9D08, 0x24DEA638, 0x24DEAF68, 0x24DEB898, 0x24DEC1C8],
    [0x24DF0B48, 0x24DF1478, 0x24DF1DA8, 0x24DF26D8, 0x24DF3008, 0x24DF3938, 0x24DF4268, 0x24DF4B98],
    [0x24DF9518, 0x24DF9E48, 0x24DFA778, 0x24DFB0A8, 0x24DFB9D8, 0x24DFC308, 0x24DFCC38, 0x24DFD568],
    [0x24E01EE8, 0x24E02818, 0x24E03148, 0x24E03A78, 0x24E043A8, 0x24E04CD8, 0x24E05608, 0x24E05F38],
    [0x24E0A8B8, 0x24E0B1E8, 0x24E0BB18, 0x24E0C448, 0x24E0CD78, 0x24E0D6A8, 0x24E0DFD8, 0x24E0E908],
    [0x24E13288, 0x24E13BB8, 0x24E144E8, 0x24E14E18, 0x24E15748, 0x24E16078, 0x24E169A8, 0x24E172D8]
    ] # 8 stages so 8 lists within the main list

filenames = ["YTR_Stage.ref", "HLG_Stage.ref", "GD_Stage.ref", "CBan_Stage.ref", "CBi_Stage.ref", "HF_Stage.ref", "YL_Stage.ref", "WZP_Stage.ref"] # filenames to create for each list in the main list
filenames2 = [filename.replace(".ref", ".data") for filename in filenames]
stage_extension = [".DW2YTR", ".DW2HLG", ".DW2GD", ".DW2CBan", ".DW2CBi", ".DW2HF", ".DW2YL", ".DW2WZP"]
dw2_mod = ".DW2UnitMod"
unit_file = "DW2unit.2data"
unit_ref_file = "DW2unit.ref"
folds = ["DW2(Stage_Data)", "DW2(Stage_Ref)", "Backups_For_Mod_Disabling", "DW2(unit)", "backgrounds", "Icon_Files"]

def rem(files1, files2, files3, files4): # everytime the script is ran delete the old files to create fresh unmodified versions
    for a in files1:
        filepath1 = os.path.join(folds[1], a)
        if os.path.isfile(filepath1):
            os.remove(filepath1)
    for b in files2:
        filepath2 = os.path.join(folds[0], b)
        if os.path.isfile(filepath2):
            os.remove(filepath2)
    filepath3 = os.path.join(folds[3], files3)
    if os.path.isfile(filepath3):
        os.remove(filepath3)
    filepath4 = os.path.join(folds[3], files4)
    if os.path.isfile(filepath4):
        os.remove(filepath4)
class TheCheck:
    @staticmethod
    def validate_numeric_input(new_value):
        return new_value == "" or (new_value.replace(".", "", 1).isdigit() and '.' not in new_value and float(new_value) >= 0)
def check_backup1(): # Create backups of the .data files
    for file in filenames2: # .data filename list
        try_file = os.path.join(folds[0], file)
        backup_file = os.path.join(folds[2], file)
        if not os.path.exists(backup_file):
            shutil.copy(try_file, backup_file)
        else:
            pass
def check_backup2(): # create backups of .ref files
    for ofile in filenames: # .ref filename list
        otry_file = os.path.join(folds[1], ofile)
        obackup_file = os.path.join(folds[2], ofile)
        if not os.path.exists(obackup_file):
            shutil.copy(otry_file, obackup_file)
        else:
            pass
class MainEditor: # the main screen
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dynasty Warriors Modding Editors")
        self.root.iconbitmap(os.path.join(folds[5], "icon3.ico"))
        self.root.minsize(500, 500)
        self.root.resizable(False, False)
        self.lab4 = tk.Label(self.root, text="Credit goes to Michael, Passion Wagon, Auriv, and The Tempest for documentation for DW2.")
        self.lab4.place(x=0, y=200)
        self.editor_button = tk.Button(self.root, text="Dynasty Warriors 2 Modding Editors", command=self.open_modding_editor)
        self.editor_button.place(x=10, y=40)
    def open_modding_editor(self):
        self.root.destroy()
        modding_editor = ModdingEditor()

    def run(self):
        self.root.mainloop()
class DW2ModManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DW2 Mod Manager")
        self.root.iconbitmap(os.path.join(folds[5], "icon3.ico"))
        self.root.minsize(400, 400)
        self.root.resizable(False, False,)
        tk.Button(self.root, text="Stage Mods", command=self.dw2_stage_mods, height=10, width=50).place(x=10, y=10)
        tk.Button(self.root, text="Unit Mods", command=self.dw2_unit_mods, height=10, width=50).place(x=10, y=210)
    def dw2_stage_mods(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("DW2 Stage Mods")
        self.root.iconbitmap(os.path.join(folds[5], "icon1.ico"))
        self.root.minsize(400, 400)
        self.root.resizable(False, False)
        self.mod_status = tk.Label(self.root, text="", fg="green")
        self.mod_status.place(x=10, y=170)
        tk.Button(self.root, text="Enable Mod", command=self.ask_open_file, height=10, width=50).place(x=10, y=10)
        tk.Button(self.root, text="Disable Mod", command=self.ask_open_ofile, height=10, width=50).place(x=10, y=210)
    def dw2_unit_mods(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("DW2 Unit Mods")
        self.root.iconbitmap(os.path.join(folds[5], "icon2.ico"))
        self.root.minsize(400, 400)
        self.root.resizable(False, False)
        self.mod_status = tk.Label(self.root, text="", fg="green")
        self.mod_status.place(x=10, y=170)
        tk.Button(self.root, text="Enable Mod", command=self.ask_open_unit1, height=10, width=50).place(x=10, y=10)
        tk.Button(self.root, text="Disable Mod", command=self.ask_open_unit2, height=10, width=50).place(x=10, y=210)

    # for unit mods
    def ask_open_unit1(self): # This is for enabling the user selected mod
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select mod file",
            filetypes=(
                ("Supported Files", "*.DW2UnitMod;"),
            ))
        try:
            if file_path:
                # Apply the mod to file2 using the selected offsets
                with open(file2, "r+b") as f1:
                    with open(file_path, "rb") as f2:
                        f1.seek(unit_data[0])
                        for i in range(0, 53):
                            unitdata1 = f2.read(7)
                            f1.write(unitdata1)
                        f1.seek(unit_data[1])
                        for j in range(0, 201):
                            unitdata2 = f2.read(7)
                            f1.write(unitdata2)
                self.mod_status.config(text=f"Mod file '{os.path.basename(file_path)}' enabled successfully.", fg="green")
        except Exception as e:
            self.mod_status.config(text=f"Error: {str(e)}", fg="red")
    def ask_open_unit2(self): # For disabling mods
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select mod file",
            filetypes=(
                ("Supported Files", "*.2data;"),
            ))
        try:
            if file_path:
                # Apply the mod to file2(game file) using the offsets obtained from stage_data list
                with open(file2, "r+b") as f1: # DW2.bin
                    with open(file_path, "rb") as f2: # File selected from Backups_For_Mod_Disabling that will be used to disable the mod, writing the original non-modded values
                        f1.seek(unit_data[0])
                        for i in range(0, 53):
                            unitdata1 = f2.read(7)
                            f1.write(unitdata1)
                        f1.seek(unit_data[1])
                        for j in range(0, 201):
                            unitdata2 = f2.read(7)
                            f1.write(unitdata2)
                self.mod_status.config(text=f"The mod that used the '{os.path.basename(file_path)}' template was disabled.", fg="green")
        except Exception as e:
            self.mod_status.config(text=f"Error: {str(e)}", fg="red")

    # For stage mods
    def ask_open_file(self): # This is for enabling the user selected mod
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select mod file",
            filetypes=(
                ("Supported Files", "*.DW2YTR;*.DW2HLG;*.DW2GD;*.DW2CBan;*.DW2CBi;*.DW2HF;*.DW2YL;*.DW2WZP"),
            ))
        try:
            if file_path:
                for i, ext in enumerate(stage_extension):
                    if ext in file_path:
                        offsets = stage_data[i]
                    else:
                        pass
                # Apply the mod to file2 using the selected offsets
                with open(file2, "r+b") as f1:
                    with open(file_path, "rb") as f2:
                        for offset in offsets:
                            f1.seek(offset)
                            for off in range(0, 64):  # read 32 bytes at a time and write it up to 64 times per offset in list(8 in the list)
                                sdata = f2.read(32)
                                f1.write(sdata)
                self.mod_status.config(text=f"Mod file '{os.path.basename(file_path)}' enabled successfully.", fg="green")
                return
        except Exception as e:
            self.mod_status.config(text=f"Error: {str(e)}", fg="red")
            
    def ask_open_ofile(self): # For disabling mods
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select mod file",
            filetypes=(
                ("Supported Files", "*.data;"),
            ))
        try:
            if file_path:
                for i, ext in enumerate(filenames2):
                    if ext in file_path:
                        offsets = stage_data[i]
                    else:
                        pass
                # Apply the disable file to file2(game file) using the offsets obtained from stage_data list
                with open(file2, "r+b") as f1: # DW2.bin
                    with open(file_path, "rb") as f2: # File selected from Backups_For_Mod_Disabling that will be used to disable the mod, writing the original non-modded values
                        for offset in offsets: # Runs through the 8 offsets in the stage_data list based on the position stage_data[i]
                            f1.seek(offset) # seek offset that stores unit slots
                            for off in range(0, 64):  # read 32 bytes at a time and write it up to 64 times per offset in list(8 in the list)
                                sdata = f2.read(32) # original data being read from file_path which is the file to revert mods
                                f1.write(sdata) # write the non-modded data
                self.mod_status.config(text=f"The mod that used the '{os.path.basename(file_path)}' template was disabled.", fg="green")
                return
        except Exception as e:
            self.mod_status.config(text=f"Error: {str(e)}", fg="red")
    def run(self):
        self.root.mainloop()
        
class ModdingEditor: # The main modding editor
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dynasty Warriors 2 Modding")
        self.root.iconbitmap(os.path.join(folds[5], "icon3.ico"))
        self.root.minsize(400, 400)
        self.root.resizable(False, False)
        self.button_unit_editor = tk.Button(self.root, text="Unit Editor", command=self.open_unit_editor, height=10, width=10) # for unit data
        self.button_unit_editor.place(x=10, y=40)
        self.button_stage_editor = tk.Button(self.root, text="Stage Editor", command=self.open_stage_editor, height=10, width=10) # for stage data
        self.button_stage_editor.place(x=150, y=40)
        self.button_name_editor = tk.Button(self.root, text="Name Editor", command=self.open_name_editor, height=10, width=10) # for name data
        self.button_name_editor.place(x=290, y=40)
        self.button_mod_manager = tk.Button(self.root, text="Mod Manager", command = self.open_dw2_mod_manager, height=5, width=25).place(x=10, y=250)
        self.button_clean_files = tk.Button(self.root, text="Item Editor", command = self.open_item_editor, height=5, width=25).place(x=200, y=250)
    def open_unit_editor(self):
        self.root.destroy()
        unit_editor = UnitEditor()
    def open_name_editor(self):
        self.root.destroy()
        name_editor = NameEditor()
    def open_stage_editor(self):
        self.root.destroy()
        stage_editor = StageEditor(filenames, filenames2, file2, unit_names)
    def open_dw2_mod_manager(self):
        self.root.destroy()
        mod_manager = DW2ModManager()
    def open_item_editor(self):
        self.root.destroy()
        item_editor = ItemEditor()
    def run(self):
        self.root.mainloop()

class ItemEditor(TheCheck): # item Editor for editing item values
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Item Editor")
        self.root.iconbitmap(os.path.join(folds[5], "icon5.ico"))
        self.root.minsize(800, 500)
        self.root.resizable(False,False)

        self.itemlist = [] # list storing item values
        # The following tkinter variables store item values. HP refers to health and s refers to stats. All of them have 4 different items with different values
        self.hp1 = tk.IntVar()
        self.hp2 = tk.IntVar()
        self.hp3 = tk.IntVar()
        self.hp4 = tk.IntVar()
        self.arrow1 = tk.IntVar()
        self.arrow2 = tk.IntVar()
        self.arrow3 = tk.IntVar()
        self.arrow4 = tk.IntVar()
        self.s1 = tk.IntVar()
        self.s2 = tk.IntVar()
        self.s3 = tk.IntVar()
        self.s4 = tk.IntVar()
        self.s5 = tk.IntVar()
        self.s6 = tk.IntVar()
        self.s7 = tk.IntVar()
        self.s8 = tk.IntVar()

        # Call the GUI
        self.item_labels()
        self.item_entries_with_button()
    def item_labels(self): # Handles the GUI layout
        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.place(x=400, y=330)
        self.info_label = tk.Label(self.root, text="""You can change the value the items have with the Item Editor. Stat increase items refer to
        the attack and defense items that are given when an officer or gate captain is defeated.""").place(x=300, y=400)
        tk.Label(self.root, text="Health Item 1").place(x=0, y=0)
        tk.Label(self.root, text="Health Item 2").place(x=0, y=80)
        tk.Label(self.root, text="Health Item 3").place(x=0, y=160)
        tk.Label(self.root, text="Health item 4").place(x=0, y=240)
        tk.Label(self.root, text="Arrows 1").place(x=200, y=0)
        tk.Label(self.root, text="Arrows 2").place(x=200, y=80)
        tk.Label(self.root, text="Arrows 3").place(x=200, y=160)
        tk.Label(self.root, text="Arrows 4").place(x=200, y=240)
        tk.Label(self.root, text="Stat increase Item 1").place(x=400, y=0)
        tk.Label(self.root, text="Stat increase Item 2").place(x=400, y=80)
        tk.Label(self.root, text="Stat increase Item 3").place(x=400, y=160)
        tk.Label(self.root, text="Stat increase Item 4").place(x=400, y=240)
        tk.Label(self.root, text="Stat increase Item 5").place(x=600, y=0)
        tk.Label(self.root, text="Stat increase Item 6").place(x=600, y=80)
        tk.Label(self.root, text="Stat increase Item 7").place(x=600, y=160)
        tk.Label(self.root, text="Stat increase Item 8").place(x=600, y=240)
    def item_entries_with_button(self):
        tk.Entry(self.root, textvariable=self.hp1, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=40)
        tk.Entry(self.root, textvariable=self.hp2, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=120)
        tk.Entry(self.root, textvariable=self.hp3, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=200)
        tk.Entry(self.root, textvariable=self.hp4, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=280)
        tk.Entry(self.root, textvariable=self.arrow1, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=200, y=40)
        tk.Entry(self.root, textvariable=self.arrow2, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=200, y=120)
        tk.Entry(self.root, textvariable=self.arrow3, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=200, y=200)
        tk.Entry(self.root, textvariable=self.arrow4, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=200, y=280)
        tk.Entry(self.root, textvariable=self.s1, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=400, y=40)
        tk.Entry(self.root, textvariable=self.s2, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=400, y=120)
        tk.Entry(self.root, textvariable=self.s3, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=400, y=200)
        tk.Entry(self.root, textvariable=self.s4, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=400, y=280)
        tk.Entry(self.root, textvariable=self.s5, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=600, y=40)
        tk.Entry(self.root, textvariable=self.s6, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=600, y=120)
        tk.Entry(self.root, textvariable=self.s7, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=600, y=200)
        tk.Entry(self.root, textvariable=self.s8, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=600, y=280)
        tk.Button(self.root, text="Submit item values to the DW2.bin file", command= self.item_writer, height=3).place(x=30, y=330) # Runs the item writing function

        self.item_reader() # Calls the data reading
    def item_reader(self):
        with open(file2, "rb") as f1:
            f1.seek(itemsoffset)
            for i in range(0, 16):
                itemid = f1.read(4)
                itemvalue = int.from_bytes(f1.read(4), "little")
                itemeffect = f1.read(4)
                self.itemlist.append(itemvalue)
            self.hp1.set(self.itemlist[0])
            self.hp2.set(self.itemlist[1])
            self.hp3.set(self.itemlist[2])
            self.hp4.set(self.itemlist[3])
            self.arrow1.set(self.itemlist[4])
            self.arrow2.set(self.itemlist[5])
            self.arrow3.set(self.itemlist[6])
            self.arrow4.set(self.itemlist[7])
            self.s1.set(self.itemlist[8])
            self.s2.set(self.itemlist[9])
            self.s3.set(self.itemlist[10])
            self.s4.set(self.itemlist[11])
            self.s5.set(self.itemlist[12])
            self.s6.set(self.itemlist[13])
            self.s7.set(self.itemlist[14])
            self.s8.set(self.itemlist[15])
    def item_writer(self): # Handles writing of the current item values
        try:
            col = [self.hp1.get().to_bytes(4, "little"), self.hp2.get().to_bytes(4, "little"), self.hp3.get().to_bytes(4, "little"),
                         self.hp4.get().to_bytes(4, "little"), self.arrow1.get().to_bytes(4, "little"), self.arrow2.get().to_bytes(4, "little"),
                         self.arrow3.get().to_bytes(4, "little"), self.arrow4.get().to_bytes(4, "little"), self.s1.get().to_bytes(4, "little"),
                   self.s2.get().to_bytes(4, "little"), self.s3.get().to_bytes(4, "little"), self.s4.get().to_bytes(4, "little"), self.s5.get().to_bytes(4, "little"),
                   self.s6.get().to_bytes(4, "little"), self.s7.get().to_bytes(4, "little"), self.s8.get().to_bytes(4, "little")]
            with open(file2, "r+b") as w1: # for writing current item values
                w1.seek(itemsoffset) # seek item offset
                for item in col: # for each item value in the col list
                    itemid = w1.read(4) # ID of the item
                    w1.write(item) # write the current item value
                    itemeffect = w1.read(4) # Effect of the item
            self.status_label.config(text=f"Values were written without issues.", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Error with entries: {str(e)}", fg="red")
        
class NameEditor(TheCheck): # for name editing
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Name Editor")
        self.root.iconbitmap(os.path.join(folds[5], "icon4.ico"))
        self.root.minsize(700, 400)
        self.root.resizable(False,False)

        self.name_offsets1 = [0x16141F78, 64, 15] # offset, slot range, byte reading length
        self.name_offsets2 = [0x161424A8, 27, 15] # offset, slot range, byte reading length
        self.name_offsets3 = [0x1615A410, 41, 7] # offset, slot range, byte reading length
        self.name_offsets4 = [0x1615A688, 14, 7] # offset, slot range, byte reading length

        self.noffset1 = tk.StringVar()

        tk.Label(self.root, text="Unit Names:").place(x=10, y=0)
        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.place(x=200, y=200)
        
        self.selected_slot = tk.IntVar(self.root)
        self.selected_slot.set(0)  # Default value
        
        tk.Label(self.root, text="Unit Name Slots:").place(x=200, y=0)
        slot_combobox = ttk.Combobox(self.root, textvariable=self.selected_slot, values=list(range(146)))
        slot_combobox.bind("<<ComboboxSelected>>", self.slot_selected)
        slot_combobox.place(x=300, y=0)

        tk.Entry(self.root, textvariable=self.noffset1).place(x=10, y=30)
        update_button = ttk.Button(self.root, text="Update Name", command=self.update_name)
        update_button.place(x=10, y=60)

    def slot_selected(self, event=None): # update display data
        self.selected_slot_value = self.selected_slot.get()
        self.name_display(self.selected_slot_value)

    def name_display(self, selected_slot_value):
        if selected_slot_value < self.name_offsets1[1]: # used for name_offsets1
            offset = self.name_offsets1[0] + selected_slot_value * 16  # offset based on the base offset and selected slot
            byte_length = self.name_offsets1[2]
            self.current_offset = self.name_offsets1
        elif self.name_offsets1[1] <= selected_slot_value < (self.name_offsets1[1] + self.name_offsets2[1]): # used for name_offsets2
            offset = self.name_offsets2[0] + (selected_slot_value - self.name_offsets1[1]) * 16  # offset based on the base offset and selected slot
            byte_length = self.name_offsets2[2]
            self.current_offset = self.name_offsets2
        elif (self.name_offsets1[1] + self.name_offsets2[1]) <= selected_slot_value < (self.name_offsets1[1] + self.name_offsets2[1] + self.name_offsets3[1]): # used for name_offsets3
            offset = self.name_offsets3[0] + (selected_slot_value - (self.name_offsets1[1] + self.name_offsets2[1])) * 8  # offset based on the base offset and selected slot
            byte_length = self.name_offsets3[2]
            self.current_offset = self.name_offsets3
        elif (self.name_offsets1[1] + self.name_offsets2[1] + self.name_offsets3[1]) <= selected_slot_value < 146: # used for name_offsets4
            offset = self.name_offsets4[0] + (selected_slot_value - (self.name_offsets1[1] + self.name_offsets2[1] + self.name_offsets3[1])) * 8  # offset based on the base offset and selected slot
            byte_length = self.name_offsets4[2]
            self.current_offset = self.name_offsets4
        else:
            return

        
        with open(file2, "r+b") as file:
            seeker = file.seek(offset)
            self.status_label.config(text=f"Current offset of the Unit Name Slot '{self.selected_slot_value}' is {seeker}", fg="green")
            name_bytes = file.read(byte_length)
            self.noffset1.set(name_bytes)
    def update_name(self):
        new_name = self.noffset1.get()
        byte_limit = self.current_offset[2]  # Get byte limit from current offset info
        new_name_truncated = new_name[:byte_limit].encode('utf-8')  # Truncate and encode the name

        # Ensure new_name_truncated is exactly byte_limit bytes long
        new_name_truncated = new_name_truncated.ljust(byte_limit, b'\x00')

        try:
            with open(file2, "r+b") as file:
                # Determine the correct offset based on the current offset and selected slot
                if self.current_offset is self.name_offsets1:
                    offset = self.current_offset[0] + self.selected_slot.get() * 16
                elif self.current_offset is self.name_offsets2:
                    offset = self.current_offset[0] + (self.selected_slot.get() - self.name_offsets1[1]) * 16
                elif self.current_offset is self.name_offsets3:
                    offset = self.current_offset[0] + (self.selected_slot.get() - (self.name_offsets1[1] + self.name_offsets2[1])) * 8
                elif self.current_offset is self.name_offsets4:
                    offset = self.current_offset[0] + (self.selected_slot.get() - (self.name_offsets1[1] + self.name_offsets2[1] + self.name_offsets3[1])) * 8
                else:
                    return

                file.seek(offset)
                file.write(new_name_truncated)
        except Exception as e:
            print(f"An error occurred: {e}")
            # Handle the exception as needed
    
    def run(self):
        self.root.mainloop()

class UnitEditor(TheCheck): #
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Unit Editor")
        self.root.iconbitmap(os.path.join(folds[5], "icon2.ico"))
        self.root.minsize(500, 400)
        self.root.resizable(False, False)
        self.unit_path = os.path.join(folds[3], unit_file)
        self.ounit_path = os.path.join(folds[2], unit_file)
        self.unit_ref_data = os.path.join(folds[3], unit_ref_file)
        self.unit_reading()
        self.unit_ref()
        
        self.name = tk.IntVar()
        self.unknown = tk.IntVar()
        self.model = tk.IntVar()
        self.color = tk.IntVar()
        self.motion = tk.IntVar()
        self.horse = tk.IntVar()
        self.itemcount = tk.IntVar()
        self.modname = tk.StringVar()
        hex_values = [hex(i) for i in range(254)]
        self.selected_slot = tk.IntVar(self.root)
        self.selected_slot.set(0)  # Default value
        slot_combobox = ttk.Combobox(self.root, textvariable=self.selected_slot, values=hex_values)
        slot_combobox.bind("<<ComboboxSelected>>", self.slot_selected)
        slot_combobox.place(x=350, y=10)
        tk.Button(self.root, text = "Create Unit Mod", command = self.create_unit_mod, height=3).place(x=10,y=330)
        mm1 = tk.Entry(self.root, textvariable = self.modname).place(x=120,y=300)
        mm2 = tk.Label(self.root, text = f"Enter a mod name").place(x=10,y=300)   
        tk.Button(self.root, text="Submit values to unit.data file", command= self.submit_unit, height=3).place(x=300, y=330)
        self.unit_labels()
        self.unit_entries()
    def unit_labels(self):
        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.place(x=10, y=250)
        tk.Label(self.root, text="Name").place(x=160, y=0)
        tk.Label(self.root, text="Model").place(x=160, y=40)
        tk.Label(self.root, text="Color").place(x=160, y=80)
        tk.Label(self.root, text="Weapon+Motion").place(x=160, y=120)
        tk.Label(self.root, text="Horse").place(x=160, y=160)
        tk.Label(self.root, text="Amount of items and heals").place(x=160, y=200)
        tk.Label(self.root, text="Character slot:").place(x=240, y=10)
    def unit_entries(self):
        tk.Entry(self.root, textvariable=self.name, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=0)
        tk.Entry(self.root, textvariable=self.model, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=40)
        tk.Entry(self.root, textvariable=self.color, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=80)
        tk.Entry(self.root, textvariable=self.motion, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=120)
        tk.Entry(self.root, textvariable=self.horse, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=160)
        tk.Entry(self.root, textvariable=self.itemcount, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=200)
    def create_unit_mod(self):
        sep = "." # to be used for correcting
        new_reader = os.path.join(folds[3], unit_file) # get the .data file that is in the same list position as the .ref files in folds[0]
        try:
            usermodname = self.modname.get().split(sep, 1)[0] + dw2_mod # Create modname with the user entered name and stage extension based on the .ref file selected
            with open(new_reader, "rb") as r1:
                data = r1.read()
                with open(usermodname, "wb") as w1:
                    w1.write(data)
            self.status_label.config(text=f"Mod file '{usermodname}' created successfully.", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Error creating mod file '{usermodname}': {str(e)}", fg="red")

    def slot_selected(self, event=None): # update display data
        self.selected_slot_value = self.selected_slot.get()
        self.unit_display(self.selected_slot_value)
    def submit_unit(self):
        try:
            col = [self.name.get().to_bytes(1, "little"), self.unknown.get().to_bytes(1, "little"), self.model.get().to_bytes(1, "little"),
                         self.color.get().to_bytes(1, "little"), self.motion.get().to_bytes(1, "little"), self.horse.get().to_bytes(1, "little"),
                         self.itemcount.get().to_bytes(1, "little")]
            unit_slot = self.selected_slot.get()
            with open(self.unit_ref_data, "rb") as r1: # for obtaining the offset for a unit slot from the .ref file
                uservalue = unit_slot * 8
                r1.seek(uservalue)
                getoffset = int.from_bytes(r1.read(8), "little")
                with open(self.unit_path, "r+b") as f1: # for updating the unit slot with the current values from col list
                    f1.seek(getoffset)
                    for b in col:
                        f1.write(b)
            self.status_label.config(text=f"Values were written without issues.", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Error with entries: {str(e)}, please use values less than 255.", fg="red")
    def unit_reading(self):
        with open(file2, "rb") as f1:
            with open(self.unit_path, "ab") as f2:
                f1.seek(unit_data[0])
                for i in range(0, 53):
                    unitdata1 = f1.read(7)
                    f2.write(unitdata1)
                f1.seek(unit_data[1])
                for j in range(0, 201):
                    unitdata2 = f1.read(7)
                    f2.write(unitdata2)
                for a in unit_data:
                    f2.write(a.to_bytes(4, "little"))
        if not os.path.exists(self.ounit_path):
            shutil.copy(self.unit_path, self.ounit_path)
    def unit_ref(self):
        with open(self.unit_path, "rb") as r1:  # Open the corresponding .ref file for writing
            with open(self.unit_ref_data, "ab") as r2:
                offset = 0  # Initialize offset counter
                while True:
                    data_chunk = r1.read(7)  # Read a 7-byte chunk from .data file
                    if not data_chunk:  # Break loop if end of file is reached
                        break
                    r2.write(offset.to_bytes(8, "little"))  # Write the offset to the .ref file
                    offset += 7  # Move offset to the next chunk
    def unit_display(self, selected_slot_value):
        with open(self.unit_ref_data, "rb") as r1: # .ref file
            useroffset = self.selected_slot_value
            uservalue = self.selected_slot_value * 8
            r1.seek(uservalue)
            getoffset = int.from_bytes(r1.read(8), "little")
            with open(self.unit_path, "r+b") as r2:
                r2.seek(getoffset)
                unitname = int.from_bytes(r2.read(1), "little")
                unk = int.from_bytes(r2.read(1), "little")
                unitmodel = int.from_bytes(r2.read(1), "little")
                unitcolor = int.from_bytes(r2.read(1), "little")
                unitmotion = int.from_bytes(r2.read(1), "little")
                unithorse = int.from_bytes(r2.read(1), "little")
                unititemcount = int.from_bytes(r2.read(1), "little")

                self.name.set(unitname)
                self.unknown.set(unk)
                self.model.set(unitmodel)
                self.color.set(unitcolor)
                self.motion.set(unitmotion)
                self.horse.set(unithorse)
                self.itemcount.set(unititemcount)
                
    def run(self):
        self.root.mainloop()


class StageEditor(TheCheck): # for modding stage/battles
    def __init__(self, filenames, filenames2, file2, unit_names):
        self.filenames = filenames
        self.filenames2 = filenames2
        self.file2 = file2
        self.unit_names = unit_names
        self.root = tk.Tk()
        self.root.title("Stage Editor")
        self.root.iconbitmap(os.path.join(folds[5], "icon1.ico"))
        self.root.minsize(1500, 800)
        self.root.resizable(False, False)
        # Load the default image based on the initial combobox selection
        initial_map_index = 0
        initial_image_path = self.get_image_filename(initial_map_index)
        self.img = PhotoImage(file=initial_image_path)
        # Create a Label widget to display the image
        self.img_label = tk.Label(self.root, image=self.img)
        self.img_label.place(x=0, y=0)
        
        self.stage_data_create()
        self.stage_data_ref()
        # Create dropdown menu for selecting stage file
        self.selected_file = tk.StringVar(self.root)
        self.selected_file.set(self.filenames[0])  # Default value
        file_combobox = ttk.Combobox(self.root, textvariable=self.selected_file, values=self.filenames)
        file_combobox.bind("<<ComboboxSelected>>", self.stage_search_on_map_change)
        file_combobox.place(x=1100, y=10)
        tk.Label(self.root, text="Stage to modify").place(x=1000, y=10)
        # Create dropdown menu for selecting unit slot
        self.selected_slot = tk.IntVar(self.root)
        self.selected_slot.set(0)  # Default value
        slot_combobox = ttk.Combobox(self.root, textvariable=self.selected_slot, values=list(range(512)))
        slot_combobox.bind("<<ComboboxSelected>>", self.slot_selected)
        slot_combobox.place(x=830, y=10)
        tk.Label(self.root, text="Unit Slot To Modify").place(x=700, y=10)
        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.place(x=480, y=200)
        # Create a ComboBox
        self.combo = ttk.Combobox(self.root, values=self.unit_names, width=30, state="readonly")
        self.combo.place(x=1200,y=600)
        self.combo.set(self.unit_names[0])  # Set the default selection to the first item
        # Bind the ComboBox selection change event
        self.combo.bind("<<ComboboxSelected>>", self.on_select)
        self.xcord = tk.IntVar()
        self.ycord = tk.IntVar()
        self.direct = tk.IntVar()
        self.AreaP = tk.IntVar()
        self.PullingB = tk.IntVar()
        self.Lif = tk.IntVar()
        self.LeaderU = tk.IntVar()
        self.GuardU = tk.IntVar()
        self.Att = tk.IntVar()
        self.Def = tk.IntVar()
        self.AmountG = tk.IntVar()
        self.UnitS = tk.IntVar()
        self.UnitG = tk.IntVar()
        self.AIT = tk.IntVar()
        self.UnitC = tk.IntVar()
        self.Hid = tk.IntVar()
        self.Advance = tk.IntVar()
        self.ItemD = tk.IntVar()
        self.AIL = tk.IntVar()
        self.modname = tk.StringVar()
        tk.Button(self.root, text = "Submit values to DATA file", command = self.submit_stage_values, height=5, width=20).place(x=1275,y=15)
        tk.Button(self.root, text = "Create Stage Mod", command = self.create_stage_mod, width=15).place(x=550,y=10)
        mm1 = tk.Entry(self.root, textvariable = self.modname).place(x=395,y=10)
        mm2 = tk.Label(self.root, text = f"Enter a mod name").place(x=280,y=10)
        self.stage_labels()
        self.stage_entries()
    def stage_labels(self):
        tk.Label(self.root, text="Integer values to use for Leader unit and guard unit:").place(x=1200, y=570)
        tk.Label(self.root, text="""Unit Groups:
        0-Player
        1-Commander
        2-General (Doesn't advance with Group 3)
        3-Playable Officers
        4-NPC Officers
        5-Gate Captains/Bodyguards/Troops that don't respawn
        6-Troops""").place(x=700, y=570)
        tk.Label(self.root, text="Initial Position X").place(x=160, y=0)
        tk.Label(self.root, text="Initial Position Y").place(x=160, y=40)
        tk.Label(self.root, text="Direction").place(x=160, y=80)
        tk.Label(self.root, text="Area Priority Targetting").place(x=160, y=120)
        tk.Label(self.root, text="Pulling Back").place(x=160, y=160)
        tk.Label(self.root, text="Life Stat").place(x=160, y=200)
        tk.Label(self.root, text="Leader Unit").place(x=160, y=240)
        tk.Label(self.root, text="Guard Units").place(x=160, y=280)
        tk.Label(self.root, text="Attack Stat").place(x=160, y=320)
        tk.Label(self.root, text="Defense Stat").place(x=160, y=360)
        tk.Label(self.root, text="Amount of guards (9 is max)").place(x=160, y=400)
        tk.Label(self.root, text="Unit slot that unit belongs to").place(x=160, y=440)
        tk.Label(self.root, text="Unit Group").place(x=160, y=480)
        tk.Label(self.root, text="AI Type/Kind (4=horse, 2=bowman)").place(x=160, y=520)
        tk.Label(self.root, text="Unit Commands (1=Attack enemy target, 3=Follow ally target)").place(x=160, y=560)
        tk.Label(self.root, text="Hide Unit").place(x=160, y=600)
        tk.Label(self.root, text="Advancing Target/Follow Target").place(x=160, y=640)
        tk.Label(self.root, text="Item they leave after death").place(x=160, y=680)
        tk.Label(self.root, text="AI Level").place(x=160, y=720)
    def stage_entries(self):
        tk.Entry(self.root, textvariable=self.xcord, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=0)
        tk.Entry(self.root, textvariable=self.ycord, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=40)
        tk.Entry(self.root, textvariable=self.direct, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=80)
        tk.Entry(self.root, textvariable=self.AreaP, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=120)
        tk.Entry(self.root, textvariable=self.PullingB, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=160)
        tk.Entry(self.root, textvariable=self.Lif, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=200)
        tk.Entry(self.root, textvariable=self.LeaderU, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=240)
        tk.Entry(self.root, textvariable=self.GuardU, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=280)
        tk.Entry(self.root, textvariable=self.Att, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=320)
        tk.Entry(self.root, textvariable=self.Def, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=360)
        tk.Entry(self.root, textvariable=self.AmountG, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=400)
        tk.Entry(self.root, textvariable=self.UnitS, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=440)
        tk.Entry(self.root, textvariable=self.UnitG, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=480)
        tk.Entry(self.root, textvariable=self.AIT, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=520)
        tk.Entry(self.root, textvariable=self.UnitC, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=560)
        tk.Entry(self.root, textvariable=self.Hid, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=600)
        tk.Entry(self.root, textvariable=self.Advance, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=640)
        tk.Entry(self.root, textvariable=self.ItemD, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=680)
        tk.Entry(self.root, textvariable=self.AIL, validate="key", validatecommand=(self.root.register(self.validate_numeric_input), "%P")).place(x=0, y=720)
    # Function to handle selection change
    def on_select(self, event):
        selected_unit = self.combo.get()
    def stage_data_create(self): # make the .data files to store 32 byte unit slot data
        with open(file2, "rb") as f1: # the main file to obtain references from
                for i in range(len(stage_data)): # For using all lists within stage_data
                    for offsets in stage_data[i]: # for each offset in each list
                        with open(os.path.join(folds[0], filenames2[i]), "ab") as f2: # create the filename from filenames based on the current list
                            f1.seek(offsets) # seek each offset within each list
                            for j in range(0, 64): # read 32 chunks of data 64 times for each offset in each list
                                offset = f1.tell()
                                sdata = f1.read(32)
                                f2.write(sdata)
                    with open(os.path.join(folds[0], filenames2[i]), "ab") as f2:
                        for a in stage_data[i]:
                            f2.write(a.to_bytes(4, "little"))
        check_backup1()

    def stage_data_ref(self): # make the .ref files store offsets for each slot in the .data files
        for i in range(len(filenames)):  # Iterate over all filenames
            with open(os.path.join(folds[0], filenames2[i]), "rb") as f_data:  # Open the .data file for reading
                with open(os.path.join(folds[1], filenames[i]), "ab") as f_ref:  # Open the corresponding .ref file for writing
                    offset = 0  # Initialize offset counter
                    while True:
                        data_chunk = f_data.read(32)  # Read a 32-byte chunk from .data file
                        if not data_chunk:  # Break loop if end of file is reached
                            break
                        f_ref.write(offset.to_bytes(8, "little"))  # Write the offset to the .ref file
                        offset += 32  # Move offset to the next chunk
        check_backup2()

    def get_image_filename(self, map_index):
        map_filenames = ["YTR.png", "HLG.png", "GuanDu.png", "ChangBan.png", "ChiBi.png", "HeFei.png", "YiLing.png", "WuZhangPlains.png"]
        return os.path.join(folds[4], map_filenames[map_index])
    def stage_search_on_map_change(self, event=None): # for when user chooses a map or slot
        selected_file_value = self.selected_file.get()
        selected_slot_value = self.selected_slot.get()
        self.stage_search(selected_file_value, selected_slot_value)

        # Update the displayed image based on the selected map
        selected_map_index = self.filenames.index(selected_file_value)
        image_filename = self.get_image_filename(selected_map_index)
        self.img = PhotoImage(file=image_filename)
        self.img_label.configure(image=self.img)
    
    def slot_selected(self, event=None): # update display data
        selected_file_value = self.selected_file.get()
        selected_slot_value = self.selected_slot.get()
        self.stage_search(selected_file_value, selected_slot_value)
    
    def stage_search(self, selected_file, selected_slot): # search the data for unit slots in the .data files, this handles unit reading that entries display
        global Unused1, Unused2, Unk, getoffset
        file_index = self.filenames.index(selected_file)
        new_select = os.path.join(folds[1], selected_file)
        new_read = os.path.join(folds[0], self.filenames2[file_index])
        with open(new_select, "rb") as r1: # .ref file
            useroffset = selected_slot
            uservalue = selected_slot * 8
            r1.seek(uservalue)
            getoffset = int.from_bytes(r1.read(8), "little")
            
            with open(new_read, "rb") as f1: # .data file
                f1.seek(getoffset)
                slotoffset = f1.tell()
                x = int.from_bytes(f1.read(2), "little")
                y = int.from_bytes(f1.read(2), "little")
                direction = int.from_bytes(f1.read(1), "little")
                AreaPrior = int.from_bytes(f1.read(1), "little")
                PullingBack = int.from_bytes(f1.read(1), "little")
                Unused1 = f1.read(1)
                Life = int.from_bytes(f1.read(2), "little")
                LeaderUnit = int.from_bytes(f1.read(1), "little")
                GuardUnits = int.from_bytes(f1.read(1), "little")
                Attack = int.from_bytes(f1.read(1), "little")
                Defense = int.from_bytes(f1.read(1), "little")
                AmountGuards = int.from_bytes(f1.read(1), "little")
                UnitSlot = int.from_bytes(f1.read(1), "little")
                UnitGroup = int.from_bytes(f1.read(1), "little")
                AIType = int.from_bytes(f1.read(1), "little")
                UnitCommand = int.from_bytes(f1.read(1), "little")
                Hide = int.from_bytes(f1.read(1), "little")
                Unused2 = f1.read(1)
                AdvancingTarget = int.from_bytes(f1.read(1), "little")
                ItemDrop = int.from_bytes(f1.read(1), "little")
                AILevel = int.from_bytes(f1.read(1), "little")
                Unk = f1.read(8)
                
                self.xcord.set(x)
                self.ycord.set(y)
                self.direct.set(direction)
                self.AreaP.set(AreaPrior)
                self.PullingB.set(PullingBack)
                self.Lif.set(Life)
                self.LeaderU.set(LeaderUnit)
                self.GuardU.set(GuardUnits)
                self.Att.set(Attack)
                self.Def.set(Defense)
                self.AmountG.set(AmountGuards)
                self.UnitS.set(UnitSlot)
                self.UnitG.set(UnitGroup)
                self.AIT.set(AIType)
                self.UnitC.set(UnitCommand)
                self.Hid.set(Hide)
                self.Advance.set(AdvancingTarget)
                self.ItemD.set(ItemDrop)
                self.AIL.set(AILevel)
    def create_stage_mod(self): # for creating a mod file with custom extension
        sep = "." # to be used for correcting
        file_index = self.filenames.index(self.selected_file.get()) # get the current selected .ref file
        new_reader = os.path.join(folds[0], self.filenames2[file_index]) # get the .data file that is in the same list position as the .ref files in folds[0]
        try:
            usermodname = self.modname.get().split(sep, 1)[0] + stage_extension[file_index] # Create modname with the user entered name and stage extension based on the .ref file selected
            with open(new_reader, "rb") as r1:
                data = r1.read()
                with open(usermodname, "wb") as w1:
                    w1.write(data)
            self.status_label.config(text=f"Mod file '{usermodname}' created successfully.", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Error creating mod file '{usermodname}': {str(e)}", fg="red")
    def submit_stage_values(self): # write the data on each click to the template files(.data files) rather than main file(file2)
        file_index = self.filenames.index(self.selected_file.get())
        new_reader = os.path.join(folds[1], self.selected_file.get()) # For the reference files(.ref)
        new_writer = os.path.join(folds[0], self.filenames2[file_index])
        try:
            collectit = [self.xcord.get().to_bytes(2, "little"), self.ycord.get().to_bytes(2, "little"), self.direct.get().to_bytes(1, "little"),
                         self.AreaP.get().to_bytes(1, "little"), self.PullingB.get().to_bytes(1, "little"), Unused1, self.Lif.get().to_bytes(2, "little"),
                         self.LeaderU.get().to_bytes(1, "little"), self.GuardU.get().to_bytes(1, "little"), self.Att.get().to_bytes(1, "little"),
                         self.Def.get().to_bytes(1, "little"), self.AmountG.get().to_bytes(1, "little"), self.UnitS.get().to_bytes(1, "little"),
                         self.UnitG.get().to_bytes(1, "little"), self.AIT.get().to_bytes(1, "little"), self.UnitC.get().to_bytes(1, "little"),
                         self.Hid.get().to_bytes(1, "little"), Unused2, self.Advance.get().to_bytes(1, "little"), self.ItemD.get().to_bytes(1, "little"),
                         self.AIL.get().to_bytes(1, "little"), Unk]
            selected_slot = self.selected_slot.get()
            with open(new_reader, "r+b") as r1: # for obtaining the offset for a unit slot from the .ref file
                useroffset = selected_slot
                uservalue = selected_slot * 8
                r1.seek(uservalue)
                getoffset = int.from_bytes(r1.read(8), "little")
                with open(new_writer, "r+b") as f1: # for updating the unit slot with the current values from collectit
                    f1.seek(getoffset)
                    for b in collectit:
                        f1.write(b)
            self.status_label.config(text=f"Values submitted without issues.", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Error with entries: {str(e)}", fg="red")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    for f in folds:
        os.makedirs(f, exist_ok = True)
    rem(filenames, filenames2, unit_file, unit_ref_file) # clean old files
    main_editor = MainEditor()
    main_editor.run()
