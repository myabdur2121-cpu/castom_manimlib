from mnaim import * 
import numpy as np 

class SmoothPolygon(VMobject):
  '''
  this is a smooth closed shapes besed on vertices points. but sometimes it give discontinuity about starting point. 
  Example:
  class AnimationScene2(Scene):
    def construct(self):
        points = [
            np.array([-1,2,0]),
            np.array([1,1,0]),
            np.array([2,-1,0]),
            np.array([-2,-1,0]),
        ]
        shape = SmoothPolygon(points)
        self.add(shape)
  '''
  
    DEFULT_POINTS = [DR,DL,UL,UR]
  
    def __init__(self,vertices = DEFULT_POINTS ,**kwargs):
        self.vertices = [vertices[-1],*vertices,vertices[0],vertices[1]]
        super().__init__(**kwargs)
        self.set_points_smoothly(self.vertices)
        self.set_points(self.points[4:(4*len(self.vertices)-8)])

