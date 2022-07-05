import sys

sys.path.append("./src/mnemonic")

from mnemonic import Mnemonic

print("start...")

mnemo = Mnemonic("english")
words = mnemo.generate(strength=128)
print("words,\n" , words)
seed = mnemo.to_seed(words, passphrase="")
print(f"seed, {len(seed)}\n" , seed)

entropy = mnemo.to_entropy(words)
print(f"entropy, {len(entropy)}\n" , entropy)