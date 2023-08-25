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
            bpy.context.active_object.name = an_object.name+'_head'
            bpy.ops.object.empty_add(type='ARROWS', align='WORLD', location=an_object.location)
            bpy.context.active_object.name = an_object.name+'_tail'



        print('executing save locations')
        return success

class HSM_OT_append_layout_armature(Operator):
    '''appends layout armature which helps in converting
    custom mesh to muscle via x-muscle'''
    bl_idname = 'hsm.append_layout_armature'
    bl_label = 'append layout armature'

    def execute(self, context):
        for an_object in bpy.context.selected_objects:
            if not an_object.name+'__tmp_layout_armature' in bpy.data.objects.keys():
                path = r"C:\Projects\assets\muscle_strip_base__V_008.blend\Collection"
                coll_names = ['manual_muscleLayout__COLLECTION']
                for aCol in coll_names:
                    bpy.ops.wm.append(filename=aCol, directory=path)

                bpy.data.objects['muscle_object_armature'].name = an_object.name+'__tmp_layout_armature'
                tmp_armature = bpy.data.objects[an_object.name+'__tmp_layout_armature']
                head = tmp_armature.pose.bones['muscle_head']
                tail = tmp_armature.pose.bones['muscle_tail']
                bpy.data.objects[an_object.name+'__tmp_layout_armature'].data.name = an_object.name+'__tmp_layout_armature__ARMATUREDATA'


                tmp_armature.location = an_object.location

                headCon =head.constraints.add(type = 'COPY_LOCATION')
                headCon.target = bpyd

                bpy.data.objects['muscle_direction'].name = an_object.name+'_'+bpy.data.objects['muscle_direction'].name+'__MESHDATA'
            else:
                print(f'required armature already exists, skipping "{an_object.name}" object ')
            return {'FINISHED'}



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


    def draw(self, context):
        layout = self.layout
        row1 = layout.row(align=True)
        row2 = layout.row(align=True)
        row1.operator('hsm.create_insertion_locators', text='create insertions')
        row2.operator('hsm.append_layout_armature',text = 'append layout armature')

operators = [HSM_OT_create_insertion_locators,HSM_OT_append_layout_armature]
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
