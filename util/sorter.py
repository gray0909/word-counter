def merge_sort(word_list):
    if len(word_list) <= 1:
        return word_list
    m = int(len(word_list) / 2)
    l_list, r_list = merge_sort(word_list[:m]), merge_sort(word_list[m:])
    return merge(l_list, r_list, word_list.copy())


def merge(l_list, r_list, m_list):
    lp, rp = 0, 0
    while lp < len(l_list) and rp < len(r_list):

        if l_list[lp][1] >= r_list[rp][1]:
            m_list[lp + rp] = l_list[lp]
            lp += 1
        else:
            m_list[lp + rp] = r_list[rp]
            rp += 1

    for lp in range(lp, len(l_list)):
        m_list[lp + rp] = l_list[lp]

    for rp in range(rp, len(r_list)):
        m_list[lp + rp] = r_list[rp]
    return m_list


class TopWordSort:

    def __init__(self, unsorted_list):
        self.unsorted_list = unsorted_list
        self.sorted_list = list()
        self.set_sort_word_list()

    def set_sort_word_list(self):
        self.sorted_list = merge_sort(self.unsorted_list)



