def uniqify(seq):
    """
    An order preserving uniqifier that takes a sequence and gives out the
    uniqified sequence. Works even on object lists.

    CREDIT:
        Dave Kirby
    """
    noDupes = []
    [noDupes.append(i) for i in seq if not noDupes.count(i)]
    return noDupes

#-------------------------------------------------------------------------------
