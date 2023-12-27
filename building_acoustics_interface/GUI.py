import pygame as pg
import pygame_gui
from pygame.locals import *

from renderer import *
from toolbar import *
from graphDisplay import *


class GUI:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1200, 700
        self.FPS = 60
        self.window_surface = pg.display.set_mode(self.RES, DOUBLEBUF)
        self.manager = pygame_gui.UIManager(self.RES)
        self.background_surface = pg.Surface((self.WIDTH, self.HEIGHT))
        self.background_surface.fill(pg.Color('white'))

        self.render_surface = pg.Surface((800, 600))
        self.render_surface.fill(pg.Color('white'))
        self.renderer = SoftwareRender(self.render_surface)

        self.toolbar = Toolbar(self.manager, self.WIDTH, 50)

        self.graph_display = GraphDisplay(self.manager)

        self.clock = pg.time.Clock()

    def run(self):
        while True:
            time_delta = self.clock.tick(60)/1000.0
            self.renderer.draw()
            self.renderer.camera.control()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.toolbar.file_button:
                        self.toolbar.file_dialog = pygame_gui.windows.UIFileDialog(pg.Rect((0,0), (400, 300)), manager=self.manager)

                self.manager.process_events(event)
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
            self.manager.update(time_delta)
            #self.background_surface.blit(self.graph_display.processed_plot, (800, 0))
            self.window_surface.blit(self.background_surface, (0, 0))
            self.window_surface.blit(self.render_surface, (0, 100))
            self.manager.draw_ui(self.window_surface)

if __name__ == '__main__':
    app = GUI()
    app.run()