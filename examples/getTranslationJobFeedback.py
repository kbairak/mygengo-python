# -*- coding: utf-8 -*-
#!/usr/bin/python

from mygengo import MyGengo

# Get an instance of MyGengo to work with...
gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly false, depending on your dev needs
)

# Very much like grabbing a comment history. Returns a data set, iterate
# if you want specifics!
print gengo.getTranslationJobFeedback(id = 42)
