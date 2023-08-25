bl_info = {
    "name": "muscle_tools",
    "description": "This Addon simplifies building muscles for x muscle plugin",
    "author": "Haika_studios",  # srivamsi
    "version": (1, 0),
    "blender": (3, 6, 1),
    #"location": "View3D > N ",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "support": "",
    "category": "Generic"
}
success = {'FINISHED'}
import bpy
from bpy.types import Operator, Panel


# operators
class HSM_OT_create_insertion_locators(Operator):
    '''creates insertion locators'''
    bl_idname = 'hsm.create_insertion_locators'
    bl_label = 'create insertion locators'

    def execute(self, context):
        for an_object in bpy.context.selected_objects:
            bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=an_object.location)
            if an_object.name.endswith('_', len(an_object.name) - 2, len(an_object.name) - 1):
                bpy.context.active_object.name = an_object.name[:len(an_object.name)-3]+'_head'+an_object.name[len(an_object.name)-2:]
            else:
                bpy.context.active_object.name = an_object.name+'_head'
            bpy.ops.object.empty_add(type='ARROWS', align='WORLD', location=an_object.location)
            if an_object.name.endswith('_', len(an_object.name) - 2, len(an_object.name) - 1):
                bpy.context.active_object.name = an_object.name[:len(an_object.name)-3]+'_tail'+an_object.name[len(an_object.name)-2:]
            else:
                bpy.context.active_object.name = an_object.name+'_tail'



        print('executing save locations')
        return success

class HSM_OT_append_layout_armature(Operator):
    def execute(self, context):
        for an_object in bpy.context.selected_objects:
            bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=an_object.location)
            if an_object.name.endswith('_', len(an_object.name) - 2, len(an_object.name) - 1):
                bpy.context.active_object.name = an_object.name[:len(an_object.name)-3]+'_head'+an_object.name[len(an_object.name)-2:]
            else:
                bpy.context.active_object.name = an_object.name+'_head'
            bpy.ops.object.empty_add(type='ARROWS', align='WORLD', location=an_object.location)
            if an_object.name.endswith('_', len(an_object.name) - 2, len(an_object.name) - 1):
                bpy.context.active_object.name = an_object.name[:len(an_object.name)-3]+'_tail'+an_object.name[len(an_object.name)-2:]
            else:
                bpy.context.active_object.name = an_object.name+'_tail'



        print('executing save locations')
        return success

# operators end


# UI
class HSMMUSCLE_PT_musclePanel(Panel):
    """Creates a Panel in the n panel"""
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'muscle tools'
    bl_label = "muscle tools"

    # bl_idname = "SCENE_PT_layout"
    # bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator('hsm.create_insertion_locators', text='create insertions')

operators = [HSM_OT_create_insertion_locators]
UI_panels = [HSMMUSCLE_PT_musclePanel]

classes = operators+UI_panels

def register():
    for aClass in classes:
        bpy.utils.register_class(aClass)


def unregister():
    for aClass in classes:
        bpy.utils.unregister_class(aClass)


if __name__ == "__main__":
    register()
