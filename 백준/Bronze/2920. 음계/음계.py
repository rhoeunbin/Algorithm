sound = list(map(int, input().split()))

sound_a = sorted(sound)
sound_d = sorted(sound, reverse=True)

if sound == sound_a:
    print('ascending')
elif sound == sound_d:
    print('descending')
else:
    print('mixed')