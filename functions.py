from dictionaries import *

#Define the contrast of the text color and background color
TEXTCOLORTOBLACK = ["white", "special", "red", "orange", "yellow", "lime", "green", "blue", "pink", "blue-circle", "green-circle", "orange-circle"]
TEXTCOLORTOWHITE = ["dblue", "purple", "brown", "black", "gray", "purple-circle", "brown-circle", "black-circle"]
TEXTCOLORTOCLEAR = "ko"

#Creates a dictionary based on current character
def build_field_sequence(character, max_value, VALUE, field_name, field_color):
    seq_dictionary = dict()

    #Fills all fields with default answers
    for idx in range(max_value):
        seq_dictionary[f"{VALUE}{idx + 1}"] = {
            "value" : "clear",
            "background_color" : TEXTCOLORTOCLEAR,
            "text_contrast_color" : "clear",
        }

    for dial in character['dial']:

        # Realiza o preenchimento em cima de clear com os valores em dial
        # pdb.set_trace()
        try:
            if field_color in dial:
                background_color = power_to_color[dial[field_color]]
            else:
                background_color = "white"
        except:
            raise Exception(f"cor {dial[field_color]} não encontrada")

        if background_color in TEXTCOLORTOBLACK:
          text_contrast_color = "black"
        elif background_color in TEXTCOLORTOWHITE: 
          text_contrast_color = "white"
        else:
            text_contrast_color = "clear"
        # text_contrast_color

        seq_dictionary[f"{VALUE}{dial['click_number']}"] = {
            "value" : dial[field_name],
            "background_color" : background_color,
            "text_contrast_color" : text_contrast_color,
        }
    return seq_dictionary