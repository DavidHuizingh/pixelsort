from pixelsort import pixelsort
from PIL import Image, ImageQt
from pathlib import Path
from time import sleep
from math import floor

import sys
#if __name__ == "__main__":
from PySide2 import QtWidgets, QtGui, QtCore


#QApplication = QtWidgets.QApplication

from pixel_sorter_gui import Ui_MainWindow as sorter_gui
from CustomWidgets.Param_Slider import Param_Slider
from CustomWidgets.Param_Clength import Param_Clength
from CustomWidgets.QtImageViewer_Pyside2 import QtImageViewer

from multiprocessing import Process, freeze_support
import qdarkgraystyle
import qdarkstyle
style = qdarkstyle

dev_debug = True
#debug_image_main = "images/squirrel.jpg"
debug_image_main = "images/DSC04688.JPG"
debug_image_mask = "images/Masks/Head circle_Inverted.jpg"
 

def _setup_all_sort_options():
    '''Sets up parameter, interval function, and sorting function options.
    Passes back a dictionary of dictionaries.'''
    ## PARAMETERS (for those that make sense to do so for):
    # https://github.com/satyarth/pixelsort#parameters
    parameter_randomness = Option()
    parameter_randomness._setup(isParam=True, name="randomness", name_display="Randomness", isEnabled=True,
        desc="What percentage of intervals not to sort. 0 by default.",
        val_default=0, val_range_min=0, val_range_max=100, slider_tick_interval=10,
        associated_parameters=None, parameter_always_visible=True)

    parameter_threshold_lower = Option()
    parameter_threshold_lower._setup(isParam=True, name="threshold_lower", name_display="Threshold - L", isEnabled=True,
        desc="How dark must a pixel be to be considered as a 'border' for sorting? Takes values from 0-1. 0.25 by default. Used in edges and threshold modes.",
        val_default=.25, val_range_min=0, val_range_max=100, slider_tick_interval=10,
        associated_parameters=None, parameter_always_visible=False)

    parameter_threshold_upper = Option()
    parameter_threshold_upper._setup(isParam=True, name="threshold_upper", name_display="Threshold - U", isEnabled=True,
        desc="How bright must a pixel be to be considered as a 'border' for sorting? Takes values from 0-1. 0.8 by default. Used in threshold mode.",
        val_default=.8, val_range_min=0, val_range_max=100, slider_tick_interval=10,
        associated_parameters=None, parameter_always_visible=False)

    parameter_clength = Option()
    parameter_clength._setup(isParam=True, name="clength", name_display="Characteristic Length", isEnabled=True,
        desc="Characteristic length for the random width generator. Used in mode random and waves.",
        val_default=50, val_range_min=0, val_range_max=None,
        associated_parameters=None, parameter_always_visible=False)

    parameter_angle = Option()
    parameter_angle._setup(isParam=True, name="angle", name_display="Angle", isEnabled=True,
        desc="Angle at which you're pixel sorting in degrees. 0 (horizontal) by default.",
        val_default=0, val_range_min=0, val_range_max=360, slider_tick_interval=15,
        associated_parameters=None, parameter_always_visible=True)

    parameters_list = [
        parameter_randomness,
        parameter_threshold_lower,
        parameter_threshold_upper,
        parameter_clength,
        parameter_angle        
        ]

    
    ## INTERVAL FUNCTIONS ###
    # https://github.com/satyarth/pixelsort#interval-functions
    interval_func_random = Option()
    interval_func_random._setup(isParam=False, name="random", name_display="Random", isEnabled=True,
        desc="Randomly generate intervals. Distribution of widths is linear by default. Interval widths can be scaled using clength.",
        val_default=None, val_range_min=None, val_range_max=None,
        associated_parameters=[parameter_clength]) #clength

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
        associated_parameters=[parameter_clength]) #clength
    # Disabled:
    interval_func_file = Option()
    interval_func_file._setup(isParam=False, name="file", name_display="File", isEnabled=False,
        desc="Intervals taken from another specified input image. Must be black and white, and the same size as the input image.",
        val_default=None, val_range_min=None, val_range_max=None,
        associated_parameters=None) #???
    # Disabled:
    interval_func_file_edges = Option()
    interval_func_file_edges._setup(isParam=False, name="file-edges", name_display="File-Edges", isEnabled=False,
        desc="Intevals defined by performing edge detection on the file specified by -f. Must be the same size as the input image.",
        val_default=None, val_range_min=None, val_range_max=None,
        associated_parameters=None) #???

    interval_func_none = Option()
    interval_func_none._setup(isParam=False, name="none", name_display="None", isEnabled=True,
        desc="Sort whole rows, only stopping at image borders.",
        val_default=None, val_range_min=None, val_range_max=None,
        associated_parameters=None) #???

    interval_function_list = [
        interval_func_random,
        interval_func_edges,
        interval_func_threshold,
        interval_func_waves,
        interval_func_file,
        interval_func_file_edges,
        interval_func_none
        ]

    # Creates dictionary of all the enabled parameters. 
    # <parameter name>, <parameter object>
    parameters_dict = {param.name: param for param in parameters_list if param.isEnabled}

    # Creates dictionary of all the enabled functions. 
    # <function name>, <function object>
    interval_functions_dict = {func.name : func for func in interval_function_list if func.isEnabled}

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
        self.slider_tick_interval = None
        self.associated_parameters = None       # if function
        self.parameter_always_visible = None
        self.pw = None                          # pw (parameter widget) if parameter
        self.slider_val = None                  #
        self.app_ui_update_method = None            # Sort_App method to that should be called when these parameters are interacted with. 

    def _setup(self, isParam, name, name_display, isEnabled, desc, val_default=None, val_range_min=None, val_range_max=None, slider_tick_interval=None, associated_parameters=None, parameter_always_visible=None):
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
        self.slider_tick_interval = slider_tick_interval
        self.associated_parameters = associated_parameters
        self.parameter_always_visible = parameter_always_visible

    def set_visibility_parameter_widget(self, isVisible):
        '''Allows a parameter to hide it's own widget.'''

        self.pw.Frame.setVisible(isVisible)

    def generate_param_widget(self, frame, app_ui_update_method):
        '''Pass in a QFrame that this widget will be constructed in.
        Creates the parameter widget to be used in the UI.'''

        self.app_ui_update_method = app_ui_update_method
        if self.name == "clength":
            self.pw = Param_Clength()
            self.pw.setupUi(Frame=frame, param_name=self.name)
            self.pw.t_param_clength.setText(self.name_display)
            self.pw.t_param_clength_desc.setText(self.desc)
            q_validator = QtGui.QIntValidator()
            q_validator.setBottom(0)
            self.pw.tb_param_clength.setValidator(q_validator)
            self.pw.tb_param_clength.setText(f"{self.val_default}")

            self.pw.tb_param_clength.editingFinished.connect(lambda:
                self._validate_tb_and_update_values(tb=self.pw.tb_param_clength)
                )

        else: #SLIDERS
            self.pw = Param_Slider()

            # SLIDER WITH TB:
            if self.name == "angle":
                self.pw.setupUi(Frame=frame, param_name=self.name, is_value_display_tb=True)
                # Setup textbox
                self.pw.tb_param_generic_value.setText(str(self.val_default))
                q_validator = QtGui.QIntValidator()
                q_validator.setRange(self.val_range_min, self.val_range_max)
                self.pw.tb_param_generic_value.setValidator(q_validator)
                self.pw.tb_param_generic_value.editingFinished.connect(lambda:
                    self._validate_tb_and_update_values(
                        tb=self.pw.tb_param_generic_value,
                        slider=self.pw.slider_param_generic)
                        )
            # SLIDER NO TB:
            else:
                self.pw.setupUi(Frame=frame, param_name=self.name)
                self.pw.t_param_generic_value.setText(str(self.val_default))
            
            self.pw.t_param_generic.setText(self.name_display)
            self.pw.t_param_generic_desc.setText(self.desc)            
            
            self.pw.slider_param_generic.setMinimum(self.val_range_min)
            self.pw.slider_param_generic.setMaximum(self.val_range_max)
            self.pw.slider_param_generic.setTickInterval(self.slider_tick_interval)
            
            if self.name in ["threshold_lower", "threshold_upper"]:
                # Store method as object to be called later:
                self.conversion_method = self._val_converter_threshold
                input_to_slider = self.val_default * 100
                self.pw.slider_param_generic.setValue(input_to_slider)
            else:
                # Store method as object to be called later:
                self.conversion_method = self._val_converter_none
                self.pw.slider_param_generic.setValue(self.val_default)
            
            # SLIDER WITH TB:
            if self.name == "angle":
                self._update_slider_display_and_values(tb=self.pw.tb_param_generic_value)
                self.pw.slider_param_generic.valueChanged.connect(lambda:
                    self._update_slider_display_and_values(tb=self.pw.tb_param_generic_value)
                    )
                # Only call UI update when RELEASED:
                self.pw.slider_param_generic.sliderReleased.connect(lambda:
                    self.app_ui_update_method()
                    )              
            # SLIDER WITH NO TB:
            else:
                self._update_slider_display_and_values()
                self.pw.slider_param_generic.valueChanged.connect(lambda:
                    self._update_slider_display_and_values()
                    )
                # Only call UI update when RELEASED:
                self.pw.slider_param_generic.sliderReleased.connect(lambda:
                    self.app_ui_update_method()
                    )

    # SLIDERS BOXES:    
    def _update_slider_display_and_values(self, tb=None):
        '''Called whenever slider value changes.
        Applies any conversions needed, updates value displayed, and stores the value for when the pixel_sorter is called.'''

        s_val = self.pw.slider_param_generic.value()
        # The magic of storing a method as an object happens here:
        self.val_current = self.conversion_method(s_val)
        if tb is None:
            self.pw.t_param_generic_value.setText(str(self.val_current))
        else:
            tb.setText(str(self.val_current))

    def _val_converter_threshold(self, slider_val):
        '''Converts slider value -> value within range. Method used by both parameter thresholds.'''
        converted_val = slider_val / 100
        return converted_val
    def _val_converter_none(self, slider_val):
        '''Throwaway method. Passes back value passed in. Hot potato.'''
        return slider_val

    # TEXT BOXES:
    def _validate_tb_and_update_values(self, tb, slider=None):
        '''Pass in the text box that needs validating. It will also update the slider to the tb's value if one is passed in.
        This method makes sure text entered in box is numerical.'''
        # The QIntValidator should force this value to be an int already.

        tb_text = tb.text()        
        if tb_text in ["", None]:
            pass
        elif tb_text.isnumeric:
            self.val_current = int(tb_text)
            if slider is not None:
                slider.setValue(self.val_current)
        # Calls app's method that updates UI
        self.app_ui_update_method()       

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

    def generate_image_sets(self, is_image_file=True):
        '''Creates thumbnail, preview, preview_fast, and full images'''
        # TODO: This is a waste of processing since only one or two images are actually needed.
        # Change child image creation to happen "on demand" instead of pre-creating everything.

        if is_image_file:
            self.full = Image.open(self.path)
        else:
            # If making a Sorter_Image from an unsaved image, the self.full needs to be set before this is called.
            pass

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

    def match_image_size(self, image_to_match):
        '''Pass in a PIL object. Returns a PIL Image that matches the dimensions of the one passed in.'''
        
        #image_resized = self.original.copy()
        image_resized = self.original.copy().resize(image_to_match.size)
        return image_resized

    def create_pixmap(self, pil_img):
        '''Pass in a PIL.Image object. Returns a QtGui.QPixmap object.'''
        
        pix_map = pil_img.toqpixmap()
        return pix_map

    def get_picture_size(self, picture_size):
        '''Picture size can be "full", "preview", or "fast". Returns the Image of the specificed size.'''

        if picture_size == "full":
            return self.full
        elif picture_size == "preview":
            return self.preview
        elif picture_size == "fast":
            return self.preview_fast       
        
class Sort_Gui(QtWidgets.QMainWindow, sorter_gui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class Sort_App():

    class Decorators():
        # First time using decorators.
        # The solution on how to use decorators in classes was inspired by this article:
        # https://medium.com/@vadimpushtaev/decorator-inside-python-class-1e74d23107f6
        # And extended in order to call Sort_App variables using this guide:
        # https://stackoverflow.com/questions/7590682/access-self-from-decorator
        
        # TEMPLATE:
        '''
        @classmethod
        def dec_name(cls_d, func):
            def _dec_name(self, *args, **kwargs):

                func_return = func(self, *args, **kwargs)
                
                return func_return
            return _dec_name
        '''
        @classmethod
        def fast_preview_check(cls_d, func):
            def _fast_preview(self, *args, **kwargs):
                #print('''Decorator: "fast_preview_check" called''')
                func_return = func(self, *args, **kwargs)
                if not self.gui.cb_live_preview.isChecked():
                    pass
                else:   # is Checked
                    try:
                        self.generate_sorts(desired_picture_size="fast")
                    except:
                        print('''Decorator: "fast_preview_check" failed.''')
                
                return func_return
            return _fast_preview

        @classmethod
        def image_size_warning_check(cls_d, func):
            def _image_size_warning_check(self, *args, **kwargs):
                #print('''Decorator: "image_size_warning_check" called''')
                func_return = func(self, *args, **kwargs)
                # Relies on self.sorter_images.
                try:
                    first_image = self.sorter_images[0]
                except:
                    first_image = None
                if first_image:
                    image_size = first_image.full.size
                    if all(res > 2000 for res in image_size):
                        warning_label = self.gui.t_image_size_warning_dynamic   
                        warning_label.setHidden(False)
                        warning_label.setText(f'''*Warning: large image size ({image_size[0]}x{image_size[1]}). This will take a while to process. Consider checking the "preview" option.''')

                        # If the preview option is checked, this warning will be "striked out":
                        f = warning_label.font()
                        f.setStrikeOut(self.gui.cb_sort_option_preview.isChecked())
                        warning_label.setFont(f)
                    else:
                        self.gui.t_image_size_warning_dynamic.setHidden(True)

                return func_return
            return _image_size_warning_check

        ### DECORATOR TESTS ###
        @classmethod
        def dec_test_sort_app_variables(cls_d, func):
            #passed_tp = self.passed_tp
            def wrapper(self, *args, **kwargs):
                #print(f"test_print = {passed_tp}")
                #print(f"Self is {self}")
                app_text = self.gui.t_image_size_warning_dynamic.text()
                print(f"warning label text = {app_text}")
                func_return = func(self, *args, **kwargs)
                print("Ended")
                return func_return
            return wrapper

        @classmethod
        def dec_test(cls_d, func):
            def wrapper(self, *args, **kwargs):
                print("Started")
                func_return = func(self, *args, **kwargs)
                print("Ended")
                return func_return
            return wrapper

    def __init__(self):
        '''This is the main program running the application.'''
        # Declare variables
        # Create UI object
        # Run UI setup stuff
        # Launch GUID
        self.test_print = 20
        all_options = _setup_all_sort_options()
        self.sort_parameters = all_options["parameters"]
        self.sort_interval_functions = all_options["interval functions"]
        self.sorting_functions = all_options["sorting functions"]

        self.gui_active_mask_section = None         # Updated whenever "self.gui_mask_option_select()" is run
        
        self.sorter_images = None                   # list of Sorter_Image objects used as main images
        self.sorter_image_masks = None              # list of Sorter_Image objects used for masks
        self.output_dir = None        
        self.p_image_in = None      # LEGACY
        self.test_image = Path() / "images" / "DSC04688_EDIT_1000.jpg"

        # This is THE user interface
        self.app = QtWidgets.QApplication(sys.argv)
        self.gui = Sort_Gui()
        self.setup_gui()
        if dev_debug:
            self.setup_debugging()
        self.app_launch()

    def setup_debugging(self):
        '''Developer options'''

        def load_image_main():
            self.images_picked(picker_wig=None,
                sorter_image_type="main",
                label_wig=self.gui.l_loaded_image_preview,
                debug_override_images=[debug_image_main]
                )
        def load_image_mask():
            self.images_picked(picker_wig=None,
                sorter_image_type="mask",
                label_wig=self.gui.l_loaded_mask_preview,
                debug_override_images=[debug_image_mask]
                )

        load_image_main()
        load_image_mask()

    @Decorators.image_size_warning_check
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

        gui.b_choose_image.pressed
        gui.b_choose_image.clicked.connect(lambda: self.show_image_picker(
            sorter_image_type="main", label_wig=gui.l_loaded_image_preview)
            )
        gui.b_load_current.clicked.connect(lambda: self.make_sorter_image_from_sorted_image())


        gui.b_choose_mask.clicked.connect(lambda: self.show_image_picker(
            sorter_image_type="mask", label_wig=gui.l_loaded_mask_preview)
            )
        gui.b_choose_mask_folder.clicked.connect(lambda: self.show_image_picker(
            sorter_image_type="mask", label_wig=gui.l_loaded_mask_preview)
            )
        
        gui.b_choose_save_location.pressed.connect(lambda: self.select_output_location())
        self.output_dir = Path(__file__).parent
        gui.t_save_location_current.setText(str(self.output_dir.absolute()))

        # Sets the interval functions drop down by cycling through interval_functions_dict:
        for func_object in self.sort_interval_functions.values():
            gui.cb_interval_function.addItem(func_object.name)
            # Commented out because this sets the tool tip of the "drop down" and not per item inside of it.
            # Basically, can only hold 1 value 
            #gui.cb_interval_function.setToolTip(func_object.desc)

        # fancy way of setting "description" field for current index.
        gui.t_interval_function_desc.setText(
            self.sort_interval_functions[gui.cb_interval_function.currentText()].desc                
            )
        
        gui.cb_interval_function.currentIndexChanged.connect(lambda:
            self.gui_cb_interval_function_changed()
            )
        
        ### SETUP PARAMETERS ###        
        for param_obj in self.sort_parameters.values():
            # Creates a QFrame, parents it, adds it to the layout, and passes it into the parameter to generate the rest of the widget.
            frame = QtWidgets.QFrame(parent=self.gui.scroll_area_settings_content)
            self.gui.vl_parameters.addWidget(frame)
            param_obj.generate_param_widget(frame=frame, app_ui_update_method=self.update_ui_from_param)
            
        ### SETUP PIXEL ORDERING ###
        for name in self.sorting_functions.keys():
            gui.cb_pixel_ordering_option.addItem(name)
            #gui.cb_pixel_ordering_option.setToolTip(desc)

        gui.t_pixel_ordering_option_desc.setText(
                self.sorting_functions[gui.cb_pixel_ordering_option.currentText()]                
                )

        def pixel_ordering_option_changed():
            # sorting_functions are simple dictionaries:
            # "sort name" : "sort description"
            sorting_option_desc = self.sorting_functions[gui.cb_pixel_ordering_option.currentText()]
            self.gui.t_pixel_ordering_option_desc.setText(sorting_option_desc)
            self.update_ui_from_param()

        gui.cb_pixel_ordering_option.currentIndexChanged.connect(lambda:
            pixel_ordering_option_changed()
            )

        ### IMAGE OUTPUT BUTTONS ###
        gui.b_generate_pixel_sort.pressed.connect(lambda:
            self.pixel_sort_called()
            )

        gui.b_save_image.pressed.connect(lambda:
            self.save_image_handler()
            )

        ### IMAGE DISPLAY ###

        # 

        ### OTHER ###
        gui.b_open_in_native_viewer.pressed.connect(lambda:
            self.open_in_native_viewer_handler(button_pressed=True)
            )

        gui.cb_live_preview.clicked.connect(lambda:
            self.update_ui_from_param()
            )

        self.gui_cb_interval_function_changed()

        gui.cb_sort_option_preview.clicked.connect(lambda:
            self.update_ui_from_param()
            )

        self.update_ui_preview_label_size()

        ### SET STYLING ###
        self.app.setStyleSheet(style.load_stylesheet())
    
    @Decorators.fast_preview_check
    @Decorators.image_size_warning_check
    def update_ui_from_param(self):
        '''Calling this method will trigger UI related decorators attached to it.
        This method is just a dummy and is used purely to call these decorators.'''
        pass

    def update_ui_preview_label_size(self, original_img=None, sorted_img=None, img_name = None):
        '''Updates the UI to display information about the image's resolution.
        If parameters are incomplete, text will be set to "------".'''
        
        blank = "-------"        
        if img_name is None:
            img_name = blank        

        try:
            size_original, size_display = (f"{original_img.size[0]}x{original_img.size[1]}", f"{sorted_img.size[0]}x{sorted_img.size[1]}")
        except:
            size_original, size_display = (blank, blank)
        
        try:
            image_ratio = (sorted_img.size[0] / original_img.size[0])
        except:
            image_ratio = blank
        
        self.gui.t_image_preview_orig_name_dyn.setText(f'''Image Name: {img_name}''')
        self.gui.t_image_preview_sizes_dyn.setText(f'''Sizes:\n- original ({size_original}),\n- displayed ({size_display})''')
        self.gui.t_image_preview_ratio_dyn.setText(f'''Displayed Ratio: {image_ratio}''')

    def open_in_native_viewer_handler(self, PIL_image=None, button_pressed=False):
        '''Checks to see if image should be opened in user's native image viewing app.'''
        # This method needs either an PIL image passed in, or for an output image file to have been saved.

        if self.gui.cb_post_sort_option_picture_viewer.isChecked() or button_pressed:
            try:
                try:
                    PIL_image = self.image_sorted
                except:
                    if PIL_image == None:
                        PIL_image = Image.open(self.output_file)
                PIL_image.show()
            except:
                pass

    def fast_preview_handler(self):
        '''Call this every time a fast preview might want to be generated.'''

        if self.gui.cb_live_preview.isChecked():
            if self.sorter_images != None:
                self.generate_sorts(desired_picture_size="fast")

    def pixel_sort_called(self):
        '''Called whenever a button is pressed.'''

        # Runs all the required methods in respect to user's settings and post-processed options.
        if self.gui.cb_sort_option_preview.isChecked():
            desired_picture_size = "preview"
        else:
            desired_picture_size = "full"
        
        self.generate_sorts(desired_picture_size=desired_picture_size)

    def save_image_handler(self):
        '''Called when the "save" button is pressed.'''

        if self.output_file:
            # Code below prevents overriding existing images:
            output_file_valid = self.output_file
            i = 0
            while output_file_valid.exists():
                i += 1
                output_file_valid = self.output_file / f"_{i}"
            
            self.image_sorted.save(str(output_file_valid))
            #output_file_valid.save(self.image_sorted)
        else:
            print("No images could be saved :(")

    def generate_sorts(self, desired_picture_size):
        '''Starts the Pixel Sorting magic. desired_picture_size can be "full", "preview", or "fast".'''

        if self.gui.rb_mask_none.isChecked() or self.sorter_image_masks is None:
            areMaskedUsed = False
        else:
            areMaskedUsed = True

        for sorter_image in self.sorter_images:
            image = sorter_image.get_picture_size(picture_size=desired_picture_size)
            
            # If "fast_preview" is on, only generates the first mask and skips the rest.
            if desired_picture_size == "fast":
                if areMaskedUsed:       # Masks
                    sorter_mask = self.sorter_image_masks[0]
                    mask = sorter_mask.match_image_size(image_to_match=image)
                else:                   # No Masks
                    sorter_mask = None
                    mask = None
                
                self.image_sort_create(
                    desired_picture_size=desired_picture_size,
                    sorter_image=sorter_image, sorter_mask=sorter_mask,
                    image=image, image_mask=mask)

            # If "full" or "preview" but doesn't have a mask:
            elif not areMaskedUsed:       # If using a mask:
                self.image_sort_create(
                    desired_picture_size=desired_picture_size,
                    sorter_image=sorter_image, image=image)
                if self.gui.cb_post_sort_option_save_on_create.isChecked():
                    self.save_image_handler()
                    self.open_in_native_viewer_handler(PIL_image=self.image_sorted)

            # "full" or "preview" with mask(s):
            else:
                for sorter_mask in self.sorter_image_masks:
                    mask = sorter_mask.match_image_size(image_to_match=image)
                    self.image_sort_create(
                        desired_picture_size=desired_picture_size,
                        sorter_image=sorter_image, sorter_mask=sorter_mask,
                        image=image, image_mask=mask)
                    if self.gui.cb_post_sort_option_save_on_create.isChecked():
                        self.save_image_handler()
                        self.open_in_native_viewer_handler(PIL_image=self.image_sorted)

    def image_sort_create(self, desired_picture_size, sorter_image, image, sorter_mask=None, image_mask=None):
        '''Sorts pixels, sets Pixmap, creates output file path (doesn't save). If no masks are used, don't pass in any masks.'''
        
        clength_full = self.sort_parameters["clength"].val_current
        size_f = sorter_image.full.size[0]
        size_desired = image.size[0]
        clength_adjusted = int(clength_full / (size_f / size_desired))
        
        image_sorted = pixelsort(
            image=image,
            mask_image=image_mask,
            interval_image=None,
            randomness=self.sort_parameters["randomness"].val_current,
            clength=clength_adjusted,
            sorting_function=self.gui.cb_pixel_ordering_option.currentText(),
            interval_function=self.gui.cb_interval_function.currentText(),
            lower_threshold=self.sort_parameters["threshold_lower"].val_current,
            upper_threshold=self.sort_parameters["threshold_upper"].val_current,
            angle=self.sort_parameters["angle"].val_current
            ).convert("RGB")

        pix_map = image_sorted.toqpixmap()
        self.gui.image_viewer_hq.setImage(pix_map)
        self.process_events()

        # Sets up the output file for the "save" function.
        if image_mask is None:
            mask_str = ""
        else:
            mask_str = f"Mask-{sorter_mask.path.stem}_"
        self.output_file = self.output_dir / f"{sorter_image.path.stem}_{mask_str}{desired_picture_size}{sorter_image.path.suffix}"
        
        self.update_ui_preview_label_size(
            original_img=sorter_image.full,
            sorted_img=image_sorted,
            img_name=sorter_image.path.name)
        
        self.image_sorted = image_sorted
        return self.image_sorted
    
    @Decorators.fast_preview_check
    def gui_cb_interval_function_changed(self):
        '''Called whenever the user or program changes the option chosen in the combo box / dropdown.
        Sets the visibility of the parameters based on the option chosen.'''
        cb_text = self.gui.cb_interval_function.currentText()
        for func_object in self.sort_interval_functions.values():
            if cb_text == func_object.name.lower():
                self.gui.t_interval_function_desc.setText(func_object.desc)
                # Turns "optional" widgets off and permanent widgets on
                [param_obj.set_visibility_parameter_widget(param_obj.parameter_always_visible) for param_obj in self.sort_parameters.values()]

                # Turns on associated parameters:
                if func_object.associated_parameters is not None:
                    for param_obj in func_object.associated_parameters:
                        param_obj.set_visibility_parameter_widget(True)
                break

    def gui_mask_option_select(self):
        '''Finds the radio button selected and changes the mask frame that match the selection.'''
        for section, radio in self.gui_mask_radios.items():
            # enables the frames based on radiobutton checked
            self.gui_mask_frames[section].setHidden(not radio.isChecked())
            
            # updates the active section variable
            if radio.isChecked():
                self.gui_active_mask_section = section

    def show_image_picker(self, sorter_image_type, label_wig):
        '''Opens the window to select an image in.
        Pass in how the image will be used ("main" or "mask") and the label widget that will display the thumbnail.'''
        
        children = self.gui.findChildren(QtWidgets.QFileDialog)
        if children:
            print("Dialog box already open. Preventing more occurrences.")
        else:
            picker = QtWidgets.QFileDialog(self.gui)
            # https://doc.qt.io/qtforpython/PySide2/QtWidgets/QFileDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QFileDialog.FileMode
            
            if sorter_image_type == "mask" and self.gui_active_mask_section == "folder":
                picker.setFileMode(QtWidgets.QFileDialog.Directory)
            elif sorter_image_type == "main":
                picker.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
                picker.setMimeTypeFilters(['image/jpeg', 'image/png', 'image/tiff', "application/octet-stream"])
            p = str(Path().absolute())
            picker.setDirectory(p)
            picker.fileSelected.connect(lambda: self.images_picked(
                picker_wig=picker, sorter_image_type=sorter_image_type, label_wig=label_wig)
                )
            picker.show()

    @Decorators.image_size_warning_check
    def images_picked(self, picker_wig, sorter_image_type, label_wig, debug_override_images=None):
        '''Pass in a path to an image and the label widget that it show show up in.'''
        
        if not debug_override_images:
            pic_urls = picker_wig.selectedFiles()
            picker_wig.setParent(None)
        
        else:
            pic_urls = debug_override_images

        if pic_urls:
            # Checks if what user selected is a dir or files:
            if Path(pic_urls[0]).is_dir():
                selected_dir = Path(pic_urls[0])
                
                files_in_folder = []
                for file_type in ["*.jpg", "*.png", "*.bmp", "*.tiff"]:
                    files_in_folder.extend(selected_dir.glob(file_type))
                #files_in_folder = selected_dir.glob("*.*")

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
            [sorter_image.generate_core_mask_sets() for sorter_image in self.sorter_image_masks]     # Generates needed PIL images
            self.check_if_image_and_mask_image_share_a_path()

            if self.gui_active_mask_section == "folder":
                # add paths to scroll_area_found_masks widget
                
                self.remove_folder_text(associated_wig=self.gui.scroll_area_found_masks)

                # These are reversed only because I want them in alphabetical order :). As is, the list is already in
                # alphabetical order, but I add them to the list from the bottom up so I can keep the spacer at the bottom.
                for sorter_mask in reversed(self.sorter_image_masks):
                    self.add_folder_text(associated_wig=self.gui.scroll_area_found_masks, img_path=sorter_mask.path)
                    
            elif self.gui_active_mask_section == "single":
                first_img = self.sorter_image_masks[0]

        # Displays first image's thumbnail:
        try:        # first_img may not have been set.    
            pix_map = first_img.create_pixmap(first_img.thumbnail)
            label_wig.setPixmap(pix_map)
            label_wig.setMaximumSize(QtCore.QSize(200, 200))
        except:
            pass
        self.process_events()

    @Decorators.image_size_warning_check
    def make_sorter_image_from_sorted_image(self):
        '''Takes the currently sorted image and makes it the new image that will be processed.'''
        try:
            sorter_image =self.sorter_images[0]
            new_sorter_image = Sorter_Image(img_file_path=sorter_image.path, sorter_img_type=sorter_image.type)
            # Loads PIL sorted image to Sorter_Images's "full" area
            new_sorter_image.full = self.image_sorted
            new_sorter_image.generate_image_sets(is_image_file=False)
            self.sorter_images=[new_sorter_image]
            
            # Sets preview
            pix_map = new_sorter_image.create_pixmap(new_sorter_image.thumbnail)
            self.gui.l_loaded_image_preview.setPixmap(pix_map)
        except:
            print("Couldn't make new image from currently sorted image.")

    def add_folder_text(self, associated_wig, img_path):
        '''Adds text to associated widget'''

        mask_label = QtWidgets.QLabel(associated_wig)
        mask_label.setObjectName(f"t_found_mask_{img_path.stem}")
        mask_label.setText(f"{img_path.name}")
        self.gui.vl_found_masks.insertWidget(0, mask_label)

    def remove_folder_text(self, associated_wig):
        '''Removes all text in the associated widget'''

        children = self.gui.scroll_area_found_masks.children()
        for child in children:
            if type(child) == QtWidgets.QLabel:
                child.setParent(None)

    def check_if_image_and_mask_image_share_a_path(self):
        '''Checks if new images overlap with any previously selected images by comparing Paths.'''

        if self.sorter_images and self.sorter_image_masks:
            for mask in self.sorter_image_masks:
                if mask.path in [img.path for img in self.sorter_images]:
                    self.sorter_image_masks.remove(mask)

    def select_output_location(self):
        '''Opens the window to select where the created image(s) will be saved in.'''

        children = self.gui.findChildren(QtWidgets.QFileDialog)
        if children:
            print("Dialog box already open. Preventing more occurrences.")
        else:
            output_picker = QtWidgets.QFileDialog(self.gui)
            output_picker.setFileMode(QtWidgets.QFileDialog.Directory)
            p = str(Path().absolute())
            output_picker.setDirectory(p)
            output_picker.fileSelected.connect(lambda: self.output_location_selected(output_picker_wig=output_picker))
            output_picker.show()

    def output_location_selected(self, output_picker_wig=QtWidgets.QFileDialog):
        '''Called when user chooses the folder to output to.'''
        directory = output_picker_wig.selectedFiles()[0]      # SHOULD only return a Directory
        self.output_dir = Path(directory)
        self.gui.t_save_location_current.setText(str(self.output_dir.absolute()))
        # Makes sure widget is removed from main gui so that if this funct is called again, it can
        # prevent opening two dialog windows (not sure why this is a problem.)
        output_picker_wig.setParent(None)

    def process_events(self):
        '''Forces Qt Application to "processEvents"'''
        QtGui.QGuiApplication.processEvents()

    def app_launch(self):
        '''Runs the app. Basically the last step.'''
        #self.app = QtWidgets.QApplication(sys.argv)
        self.gui.show()
        self.app.exec_()

if __name__ == '__main__':
    freeze_support()
    sa = Sort_App()
