import json

import pyglet

import gamestate

class SceneHandler(object):
    def __init__(self, scene_object, environment_object):
        self.scene = scene_object
        self.environment = environment_object
        self.actors = {}
    
    def on_mouse_release(self, x, y, button, modifiers):
        if self.scene.actors.has_key("main"):
            main = self.scene.actors["main"]
            print self.scene.walkpath.move_sequence(main.walkpath_point, (x, y))
            main.prepare_move(*self.scene.camera.mouse_to_canvas(x, y))
    
    def __repr__(self):
        return "SceneHandler(scene_object=%s, environment_object=%s)" % (str(self.scene), str(self.environment))