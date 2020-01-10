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

def Mseqgen(coef, seq_len):
    ans = []
    tap = [1 for _ in range(len(coef))]
    tap[0] = 1

    for i in range(seq_len):
        print("#", tap, i)
        if tap[-1] == 0:
            ans.append(-1)
        else:
            ans.append(1)

        tmp = 0
        for j in range(len(coef)):
            tmp += coef[j] * tap[j]
            tmp = tmp % 2
        for j in reversed( range(1, len(tap))):
            tap[j] = tap[j-1]
        tap[0] = tmp
        
    return ans
