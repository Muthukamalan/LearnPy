import os 
import csv


def file_format(file_name:str,destination:str,*,logger=None)->bool:
    assert os.path.isdir(destination),"Directory not Exists!!"
    assert os.path.isfile(file_name),"File not exists!!"

    with open(file_name,'r',encoding='utf-8') as file:
        reader = csv.reader(file)
        rows   = list(reader)
    
    # Open the Output CSV file in write mode;
    with open(file_name,'w',newline='',encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        # Iterate through each row and remove double quotes
        for row in rows:
            cleaned_row = [ value.replace('"','') for value in row ] 
            writer.writerow(cleaned_row)
    
    if logger is not None:
        logger.debug(msg="file formatted successfully!!")


