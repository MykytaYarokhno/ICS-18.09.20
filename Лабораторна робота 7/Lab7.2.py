from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

c = Counter("Отримувані  зображення  можуть  бути  використані  як  ілюстрації  в публікаціях.")
plt.bar(*zip(*c.most_common()), width=.5)
plt.show()
