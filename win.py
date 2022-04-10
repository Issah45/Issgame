import pygame
from isseng.init import setup
setup()

wnEvents = pygame.event.get()
wnExit = pygame.QUIT

class Win:
	def __init__(self, size=(800, 600), bg=(255, 255, 255)):
		self.width = size[0]
		self.height = size[1]
		self.size = size
		self.bg = bg
		self.isOpen = True

	def open(self):
		self.wn = pygame.display.set_mode(self.size)

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.isOpen = False
		self.wn.fill(self.bg)

	def render(self, title="Isseng Window"):
		pygame.display.update()
		self.title = title
		self.setTitle()

	def setTitle(self):
		pygame.display.set_caption(self.title)