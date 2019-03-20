#----------------------------------------------------------------------
#----------------------------------------------------------------------
#--                                                                  --
#--     MA2 Python lib                                               --
#--                                                                  --
#--                                                                  --
#--     Author: Szymon Plotkowski                                    --
#--     Company: Green Beam Design                                   --
#--     Email: szymonplotkowski@gmail.com                            --
#--     Site: www.gbd.com.pl                                         --
#--                                                                  --
#--                                                                  --
#----------------------------------------------------------------------
#----------------------------------------------------------------------


#=======================================================================================================
#========================CAMERAFILE CLASS===============================================================
#=======================================================================================================

class MA2Camera:

    #===================================================================================================
    #TODO: Docstrings

    def __init__ (self, filename='default_camera_name.xml', showfile='Created with MA2MBL4P'):

        self.__filename = filename
        self.__showfile = showfile

        with open(self.__filename, "w+") as __camera:
            __camera.write('<?xml version="1.0" encoding="utf-8"?>\n')
            __camera.write(
                '<MA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.malighting.de/grandma2/xml/MA" xsi:schemaLocation="http://schemas.malighting.de/grandma2/xml/MA http://schemas.malighting.de/grandma2/xml/3.4.0/MA.xsd" major_vers="3" minor_vers="4" stream_vers="0">\n')
            __camera.write('\t<Info datetime="2018-01-20T19:30:29" showfile="' +self.__showfile+ '" />\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def camera_object (self, camera_index=1, camera_name='default_camera_name', loc_x=0, loc_y=0, loc_z=0, rot_x=0, rot_y=0, rot_z=0):

        self.__cameraindex= str(camera_index)
        self.__cameraname= camera_name
        self.__loc_x= str(loc_x)
        self.__loc_y= str(loc_y)
        self.__loc_z= str(loc_z)
        self.__rot_x= str(rot_x)
        self.__rot_y= str(rot_y)
        self.__rot_z= str(rot_z)

        with open (self.__filename, "a") as __camera:
            __camera.write('\t<Camera index="' + self.__cameraindex + '" name="' + self.__cameraname +'" ')
            __camera.write('location_x="' + self.__loc_x + '" location_y="' + self.__loc_y + '" location_z="' + self.__loc_z +'">\n')
            __camera.write('\t\t<Rotation rotation_x="'+ self.__rot_x +'" rotation_y="'+ self.__rot_y +'" rotation_z="'+ self.__rot_z +'" />\n')
            __camera.write('\t</Camera>\n')
            return

    # ===================================================================================================
    # TODO: Docstrings

    def close_file (self):
        with open(self.__filename, "a") as __camera:
            __camera.write('</MA>')
            __camera.close()
            return

#=======================================================================================================
#========================GROUPFILE CLASS===============================================================
#=======================================================================================================

class MA2Group:

    #===================================================================================================
    #TODO: Docstrings

    def __init__ (self, filename='default_group_name.xml', showfile='Created with MA2MBL4P'):

        self.__filename = filename
        self.__showfile = showfile

        with open(self.__filename, "w+") as __group:
            __group.write('<?xml version="1.0" encoding="utf-8"?>\n')
            __group.write(
                '<MA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.malighting.de/grandma2/xml/MA" xsi:schemaLocation="http://schemas.malighting.de/grandma2/xml/MA http://schemas.malighting.de/grandma2/xml/3.4.0/MA.xsd" major_vers="3" minor_vers="4" stream_vers="0">\n')
            __group.write('\t<Info datetime="2018-01-20T19:30:29" showfile="' +self.__showfile+ '" />\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def group_start (self, group_index=1, group_name='default_group_name'):

        self.__groupindex= str(group_index)
        self.__groupname= group_name

        with open (self.__filename, "a") as __group:
            __group.write('\t<Group index="' + self.__groupindex + '" name="' + self.__groupname + '">\n')
            __group.write('\t\t<Subfixtures>\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def group_obj_line (self, fixid='1' , subfix='0' ):

        self.__fixid = str(fixid)
        self.__subfix = str(subfix)

        with open (self.__filename, "a") as __group:
            __group.write('\t\t\t<Subfixture fix_id="' +self.__fixid+ '" ')
            if self.__subfix == '0' :
                __group.write('/>\n')
            else:
                __group.write('sub_index="' + self.__subfix + '" />\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def group_end (self):

        with open (self.__filename, "a") as __group:
            __group.write('\t\t</Subfixtures>\n')
            __group.write('\t</Group>\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def close_file (self):
        with open(self.__filename, "a") as __group:
            __group.write('</MA>')
            __group.close()
            return

    #===================================================================================================
    #TODO: USAGE EXAMPLE



#=======================================================================================================
#========================LAYOUTFILE CLASS===============================================================
#=======================================================================================================

"""Create a object that help to write xml MA2 layout file"""

class MA2Layout:

    #===================================================================================================

    """- __init__  - INPUT: ( filename (string), showfile (string) ) ; EFFECT: Initialize MA2layout object and generate file with proper MA2 Layout XML syntax header"""


    def __init__ (self, filename='default_layout_name.xml', showfile='Created with MA2MBL4P'):
        self.__filename = filename
        self.__showfile = showfile
        with open(self.__filename, "w+") as __layout:
            __layout.write('<?xml version="1.0" encoding="utf-8"?>\n')
            __layout.write(
                '<MA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.malighting.de/grandma2/xml/MA" xsi:schemaLocation="http://schemas.malighting.de/grandma2/xml/MA http://schemas.malighting.de/grandma2/xml/3.4.0/MA.xsd" major_vers="3" minor_vers="4" stream_vers="0">\n')
            __layout.write('\t<Info datetime="2018-01-20T19:30:29" showfile="' +self.__showfile+ '" />\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def layout_start (self, lay_no=1, lay_name='default_layout_name'):
        self.__lay_no = lay_no
        self.__lay_name = lay_name
        with open(self.__filename ,"a") as __layout:
              __layout.write ('\t<Group index=";' +__lay_no+ '" name="' +__lay_name+ '">\n')
              return

    #===================================================================================================
    #TODO: Docstrings

    def layout_fix_declaration_start (self):
        with open(self.__filename, "a") as __layout:
            __layout.write('\t\t<Subfixtures>\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def layout_fixture_declaration_line (self, fixid='1', instance='0'):

        self.__fixid = fixid
        self.__instance = instance

        with open(self.__filename, "a") as __layout:
            if self.__instance == 0:
                __layout.write('\t\t\t<Subfixture fix_id="' + self.__fixid + '"/>\n')
            else:
                __layout.write('\t\t\t<Subfixture fix_id="' + self.__fixid + '" sub_index="' + self.__instance + '"/>\n')

    #===================================================================================================
    #TODO: Docstrings

    def layout_fixtures_declaration_close(self):
        with open(self.__filename, "a") as __layout:
            __layout.write('\t\t</Subfixtures>\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def layout_data(self, lay_nr='1', visible='true', bckgrnd='000000', grid_h='1', grid_w='1', snap_h='0.5', snap_w='0.5', gauge='"Filled &amp; Symbol"', vmode='"DMX Layer"' ):

        self.__lay_nr = lay_nr
        self.__visible = visible
        self.__bckgrnd = bckgrnd
        self.__grid_h = grid_h
        self.__grid_w = grid_w
        self.__snap_h = snap_h
        self.__snap_w = snap_w
        self.__gauge = gauge
        self.__vmode = vmode

        with open(self.__filename ,"a") as __layout:
            __layout.write ('\t\t<LayoutData index="'+self.__lay_nr+'" marker_visible="'+self.__visible+'" background_color="'+self.__bckgrnd+'" visible_grid_h="'+self.__grid_h+'" visible_grid_w="'+self.__grid_w+'" snap_grid_h="'+self.__snap_h+'" snap_grid_w="'+self.__snap_w+'" default_gauge="'+self.__gauge+'" subfixture_view_mode="'+self.__vmode+'">\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def layout_fixture_obj_start(self):
        with open(self.__filename, "a") as __layout:
            __layout.write('\t\t\t<SubFixtures>\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def layout_fixture_obj_line (self, fixid='1', center_x='1', center_y='1', instance='0', size_h='1', size_w='1', bckgrnd='00000000', icon='None', sh_id='1', sh_type='1', fn_type='Spot', select_gr='1'):

        self.__fixid = fixid
        self.__center_x = center_x
        self.__center_y = center_y
        self.__instance = instance
        self.__size_h = size_h
        self.__size_w = size_w
        self.__bckgrnd = bckgrnd
        self.__icon = icon
        self.__sh_id = sh_id
        self.__sh_type = sh_type
        self.__fn_type = fn_type
        self.__select_gr = select_gr

        with open(self.__filename, "a") as __layout:
            if self.__instance == '0':
                __layout.write('\t\t\t\t<LayoutSubFix center_x="' + self.__center_x + '" center_y="' + self.__center_y + '" size_h="' + self.__size_h + '" size_w="' + self.__size_w + '" background_color="' + self.__bckgrnd + '" icon="' + self.__icon + '" show_id="' + self.__sh_id + '" show_type="' + self.__sh_type + '" function_type="' + self.__n_type + '" select_group="' + self.__select_gr + '">\n')
                __layout.write('\t\t\t\t\t<image />\n')
                __layout.write('\t\t\t\t\t<Subfixture fix_id="' + self.__fixid + '" />\n')
                __layout.write('\t\t\t\t</LayoutSubFix>\n\n')
            else:
                __layout.write('\t\t\t\t<LayoutSubFix center_x="' + self.__center_x + '" center_y="' + self.__center_y + '" size_h="' + self.__size_h + '" size_w="' + self.__size_w + '" background_color="' + self.__bckgrnd + '" icon="' + self.__icon + '" show_id="' + self.__sh_id + '" show_type="' + self.__sh_type + '" function_type="' + self.__fn_type + '" select_group="' + self.__select_gr + '">\n')
                __layout.write('\t\t\t\t\t<image />\n')
                __layout.write('\t\t\t\t\t<Subfixture fix_id="' + self.__fixid + '" sub_index="' + self.__instance + '" />\n')
                __layout.write('\t\t\t\t</LayoutSubFix>\n\n')
                return

    #===================================================================================================
    #TODO: Docstrings

    def layout_fixture_obj_close(self):
        with open(self.__filename, "a") as __layout:
            __layout.write('\t\t\t</SubFixtures>\n')
            return

    #===================================================================================================
    #TODO: Docstrings


    def layout_objects(self, obj_name, obj_type, obj_nr, center_x, center_y, size_h='1', size_w='1', font='Small', bckgrnd='3c3c3c', border='5a5a5a', icon='None', txt='', sh_id='1', sh_name='1', sh_type='1', fn_type='Pool icon', select_gr='1'):

        self.__obj_name = obj_name
        self.__obj_type = obj_type
        self.__obj_nr = obj_nr
        self.__center_x = center_x
        self.__center_y = center_y
        self.__size_h = size_h
        self.__size_w = size_w
        self.__font = font
        self.__bckgrnd = bckgrnd
        self.__border = border
        self.__icon = icon
        self.__txt = txt
        self.__sh_id = sh_id
        self.__sh_name = sh_name
        self.__sh_type = sh_type
        self.__fn_type = fn_type
        self.__select_gr = select_gr

        with open(self.__filename, "a") as __layout:
            __layout.write('\t\t\t\t<LayoutCObject font_size="' + self.__font + '" center_x="' + self.__center_x + '" center_y="' + self.__center_y + '" size_h="' + self.__size_h + '" size_w="' + self.__size_w + '" background_color="' + self.__bckgrnd + '" border_color="' + self.__border + '" icon="' + self.__icon + '" text="' + self.__txt + '" show_id="' + self.__sh_id + '" show_name="' + self.__sh_name + '" show_type="' + self.__sh_type + '" function_type="' + self.__f_type + '" select_group="' + self.__select_gr + '">\n')
            __layout.write('\t\t\t\t\t<image />\n')
            __layout.write('\t\t\t\t\t<CObject name="' + self.__obj_name + '">\n')

            if self.__obj_type == 'timecode_slot':
                __layout.write('\t\t\t\t\t\t<No>3</No>\n')
                __layout.write('\t\t\t\t\t\t<No>6</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'image':
                __layout.write('\t\t\t\t\t\t<No>8</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'macro':
                __layout.write('\t\t\t\t\t\t<No>13</No>\n')
                __layout.write('\t\t\t\t\t\t<No>1</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'plugin':
                __layout.write('\t\t\t\t\t\t<No>15</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'preset':
                self.__obj = self.__obj_nr.split('.', 1)
                __layout.write('\t\t\t\t\t\t<No>17</No>\n')
                __layout.write('\t\t\t\t\t\t<No>1</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj[1] + '</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj[2] + '</No>\n')

            elif self.__obj_type == 'world':
                __layout.write('\t\t\t\t\t\t<No>18</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'filter':
                __layout.write('\t\t\t\t\t\t<No>19</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'group':
                __layout.write('\t\t\t\t\t\t<No>22</No>\n')
                __layout.write('\t\t\t\t\t\t<No>1</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'form':
                __layout.write('\t\t\t\t\t\t<No>23</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'fx':
                __layout.write('\t\t\t\t\t\t<No>24</No>\n')
                __layout.write('\t\t\t\t\t\t<No>1</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'seq':
                __layout.write('\t\t\t\t\t\t<No>25</No>\n')
                __layout.write('\t\t\t\t\t\t<No>1</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'timer':
                __layout.write('\t\t\t\t\t\t<No>25</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'ex_page':
                __layout.write('\t\t\t\t\t\t<No>30</No>\n')
                __layout.write('\t\t\t\t\t\t<No>1</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'ch_page':
                __layout.write('\t\t\t\t\t\t<No>31</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'timecode':
                __layout.write('\t\t\t\t\t\t<No>35</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            elif self.__obj_type == 'view':
                __layout.write('\t\t\t\t\t\t<No>39</No>\n')
                __layout.write('\t\t\t\t\t\t<No>1</No>\n')
                __layout.write('\t\t\t\t\t\t<No>6</No>\n')
                __layout.write('\t\t\t\t\t\t<No>' + self.__obj_nr + '</No>\n')

            __layout.write('\t\t\t\t\t</CObject>\n')
            __layout.write('\t\t\t\t</LayoutCObject>\n\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def layout_objects_close(self):
        with open(self.__filename, "a") as __layout:
            __layout.write('\t\t\t</CObject>\n')
            return

    #===================================================================================================
    #TODO: Docstrings

    def layout_close(self):
        with open(self.__filename, "a") as __layout:
            __layout.write('\t\t</LayoutData>\n')
            __layout.write('\t</Group>\n')
            return

    #===================================================================================================
    #TODO: Docstrings
    def close_file(self):
        with open(self.__filename, "a") as __layout:
            __layout.write('</MA>')
            __layout.close()
            return

    #===================================================================================================
    #TODO: Usage example




#=======================================================================================================
#========================MACROFILE CLASS================================================================
#=======================================================================================================

"""Creates a object that help to write a xml MA2 macrofile """

class MA2Macro:

    #===================================================================================================

    """- __init__  - INPUT: ( filename (string), showfile (string) ) ; EFFECT: Initialize MA2macro object and generate file with proper MA2 Macro XML syntax header"""

    def __init__ (self, filename='default_macro_name.xml', showfile='Created with MA2MBL4P'):
        self.__filename = filename
        self.__showfile = showfile

        with open(self.__filename, "w+") as __macro:
            __macro.write('<?xml version="1.0" encoding="utf-8"?>\n')
            __macro.write(
                '<MA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.malighting.de/grandma2/xml/MA" xsi:schemaLocation="http://schemas.malighting.de/grandma2/xml/MA http://schemas.malighting.de/grandma2/xml/3.4.0/MA.xsd" major_vers="3" minor_vers="4" stream_vers="0">\n')
            __macro.write('\t<Info datetime="2018-01-20T19:30:29" showfile="' +self.__showfile+ '" />\n')
            return
    #===================================================================================================

    """- macro_start - INPUT: ( macro number (int), macro name (string) ) ; EFFECT: append proper "Macro start" syntax to filename definied in object"""

    def macro_start (self, macro_number=1, macro_name='default_macro_name'):
        self.__macronumber = str (macro_number)
        self.__macroname = macro_name
        with open(self.__filename ,"a") as __macro:
            __macro.write ('\t<Macro index="'+self.__macronumber+'" name="'+self.__macroname+'">\n')
            return
    #===================================================================================================

    """- macro_line -INPUT: ( macro line number (int), macro command (string) ) ; EFFECT: append proper "Macro line" syntax to filename definied in object"""

    def macro_line (self, linenumber=1, macroline='default_macro_line'):
        self.__linenumber=str(linenumber)
        self.__macroline = macroline
        with open(self.__filename , "a") as __macro:
            __macro.write ('\t \t <Macroline index="'+ self.__linenumber +' ">\n')
            __macro.write ('\t \t \t <text>'+self.__macroline+'</text>\n' )
            __macro.write ('\t \t </Macroline>\n')
            return

    #===================================================================================================
    """- macro_end - INPUT: () ; EFFECT: append proper "macro end" syntax to filename definied in object"""
    def macro_end(self):
        with open(self.__filename, "a") as __macro:
            __macro.write('\t</macro>\n')
            return


    # ==================================================================================================
    """- close _file - INPUT: () ; EFFECT append proper "End of file" syntax to filename definied in object and closes file object """

    def close_file(self):
        with open(self.__filename, "a") as __macro:
            __macro.write('</MA>')
            __macro.close()
            return

    #====================================================================================================
    #Setters and getters

    def set_filename (self, filename):
        self.__filename = filename
        return

    def get_filename (self):
        return self.__filename

    def set_showfile (self, showfile):
        self.__showfile = showfile
        return

    def get_showfile (self):
        return self.__showfile

    def get_macronumber (self):
        return self.__macronumber

    def get_macroline (self):
        return self.__macroline

    def get_linenumber (self):
        return self.__linenumber
#========================================================================================================


"""USAGE EXAMPLE

Object = MA2macro ('filename.xml', 'Showname')
Object.macro_start (1 , 'First macro')
Object.macro_line (1, 'Fixture 1 Thru 30')
Object.macro_line (2, 'At 100')
Object.macro_line (3, 'Store 1')
Object.macro_line (4, 'Clear All')
Object.macro_end()
Object.macro_start (1 , 'First macro')
Object.macro_line (1, 'Select @')
Object.macro_line (2, 'Store 1')
Object.macro_line (3, 'Clear All')
Object.macro_end()
Object.close_file()

GIVES filename.xml FILE:

<?xml version="1.0" encoding="utf-8"?>
<MA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.malighting.de/grandma2/xml/MA" xsi:schemaLocation="http://schemas.malighting.de/grandma2/xml/MA http://schemas.malighting.de/grandma2/xml/3.4.0/MA.xsd" major_vers="3" minor_vers="4" stream_vers="0">
	<Info datetime="2018-01-20T19:30:29" showfile="Showname" />
	<Macro index="1" name="First macro">
	 	 <Macroline index="1 ">
	 	 	 <text>Fixture 1 Thru 30</text>
	 	 </Macroline>
	 	 <Macroline index="2 ">
	 	 	 <text>At 100</text>
	 	 </Macroline>
	 	 <Macroline index="3 ">
	 	 	 <text>Store 1</text>
	 	 </Macroline>
	 	 <Macroline index="4 ">
	 	 	 <text>Clear All</text>
	 	 </Macroline>
	</macro>
	<Macro index="1" name="First macro">
	 	 <Macroline index="1 ">
	 	 	 <text>Select @</text>
	 	 </Macroline>
	 	 <Macroline index="2 ">
	 	 	 <text>Store 1</text>
	 	 </Macroline>
	 	 <Macroline index="3 ">
	 	 	 <text>Clear All</text>
	 	 </Macroline>
	</macro>
</MA>


"""