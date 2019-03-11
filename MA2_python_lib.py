#----------------------------------------------------------------------
#----------------------------------------------------------------------
#--                                                                  --
#--     MA2 Python lib                                               --
#--                                                                  --
#--                                                                  --
#--     Author: Szymon Plotkowski                                    --
#--     Company: Green Beam Design                                   --
#--     Email: splotkowski@gmail.com                                 --
#--     Site: www.gbd.com.pl                                         --
#--                                                                  --
#--                                                                  --
#----------------------------------------------------------------------
#----------------------------------------------------------------------



#MACROFILE CLASS========================================================================================
"""Creates a object that help to write a xml MA2 macrofile """

class MA2macro:

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