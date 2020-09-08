class Song:
	def __init__(self, lyrics):
		self.lyrics = list(lyrics)

	def sing_me_a_song(self, lyrics):
		for i in lyrics:
			print(i, end='\n')


happy_bday = Song(["May god bless you, ",
				   "Have a sunshine on you,",
				   "Happy Birthday to you !"])

happy_bday.sing_me_a_song(happy_bday.lyrics)
