import sys
from lib.label import Label
from lib.badge import Badge
from lib.envelope import Envelope

if __name__ == "__main__":
  data = [
    'papers-512',
    'Epamindas Silva Silveira Paes Lima',
    'ThoughtWorks',
    'Santo Antonio de Porto Alegre'
  ]

  device = settings.DEVICE

  if len(sys.argv) == 3:
    device = sys.argv[2]

  if sys.argv[1] == 'badge':
    Badge(*data, device=device)
  elif sys.argv[1] == 'env':
    Envelope(*data, device=device)
