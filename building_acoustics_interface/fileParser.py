from object_3d import *

class FileParser:
    def __init__(self, render, file_path):
        self.render = render
        self.path = file_path
        self.parse_file()

    def parse_file(self):
        self.read_file()
        self.find_type()
        if (self.type == 'MSH 2.2'):
            self.parse_msh_2_2()
        elif (self.type == 'MSH 4.1'):
            self.parse_msh_4_1()
        elif (self.type == 'OBJ'):
            self.parse_obj()
        elif (self.type == 'Unknown' or self.type == 'Not found'):
            print("no good file")
            self.object = Object3D(self.render, [], [])
    
    def parse_msh_2_2(self):
        vertices, faces = [], []
        nodes_section = False
        faces_section = False
        for line in self.file.split('\n'):
            if (line == '$Nodes'):
                nodes_section = True
            elif (line == '$EndNodes'):
                nodes_section = False
            elif (line == '$Elements'):
                print("i get here")
                faces_section = True
            elif (line == '$EndElements'):
                faces_section = False

            elif (nodes_section):
                if line.strip():
                    check = line.split()[1:]
                    if (len(check) != 0):
                        values = [float(val) for val in check + [1]]
                        vertices.append(values)
            elif (faces_section):
                if line.strip():
                    if (len(line.split()[1:]) == 7):
                        values = [int(val) - 1 for val in line.split()[-3:]]
                        faces.append(values)
        self.object = Object3D(self.render, vertices, faces)

    
    def find_type(self):
        print(self.path)
        last_dot_index = self.path.rfind('.')
        if (last_dot_index != -1):
            extension = self.path[last_dot_index:]
            if (extension.lower() == '.msh'):
                if (self.file.split('\n')[1] == '2.2 0 8'):
                    print("I found the version")
                    self.type = 'MSH 2.2'
                elif(self.file.split('\n')[1] == '4.1 0 8'):
                    self.type = 'MSH 4.1'
                else:
                    self.type = 'Unknown'
                    print('Not a supported msh file version')
            elif (extension.lower() == '.obj'):
                self.type = 'OBJ'
            else: # Add more file types as needed
                self.type = 'Unknown'
                print('Not a supported file extention')
        else:
            self.type = 'Not found'
            print('No file extension found.')


    def read_file(self):
         with open(self.path, 'r') as f:
            self.file = f.read()