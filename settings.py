class  Setting(object):
    """store all settings for surface."""

    def __init__(self):
        """screen settings"""
        self.screen_size = (640, 480)       #screen size
        self.bg_color = (255, 255, 255)     #white

        """surface settings"""
        self.sur_color = (0, 0, 0)      #black
        self.sur_size = (20, 20)        #surface size
        self.sur_topleft = (100, 100)
        self.sur_speed = 10     #surface moving speed

        """refresh rate"""
        self.fps = 10
