import pygame as pg
import pygame_gui

class ReceiverWindow:
    def __init__(self, manager, width, height, parent_heigth, parent_width):
        self.manager = manager
        self.parent_heigth = parent_heigth
        self.parent_width = parent_width
        self.width = width
        self.height = height
        self.window = self.create_window()

    def create_window(self):
        window_orientation = pg.Rect(((self.parent_width / 2) - self.width / 2, (self.parent_heigth / 2) - self.height / 2), (self.width, self.height))
        window = pygame_gui.elements.UIWindow(window_orientation, 
                                              manager=self.manager, 
                                              window_display_title="Receiver settings")
        self.add_labels(window)
        self.add_textboxes(window)
        self.add_buttons(window)
        return window

    def add_labels(self, window):
        pygame_gui.elements.UILabel(pg.Rect((10, 100), (100, 50)), 
                                    text="x-coordinate: ",
                                    container = window.get_container(),
                                    manager=self.manager)
        pygame_gui.elements.UILabel(pg.Rect((210, 100), (100, 50)), 
                                    text="y-coordinate: ",
                                    container = window.get_container(),
                                    manager=self.manager)
        pygame_gui.elements.UILabel(pg.Rect((410, 100), (100, 50)), 
                                    text="z-coordinate: ",
                                    container = window.get_container(),
                                    manager=self.manager)
    
    def add_textboxes(self, window):
        self.x_textbox = pygame_gui.elements.UITextEntryLine(pg.Rect((120, 100), (80, 50)),
                                            manager=self.manager,
                                            container=window.get_container())
        self.y_textbox = pygame_gui.elements.UITextEntryLine(pg.Rect((320, 100), (80, 50)),
                                           manager=self.manager,
                                           container=window.get_container())
        self.z_textbox = pygame_gui.elements.UITextEntryLine(pg.Rect((520, 100), (80, 50)),
                                           manager=self.manager,
                                           container=window.get_container())
    
    def add_buttons(self, window):
        self.save_pos_receiver_button = pygame_gui.elements.UIButton(pg.Rect((500, 190), (100, 50)), 
                                                        text='Save', 
                                                        manager=self.manager,
                                                        container=window.get_container()) 
    
    def get_saved_pos(self):
        return [float(self.x_textbox.get_text()), 
                float(self.y_textbox.get_text()), 
                float(self.z_textbox.get_text())]
        
    def kill_window(self):
        self.window.kill()

   