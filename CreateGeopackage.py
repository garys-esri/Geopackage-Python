#-------------------------------------------------------------------------------
#
# Author:      Scott Cecilio
#
# Created:     16/04/2015
# Copyright:   (c) scot6793 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

# Set local variables
sqlite_database_path = arcpy.GetParameterAsText(0)
# Execute CreateSQLiteDatabase
arcpy.gp.CreateSQLiteDatabase(sqlite_database_path, "GEOPACKAGE")
