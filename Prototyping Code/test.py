from pixelsort import pixelsort
from PIL import Image
from pathlib import Path
from time import sleep

from multiprocessing import Process, freeze_support

def main_prog():
    f_images = "images"
    i = "squirrel.jpg"
    #i = "DSC04688_EDIT_1000.jpg"
    p = Path()
    image_p_in = p / f_images / i


    mask_user_selection_options = ["None", "Single", "Folder"]
    mask_user_selection = "Single"
    mask_selected = "squirrel_mask_Inverted.jpg"


    f_masks = p / f_images / "Masks"
    p_masks = list(f_masks.glob("*.jpg"))

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

    sort_settings_list = []

    if mask_user_selection == "None":
        p_masks = None
        sort_settings_list = [sort_settings.copy()]
    elif mask_user_selection == "Single":
        settings_with_mask = sort_settings.copy()
        settings_with_mask["mask_image"] = p / f_images / "Masks" / mask_selected
        sort_settings_list.append(settings_with_mask)
    elif mask_user_selection == "Folder":
        for p_mask in p_masks:
            settings_with_mask = sort_settings.copy()
            settings_with_mask["mask_image"] = p_mask
            sort_settings_list.append(settings_with_mask)     
    else:
        print("error")

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
        image_p_out = p / f_images / "SORTED" / f"{image_p_in.stem}_SORTED_{settings_changed_formatted}{image_p_in.suffix}"
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

        print(f"Saved image path: {image_p_out.absolute()}")
        sleep(1)
        img_rgb.show()

    #img_sorted = Image.SAVE("SORTED.jpg")

    print("Done")

if __name__ == "__main__":
    freeze_support()
    main_prog()