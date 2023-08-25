bl_info = {
    "name": "somethingsomething",
    "description": "This Addon simplifies building muscles for x muscle plugin",
    "author": "Haika_studios",  # srivamsi
    "version": (1, 0),
    "blender": (3, 6, 1),
    "location": "View3D > N ",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "support": "",
    "category": "Generic"
}
import bpy



# operators
class HSMUSCLE_OT_get_layout(bpy.types.Operator):
    '''gathers '''
    bl_idname = "hs_muscle.get_layout"
    bl_label = "gets the layout rig"

    def execute(self,context):
        path = r"C:\Projects\assets\muscle_strip_base__V_008.blend\Collection"
        coll_names = ['manual_muscleLayout__COLLECTION']
        for aCol in coll_names:
            bpy.ops.wm.append(filename=aCol,directory = path)

        return {'FINISHED'}

# operators end




# UI
class VIEW3D_PT_x_muscle_extension(bpy.types.Panel):
    """Creates a renaming Panel"""
    bl_label = "x-muscle extension"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "HS-muscle-X"

    # bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        row1 = layout.row(align=True)
        row1.operator('hs_muscle.get_layout', text='get layout')


# UI End



frames = [VIEW3D_PT_x_muscle_extension]
operators = []

classes = frames + operators


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
