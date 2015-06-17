def DA(a, b):
    import copy
    m_pref = copy.deepcopy(a)
    f_pref = copy.deepcopy(b)

    n = len(m_pref)
    m = len(f_pref)
    unmatch_m = n
    unmatch_f = m
    
    m_engage = [-1] * n
    f_engage = [-1] * m
    proposing = -1
    proposed = -1
    
    while(m_engage.count(-1) != 0):
        for proposing in range(n):
            if m_engage[proposing] == -1:
                proposed = m_pref[proposing].pop(0)
                if proposed == unmatch_f:
                    m_engage[proposing] = proposed
                elif f_engage[proposed] == -1:
                    if f_pref[proposed].index(proposing) < f_pref[proposed].index(unmatch_m): 
                        f_engage[proposed] = proposing
                        m_engage[proposing] = proposed
                else:
                    if f_pref[proposed].index(proposing) < f_pref[proposed].index(f_engage[proposed]):
                        m_engage[f_engage[proposed]] = -1
                        m_engage[proposing] = proposed
                        f_engage[proposed] = proposing

            
    return m_engage 