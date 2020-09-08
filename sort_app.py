from pixelsort import pixelsort
from PIL import Image, ImageQt
from pathlib import Path
from time import sleep
from math import floor

import sys
from PySide2 import QtWidgets, QtGui

#QApplication = QtWidgets.QApplication


from pixel_sorter_gui import Ui_MainWindow as sorter_gui


### CONFIG ###

d_images = "images"
i = "squirrel.jpg"
#i = "DSC04688_EDIT_1000.jpg"
p = Path()
image_p_in = p / d_images / i


mask_user_selection_options = ["None", "Single", "Folder"]
mask_user_selection = "Single"
mask_selected = "squirrel_mask_Inverted.jpg"


d_masks = p / d_images / "Masks"
p_masks = list(d_masks.glob("*.jpg"))


### STATIC SETTINGS ###

sort_settings_default = {
    "mask_image" : None,                        # None Default             
    "interval_image" : None,                    # None Default
    "randomness": 0,                            # 0 Default
    "clength": 50,                              # 50 Default
    "sorting_function": "lightness",            # "lightness" Default               
    "interval_function": "threshold",           # "threshold" Default
    "lower_threshold": 0.25,                    # .25 Default
    "upper_threshold": 0.8,                     # .8 Default
    "angle": 0       
}

sort_settings = {
    "mask_image" : None,                        # None Default             
    "interval_image" : None,                    # None Default
    "randomness": 0,                            # 0 Default
    "clength": 250,                              # 50 Default
    "sorting_function": "intensity",            # "lightness" Default               
    "interval_function": "random",           # "threshold" Default
    "lower_threshold": 0.4,                    # .25 Default
    "upper_threshold": 0.7,                     # .8 Default
    "angle": 270                                  # 0 Default
    #"settings_changed_formatted" : None        # ADDED LATER
    }


class Option():
    def __init__(self):
        '''This class helps make data more accessable later.'''
        self.isParam = None
        self.name = None
        self.name_display = None
        self.isEnabled = None
        self.desc = None
        self.val_default = None
        self.val_current = None
        self.val_range_min = None
        self.val_range_max = None
        #self.val_type = None
        self.associated_parameters = None       # if function

    def _setup(self, isParam, name, name_display, isEnabled, desc, val_default=None, val_range_min=None, val_range_max=None, associated_parameters=None):
        '''Allows easy loading of settings.'''
        self.isParam = isParam
        self.name = name
        self.name_display = name_display
        self.isEnabled = isEnabled
        self.desc = desc
        self.val_default = val_default
        self.val_current = self.val_default
        self.val_range_min = val_range_min
        self.val_range_max = val_range_max
        self.associated_parameters = associated_parameters


def _setup_all_sort_options():
    '''Sets up parameter, interval function, and sorting function options.
    Passes back a dictionary of dictionaries.'''
    ## PARAMETERS (for those that make sense to do so for):
    # https://github.com/satyarth/pixelsort#parameters
    parameter_randomness = Option()
    parameter_randomness._setup(isParam=True, name="randomness", name_display="Randomness", isEnabled=True,
        desc="What percentage of intervals not to sort. 0 by default.",
        val_default=0, val_range_min=0, val_range_max=100, associated_parameters=None)

    parameter_threshold_lower = Option()
    parameter_threshold_lower._setup(isParam=True, name="threshold_lower", name_display="Threshold - L", isEnabled=True,
        desc="How dark must a pixel be to be considered as a 'border' for sorting? Takes values from 0-1. 0.25 by default. Used in edges and threshold modes.",
        val_default=.25, val_range_min=0, val_range_max=1, associated_parameters=None)

    parameter_threshold_upper = Option()
    parameter_threshold_upper._setup(isParam=True, name="threshold_upper", name_display="Threshold - U", isEnabled=True,
        desc="How bright must a pixel be to be considered as a 'border' for sorting? Takes values from 0-1. 0.8 by default. Used in threshold mode.",
        val_default=.8, val_range_min=0, val_range_max=1, associated_parameters=None)

    parameter_clength = Option()
    parameter_clength._setup(isParam=True, name="clength", name_display="Characteristic Length", isEnabled=True,
        desc="Characteristic length for the random width generator. Used in mode random and waves.",
        val_default=50, val_range_min=0, val_range_max=None, associated_parameters=None)

    parameter_angle = Option()
    parameter_angle._setup(isParam=True, name="angle", name_display="Angle", isEnabled=True,
        desc="Angle at which you're pixel sorting in degrees. 0 (horizontal) by default.",
        val_default=0, val_range_min=0, val_range_max=360, associated_parameters=None)

    parameters_list = [
        parameter_randomness,
        parameter_threshold_lower,
        parameter_threshold_upper,
        parameter_clength,
        parameter_angle        
        ]

    # Creates dictionary of all the enabled parameters. 
    # <parameter name>, <parameter object>
    parameters_dict = {(param.name, param) for param in parameters_list if param.isEnabled}
    
    ## INTERVAL FUNCTIONS:
    # https://github.com/satyarth/pixelsort#interval-functions
    interval_func_random = Option()
    interval_func_random._setup(isParam=False, name="random", name_display="Random", isEnabled=True,
        desc="Randomly generate intervals. Distribution of widths is linear by default. Interval widths can be scaled using clength.",
        val_default=None, val_range_min=None, val_range_max=None,
        associated_parameters=None) #clength

    interval_func_edges = Option()
    interval_func_edges._setup(isParam=False, name="edges", name_display="Edges", isEnabled=True,
        desc="Performs an edge detection, which is used to define intervals. Tweak threshold with threshold.",
        val_default=None, val_range_min=None, val_range_max=None,
        associated_parameters=[parameter_threshold_lower]) #threshold lower

    interval_func_threshold = Option()
    interval_func_threshold._setup(isParam=False, name="threshold", name_display="Threshold", isEnabled=True,
        desc="Intervals defined by lightness thresholds; only pixels with a lightness between the upper and lower thresholds are sorted.",
        val_default=None, val_range_min=None, val_range_max=None,
        associated_parameters=[parameter_threshold_lower, parameter_threshold_upper])   # threshold lower and upper

    interval_func_waves = Option()
    interval_func_waves._setup(isParam=False, name="waves", name_display="Waves", isEnabled=True,
        desc="Intervals are waves of nearly uniform widths. Control width of waves with clength.",
        val_default=None, val_range_min=None, val_range_max=None,
        associated_parameters=None) #clength
    # Disabled:
    interval_func_file = Option()
    interval_func_file._setup(isParam=False, name="file", name_display="File", isEnabled=False,
        desc="Intervals taken from another specified input image. Must be black and white, and the same size as the input image.",
        val_default=None, val_range_min=None, val_range_max=None,
        associated_parameters=None)
    # Disabled:
    interval_func_file_edges = Option()
    interval_func_file_edges._setup(isParam=False, name="file-edges", name_display="File-Edges", isEnabled=False,
        desc="Intevals defined by performing edge detection on the file specified by -f. Must be the same size as the input image.",
        val_default=None, val_range_min=None, val_range_max=None,
        associated_parameters=None)

    interval_func_none = Option()
    interval_func_none._setup(isParam=False, name="none", name_display="None", isEnabled=True,
        desc="Sort whole rows, only stopping at image borders.",
        val_default=None, val_range_min=None, val_range_max=None,
        associated_parameters=None)

    interval_function_list = [
        interval_func_random,
        interval_func_edges,
        interval_func_threshold,
        interval_func_waves,
        interval_func_file,
        interval_func_file_edges,
        interval_func_none
        ]

    # Creates dictionary of all the enabled functions. 
    # <function name>, <function object>
    interval_functions_dict = {(func.name, func) for func in interval_function_list if func.isEnabled}

    sorting_functions = {
        "lightness" : "Sort by the lightness of a pixel according to a HSV representation.",
        "hue" : "Sort by the hue of a pixel according to a HSV representation.",
        "saturation" : "Sort by the saturation of a pixel according to a HSV representation.",
        "intensity" : "Sort by the intensity of a pixel, i.e. the sum of all the RGB values.",
        "minimum" : "Sort on the minimum RGB value of a pixel (either the R, G or B)."
        }
    

    # Combining everything to pass back:
    all_options = {
        "parameters" : parameters_dict,
        "interval functions" : interval_functions_dict,
        "sorting functions" : sorting_functions
    }

    return all_options


class Sorter_Image():
    def __init__(self, img_file_path, sorter_img_type, associated_main_image=None):
        '''Holds common properties associated with an image. All images part of this set are stored as PIL.Image objects.'''
        self.path = img_file_path
        self.type = sorter_img_type                             # "main", "mask", (future option)
        self.associated_main_image = associated_main_image      # For "mask" images. Allows it to get it's dimensions more conveniently.
        self.thumbnail = None
        self.preview = None
        self.preview_fast = None
        self.full = None
        self.original = None    # used for masks


    def generate_image_sets(self):
        '''Creates thumbnail, preview, preview_fast, and full images'''
        '''
        img = Image.open(self.path)
        self.full = img.convert("RGB")      # ensures there is no alpha right from the start
        '''

        self.full = Image.open(self.path)
        #self.full.convert("RGBA")

        self.thumbnail =  self.full.copy()
        self.thumbnail.thumbnail((200, 200))

        self.preview_fast = self.full.copy()
        self.preview_fast.thumbnail((400, 400))

        self.preview = self.full.copy()
        self.preview.thumbnail((1000, 1000))

        #self.thumbnail = self.full.thumbnail((300, 200))
        #self.preview_fast = self.full.thumbnail((400, 400))
        #self.preview = self.full.thumbnail((1000, 1000))
    
    def generate_core_mask_sets(self):
        '''Creates essential mask variations (original and thumbnail). Should be called after being created.'''
        self.original = Image.open(self.path)

        self.thumbnail = self.original.copy()
        self.thumbnail.thumbnail((200, 200))

    def generate_masks_from_associated_image(self):
        '''Sizes mask based on "associated" Sorter_Image object.'''
        # Masks make use of the "original" since they need to have corrisponding "full" images to match their associated image.
        self.original = Image.open(self.path)

        self.full = self.original.copy()
        self.full.resize(self.associated_main_image.full.size)
        
        #self.thumbnail = self.original.copy()
        #self.thumbnail.resize(self.associated_main_image.thumbnail.size)

        self.preview_fast = self.original.copy()
        self.preview_fast.resize(self.associated_main_image.preview_fast.size)

        self.preview = self.original.copy()
        self.preview.resize(self.associated_main_image.preview.size)
        

    def create_pixmap(self, pil_img):
        '''Pass in a PIL.Image object. Returns a QtGui.QPixmap object.'''
        
        pix_map = pil_img.toqpixmap()
        return pix_map
    
    def _create_dimensions(self, longest_desired_size):
        '''NOW OBSOLETE!!! Creates W and H of an image based on the longest edge's desired size. Returns Tuple (WxH).'''
        # UPDATE: THERE IS A BUILT IN FUNCTION FOR THIS OMG
        # Image().thumbnail(<width>, <height>)

        full_w, full_h = self.full.size
        if full_w >= full_h:    # width is larger
            downscale_ratio = full_w / longest_desired_size
            resized_w = longest_desired_size
            resized_h = floor(full_h / downscale_ratio)
            
        else:                   # height is larger
            downscale_ratio = full_h / longest_desired_size
            resized_h = longest_desired_size
            resized_w = floor(full_w / downscale_ratio)
        
        return resized_w, resized_h

        

class Sort_Gui(QtWidgets.QMainWindow, sorter_gui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class Sort_App():
    def __init__(self):
        '''This is the main program running the application.'''
        # Declare variables
        # Create UI object
        # Run UI setup stuff
        # Launch GUID

        all_options = _setup_all_sort_options()
        self.sort_parameters = all_options["parameters"]
        self.sort_interval_functions = all_options["interval functions"]
        self.sorting_functions = all_options["sorting functions"]

        self.gui_active_mask_section = None         # Updated whenever "self.gui_mask_option_select()" is run
        
        self.sorter_images = None                   # list of Sorter_Image objects used as main images
        self.sorter_image_masks = None              # list of Sorter_Image objects used for masks
        
        self.p_image_in = None      # LEGACY
        self.test_image = Path() / "images" / "DSC04688_EDIT_1000.jpg"


        # This is THE user interface
        self.app = QtWidgets.QApplication(sys.argv)
        self.gui = Sort_Gui()
        self.setup_gui()
        self.app_launch()

    def setup_gui(self):
        '''Links gui elements to actions'''

        ### RADIO BUTTIONS AND WINDOW ###
        gui = self.gui
        self.gui_mask_radios = {
            "none" : gui.rb_mask_none,
            "single" : gui.rb_mask_single,
            "folder" : gui.rb_mask_folder,
            }
        self.gui_mask_frames = {
            "none" : gui.f_hl_mask_none,
            "single" : gui.f_hl_mask_single,
            "folder" : gui.f_vl_mask_folder,            
            }
        
        gui.rb_mask_none.clicked.connect(lambda: self.gui_mask_option_select())
        gui.rb_mask_single.clicked.connect(lambda: self.gui_mask_option_select())
        gui.rb_mask_folder.clicked.connect(lambda: self.gui_mask_option_select())
        self.gui_mask_option_select()

        gui.b_choose_image.pressed.connect(lambda: self.show_image_picker(
            sorter_image_type="main", label_wig=gui.l_loaded_image_preview)
            )
        gui.b_choose_mask.pressed.connect(lambda: self.show_image_picker(
            sorter_image_type="mask", label_wig=gui.l_loaded_mask_preview)
            )
        gui.b_choose_mask_folder.pressed.connect(lambda: self.show_image_picker(
            sorter_image_type="mask", label_wig=gui.l_loaded_mask_preview)
            )

        # Sets the interval functions drop down by cycling through interval_functions_dict:
        '''
        for i, func_object in enumerate(self.sort_interval_functions.values()):
            gui.cb_interval_function.setItemText(index=i, text=func_object.name_display)
        ''' 
        gui.cb_interval_function.addItems([self.sort_interval_functions.values().name_display])

        gui.cb_interval_function.currentIndexChanged.connect(lambda: self.gui_cb_interval_function_changed())
            
    def gui_cb_interval_function_changed(self):
        '''Called whenever the user or program changes the option chosen in the combo box / dropdown.'''
        cb_text = self.gui.cb_interval_function.currentText()
        for func_object in self.sort_interval_functions.values():
            if cb_text == func_object.name_display:
                # set description
                # set helpers
                break
            else:
                pass

    def gui_mask_option_select(self):
        '''Finds the radio button selected and changes the mask frame that match the selection.'''
        for section, radio in self.gui_mask_radios.items():
            # enables the frames based on radiobutton checked
            self.gui_mask_frames[section].setHidden(not radio.isChecked())
            
            # updates the active section variable
            if radio.isChecked():
                self.gui_active_mask_section = section


    def test(self, what_to_print="not set"):
        print(f"{what_to_print}")


    def show_image_picker(self, sorter_image_type="", label_wig=QtWidgets.QLabel):
        '''Opens the window to select an image in.
        Pass in how the image will be used ("main" or "mask") and the label widget that will display the thumbnail.'''
        
        picker = QtWidgets.QFileDialog(self.gui)
        # https://doc.qt.io/qtforpython/PySide2/QtWidgets/QFileDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QFileDialog.FileMode
        
        if sorter_image_type == "mask" and self.gui_active_mask_section == "folder":
            picker.setFileMode(QtWidgets.QFileDialog.Directory)
        else:
            picker.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
            picker.setMimeTypeFilters(['image/jpeg', 'image/png', 'image/tiff', "application/octet-stream"])
        p = str(Path().absolute())
        picker.setDirectory(p)
        picker.fileSelected.connect(lambda: self.images_picked(
            picker_wig=picker, sorter_image_type=sorter_image_type, label_wig=label_wig)
            )
        picker.show()


    def images_picked(self, picker_wig=QtWidgets.QFileDialog, sorter_image_type="", label_wig=QtWidgets.QLabel):
        '''Pass in a path to an image and the label widget that it show show up in.'''
        pic_urls = picker_wig.selectedFiles()
        if pic_urls:
            # Checks if what user selected is a dir or files:
            if Path(pic_urls[0]).is_dir():
                selected_dir = Path(pic_urls[0])
                files_in_folder = selected_dir.glob("*.*")
                pic_paths = [Path(pic) for pic in files_in_folder]
            else:   # files are images
                pic_paths = [Path(pic) for pic in pic_urls]

        # Creates Sorter_Image objs from the found pics:
        imgs = [(Sorter_Image(img_file_path=p, sorter_img_type=sorter_image_type)) for p in pic_paths]
        if sorter_image_type == "main":
            self.sorter_images = imgs
            [sorter_image.generate_image_sets() for sorter_image in self.sorter_images]         # Generates needed PIL images
            self.check_if_image_and_mask_image_share_a_path()
            first_img = self.sorter_images[0]
        elif sorter_image_type == "mask":
            self.sorter_image_masks = imgs
            [sorter_image.generate_core_mask_sets() for sorter_image in self.sorter_images]     # Generates needed PIL images
            self.check_if_image_and_mask_image_share_a_path()
            
            if self.gui_active_mask_section == "folder":
                # add paths to scroll_area_found_masks widget
                pass
            elif self.gui_active_mask_section == "single":
                first_img = self.sorter_image_masks[0]

      
        # Displays first image's thumbnail:
        try:        # first_img may not have been set.    
            pix_map = first_img.create_pixmap(first_img.thumbnail)
            label_wig.setPixmap(pix_map)
            label_wig.setMaximumSize(QtCore.QSize(200, 200))
            
            # self.l_loaded_image_preview.setMaximumSize(QtCore.QSize(200, 200))
        except:
            pass


        self.process_events()
    
    
    def check_if_image_and_mask_image_share_a_path(self):
        '''Checks if new images overlap with any previously selected images by comparing Paths.'''
        if self.sorter_images and self.sorter_image_masks:
            for mask in self.sorter_image_masks:
                if mask.path in [img.path for img in self.sorter_images]:
                    self.sorter_image_masks.remove(mask)

    def ultra_funct(self):
        sort_settings_list = []

        if mask_user_selection == "None":
            p_masks = None
            sort_settings_list = [sort_settings.copy()]
        elif mask_user_selection == "Single":
            settings_with_mask = sort_settings.copy()
            settings_with_mask["mask_image"] = p / d_images / "Masks" / mask_selected
            sort_settings_list.append(settings_with_mask)
        elif mask_user_selection == "Folder":
            for p_mask in p_masks:
                settings_with_mask = sort_settings.copy()
                settings_with_mask["mask_image"] = p_mask
                sort_settings_list.append(settings_with_mask)     
        else:
            print("error")

        QtWidgets.QStackedWidget.changeEvent()
        

        '''
        if not mask_user_selection in ["Single", "Folder"] or (["", None] in p_masks and sort_settings["mask_image"] == None):
            # Not using masks:
            p_masks = None
            sort_settings_list = [sort_settings]
        else:
            # Using mask(s):
            for p_mask in p_masks:
                settings_with_mask = sort_settings.copy()
                settings_with_mask["mask_image"] = p_mask
                sort_settings_list.append(settings_with_mask)
        '''

        for settings in sort_settings_list:
            settings_changed = {}
            for s_name, s_df_val in sort_settings_default.items():
                    s_val = settings[s_name]            
                    if s_val != s_df_val:
                        if s_name == "mask_image":
                            try:
                                s_val = s_val.stem
                            except:
                                s_val = "error"                
                        print(f"{s_name} set to {s_val} (from {s_df_val}).")
                        settings_changed[s_name] = s_val
            
            # take the changed settings and make a naming out of it.
            settings_changed_formatted = "_".join([f"{name}-{val}" for name, val in settings_changed.items()])
            # Adds a section to the sort_settings so that the name can be retreived later.
            settings["settings_changed_formatted"] = settings_changed_formatted
            print(f"Settings changed: {settings_changed_formatted}")


        for settings in sort_settings_list:

            settings_changed_formatted = settings["settings_changed_formatted"]
            image_p_out = p / d_images / "SORTED" / f"{image_p_in.stem}_SORTED_{settings_changed_formatted}{image_p_in.suffix}"
            img = Image.open(image_p_in)
            try:
                img_mask = Image.open(settings["mask_image"])
            except:
                img_mask = None

            img_sorted = pixelsort(
                img,
                mask_image=img_mask,
                interval_image=settings["interval_image"],
                randomness=settings["randomness"],
                clength=settings["clength"],
                sorting_function=settings["sorting_function"],
                interval_function=settings["interval_function"],
                lower_threshold=settings["lower_threshold"],
                upper_threshold=settings["upper_threshold"],
                angle=settings["angle"]
                )

            #img_sorted = pixelsort(img, interval_function="edges", )

            img_rgb = img_sorted.convert("RGB")
            img_rgb.save(image_p_out)

            # Loading PILLOW images directly into PyQt5 (without saving them)
            # SHOULD WORK:
            #qim = ImageQt.fromqimage(img_rgb)
            #pix = QtGui.QPixmap.fromImage(qim)

            print(f"Saved image path: {image_p_out.absolute()}")
            sleep(1)
            img_rgb.show()

        #img_sorted = Image.SAVE("SORTED.jpg")

        print("Done")


    def process_events(self):
        '''Forces Qt Application to "processEvents"'''
        QtGui.QGuiApplication.processEvents()


    def app_launch(self):
        '''Runs the app. Basically the last step.'''
        #self.app = QtWidgets.QApplication(sys.argv)
        self.gui.show()
        self.app.exec_()


'''
class ImagePicker:
    def __init__(self, ui):
        self.ui = ui

    def get_widget(self):
        picker = QtWidgets.QFileDialog(self.ui)
        # https://doc.qt.io/qtforpython/PySide2/QtWidgets/QFileDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QFileDialog.FileMode
        picker.setFileMode(QtWidgets.QFileDialog.ExistingFiles)        # This works
        #picker.setFileMode(QtWidgets.QFileDialog.Directory)            # This works

        #picker.setMimeTypeFilters(['image/jpeg', 'image/png', 'image/bmp', 'image/tiff', 'image/gif', 'image/webp', QtWidgets.QFileDialog.Directory])
        picker.setMimeTypeFilters(['image/jpeg', 'image/png', 'image/tiff', "application/octet-stream"])
        #picker.setMimeTypeFilters("Images Files (*jpeg *png *tiff);;Directory (*)")
        picker.show()
        return picker
'''

if __name__ == '__main__':
    sa = Sort_App()
    #sa.app_launch()
