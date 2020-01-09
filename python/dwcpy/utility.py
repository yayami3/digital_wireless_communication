# TransVersalFilter
def TVF(signal_in, tap):
    len_sig = len(signal_in)
    len_tap = len(tap)

    zeropadding = [0 for _ in range(len_tap-1)]
    padded_signal_in = zeropadding + signal_in + zeropadding
    
    signal_out = [0 for _ in range(len_sig+len_tap-1)]
    for i in range(len_sig+len_tap-1):
        for s, w in zip(reversed(padded_signal_in[i:i+len_tap]), tap):
            signal_out[i] += s*w

    return signal_out
