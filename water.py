import pygame
import math
import settings
import time


class Water:
    def __init__(self, start: tuple[int], end: tuple[int], wave_length: float, wave_height: float) -> None:
        self.__start = start
        self.__end = end
        self.__wave_length = wave_length
        self.__wave_height = wave_height
        self.__water_points = [[x, self.__start[1]] for x in range(self.__start[0], self.__end[0])]
        self.__water_level: int = start[1]
    
    def draw(self, screen):
        for point in self.__water_points:
            t = time.time()
            velocity: float = self.__wave_length / t
            k: float = (2 * math.pi) / self.__wave_length
            w: float = (2 * math.pi) / self.__wave_length * velocity * t
            
            # - : left to right | + : right to left               |
            y: float = self.__wave_height * math.sin(k * point[0] - w * t)
            
            point[1] = self.__water_level + y

            min_wave_level: int = self.__start[1] + self.__wave_height

            for i in range(int(point[1]), min_wave_level):
                pygame.draw.line(screen, settings.BLUE, point, (point[0], i))
                
            pygame.draw.rect(screen, settings.BLUE, (self.__start[0], min_wave_level, self.__end[0], settings.HEIGHT))
            