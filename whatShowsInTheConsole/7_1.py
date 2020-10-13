vechicle = 'bus'


def drive():
    # if you're assigning to "vechicle", it will only look for "vechicle" in
    # local scope. Assigning to a name makes it local to that function. Since
    # there is no such local variable at the point you're trying to use it, you
    # get an error.

    # because assignment says "this thing is local, only look for it in local
    # scope".
    vechicle = vechicle
    print('driving a {}'.format(vechicle))


drive()
