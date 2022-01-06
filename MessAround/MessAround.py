import os
import sys
import zipfile

zip = sys.argv[1]
print(sys.argv)
print(sys.argv[1])
print(os.path.exists(zip))

if os.path.exists(zip) is True:
    zip_ref = zipfile.ZipFile(zip, 'r')
    zip_ref.extractall(".") #cur directory
    zip_ref.close()

    for root, dirs, files in os.walk("."):  
        for filename in files:
            print(filename)
            if filename.endswith(".geojson"):
                jsonFile = os.path.join(root, filename)
                #os.startfile(jsonFile)