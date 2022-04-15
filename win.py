import pygame

class Win:
	def __init__(self, size=(800, 600)):
		self.width = size[0]
		self.height = size[1]
		self.size = size
		self.isOpen = True
		self.wn = pygame.display.set_mode(self.size)

	def CloseWn(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.isOpen = False

	def SetTitle(self, title="Isseng Window"):
		self.title = title
		pygame.display.set_caption(self.title)

	def SetColor(self, bg=(255, 255, 255)):
		self.wn.fill(bg)

def Draw():
	pygame.display.flip()