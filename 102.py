def group(l, s):
  return [l[x:x+s] for x in range(0, len(l), s)]

def process(l):
  for x, playlist in enumerate(group(l, 50)):
    print(f'Playlist {x+1} ({len(playlist)} songs):')
    for track in playlist:
      print(f'{track}', end=' ')
    print()

def links():
  with open('YOUR_TEXT_FILE_WITH_ALL_THE_SPOTIFY_SONGS_LINKS.txt', 'r') as file:
    return [line for line in file.readlines() if len(line) > 0]

process(links())
