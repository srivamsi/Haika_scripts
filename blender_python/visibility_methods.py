import bpy

def toggle_infront(*args,**kwargs):
    objects = bpy.context.selected_objects
    val = not(objects[0].show_in_front)
    for an_obj in objects:
        an_obj.show_in_front = val

toggle_infront()