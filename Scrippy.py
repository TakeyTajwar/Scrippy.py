import re




scrippy_dir = r"D:\-FILES-\Scripts\Scrippy\\"
scrippy_name = r"new.scrippy"
scrippy_path = scrippy_dir + scrippy_name
scrippy = open(scrippy_path, 'r')
objects = {}





for line in scrippy:
    if(re.match(r"^\+\w+$", line)): # import
        scrobj_name = re.search(r"(?<=\+)\w+", line).group(0)
        with open(scrippy_dir+scrobj_name+'.scrobj', 'r') as scrobj:
            objects[scrobj_name] = {}
            for obj_line in scrobj:
                m = None
            
                if(re.match(r"^\w+\s\".*\"$", obj_line)): # String
                    m = re.search(r"^(\w+)\s\"(.*)\"$", obj_line)
                    objects[scrobj_name][m.group(1)] = m.group(2)
                elif(re.match(r"^\w+\s[TF]$", obj_line)): # boolean
                    m = re.search(r"^(\w+)\s([TF])$", obj_line)
                    objects[scrobj_name][m.group(1)] = True if (m.group(2)=='T') else False
                elif(re.match(r"^\w+\s\d+$", obj_line)): # Integer
                    m = re.search(r"^(\w+)\s(\d+)$", obj_line)
                    objects[scrobj_name][m.group(1)] = int(m.group(2))
                elif(re.match(r"^\w+\s\d+\.\d+$", obj_line)): # Float
                    m = re.search(r"^(\w+)\s(\d+\.\d+)$", obj_line)
                    objects[scrobj_name][m.group(1)] = float(m.group(2))
    
    elif(re.match(r"^\w+\s\?\s\w+$", line)): # log
        m = re.search(r"^(\w+)\s\?\s(\w+)$", line)
        if(m.group(1) in objects):
            if(m.group(2) in objects[m.group(1)]):
                print(objects[m.group(1)][m.group(2)])
            else:
                print(f"AttributeDoesNotExist: {m.group(2)}")
        else:
            print(f"ObjectDoesNotExist: {m.group(1)}")
            
    elif(re.match(r"^\w+\s\:\s\w+", line)): # change attribute
        print(line)
    
